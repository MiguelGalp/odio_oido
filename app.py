from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import json
import asyncio
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime, timezone, timedelta
from dateutil.parser import parse
import logging
import twscrape
from twscrape import API, gather
from twscrape.logger import set_log_level


load_dotenv()
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://")
db = SQLAlchemy(app)
Bootstrap(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    total_engagement = db.Column(db.Integer, default=0)
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('tweets', lazy=True))
    content = db.Column(db.String(280))
    likes = db.Column(db.Integer)
    retweets = db.Column(db.Integer)
    replies = db.Column(db.Integer)
class FetchTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('fetch_times', lazy=True))
    last_fetched = db.Column(db.DateTime)
    tweet_increase = db.Column(db.Integer)
class TotalIncrease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=True))
    total_tweet_increase = db.Column(db.Integer)
try:
    with app.app_context():
        # Create the database tables
        db.create_all()
except Exception as e:
    print(f"Database error: {str(e)}")

async def fetch_tweets_and_update_engagement():
    api = API()  # or API("path-to.db") - default is `accounts.db`
    # Add your accounts
    await api.pool.add_account("Mglamour2465", "Caniggia0", "mikeglamour8@gmail.com", "445841")
    await api.pool.add_account("MoleculePe43018", "Caniggia0", "postmolecule@gmail.com", "166112")

    with app.app_context():
        try:
            
            # List of users for whom you want to track engagement
            users = ["SergioChouza", "CarlosMaslaton"]

            for user in users:
                # Get the last 20 tweets for the user using twscrape
                tweets = await gather(api.user_tweets(user, limit=20))

                # Initialize engagement metrics
                total_likes = 0
                total_retweets = 0
                total_replies = 0

                # Process engagement metrics for each tweet
                for tweet in tweets:
                    likes = tweet["likeCount"]
                    retweets = tweet["retweetCount"]
                    replies = tweet["replyCount"]

                    # Update total engagement metrics
                    total_likes += likes
                    total_retweets += retweets
                    total_replies += replies

                    # Create or update the tweet record in the database
                    db_tweet = Tweet.query.filter_by(id=tweet["id"]).first()
                    if db_tweet is None:
                        db_tweet = Tweet(id=tweet["id"], user_id=user.id, content=tweet["content"], likes=likes, retweets=retweets, replies=replies)
                        db.session.add(db_tweet)
                    else:
                        db_tweet.likes = likes
                        db_tweet.retweets = retweets
                        db_tweet.replies = replies

                # Calculate total engagement for the user
                total_engagement = total_likes + total_retweets + total_replies

                # Update the user record with the total engagement
                db_user = User.query.filter_by(id=user.id).first()
                if db_user is not None:
                    db_user.total_engagement = total_engagement

            db.session.commit()

        except Exception as e:
            # Log the exception details
            app.logger.error(f"Error in fetch_tweets_and_update_engagement: {str(e)}")
            return str(e)

# Create an event loop
loop = asyncio.get_event_loop()

# Use the event loop to run your function
loop.run_until_complete(fetch_tweets_and_update_engagement())


def get_current_engagement():
    # Setup last fetch as the instance of db within this scope
    last_tweet = Tweet.query.order_by(Tweet.id.desc()).first()
    if last_tweet is None:
        app.logger.warning("No Tweet records found")
        return jsonify({"error": "No Tweet records found"})
    # Retrieve the engagement metrics of last tweet
    total_engagement = last_tweet.likes + last_tweet.retweets + last_tweet.replies
    app.logger.info(f"Total engagement of last tweet: {total_engagement}")
    # The app´s principal logic is represented here
    if total_engagement < 100:
        return jsonify({"engagement": "Green"})
    elif total_engagement < 500:
        return jsonify({"engagement": "Yellow"})
    else:
        return jsonify({"engagement": "Red"})

@app.route('/engagement', methods=['GET'])
def engagement_route():
    return get_current_engagement()

@app.route('/tweet_activity', methods=['GET'])
def tweet_activity_route():
    # Fetch the last four hours of Tweet records
    four_hours_ago = datetime.now(timezone.utc) - timedelta(hours=4)
    records = Tweet.query.filter(Tweet.timestamp >= four_hours_ago).all()
    # Ensure all timestamps are timezone-aware
    for record in records:
        if record.timestamp.tzinfo is None or record.timestamp.tzinfo.utcoffset(record.timestamp) is None:
            record.timestamp = record.timestamp.replace(tzinfo=timezone.utc)
    # Calculate the total engagement for each hour
    engagements = []
    for i in range(4):
        start_time = datetime.now(timezone.utc) - timedelta(hours=i+1)
        end_time = datetime.now(timezone.utc) - timedelta(hours=i)
        engagement = sum((record.likes + record.retweets + record.replies) for record in records if start_time <= record.timestamp < end_time)
        engagements.append((start_time, engagement))
    # Check for any spikes in tweet activity
    spike_times = []
    for i in range(1, 4):
        if engagements[i][1] > 2 * sum(engagement[1] for engagement in engagements[:i]):
            spike_times.append(engagements[i][0])
    if spike_times:
        message = f"Spikes at the following times: {', '.join(time.strftime('%H:%M') for time in spike_times)}"
    else:
        message = "No significant spike in tweet activity in the last four hours."
    return jsonify({"message": message})


@app.route('/')
def index():
    # Retrieve the most recent User record from the database
    user = User.query.order_by(User.id.desc()).first()

    # Calculate the time difference between the current time and the timestamp of the most recent User record
    time_difference = datetime.now(timezone.utc) - user.timestamp

    # Convert the time difference to a human-readable format
    if time_difference < timedelta(minutes=1):
        time_ago = 'just now'
    elif time_difference < timedelta(hours=1):
        minutes_ago = int(time_difference.total_seconds() / 60)
        time_ago = f'{minutes_ago} minute{"s" if minutes_ago != 1 else ""} ago'
    elif time_difference < timedelta(days=1):
        hours_ago = int(time_difference.total_seconds() / 3600)
        time_ago = f'{hours_ago} hour{"s" if hours_ago != 1 else ""} ago'
    else:
        days_ago = time_difference.days
        time_ago = f'{days_ago} day{"s" if days_ago != 1 else ""} ago'

    if user is None:
        # Handle the error, e.g., by returning an error message or a default page
        return render_template('error.html')

    return render_template('index.html', engagement=user.total_engagement, time_ago=time_ago)

# Only fetch once an hour to maintain measurement standards
from app import fetch_tweets_and_update_engagement

def run_cron_job():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_tweets_and_update_engagement())

if __name__ == "__main__":
    run_cron_job()






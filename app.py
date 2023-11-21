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


load_dotenv()
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://")
db = SQLAlchemy(app)
Bootstrap(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
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
    with app.app_context():
        try:
            # Add your accounts
            await api.pool.add_account("Mglamour2465", "Caniggia0", "mikeglamour8@gmail.com", "445841")
            await api.pool.add_account("MoleculePe43018", "Caniggia0", "postmolecule@gmail.com", "166112")
            await api.pool.login_all()

            # List of users for whom you want to track engagement
            users = ["SergioChouza", "CarlosMaslaton"]

            for user in users:
                # Get the last 20 tweets for the user using twscrape
                tweets = await twscrape.search(f"from:{user}", limit=20)

                # Process engagement metrics for each tweet
                for tweet in tweets:
                    likes = tweet["likeCount"]
                    retweets = tweet["retweetCount"]
                    replies = tweet["replyCount"]

                    # Create or update the tweet record in the database
                    db_tweet = Tweet.query.filter_by(id=tweet["id"]).first()
                    if db_tweet is None:
                        db_tweet = Tweet(id=tweet["id"], user_id=user.id, content=tweet["content"], likes=likes, retweets=retweets, replies=replies)
                        db.session.add(db_tweet)
                    else:
                        db_tweet.likes = likes
                        db_tweet.retweets = retweets
                        db_tweet.replies = replies

            db.session.commit()

        except Exception as e:
            # Log the exception details
            app.logger.error(f"Error in fetch_tweets_and_update_engagement: {str(e)}")
            return str(e)

# Run the function
loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_tweets_and_update_engagement())


def get_current_toxicity():
    # Setup last fetch as the instance of db within this scope
    total_increase_record = TotalIncrease.query.order_by(TotalIncrease.timestamp.desc()).first()
    if total_increase_record is None:
        app.logger.warning("No TotalIncrease records found")
        return jsonify({"error": "No TotalIncrease records found"})
    # Retrieve the total tweet increase of last fetch
    total_tweet_increase = total_increase_record.total_tweet_increase
    app.logger.info(f"Number of TotalIncrease records: {len(TotalIncrease.query.all())}")
    # The app´s principal logic is represented here
    if total_tweet_increase < 3:
        return jsonify({"toxicity": "Green"})
    elif total_tweet_increase < 5:
        return jsonify({"toxicity": "Yellow"})
    else:
        return jsonify({"toxicity": "Red"})
@app.route('/toxicity', methods=['GET'])
def toxicity_route():
    return get_current_toxicity()
from dateutil.parser import parse
@app.route('/tweet_activity', methods=['GET'])
def tweet_activity_route():
    # Fetch the last four hours of TotalIncrease records
    four_hours_ago = datetime.now(timezone.utc) - timedelta(hours=4)
    records = TotalIncrease.query.filter(TotalIncrease.timestamp >= four_hours_ago).all()
    # Ensure all timestamps are timezone-aware
    for record in records:
        if record.timestamp.tzinfo is None or record.timestamp.tzinfo.utcoffset(record.timestamp) is None:
            record.timestamp = record.timestamp.replace(tzinfo=timezone.utc)
    # Calculate the total tweet increase for each hour
    increases = []
    for i in range(4):
        start_time = datetime.now(timezone.utc) - timedelta(hours=i+1)
        end_time = datetime.now(timezone.utc) - timedelta(hours=i)
        increase = sum(record.total_tweet_increase for record in records if start_time <= record.timestamp < end_time)
        increases.append((start_time, increase))
    # Check for any spikes in tweet activity
    spike_times = []
    for i in range(1, 4):
        if increases[i][1] > 2 * sum(increase[1] for increase in increases[:i]):
            spike_times.append(increases[i][0])
    if spike_times:
        message = f"Spikes at the following times: {', '.join(time.strftime('%H:%M') for time in spike_times)}"
    else:
        message = "No significant spike in tweet activity in the last four hours."
    return jsonify({"message": message})

@app.route('/')
def index():
    tweet_activity_data = tweet_activity_route().get_json()
    toxicity_data = get_current_toxicity().get_json()
    tweet_activity = tweet_activity_data.get('message')
    toxicity = toxicity_data.get('toxicity')
        # Retrieve the most recent TotalIncrease record from the database
    total_increase = TotalIncrease.query.order_by(TotalIncrease.timestamp.desc()).limit(1).first()

    # Calculate the time difference between the current time and the timestamp of the most recent TotalIncrease record
    time_difference = datetime.now(timezone.utc) - total_increase.timestamp

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
    if tweet_activity is None or toxicity is None:
        # Handle the error, e.g., by returning an error message or a default page
        return render_template('error.html')
    return render_template('index.html', tweet_activity=tweet_activity, toxicity=toxicity, time_ago=time_ago)
# Only fetch once an hour to maintain measurement standards
from app import fetch_tweets_and_update_counts

def run_cron_job():
    fetch_tweets_and_update_counts()

if __name__ == "__main__":
    run_cron_job()





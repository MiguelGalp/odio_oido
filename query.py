# ODIO-OIDO -- EL SCRIPT NO FUNCIONA DESDE IPs "OFICIALES" (COMO RENDER O FLIGHT) X BLOQUEO DE TWITTER
# FETCH DE LA DATA DE INTERACCON DE USUARIOS "CRUDOS" 
# VER FRECUENCIA DE CRON WORKER PARA OPTIMIZAR ÍNDICE EN "TIEMPO REAL" 

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

import asyncio
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime, timezone, timedelta
from dateutil.parser import parse

from twscrape import API, gather
from twscrape.logger import set_log_level
from threading import Timer
import time


load_dotenv()
app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://")
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_timeout': 600,  # Timeout in seconds
}
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
    content = db.Column(db.String(10000))
    likes = db.Column(db.Integer)
    retweets = db.Column(db.Integer)
    replies = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
class FetchTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('fetch_times', lazy=True))
    last_fetched = db.Column(db.DateTime)
    tweet_increase = db.Column(db.Integer)
class TotalIncrease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=True))
    total_tweet_engagement = db.Column(db.Integer)
try:
    with app.app_context():
        # Create the database tables
        db.create_all()
except Exception as e:
    print(f"Database error: {str(e)}")

async def fetch_tweets_and_update_engagement():
    api = API()  # or API("path-to.db") - default is `accounts.db`
    # Add your accounts
    await api.pool.add_account("Ver-Cuentas-Para-Scrapear")
    await api.pool.add_account("Ver-Cuentas-Para-Scrapear")
    await api.pool.login_all()

    with app.app_context():
        # Initialize total_increase
        total_increase = 0
        # Initialize hate_words
        hate_words = ["Ver-Lista-De-Palabras-Tóxicas"]  # Replace with actual words
        hate_tweet = None
        try:
            # List of users for whom you want to track engagement
            usernames = [INFO_SENSIBLE_DE_USUARIOS_REALES]
            total_tweet_engagement = 0  # Initialize total_tweet_engagement
            for username in usernames:
                # Get the user ID from the username
                user = await api.user_by_login(username)
                user_id = user.id

                # Get the timestamp of the most recent tweet we've already processed for this user
                last_tweet_timestamp = db.session.query(db.func.max(Tweet.timestamp)).filter_by(user_id=user_id).scalar()

                # Initialize engagement metrics
                total_likes = 0
                total_retweets = 0
                total_replies = 0

                # Get the tweets for the user using twscrape
                tweets = await gather(api.user_tweets(user_id, limit=10))

                # Process engagement metrics for each tweet
                for tweet in tweets:
                    # Convert the tweet date to an offset-naive datetime object in UTC
                    tweet_date = tweet.date.replace(tzinfo=None)

                    # Only process the tweet if it's more recent than the last processed tweet
                    if last_tweet_timestamp is None or tweet_date > last_tweet_timestamp:
                        likes = tweet.likeCount
                        retweets = tweet.retweetCount
                        replies = tweet.replyCount

                        # Update total engagement metrics
                        total_likes += likes
                        total_retweets += retweets
                        total_replies += replies

                        # Update total_tweet_engagement
                        total_tweet_engagement += likes + retweets + replies

                        # Create or update the tweet record in the database
                        db_tweet = Tweet.query.filter_by(id=tweet.id).first()
                        if db_tweet is None:
                            # Ensure the user exists in the user table
                            db_user = User.query.filter_by(id=user_id).first()
                            if db_user is None:
                                db_user = User(id=user_id, name=username)
                                db.session.add(db_user)

                            db_tweet = Tweet(id=tweet.id, user_id=user_id, likes=likes, retweets=retweets, replies=replies, timestamp=tweet.date)
                            db.session.add(db_tweet)
                        else:
                            db_tweet.likes = likes
                            db_tweet.retweets = retweets
                            db_tweet.replies = replies
                            db_tweet.timestamp = tweet.date

                        # Check if tweet content contains any hate word
                        if any(hate_word in tweet.rawContent for hate_word in hate_words):
                            db_tweet.content = tweet.rawContent
                            db.session.commit()
                            break

                total_increase += total_tweet_engagement

                # Ensure the user exists in the user table
                db_user = User.query.filter_by(id=user_id).first()
                if db_user is None:
                    db_user = User(id=user_id, name=username, total_engagement=total_tweet_engagement)
                    db.session.add(db_user)
                else:
                    db_user.name = username
                    db_user.total_engagement = total_tweet_engagement

            # Get the current time
            now = datetime.now()
            total_tweets = TotalIncrease(timestamp=now, total_tweet_engagement=total_increase)  # Use total_increase
            # Add the new record to the session
            db.session.add(total_tweets)

            db.session.commit()
        except Exception as e:
            # Log the exception details
            app.logger.error(f"Error in fetch_tweets_and_update_engagement: {str(e)}")
            return str(e)

from app import fetch_tweets_and_update_engagement

def run_cron_job():
    # Create a new event loop
    loop = asyncio.new_event_loop()

    # Run the fetch function
    loop.run_until_complete(fetch_tweets_and_update_engagement())

    # Schedule the next run in half hour (1800 seconds)
    Timer(1800, run_cron_job).start()

if __name__ == "__main__":
    # Start the cron job
    run_cron_job()

    # Keep the main program running
    while True:
        time.sleep(1)




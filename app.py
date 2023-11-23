from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

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
    # Ensure the session is up-to-date with the latest state of the database
    db.session.commit()

    # Retrieve the most recent User record from the database
    user = User.query.order_by(User.id.desc()).first()

    if user is None:
        # Handle the error, e.g., by returning an error message or a default page
        return render_template('error.html')

    return render_template('index.html', engagement=user.total_engagement)









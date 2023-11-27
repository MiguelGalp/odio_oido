from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_babelex import format_datetime
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
    total_tweet_engagement = db.Column(db.Integer)
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

@app.route('/')
def index():
    # Ensure the session is up-to-date with the latest state of the database
    db.session.commit()

    # Retrieve the most recent User records from the database
    users = User.query.order_by(User.id.desc()).limit(3).all()

    # Retrieve the timestamp of the most recent TotalIncrease record
    last_fetch = TotalIncrease.query.order_by(TotalIncrease.timestamp.desc()).first().timestamp

    if len(users) < 2:
        # Handle the error, e.g., by returning an error message or a default page
        return render_template('error.html')

    return render_template('index.html', engagement1=users[0].total_engagement, engagement2=users[1].total_engagement, engagement3=users[2].total_engagement, last_fetch=format_datetime(last_fetch))







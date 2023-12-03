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
    # Get all users
    users = User.query.all()
    if not users:
        app.logger.warning("No User records found")
        return jsonify({"error": "No User records found"})

    # Number of followers for each user
    followers = [89000.0, 330000.0, 1300000.0]

    # Initialize a list to store user engagement
    user_engagements = []

    # Calculate total engagement for all users
    for i, user in enumerate(users):
        if len(user.tweets) == 20:
            total_engagement = user.total_engagement
        else:
            total_engagement = user.total_engagement / len(user.tweets)
        
        normalized_engagement = total_engagement / followers[i]
        app.logger.info(f"Normalized engagement of user {user.name}: {normalized_engagement}")

        # Add the user and their engagement to the list
        user_engagements.append((user.name, normalized_engagement))

    # Sort the list by engagement in descending order
    user_engagements.sort(key=lambda x: x[1], reverse=True)

    # Convert the sorted list to a dictionary while maintaining order
    user_ranking = {}
    for name, engagement in user_engagements:
        user_ranking[name] = engagement

    # Return the user ranking
    return jsonify(user_ranking)

@app.route('/engagement', methods=['GET'])
def engagement_route():
    return get_current_engagement()

@app.route('/')
def index():
    # Ensure the session is up-to-date with the latest state of the database
    db.session.commit()

    # Retrieve the most recent User records from the database
    users = User.query.order_by(User.id.desc()).limit(3).all()

    # Get the current time and 12 hours ago
    now = datetime.now()
    twelve_hours_ago = now - timedelta(hours=12)

    # Retrieve the total_increase records from the last 12 hours
    total_increases = TotalIncrease.query.filter(TotalIncrease.timestamp.between(twelve_hours_ago, now)).order_by(TotalIncrease.timestamp.asc()).all()

    # Convert the total_increase records into a list of dictionaries
    data = [{"timestamp": format_datetime(ti.timestamp), "total_tweet_engagement": ti.total_tweet_engagement} for ti in total_increases]

    # Retrieve the timestamp of the most recent TotalIncrease record
    last_fetch = TotalIncrease.query.order_by(TotalIncrease.timestamp.desc()).first()
    if last_fetch is not None:
        last_fetch = last_fetch.timestamp
    else:
        last_fetch = "No fetches yet"

    if len(users) < 2:
        # Handle the error, e.g., by returning an error message or a default page
        return render_template('error.html')

    return render_template('index.html', engagement1=users[0].total_engagement, engagement2=users[1].total_engagement, engagement3=users[2].total_engagement, last_fetch=format_datetime(last_fetch), data=data)







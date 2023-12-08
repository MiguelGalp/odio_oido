from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_babelex import format_datetime
import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime, timezone, timedelta
from dateutil.parser import parse
from collections import OrderedDict
import logging
import math




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
    users = User.query.order_by(User.id.asc()).limit(6).all()
    if not users:
        app.logger.warning("No User records found")
        return jsonify({"error": "No User records found"})

    # Number of followers for each user
    followers = [340000.0, 3300000.0, 3300000.0, 125000.0, 345000.0, 100000.0]

    # Initialize a list to store user engagement
    user_engagements = []

    # Calculate total engagement for all users
    for i, user in enumerate(users):
        # Normalize the engagement value according to the number of followers
        normalized_engagement = user.total_engagement / followers[i]
        
        # Add the user and their normalized engagement to the list
        user_engagements.append((user.name, normalized_engagement))

    # Sort the list by engagement in descending order
    user_engagements.sort(key=lambda x: x[1], reverse=True)

    # Return the sorted list of tuples
    return user_engagements



@app.route('/engagement', methods=['GET'])
def engagement_route():
    return get_current_engagement()

@app.route('/')
def index():
    # Ensure the session is up-to-date with the latest state of the database
    db.session.commit()

    # Constant to increase the number of repetitions
    CONSTANT_FACTOR = 10000

    # Retrieve the most recent User records from the database
    users = User.query.order_by(User.id.asc()).limit(6).all()

    # Retrieve the last total_tweet_engagement value
    total_tweet_engagement = TotalIncrease.query.order_by(TotalIncrease.timestamp.desc()).first().total_tweet_engagement

    # Define the phrases
    phrases = ["El rey de los tuertos", "La cocinera del dolor", "Profesor Doolittle desde la Torre de Cristal", "La nada misma", "Lo negro absoluto", "El barrabrava que te cuida"]

    # Initialize the new list
    new_list = []

    # Get the user ranking
    user_ranking = get_current_engagement()

    # Create a list of user names
    user_names = [user.name for user in users]

    # For each user, repeat their corresponding phrase according to their relative weight in the total engagement
    for user in user_ranking:
        weight = (user[1] / total_tweet_engagement) * CONSTANT_FACTOR
        repetitions = max(1, int(weight * len(users) * CONSTANT_FACTOR))
        partial_repetition = weight * len(users) * CONSTANT_FACTOR - repetitions
        phrase = phrases[user_names.index(user[0])]
        new_list.extend([phrase] * repetitions)
        if partial_repetition > 0:
            cut_off = int(len(phrase) * partial_repetition)
            new_list.append(phrase[:cut_off])



    # Get the total engagement of all users
    engagements = [user.total_engagement for user in users]
    
    # Retrieve the timestamp of the most recent TotalIncrease record
    last_fetch = TotalIncrease.query.order_by(TotalIncrease.timestamp.desc()).first()
    if last_fetch is not None:
        last_fetch = last_fetch.timestamp
    else:
        last_fetch = "No fetches yet"

    if len(users) < 2:
        # Handle the error, e.g., by returning an error message or a default page
        return render_template('error.html')
    print(new_list)
    print(f"Weight for {user[0]}: {weight}")
    print(f"Repetitions for {user[0]}: {repetitions}")
    print(f"Partial repetition for {user[0]}: {partial_repetition}")

    return render_template('index.html', engagements=engagements, last_fetch=format_datetime(last_fetch), new_list=new_list)









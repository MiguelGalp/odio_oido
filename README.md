# CS50x Final Project. XTEMP: A Discourse Temperature Tracker For Twitter (ARGENTINA/POLITICS VERSION).

This Flask app is designed to track the Twitter activity of specific users in real-time and determine the level of engagement based on the increase in tweets over a certain period of time. The app uses SQLAlchemy to interact with a PostgreSQL database and Tweepy to access the Twitter API.

## Installation

1. Clone the repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory of the project and add your Twitter API credentials and database URL in the following format:

```
TWITTER_CONSUMER_KEY=<your_consumer_key>
TWITTER_CONSUMER_SECRET=<your_consumer_secret>
TWITTER_ACCESS_TOKEN=<your_access_token>
TWITTER_ACCESS_TOKEN_SECRET=<your_access_token_secret>
DATABASE_URL=<your_database_url>
```

4. Connect your GitHub repo to Render to generate the [Cron Job]([https://link-url-here.org](https://render.com/docs/cronjobs))

5. Run the app using `python app.py`.

## Usage

The app has two routes:

1. `/toxicity`: This route returns the current level of toxicity based on the increase in tweets over a certain period of time. The toxicity level is determined as follows:

- Green: If the total tweet increase is less than 3.
- Yellow: If the total tweet increase is between 3 and 5.
- Red: If the total tweet increase is greater than 5.

2. `/tweet_activity`: This route returns the total tweet increase for each of the last four hours and checks for any significant spikes in tweet activity during that time.

The app also has a homepage (`/`) that displays the current level of toxicity, the total tweet increase for the last hour, and the time since the last fetch.

## Database

The app uses a PostgreSQL database to store information about users, their tweet counts, and the times at which their tweet counts were last fetched. The database also stores information about the total tweet increase for each fetch.

## Cron Job

The app includes a `run_cron_job()` function that fetches the latest tweet counts for the specified users and updates the database. This function is set to run every half hour to maintain measurement standards.

## Deploy

You can deploy your own XTemp. into Render. See [here](https://twitter-temperature.onrender.com/)

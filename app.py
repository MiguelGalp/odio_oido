from flask import Flask, jsonify, request, abort, Response
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_babelex import format_datetime
import pytz 
import os
import ast
from flask import Flask, render_template
from flask_babelex import format_datetime
from flask_bootstrap import Bootstrap
from datetime import datetime, timezone, timedelta
from dateutil.parser import parse
from collections import OrderedDict
from functools import wraps
import json
import uuid

load_dotenv()

# Lee los datos de los grupos a partir de las variables de entorno y los evalúa
groups = ast.literal_eval(os.environ.get('GROUPS', '{}'))
front_groups = ast.literal_eval(os.environ.get('FRONT_GROUPS', '{}'))
front_chile = ast.literal_eval(os.environ.get('FRONT_CHILE', '{}'))

# Combina todos los usuarios de los grupos
all_users = list(set(user for group in groups.values() for user in group) 
                 | set(user for group in front_groups.values() for user in group) 
                 | set(user for group in front_chile.values() for user in group))

# Crea alias para todos los usuarios
user_aliases = {user: str(uuid.uuid4()) for user in all_users}

# Reemplaza los nombres de usuario reales por sus alias en los datos de grupo
for group, users in groups.items():
    groups[group] = [user_aliases[user] for user in users]

for group, users in front_groups.items():
    front_groups[group] = [user_aliases[user] for user in users]

for group, users in front_chile.items():
    front_chile[group] = [user_aliases[user] for user in users]


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
        # Crea las tablas en la base de datos
        db.create_all()
except Exception as e:
    print(f"Database error: {str(e)}")

def check_auth(username, password):
    # Auth check
    return username == 'admin' and password == 'secret'

def authenticate():
    # Sends a 401 response that enables basic auth
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

def calculate_engagement(tweet):
    likes = tweet.likes
    retweets = tweet.retweets
    replies = tweet.replies
    
    # Define pesos relativos para las interacciones (tags: investigación, pregunta, calidad de datos)
    weights = {'likes': 1, 'retweets': 2, 'replies': 1.5}
    
    # Define un ciclo de vida: el tweet pierde mitad de su relevancia en 3 horas
    hours_since_tweet = (datetime.utcnow() - tweet.timestamp).total_seconds() / 3600
    decay_factor = 0.5 ** (hours_since_tweet / 6)  # Half-life of 6 hours
    
    engagement_score = (likes*weights['likes'] + retweets*weights['retweets'] + replies*weights['replies']) * decay_factor
    
    return engagement_score

def calculate_normalized_engagement(total_engagement, num_tweets, followers, time_window=24):
    # Normaliza de acuerdo a un promedio de tweets diario (tags: investigación, pregunta, calidad datos)
    avg_tweets_per_day = num_tweets / time_window
    
    # Normaliza ajustado por ciclo de vida (tags: documentación, pregunta --a mí mismo)
    time_weight = 0.5
    adjusted_engagement = total_engagement * (1 + time_weight * avg_tweets_per_day)
    
    # Normaliza por número de seguidores
    normalized_engagement = float(adjusted_engagement / followers)
    
    return normalized_engagement

from datetime import datetime, timedelta

def get_current_engagement(max_possible_engagement, groups_to_consider):
    try:
        # Define el número de seguidores de cada grupo (tags: complejo, arquitectura, mejora)
        group_followers = {
            '#AmplificaLoPeor': 31400 + 1700000,
            '#AnticipaLoPeor': 6100000 + 2600000,
            '#EsCondescendiente': 366500 + 95200,
            '#CuestionaLoIncuestionable' : 875400 + 3300000,
            '#Trollea' : 362900 + 76100,
            '#Descontextualiza' : 130000 + 153900,
            '#TeInsulta' : 362600 + 76100,
            '#TeMiente' : 2800000 + 345100,
            '#TeInvisibiliza' : 174200 + 470800,
            '#TeAmenaza' : 1200000 + 349000
        }

        # Inicializa el diccionario que guarda las interacciones 
        group_engagements = {group: 0 for group in groups_to_consider}

        # Calcula temperatura de todos los grupos
        a_day_ago = datetime.utcnow() - timedelta(days=1)
        for group, aliases in groups_to_consider.items():
            for alias in aliases:
                user_name = next(user for user, user_alias in user_aliases.items() if user_alias == alias)
                user = User.query.filter_by(name=user_name).first()
                if user:
                    recent_tweets = Tweet.query.filter(Tweet.user_id == user.id, Tweet.timestamp >= a_day_ago).all()
                    engagements = [calculate_engagement(tweet) for tweet in recent_tweets]
                    total_engagement = sum(engagements)
                    max_engagement = max(engagements) if engagements else 0
                    if recent_tweets:
                        normalized_engagement = calculate_normalized_engagement(total_engagement, max_engagement, len(recent_tweets), group_followers[group]) / max_possible_engagement
                        group_engagements[group] += normalized_engagement

        # Calcula total engagement y encuentra el grupo más tóxico / con más temperatura
        total_engagement = 0
        max_engagement_group = None
        max_engagement = 0
        for group, engagement in group_engagements.items():
            total_engagement += engagement
            if engagement > max_engagement:
                max_engagement = engagement
                max_engagement_group = group

        # Ordena el diccionario por temperatura en orden descendiente
        sorted_group_engagements = sorted(group_engagements.items(), key=lambda x: x[1], reverse=True)
        print(sorted_group_engagements) 
        return sorted_group_engagements, total_engagement, max_engagement_group

    except Exception as e:
        app.logger.error(f"Error in get_current_engagement: {str(e)}")
        raise



@app.route('/api/total_engagement_argentina', methods=['GET'])
def total_engagement_argentina_route():
    max_possible_engagement = 100000.0
    group_engagements, total_engagement, max_engagement_group = get_current_engagement(max_possible_engagement, front_groups)
    return jsonify({'total_engagement': total_engagement, 'max_engagement_group': max_engagement_group})

@app.route('/api/total_engagement_chile', methods=['GET'])
def total_engagement_chile_route():
    max_possible_engagement = 100000.0  # el máximo posible (tags: pregunta, investigación...)
    group_engagements, total_engagement, max_engagement_group = get_current_engagement(max_possible_engagement, front_chile)
    return jsonify({'total_engagement': total_engagement, 'max_engagement_group': max_engagement_group})


@app.route('/engagement_by_groups', methods=['POST'])
def engagement_by_groups_route():
    # Define el máximo de interacción (tags: pregunta, investigación...)
    max_possible_engagement = 100000.0 

    # Define qué grupo es el default
    groups = request.json['front_groups']

    # Define número de seguidores del grupo default
    all_group_followers = {
        '#AmplificaLoPeor': 31400 + 1700000,
        '#AnticipaLoPeor': 6100000 + 2600000,
        '#EsCondescendiente': 366500 + 95200,
        '#CuestionaLoIncuestionable' : 875400 + 3300000,
        '#Trollea' : 362900 + 76100,
        '#Descontextualiza' : 130000 + 153900,
        '#TeInsulta' : 362600 + 76100,
        '#TeMiente' : 2800000 + 345100,
        '#TeInvisibiliza' : 174200 + 470800,
        '#TeAmenaza' : 1200000 + 349000
    }

    # Toma solo los seguidores de los grupos del default
    group_followers = {group: all_group_followers[group] for group in groups}

    # Toma la data de interacción de los grupos defaulta
    group_engagements = get_engagement_by_groups(groups, group_followers, max_possible_engagement)
    print(group_engagements) 
    return jsonify(group_engagements)

def get_engagement_by_groups(front_groups, group_followers, max_possible_engagement):
    a_day_ago = datetime.utcnow() - timedelta(days=1)
    group_engagements = {group: 0 for group in front_groups}

    # Calcula el total de interacciones de los grupos default
    for group_name, aliases in front_groups.items():
        total_engagement = 0
        for alias in aliases:
            user_name = next(user for user, user_alias in user_aliases.items() if user_alias == alias)
            user = User.query.filter_by(name=user_name).first()
            if user:
                recent_tweets = Tweet.query.filter(Tweet.user_id == user.id, Tweet.timestamp >= a_day_ago).all()
                for tweet in recent_tweets:
                    engagement = calculate_engagement(tweet)
                    normalized_engagement = calculate_normalized_engagement(engagement, max_possible_engagement, len(recent_tweets), group_followers[group_name]) / max_possible_engagement
                    total_engagement += normalized_engagement

        group_engagements[group_name] = total_engagement

    # Ordena el dict por interacciones en orden desc
    sorted_group_engagements = sorted(group_engagements.items(), key=lambda x: x[1], reverse=True)

    return sorted_group_engagements


@app.route('/api/front_groups', methods=['GET'])
def front_groups_route():
    # Devuelve las listas de aliases
    return jsonify(front_groups)

@app.route('/api/front_chile', methods=['GET'])
def front_chile_route():
    # Devuelve las listas de aliases
    return jsonify(front_chile)

@app.route('/')
def index():

    max_possible_engagement = 100000.0 

    # Obtiene las métricas de interacción actuales, las métricas de interacción totales y el grupo con mayor interacción
    group_engagements, total_engagement, max_engagement_group = get_current_engagement(max_possible_engagement, front_groups)


    # Obtiene el último TotalIncrease (para calcular picos)
    last_total_increase = TotalIncrease.query.order_by(TotalIncrease.timestamp.desc()).first()
    
    # Obtiene los aumentos totales en las últimas 6 horas
    six_hours_ago = datetime.now() - timedelta(hours=6)
    total_increases = TotalIncrease.query.filter(TotalIncrease.timestamp >= six_hours_ago).order_by(TotalIncrease.timestamp.desc()).all()

    # Calcula el promedio de las métricas de interacción en las últimas 6 horas
    average_engagement = sum([increase.total_tweet_engagement for increase in total_increases]) / len(total_increases) if total_increases else 0

    # Busca ocurrencias pico
    peak_occurrences = []
    for increase in total_increases:
        if increase.total_tweet_engagement > average_engagement * 1.1:  # 1.5 es un ejemplo de "desvío" más pronunciado
            peak_occurrences.append((increase.timestamp, increase.total_tweet_engagement))

    # Asegurar total_increases contenga al menos dos registros
    if len(total_increases) >= 2:
        # Obteniendo los dos últimos registros
        latest_engagement = total_increases[0].total_tweet_engagement
        second_latest_engagement = total_increases[1].total_tweet_engagement
    # Calcular la diferencia
        difference = latest_engagement - second_latest_engagement
    else:
    # Si no hay suficientes registros
        difference = 0  # O cualquier manejo de error 

    # Determinar el engagement_level basado en la diferencia
    if difference <= 12000:
        engagement_level = "BAJA"
    elif 12001 <= difference <= 15000:
        engagement_level = "MEDIA"
    else:
        engagement_level = "ALTA"
    
    # Obtiene el tweet con contenido de discurso de odio por orden descendente temporal (el último?)
    hate_tweet = Tweet.query.filter(Tweet.content.isnot(None)).order_by(Tweet.id.desc()).first()

    # Comprueba si se encontró un tweet de odio
    if hate_tweet is not None:
        hate_tweet_content = hate_tweet.content
    else:
        hate_tweet_content = None

    return render_template('index.html', timedelta=timedelta, hate_tweet_content=hate_tweet_content, datetime=datetime, pytz=pytz, total_engagement=total_engagement, max_engagement_group=max_engagement_group, peak_occurrences=peak_occurrences, engagement_level=engagement_level, last_total_increase=last_total_increase, min=min)







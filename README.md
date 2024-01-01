# Análisis de Interacciones en Twitter

Este proyecto tiene como objetivo analizar y clasificar las interacciones de los usuarios de Twitter. Se recogen los tweets de los usuarios y se calcula una puntuación de compromiso basada en varios factores como los likes, retweets y respuestas que reciben sus tweets.

## Tecnología 🛠️

El proyecto está construido con Python y utiliza Flask para el backend. Para el almacenamiento de datos, se utiliza una base de datos PostgreSQL. Las consultas a la base de datos se realizan utilizando SQLAlchemy.

## Rutas 🚀

El proyecto consta de varias rutas que realizan diferentes funciones:

1. `calculate_engagement(tweet)`: Esta ruta calcula la puntuación de compromiso para un tweet individual basándose en los likes, retweets y respuestas que ha recibido.

2. `calculate_normalized_engagement(total_engagement, num_tweets, followers, time_window=24)`: Esta ruta normaliza la puntuación de compromiso de un usuario basándose en el número total de tweets que ha publicado y el número de seguidores que tiene.

3. `get_current_engagement()`: Esta ruta recopila las puntuaciones de compromiso de todos los usuarios y las devuelve en una lista ordenada.

## Limitaciones ⚠️

El proyecto tiene algunas limitaciones:

1. La puntuación de compromiso se basa únicamente en los likes, retweets y respuestas. No se tienen en cuenta otros factores que podrían influir en el compromiso del usuario, como el contenido del tweet o el momento en que se publicó.

2. El proyecto recoge los tweets de los usuarios una vez por hora. Esto significa que los tweets que se publiquen fuera de este intervalo no se tendrán en cuenta en la puntuación de compromiso.

3. El proyecto asume que el número de seguidores de un usuario es un indicador de su nivel de compromiso. Sin embargo, este no siempre es el caso, ya que un usuario puede tener muchos seguidores pero recibir poco compromiso en sus tweets.

## Contribuyendo 🖇️

Por favor lee el CONTRIBUTING.md para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo LICENSE.md para detalles

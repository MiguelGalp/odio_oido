# El opio de los pueblos, Twitter/X Trackeo de Interacciones por tendencias, 2024

El opio de los pueblos es un servicio web para el análisis de datos en tiempo real. Conocé más sobre el comportamiento de las tendencias en X/Twitter. 

## Tecnologías utilizadas

- **Python**: Utilizado para el backend.
- **Flask**: Framework de Python para crear la aplicación web.
- **JavaScript**: Para la funcionalidad del lado del cliente, incluyendo solicitudes AJAX al servidor (SQLAlchemy)

## Rutas disponibles

- `GET /api/front_groups`: Devuelve un JSON con los grupos y usuarios para la interfaz de Argentina.
- `GET /api/front_chile`: Devuelve un JSON con los grupos y usuarios para la interfaz de Chile.
- `POST /engagement_by_groups`: Acepta un JSON con los grupos y usuarios seleccionados y devuelve un JSON con los compromisos de los grupos.

## Usos del servicio web

Este servicio web puede ser utilizado para analizar tendencias en Twitter, en tiempo real. Esto puede ser útil para las planificar campañas y en general como termómetros de los tópicos principales en cada país. 

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

## Explicación detallada del proyecto

Este proyecto rastrea y analiza las interacciones de los tweets de las últimas 24 horas de los usuarios especificados. Las interacciones medidas incluyen likes, retweets y respuestas a los tweets. Se da más peso tanto a los tweets más recientes como a los tweets individuales con más interacciones. 

Por favor, ten en cuenta que este repositorio solo contiene el código del frontend de la aplicación. El código del backend que realiza la búsqueda de tweets no está incluido, por lo que no se puede hacer un despliegue completo de la aplicación a partir de este repositorio.

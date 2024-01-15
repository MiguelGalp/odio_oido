# Twitter/X Compromisos 2024

Twitter/X Compromisos 2024 es un servicio web para el análisis de datos en tiempo real destinado a campañas de marketing.

## Tecnologías utilizadas

- **Python**: Lenguaje de programación principal utilizado para el backend.
- **Flask**: Framework de Python utilizado para crear la aplicación web.
- **JavaScript**: Utilizado para la funcionalidad del lado del cliente, incluyendo las solicitudes AJAX al servidor.
- **HTML/CSS**: Utilizados para la estructura y el estilo de la página web.

## Rutas disponibles

- `GET /api/front_groups`: Devuelve un JSON con los grupos y usuarios para la interfaz de Argentina.
- `GET /api/front_chile`: Devuelve un JSON con los grupos y usuarios para la interfaz de Chile.
- `POST /engagement_by_groups`: Acepta un JSON con los grupos y usuarios seleccionados y devuelve un JSON con los compromisos de los grupos.

## Usos del servicio web

Este servicio web puede ser utilizado para analizar el compromiso de diferentes grupos de usuarios de Twitter en tiempo real. Esto puede ser útil para las campañas de marketing para entender mejor a su audiencia y ajustar sus estrategias en consecuencia.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

## Explicación detallada del proyecto

Este proyecto rastrea y analiza las interacciones de los tweets de las últimas 24 horas de los usuarios especificados. Las interacciones medidas incluyen likes, retweets y respuestas a los tweets. Se da más peso tanto a los tweets más recientes como a los tweets individuales con más interacciones. 

Por favor, ten en cuenta que este repositorio solo contiene el código del frontend de la aplicación. El código del backend que realiza la búsqueda de tweets no está incluido, por lo que no se puede hacer un despliegue completo de la aplicación a partir de este repositorio.

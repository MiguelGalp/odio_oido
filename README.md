# El opio de los pueblos. Twitter/X trackeado por tópicos y por país, 2024

El opio de los pueblos es un servicio web que analiza datos en tiempo real. Conocé más sobre el comportamiento de las tendencias en X/Twitter. 

## Tecnologías utilizadas

- **Python**: Utilizado para el backend.
- **Flask**: Framework de Python para crear la aplicación web.
- **JavaScript**: Para la funcionalidad del lado del cliente.
  
## Usos del servicio web

Este servicio web puede ser utilizado para analizar tendencias en Twitter, en tiempo real. Esto puede ser útil para las planificar campañas y como termómetro de los tópicos principales en cada país. 

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.

## Explicación detallada del proyecto

Este proyecto rastrea y analiza las interacciones de los tweets de las últimas 24 horas dentro de los tópicos pre-cargados. Las interacciones trackeadas incluyen likes, retweets y respuestas a cada tweet dentro de los tópicos pre-cargados (hard-codeados). Es un cálculo normalizado: se da más peso tanto a los tweets más recientes como a los tweets individuales con más interacciones. También se normaliza por número de seguidores de cada tópico. Por ahora hardcodedos.  

Tené en cuenta que este repositorio solo contiene el código del frontend de la aplicación. El código del backend que realiza la búsqueda de tweets no está incluido, por lo que no se puede hacer un deploy completo de la aplicación a partir de este repositorio. 

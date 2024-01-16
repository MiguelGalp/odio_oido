# El opio de los pueblos. Twitter/X trackeado por tópicos y por país, 2024

El opio de los pueblos es un MVP cuyo objetivo primordial es el de utilizar la idea de "espacio latente" para generar visualizaciones de datos en tiempo real. En términos de datos "duros", la app escrappea X/Twitter para obtener el nivel de "engagement" de un grupo de tweets que, a su vez, se agrupan a través de la idea de "dominio" o tópico ("deportes", "sociedad", "política", etc). Se trata de una estrategia derivada de la Asignación Latente de Dirichlet (ALD) o Latent Dirichlet Allocation (LDA), donde, [siguiendo a Wikipedia](https://es.wikipedia.org/wiki/Latent_Dirichlet_Allocation), "la clave es que las palabras siguen una hipótesis de bolsa de palabras o, más bien que el orden no importa, que el uso de una palabra es ser parte de un tema y que comunica la misma información sin importar dónde se encuentra en el documento". Si su marco teórico es correcto, la app daría cuenta del nivel de temperatura en el discurso de twitter por tópico (y hasta por país o región). 

En este momento la app permite visualizar cuatro espacios latentes, para la Argentina y Chile. Hacia el futuro, apunto a a generar los dominios de forma dinámica a través de la IA, que, luego de analizar los tweets, devolvería las agrupaciones de usuarios por tópico o dominio. 

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

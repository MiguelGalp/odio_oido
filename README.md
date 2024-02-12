<style>
    img {
        margin-right: 20px;
    }
</style>

<div align="center" width="100%">
    <h1>El opio de los pueblos</h1>
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://github.com/rolivencia/cuentoneta/assets/32349705/b0ea0659-3c9d-4c4f-9d14-ab60d50dd832">
        <img width="25%" alt="Argentina" src="static/public/Argentina.png">
    </picture>
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://github.com/rolivencia/cuentoneta/assets/32349705/b0ea0659-3c9d-4c4f-9d14-ab60d50dd832">
        <img width="25%" alt="Argentina" src="static/public/Chile.png">
    </picture>
</div>


---

# El opio de los pueblos. Twitter/X trackeado por LDA, 2024

El opio de los pueblos es un MVP que tiene como objetivo utilizar la idea de espacio latente para generar visualizaciones de datos en tiempo real (trackeo). En términos de datos duros, la app escrappea X/Twitter para obtener el nivel de interacciones de un grupo de tweets que, a su vez, se agrupan en dominios.

El dominio es una idea derivada de lo que se llama "Asignación Latente de Dirichlet (ALD)", donde, [según el artículo en Wikipedia](https://es.wikipedia.org/wiki/Latent_Dirichlet_Allocation), "la clave es que las palabras siguen una hipótesis de bolsa de palabras o, más bien que el orden no importa, que el uso de una palabra es ser parte de un tema y que comunica la misma información sin importar dónde se encuentra en el documento". 

Como resultado final la app da cuenta del nivel de temperatura en el discurso.

En este momento la app permite visualizar cuatro dominios, para la Argentina y Chile. En el "roadmap" apunto a generar los dominios de forma dinámica a través de la IA, que, luego de analizar los tweets, devolvería las agrupaciones de tweets.

## Tecnologías utilizadas

- **Python**: Utilizado para el backend.
- **Flask**: Framework de Python para crear la aplicación web.
- **JavaScript**: Para la funcionalidad del lado del cliente.

## Usos del servicio web

Los datos son en tiempo real hasta donde X/Twitter lo permite. Al momento, la máxima ventana de tiempo entre recuperaciones es de una hora. Ver abajo para más detalles acerca de los modelos de datos y las métricas utilizadas. 

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.

## Más detalles acerca de los datos generados.

Este proyecto rastrea y analiza las interacciones de los tweets de las últimas 24 horas. Se trata de un grupo de tweets (ver el modelo de tweet en la tabla descripta dentro de los modelos, en app.py) que representa la idea de dominio según lo define la teoría llamada LDA, "Asignación Latente de Dirichlet (ALD)" en español. Las interacciones trackeadas incluyen likes, retweets y respuestas a cada tweet. Es importante mencionar que cada tweet devuelve un cálculo normalizado de interacciones donde, dentro del período de 24hs, se da más peso tanto a los tweets más recientes como a los tweets individuales con más interacciones. También se normaliza por número de seguidores dentro de cada dominio. 

Por último: tené en cuenta que este repositorio solo contiene el código del frontend de la aplicación. El código del backend que realiza la búsqueda de tweets no está incluido, por lo que no se puede hacer un deploy completo de la aplicación a partir de este repositorio. 

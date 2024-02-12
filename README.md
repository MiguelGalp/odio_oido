<div align="center" width="100%">

## MVP: PROYECTO "EL OPIO DE LOS PUEBLOS"

<img src="static/public/Argentina.png" width="25%" alt="Argentina"> &nbsp; &nbsp; &nbsp; <img src="static/public/Chile.png" width="25%" alt="Chile">

</div>

**El opio de los pueblos** es un proyecto abierto y sin fines de lucro que tiene como objetivo visualizar métricas de redes sociales en tiempo real y hacerlo en el marco de una perspectiva crítica respecto a la generación de discurso.

En específico la propuesta es la de utilizar la "Asignación Latente de Dirichlet" (LDA según sus siglas en inglés) que, [según el artículo en Wikipedia](https://es.wikipedia.org/wiki/Latent_Dirichlet_Allocation) tiene como "clave que las palabras siguen una hipótesis de bolsa de palabras o, más bien que el orden no importa, que el uso de una palabra es ser parte de un tema y que comunica la misma información sin importar dónde se encuentra en el documento". 

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

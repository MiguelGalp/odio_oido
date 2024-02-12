<div align="center" width="100%"> 
<h1>PROYECTO "EL OPIO DE LOS PUEBLOS"</h1> 
  <picture> <img width="33%" alt="El opio de los pueblos" src="static/public/niña_arg.png"> </picture> </div> 

---

El opio de los pueblos es un desarrollo abierto y sin fines de lucro con el foco en las en redes sociales.

El proyecto se inscribe en el marco de las humanidades digitales (2.0) ya que, basada en datos en tiempo real, se analizan discursos desde una perspectiva <em>Bayesiana</em> ligado a la ligüística.

La propuesta plantea como eje metodológico utilizar la "Asignación Latente de Dirichlet" (LDA según sus siglas en inglés).[Según el artículo en Wikipedia](https://es.wikipedia.org/wiki/Latent_Dirichlet_Allocation), el LDA tiene como clave "el que las palabras siguen una hipótesis de **bolsa** o, más bien, que el orden no importa, que el uso de una palabra es ser parte de un tema [incluso sin ser explícito en el texto] y que comunica la misma información sin importar dónde se encuentra en el documento".

El opio de los pueblos tiene como objetivo viabilizar miradas críticas a las redes a la vez que brindar información relevante respecto a qué se está discutiendo regionalmente en redes sociales.  

---

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

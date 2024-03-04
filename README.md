<div align="center" width="100%"> 
<h1>PROYECTO ODIO OÍDO</h1> 
  <picture> <img width="33%" alt="Un plato vacío" src="static/public/listeningTwitter.jpeg"> </picture> 

<h1>UNA MEDIDA DE TOXICIDAD EN TWITTER, POR PAÍS. 24/7</h1><h3>Sumate al proyecto para dar un indicador fiable y ayudar en el uso responsable de las redes sociales.</h3> 
</div> 

---

## Índice de contenidos

- [Origen](#Origen)
- [Qué solución da la app](#Qué-solución-da-la-app)
- [Cómo funciona la app](#Cómo-funciona-la-app)
- [Cómo contribuir](#Cómo-contribuir-al-primer-release)
- [Misión, visión y valores](#misión-visión-y-valores)
- [Comunidad](#comunidad)
- [Licencias](#licencias)
- [Links de interés](#links-de-interés)

---

## Origen

***Odio oído*** surge como un desprendimiento de la iniciativa "*Ahora*" de la ONG [Atlanticx](wwww.atlanticx.org), dedicada a la innovación en artes. Se trata de un impulso de tipo laboratorio (investigación y desarrollo) que busca ampliar las bases de diálogo entre las artes y la realidad contemporánea a partir de generar y accesibiliar datos relevantes al campo "arte + ciencia y tecnología". Más información sobre "*Ahora*" en este enlace. 

## ¿Qué *solución* aporta el MVP?

*Odio oído*, en su versión MVP actual, construye un índice de probabilidad para la toxicidad en Twitter a partir de trackear grupos de usuarios adheridos a tópicos LDA **de segunda generación**: si el modelo LDA devuelve en primera instancia tópicos como "crisis en la argentina", nuestro modelo observa el grupo "**debates** (sobre) la crisis en la argentina" o "**polarización** (alrededor de) la crisis en la argentina". 

Al normalizar el trackeo de interacciones por número de seguidores, el MVP indica (en relación indirecta) la probabilidad de que un usuario "general" se encuentre con toxicidad. 

Este enfoque, además, permite:

- Debates sobre la responsabilidad en el uso de redes sociales.
- Un instrumento de consulta para instituciones o padres. 
- Un panorama comparativo para la toxicidad por país (por ahora regional) y por tipo de evento.

## ¿Cómo funciona el MVP?

EN DOS PASOS:

1. (Offline)

- Un script (query.py) extrae información de Twitter para alimentar la base de datos de la app con información actualizada cada X minutos.
- Los datos se organizan con un modelo LDA de dominios de segunda generación.
- Se controla la adherencia de los dominios a la toxicidad. 

2. (Online). 

- Se calcula la temperatura del discuso por dominio, normalizada por número de seguidores y ciclo de vida (relevancia temporal de cada tweet)
- Se visualiza la información (un dashborad en desarrollo)
- Se almacenan los resultados

Próximamente:

- Indicador general de toxicidad mediante pesos relativos a la actividad de cada grupo/dominio.

## ¿Cómo contribuir al primer release?

Objetivo: Crear un dashboard de toxicidad en Twitter con:

- Índice de probabilidad
- Causa principal de toxicidad
- Picos de toxicidad
- Contenido tóxico

Contribuciones:

- Calidad y ampliación de datos: verificar y actualizar datos para medir la toxicidad.
- Frontend: sistema de diseño, layout responsive, dashboard.
- Producto: implementación de data (ya disponible en back):
    Picos de toxicidad
    Grupo/Dominio más tóxico
    Contenido tóxico específico

Para más información:

**Roadmap**: https://github.com/users/MiguelGalp/projects/1 (pedir acceso si te interesa participar)


## Misión, visión y valores

Misión: ***Odio oído*** tiene como misión combatir la toxicidad y la falta de transparencia en las grandes plataformas sociales, utilizando la tecnología para analizar y visibilizar el discurso de odio en Twitter. 

Visión: aspiramos a un mundo digital donde las interacciones sean respetuosas, transparentes y responsables. ***Odio oído*** busca ser una herramienta clave para la construcción de una cultura digital más sana e inclusiva. 

Valores:

Compromiso social: Creemos en el poder de la tecnología para generar un impacto positivo en la sociedad.

Transparencia: Somos transparentes en cuanto a nuestro código, metodología y resultados.

Responsabilidad: Asumimos la responsabilidad de usar la tecnología de forma ética y responsable.

Colaboración: Creemos en el trabajo colaborativo como la mejor forma de lograr nuestros objetivos.

Innovación: Buscamos constantemente nuevas formas de mejorar nuestras herramientas y análisis.

## Comunidad

Este proyecto se desarrolla con la participación y el apoyo de FrontendCafé. Es requerido unirte a nuestro server y buscar el canal # | . Allí vas a poder escribir consultas, realizar propuestas y compartir ideas para el proyecto. El código de conducta de este proyecto es extensible también a tu participación en el server de FrontendCafé en Discord.

***Odio oído*** aspira también a ser parte de For Good First Issue, una iniciativa que busca generar una lista curada de proyectos open-source con foco en desarrollos del tipo Bienes Públicos Digitales (DPGs, Digital Public Goods) , los cuales además se encuentran disponibles para colaboración abierta.

## Licencias

Este repositorio y el contenido de la web de ****Odio oído**** se publican bajo licencia Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0).

## Links de interés

[Paper que inspiró el proyecto](https://arxiv.org/pdf/2303.14603.pdf)

[Correlación entre seguidores e interacción](https://www.kaggle.com/code/chitaxiang/instagram-influencer-data-analysis)


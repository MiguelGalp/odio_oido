<div align="center" width="100%"> 
<h1>PROYECTO <u>ODIO OÍDO</u></h1> 
  <picture> <img width="33%" alt="Un plato vacío" src="static/public/listeningTwitter.jpeg"> </picture> 

---

<h1>UNA MEDIDA DE TOXICIDAD EN TWITTER, POR PAÍS. 24/7</h1><h3>Sumate al proyecto para dar un indicador fiable y ayudar en el uso responsable de las redes sociales.</h3> 
</div> 

---

## Índice de Contenidos

- [Origen](#Origen)
- [Qué solución da la app](#Qué-solución-da-la-app)
- [Cómo funciona la app](#Cómo-funciona-la-app)
- [Cómo contribuir](#Cómo-contribuir-al-primer-release)
- [Misión, visión y valores](#misión-visión-y-valores)
- [Comunidad](#comunidad)
- [Licencias](#licencias)

---

## Origen

***Odio oído*** surge como un desprendimiento de la iniciativa "*Ahora*" de la ONG [Atlanticx](wwww.atlanticx.org), dedicada a la innovación en artes. Se trata de un impulso de tipo laboratorio (investigación y desarrollo) que busca ampliar las bases de diálogo entre las artes y la realidad contemporánea a partir de generar y accesibiliar datos relevantes al campo "arte + ciencia y tecnología". Más información sobre "*Ahora*" en este enlace. 

## ¿Qué solución da el MVP?

Odio oído en su versión MVP actual construye un índice de probabilidad para la toxicidad en Twitter, de la siguiente manera:

A. Estudios sobre Twitter del Pew Research Center, la Universidad de Oxford y el Instituto Berkman Klein indican correlaciones entre: 

1. Aumento de toxicidad durante (a) eventos políticos (como por ejemplo elecciones) y durante (b) eventos sociales singulares (como debates o tragedias).
2. Una relación directa entre el aumento de la polarización política y el aumento de la toxicidad. 

B. Por otro lado, el modelo LDA de análisis del discurso puede "ubicar" dentro de estos causales de toxicidad en Twitter a discursos de individuos/usuarios. Lo hace definiendo por ejemplo que un usuario X tiene como "espacio latente" (no explícito) en su discurso los temas "polarización política", o "crisis en la argentina", u "odio hacia y persona".

C. Tomando estas dos perspectivas en conjunto, Odio oído investiga desde LDA la adherencia de usuarios a estos causales de toxicidad en Twitter.

D. Con esta data (A, B y C) Oido oído propone un modelo de análisis que da un paso más allá. Para tracker (o más precisamente: para intentar predecir la toxicidad), la app define tópicos LDA que podrían considerarse **de segunda generación**. Es decir que, sobre tópicos de primera generación como "crisis en la argentina", Odio oído construye grupos de usaurios que, finalmente, definen el "dominio" como 
- "***debates* sobre la crisis en la argentina**"
o
- "***usuarios con historial de odio* sobre política argentina**".

CONCLUSIÓN: creemos que si bien la relación es débil, con esta técnica, si los datos son representativos, existe al menos un **indicador de probabilidad general de toxicidad para Twitter**, lo que puede dar lugar a:
- Debates sobre la responsabilidad en el uso de redes sociales.
- Un instrumento de consulta para instituciones o padres. 
- Un panorama comparativo para la toxicidad por país (por ahora regional) y por tipo de evento. 

## ¿Cómo funciona el MVP?

EN DOS PASOS:

1. (Offline), un script (query.py) scrapea Twitter para alimentar la base de datos de la app con información actualizada cada media hora (ver) con los niveles de interacción. Los datos son organizados dentro de un modelo de tipo [LDA (Latend Dirichlet Allocation)](https://es.wikipedia.org/wiki/Latent_Dirichlet_Allocation).
En ***Odio oído*** se utilizan para la organización de los datos los tópicos descubiertos por LDA para conformar "dominios": áreas temáticas que agrupan usuarios alrededor de, por ejemplo, el tópico "crisis en la argentina". El modelo también está entrenado para detectar la toxicidad misma como tópico, por lo que el resultado de su aplicación al dataset (tweets de usuarios) es la conformación de grupos que, además de dominios, definen un campo discursivo **prevalentemente tóxico**

2. (Online). Una vez preparada la data en la base de datos, la app genera la **temperatura del discurso**, obtiendo un parcial de las interacciones por grupo/dominio que es normalizado según el número de seguidores. ***Odio oído*** sostiene que esa temperatura, al ser representativa de dominios con prevalencia de toxicidad que contienen debates centrales a la sociedad, tiene al menos una relación indirecta con la toxicidad general de Twitter.

El data flow online se puede representar de la siguiente manera:

A(Carga de datos) --> B(Cálculo del engagement por tweet)

B --> C(Cálculo del engagement total y promedio por grupo)

C --> D(Cálculo del engagement promedio global)

D --> E(Visualización de resultados)

E --> F(Almacenamiento de resultados)

(Muy pronto): la app llega al indicador general de toxicidad a través de la aplicación de pesos relativos a los parciales por grupo/dominio, según los grados de actividad. Si, por ejemplo, el grupo/dominio más activo es el de "política argentina" el total crudo es multiplicado por un índice X. Si, en cambio, el grupo/dominio más activo es el de "crisis en la Argentina", el factor de multiplicación es > X.

## ¿Cómo contribuir al primer release?

****Odio oído**** se encuentra en pleno desarrollo. Apuntamos hacia un primer release (0.0.1) en el mes de junio. 

El roadmap detallado se encuentra en [este enlace](https://github.com/users/MiguelGalp/projects/1) (un proyecto GitHub, pedinos acceso si te interesa participar). 

El objetivo de ese primer release es crear un *dashboard* de toxicidad en Twitter, con:

- Índice de probabilidad (lo que actualmente muestra el MPV)
- Causa principal de toxicidad
- Picos de toxicidad (para permitir correlaciones a eventos externos)
- Contenido tóxico (visualización a modo de ejemplo de tweets tóxicos)

En términos generales las contribuciones al proyecto estarán dividas entre:

1. Calidad y ampliación de los datos: la app necesita comprobar y actualizar los datos con los que se mide la toxicidad.

2. Frontend: sistema de diseño, layout responsive, dashboard. 

3. Producto: implementación de data (ya disponible en back): a. Picos de toxicidad. b. Grupo/Dominio más tóxico. c. Contenido tóxico específico. 

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


<div align="center" width="100%"> 
<h1>PROYECTO <u>ODIO OÍDO</u></h1> 
  <picture> <img width="33%" alt="Un plato vacío" src="static/public/listeningTwitter.jpeg"> </picture> 

---

<h1>UNA MEDIDA DE TOXICIDAD EN TWITTER, POR PAÍS. 24/7</h1><h3>Sumate al proyecto para dar un indicador fiable y ayudar en el uso responsable de las redes sociales.</h3> 
</div> 

---

## Índice de Contenidos

- [Origen](#Origen)
- [Cómo funciona la app](#Cómo-funciona-la-app)
- [Cómo contribuir](#Cómo-contribuir)
- [Misión, visión y valores](#misión-visión-y-valores)
- [Comunidad](#comunidad)
- [Licencias](#licencias)

---

## Origen

***Odio oído*** surge como un desprendimiento de la iniciativa "*Ahora*" de la ONG [Atlanticx](wwww.atlanticx.org), dedicada a la innovación en artes. Se trata de un impulso de tipo laboratorio (investigación y desarrollo) que busca ampliar las bases de diálogo entre las artes y la realidad contemporánea a partir de generar y accesibiliar datos relevantes al campo "arte + ciencia y tecnología". Más información sobre el laboratro *Ahora*" en este enlace. 

## ¿Cómo funciona la app?

EN DOS PASOS:

1. (Offline), la app trabaja con datos que son obtenidos dentro de un modelo de tipo [LDA (Latend Dirichlet Allocation)](https://es.wikipedia.org/wiki/Latent_Dirichlet_Allocation).
En ***Odio oído*** se utilizan los tópicos descubiertos por LDA para conformar "dominios": áreas temáticas que agrupan usuarios alrededor de, por ejemplo, el tópico "crisis en la argentina". El modelo también está entrenado para detectar la toxicidad misma como tópico, por lo que el resultado de su aplicación al dataset (tweets de usuarios) es la conformación de grupos que, además de dominios, definen un campo discursivo **prevalentemente tóxico**

2. (Online). Una vez preparada la data, la app scrapea la **temperatura del discurso**, obtiendo un parcial de las interacciones por grupo/dominio que es normalizado según el número de seguidores. ***Odio oído*** sostiene que esa temperatura, al ser representativa de dominios con prevalencia de toxicidad que contienen debates centrales a la sociedad, tiene al menos una relación indirecta con la toxicidad general de Twitter.

El data flow online se puede representar de la siguiente manera:

A(Carga de datos) --> B(Cálculo del engagement por tweet)
B --> C(Cálculo del engagement total y promedio por grupo)
C --> D(Cálculo del engagement promedio global)
D --> E(Visualización de resultados)
E --> F(Almacenamiento de resultados)


(Muy pronto): la app llega al indicador general de toxicidad a través de la aplicación de pesos relativos a los parciales por grupo/dominio, según los grados de actividad. Si, por ejemplo, el grupo/dominio más activo es el de "política argentina" el total crudo es multiplicado por un índice X. Si, en cambio, el grupo/dominio más activo es el de "crisis en la Argentina", el factor de multiplicación es > X.

## ¿Cómo contribuir?

****Odio oído**** se encuentra en pleno desarrollo. Existen tres áreas diferentes en las que contribuir. 

Datos: por un lado la app necesita mejorar y revisar la precisión con la que indica (o más precisamente intenta predecir) la toxicidad: (a) comprobar la calidad de los datos, (b) desarrollar un sistema de actualización de la base y de los grupos/dominios, (c) alcanzar más países regionales con la misma metodología.

Frontend: implementación de data (ya disponible en back): a. Picos de toxicidad. b. Grupo/Dominio más tóxico. c. Contenido tóxico específico. 

Los hitos principales del roadmap son ([este enlace](https://github.com/users/MiguelGalp/projects/1) detalla todo el proyecto, pedinos acceso si te interesa participar):

- Marzo 2024: layout, mobile
- Abril 2024: datos Chile, pico de toxicidad en front
- Mayo 2024: datos ok, contenido y grupo más tóxico en front
- Julio 2024: lda dinámico, release 0.1

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


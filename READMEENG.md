<div align="center" width="100%"> 
<h1>PROYECTO ODIO OÍDO</h1> 
  <picture> <img width="33%" alt="Un plato vacío" src="static/public/ListeningTwitter.png"> </picture> 

<h1>A MEASURE OF TOXICITY ON TWITTER, BY COUNTRY. 24/7</h1><h3>Join the project to provide a reliable indicator and help promote the responsible use of social media.</h3>
</div>

---


## Table of Contents

- [Spanish README](README.md)
- [Origin](#Origin)
- [What Solution the App Provides](#Qué-solución-da-la-apps)
- [How the App Works](#Cómo-funciona-la-app)
- [How to Contribute](#Cómo-contribuir-al-primer-release)
- [Mission, Vision, and Values](#misión-visión-y-valores)
- [Community](#comunidad)
- [Licenses](#licencias)
- [Useful Links](#links-de-interés)


---

## Origin

***Odio oído*** Directly translated to "Hate Ear" originates as an offshoot of the "*Ahora*" (Now) initiative by the NGO [Atlanticx](wwww.atlanticx.org), dedicated to innovation in the arts. It is a laboratory-type project (research and development) that aims to expand the bases of dialogue between the arts and contemporary reality by generating and making relevant data accessible in the field of "art + science and technology". More information about "*Ahora*" can be found at this link.

## What Solution Does the MVP Provide?

In its current MVP version, *Odio oído* constructs a probability index for toxicity on Twitter by tracking groups of users adhering to second-generation LDA topics. For example, if the LDA model initially returns topics like "crisis in Argentina", our model observes the group "**debates** (about) the crisis in Argentina" or "**polarization** (around) the crisis in Argentina".

By normalizing interaction tracking by the number of followers, the MVP indirectly indicates the probability that a "general" user will encounter toxicity.

This approach also allows for:

- Debates on responsibility in social media use.
- A consultation tool for institutions or parents.
- A comparative overview of toxicity by country (currently regional) and by type of event.

## How Does the MVP Work?

IN TWO STEPS:

1. (Offline)

- A script (query.py) extracts information from Twitter to feed the app's database with updated information every X minutes.
- The data is organized with a second-generation domain LDA model.
- The adherence of domains to toxicity is controlled.

2. (Online)

- The discourse temperature by domain is calculated, normalized by the number of followers and life cycle (temporal relevance of each tweet).
- The information is visualized (a dashboard in development).
- The results are stored.

Coming soon:

- General toxicity indicator through relative weights to the activity of each group/domain.

## How to Contribute to the First Release?

Goal: Create a toxicity dashboard on Twitter with:

- Probability index
- Main cause of toxicity
- Toxicity peaks
- Toxic content

Contributions:

- Data quality and expansion: verify and update data to measure toxicity.
- Frontend: design system, responsive layout, dashboard.
- Product: implementation of data (already available in the backend):
    Toxicity peaks
    Most toxic group/domain
    Specific toxic content

For more information:

**Roadmap**: [https://github.com/users/MiguelGalp/projects/1](https://github.com/users/MiguelGalp/projects/1) (request access if you are interested in participating)

## Mission, Vision, and Values

Mission: ***Odio oído***'s mission is to combat toxicity and lack of transparency on major social platforms, using technology to analyze and highlight hate speech on Twitter.

Vision: We aspire to a digital world where interactions are respectful, transparent, and responsible. ***Odio oído*** aims to be a key tool in building a healthier and more inclusive digital culture.

Values:

- Social Commitment: We believe in the power of technology to create a positive impact on society.
- Transparency: We are transparent about our code, methodology, and results.
- Responsibility: We take responsibility for using technology ethically and responsibly.
- Collaboration: We believe in collaborative work as the best way to achieve our goals.
- Innovation: We constantly seek new ways to improve our tools and analyses.

## Community

This project is developed with the participation and support of FrontendCafé. It is required to join our server and look for the channel # | . There you can ask questions, make proposals, and share ideas for the project. The code of conduct of this project also extends to your participation in the FrontendCafé server on Discord.

***Odio oído*** also aspires to be part of For Good First Issue, an initiative that aims to create a curated list of open-source projects focused on Digital Public Goods (DPGs), which are also available for open collaboration.

## Licenses

This repository and the content of the ****Odio oído**** website are published under the Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0).

## Useful Links

[Paper that inspired the project](https://arxiv.org/pdf/2303.14603.pdf)

[Correlation between followers and interaction](https://www.kaggle.com/code/chitaxiang/instagram-influencer-data-analysis)









# El opio de los pueblos analiza interacciones en X/Twitter (engagement, funcionando en el 2024!). 

El opio de los pueblos es un servicio web para el análisis de datos en tiempo real. Conocé el comportamiento de tendencias en Argentina y Chile (más países y tópicos próximamente).

## Tecnologías utilizadas

- **Python**: Lenguaje de programación principal utilizado para el backend.
- **Flask**: Framework de Python utilizado para crear la aplicación web.
- **JavaScript**: Utilizado para la funcionalidad del lado del cliente, incluyendo las solicitudes AJAX al servidor.
- **HTML/CSS**: Utilizados para la estructura y el estilo de la página web.

## Rutas disponibles

- `GET /api/front_groups`: Devuelve un JSON con los grupos y usuarios para la interfaz de Argentina.
- `GET /api/front_chile`: Devuelve un JSON con los grupos y usuarios para la interfaz de Chile.
- `POST /engagement_by_groups`: Acepta un JSON con los grupos y usuarios seleccionados y devuelve un JSON con los valores de interacciones de los grupos.

## Usos del servicio web

Este servicio web puede ser utilizado para analizar el el comportamiento de tendencias de diferentes grupos de usuarios y tópicos de Twitter en tiempo real. Esto puede ser útil para decidir campañas o entender la evolución de las tendencias en relación a los acontecimientos públicos de los países analizados. 

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

## Limitaciones del proyecto

Este repositorio solo contiene el código del frontend de la aplicación. El código del backend que realiza la búsqueda de tweets no está incluido, por lo que no se puede hacer un despliegue completo de la aplicación a partir de este repositorio. Además, debido a las limitaciones de la API de Twitter, solo se pueden analizar los tweets más recientes.

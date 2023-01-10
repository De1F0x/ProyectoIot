# Proyecto IoT

## Intro
El proyecto consiste en un sistema de contenedores inteligentes mediante el cual recogeremos una serie de datos del entorno que nos servirán para actuar en consecuencia de forma autónoma o supervisada. 

**Sensores que utilizaremos**:
1. <ins>Sensor de luminosidad:</ins> Recogemos la luminosidad en formato **float**.

2. <ins>Sensor de movimiento:</ins>  Nos interesa saber si se detecta movimiento o no, lo recogemos como un booleano.

3. <ins>Sensor de temperatura:</ins> Recogemos la temperatura detectada dentro del contenedor como un **float**.

4. <ins>Sensor de distancia:</ins> Recogemos la distancia que simula la cantidad de basura desde la tapa del contenedor como un ****float****.

5. <ins>Sensor de humedad:</ins> Recogemos la humedad dentro del contenedor de basura como un **float**.

<p align="center">
<img src="https://user-images.githubusercontent.com/72742772/211576208-b5a2d6ac-6288-4177-9a66-f4064b1b6d6d.png" alt="Esquema" width="550"/>
</p>

> Esquema de la distribución general del proyecto.

## Docker

El proyecto entero está construido sobre diferentes contenedores de Docker, distribuidos de la siguiente manera:
- ***Docker compose***:
    - Servidor Flask
    - BBDD MySQL
    - Grafana
- ***Docker***:
    - Controlador React


### API
- Hemos creado un servidor en **Flask** que hará de intermediario entre el controlador, la BBDD y la propia Raspberry, teniendo la funcionalidad de una API REST. Es capaz de recibir peticiones "GET" y "POST" mediante las cuales accederemos directamente a la información guardada en la BBDD y alterar el estado de la Raspberry.  

### Web
- Hemos utilizado React, que es una librería utilizada para crear interfaces de usuario en JavaScript. Utiliza una arquitectura de componentes, en la cual se divide la interfaz en distintos componentes reutilizables que contienen funcionalidad y lógica interna. 

- Los activadores que controlaremos serán el **de la luz** para controlar un led que indicará si el contenedor está averiado, el de **sonido** para alejar a los animales, y el **servo** para abrir la tapa de la basura. 

- Usamos la librería Axios para lanzar peticiones HTTP al servidor.

### Raspberry
- La Raspberry tiene un script configurado para enviar información acerca de la distancia, temperatura, humedad, luminosidad y movimiento cada 3 segundos. Este script esta configurado dentro del sistema para lanzarse siempre que se encienda la Raspberry. 
- La Raspberry también es capaz de interactuar con la API REST para recibir y mandar información acreca de su estado.


### BBDD
- Utilizamos la base de datos **MySQL**.
- Para visualizar los datos que tenemos guardados en la BBDD hemos utilizado **Grafana**.

## Como lanzar el proyecto:
1. En la ruta principal del proyecto encontramos un docker-compose.yml, que lanzaremos para iniciar el servidor, la BBDD y Grafana. Por otro lado, entraremos en la ruta de my-app para ejecutar el Dockerfile que iniciará una imágen en node que al mismo tiempo generará la página del controlador de la Raspberry.
2. Una vez tenemos iniciados los diferentes contenedores podremos lanzar el **script** *main.py* en la ruta raspberry.

## Comandos

### Comandos para Docker
```
docker build -t controller .
docker run controller
```

### Comandos para docker-compose
```
docker compose up -d
```

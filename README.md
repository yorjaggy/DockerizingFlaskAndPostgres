# DockerizingFlaskAndPostgres

![alt tag](https://github.com/yorjaggy/VagrantParcial1Sisdistri/blob/master/images/1.png)

In this exercise we use docker for provide a environmnt like the showed in the imagen 1: A ubuntu machine with a microframework and a database in postgres. 

The version of docker used for this exercise is 1.12.3 (as showed in the image), the docker image used was the ubuntu:14.04 and the host machine was a ubuntu 14.04 with the next specifications. 
- 8GB of RAM 
- Intel Core i7

We implement 2 virtual containers: 
- **flask**: in this container, we install the microframework Flask, we configure the container to execute a service in the port 5000. This microservice has 3 URL's:
    1. http://localhost:5000/ -> this url show all the information storage in the table "word" in the postgres database.
    2. http://localhost:5000/test -> this url add information to the database, in this case added a static text "Mi Primera Palabra".
    3. http://localhost:5000/parametro -> this url added the text inserted in the url, for example "http://localhost:5000/hola" added the text "hola" in the database.
    
- **postgres**: in this, we install the postgres database, we configure the schema, the ports to expose, we indicated which clients are allowed to authenticated to the database and we configure the start of the services.

To run this exercise, clone this repository and realize the "docker-compose up -d" command, be sure that you have in your docker images an image of ubuntu:14:04 updated. If the process end succesfully you will be able to consult any of the 3 url exposed by flask. In other cases you have to check in your configurations allow you to created this environment.

For this exercise, we built the images previously and then we call it flaskmachine:latest (for the machine builded with the Dockerfile in the folder flaskBaseImage).

For this exercise, we built the images previously and then we call it postgresmachine:latest (for the machine builded with the Dockerfile in the folder postgresBaseImage)

Video:
* put the link video here

developed by:
*yorjaggy

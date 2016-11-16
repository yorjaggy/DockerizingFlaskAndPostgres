FROM yorjaggy/ubuntupdated
MAINTAINER Yor Jaggy <jhorshaggy7_2@hotmail.com>
#Instalando python y pip
RUN apt-get update && apt-get install -y python python-pip python-dev libpq-dev
#Instalando dependencias para la conexion con la base de datos en postgres
RUN apt-get install python-psycopg2 -y
ADD restFlaskApp /restFlaskApp
WORKDIR /restFlaskApp
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python app.py

# IoT
Ubuntu SO

## Installs
### - Python
Instalar pip:
sudo apt-get install python3-pip

Instalar virtual env:
pip3 install virtualenv

Crear entorno virtual:
virtualenv venv

Instalar pyserial:
pip install pyserial

Instalar driver postgres:
pip install psycopg2

### - Git
Instalacion de git:
sudo apt-get install git

Crear una clave ssh:
ssh-keygen -t ed25519 -C "sebastianzunigasaavedra@gmail.com"

### - Postgres 
Instalacion de postgres: 
sudo apt install postgresql postgresql-contrib

Probar que quedo bien: 
sudo -u postgres psql

Para correr postgres dentro de python:
sudo apt-get install python3-dev 
sudo apt-get install libpq-dev

Para crear base de datos:
desde la consola de postgres: CREATE DATABASE arduino WITH ENCODING 'UTF8';

### - SSH
Instalacion server ssh:
sudo apt-get install openssh-server

Saber estado del servicio:
sudo systemcls status ssh

Autorizar en el firewall:
sudo ufw allow ssh

### - Arduino
Para descargar arduino:
wget https://downloads.arduino.cc/arduino-1.8.15-linux64.tar.xz

Extaer el fichero:
tar -xvf ./arduino-1.8.15-linux64.tar.xz

Instalar arduino:


## Databases

-- public.humidity definition

-- Drop table

-- DROP TABLE public.humidity;

CREATE TABLE public.humidity (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	valor int4 NOT NULL,
	created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT humidity_pk PRIMARY KEY (id)
);

-- public.luminocity definition

-- Drop table

-- DROP TABLE public.luminocity;

CREATE TABLE public.luminocity (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	valor numeric NOT NULL,
	created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT luminocity_pk PRIMARY KEY (id)
);

-- public.temperature definition

-- Drop table

-- DROP TABLE public.temperature;

CREATE TABLE public.temperature (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	valor int4 NOT NULL,
	created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT pk_temp PRIMARY KEY (id)
);

## Posible Errors

### - ModuleNotFoundError: No module named 'serial'
Falta el modulo serial, instalarlo desde pip o desde las configuraciones del 
interprete

### - ModuleNotFoundError: No module named 'psycopg2'
Falta el modulo para postgres, instalarlo desde pip o desde las configuraciones del 
interprete

### Arduino can not write in. 
- Para darle los permisos a escribir en arduino
sudo usermod -a -G dialout $USER
sudo chmod a+rw /dev/ttyUSB0



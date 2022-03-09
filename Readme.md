# IoT
Ubuntu SO
## Installs
### - PySerial

### - Git
Instalacion de git:
sudo apt-get install git

### - Postgres 
Instalacion de postgres: 
sudo apt install postgresql postgresql-contrib
Probar que quedo bien: 
sudo -u postgres psql
Para correr postgres dentro de python:
sudo apt-get install python3-dev 
sudo apt-get install libpq-dev

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



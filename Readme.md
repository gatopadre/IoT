# IoT
## Installs
### - PySerial

### - Postgres 
- Instalacion de postgres: 
sudo apt install postgresql postgresql-contrib
- Probar que quedo bien: 
sudo -u postgres psql
- Para correr postgres dentro de python:
sudo apt-get install python3-dev 
sudo apt-get install libpq-dev

## Databases
- table humidity:

CREATE TABLE public.humidity (
    id int NOT NULL GENERATED ALWAYS AS IDENTITY,
    valor int NOT NULL,
    created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT humidity_pk PRIMARY KEY (id)
);

- table luminocity:

CREATE TABLE public.luminocity (
	id int NOT NULL GENERATED ALWAYS AS IDENTITY,
	valor numeric NOT NULL,
	created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT luminocity_pk PRIMARY KEY (id)
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



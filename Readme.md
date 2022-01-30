# installs
-PySerial

# databases
- table humidity:
CREATE TABLE public.humidity (
    id int NOT NULL GENERATED ALWAYS AS IDENTITY,
    valor int NOT NULL,
    created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT humidity_pk PRIMARY KEY (id)
);

## Posibles Errores
### ModuleNotFoundError: No module named 'serial'
- falta el modulo serial, instalarlo desde pip o desde las configuraciones del 
interprete

### ModuleNotFoundError: No module named 'psycopg2'
- falta el modulo para postgres, instalarlo desde pip o desde las configuraciones del 
interprete

### No esta instalado postgres
- instalacion de postgres:
sudo apt install postgresql postgresql-contrib
- probar que quedo bien:
sudo -u postgres psql
- para correr postgres dentro de python:
sudo apt-get install python3-dev 
sudo apt-get install libpq-dev

### arduino 
- para darle los permisos a escribir en arduino
sudo usermod -a -G dialout $USER
sudo chmod a+rw /dev/ttyUSB0



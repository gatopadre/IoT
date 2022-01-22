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

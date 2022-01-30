-- tabla temperature
CREATE TABLE public.temperature (
	id int NOT NULL GENERATED ALWAYS AS IDENTITY,
	valor decimal NOT NULL,
	created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT temperature_pk PRIMARY KEY (id)
);

-- tabla humidity
CREATE TABLE public.humidity (
	id int NOT NULL GENERATED ALWAYS AS IDENTITY,
	valor decimal NOT NULL,
	created_at timestamp NULL DEFAULT CURRENT_TIMESTAMP
);


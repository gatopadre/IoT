--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

-- Started on 2022-01-18 23:33:27

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 3313 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 210 (class 1259 OID 16555)
-- Name: temperature; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.temperature (
    id integer NOT NULL,
    valor integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.temperature OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16554)
-- Name: temperature_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.temperature ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.temperature_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
    CYCLE
);


--
-- TOC entry 3307 (class 0 OID 16555)
-- Dependencies: 210
-- Data for Name: temperature; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.temperature (id, valor, created_at) FROM stdin;
2	-1	2022-01-16 14:32:54.240369
13	17	2022-01-16 15:46:06.181171
14	17	2022-01-16 15:46:19.350583
15	17	2022-01-16 15:46:32.532626
16	17	2022-01-16 15:46:45.716652
17	17	2022-01-16 15:46:58.895751
18	17	2022-01-16 15:47:12.077687
19	17	2022-01-16 15:47:25.361702
20	17	2022-01-16 15:47:38.534744
\.


--
-- TOC entry 3314 (class 0 OID 0)
-- Dependencies: 209
-- Name: temperature_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.temperature_id_seq', 20, true);


--
-- TOC entry 3166 (class 2606 OID 16560)
-- Name: temperature pk_temp; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.temperature
    ADD CONSTRAINT pk_temp PRIMARY KEY (id);


-- Completed on 2022-01-18 23:33:27

--
-- PostgreSQL database dump complete
--


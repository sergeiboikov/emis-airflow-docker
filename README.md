# About 

Pipelines for seeding/updating a database of international exchange rates, using Apache Airflow.

## Workflow

exchangerate.host API -> Apache Airflow -> PortgreSQL

## Installation

**Before anything else, you need Docker and `docker-compose` installed.*
(https://docs.docker.com/desktop/windows/install/)

1. Clone the repository in local folder.
2. Create a `.env` file in the project directory, and add the following variables:
    - `AIRFLOW_UID=50000`
    - `AIRFLOW_GID=0`
3. Execute the command `docker-compose up` from the root of the project directory.
4. Navigate to `localhost:8080/admin` to view the Airflow UI (User: `airflow`; Pwd: `airflow`).
5. Run the pipeline `create_db` for creating the table `public.exchangerates` in the database `currency_db`.
6. Run the pipeline `seed_rates` for loading historical data of international exchange rates.
7. Run the pipeline `update_rates` for loading delta data of international exchange rates.

## DAG Guide 

- `create_db`: Pipeline creates the `currency_db` database and the `public.exchangerates` table that will store data about international exchange rates. 
- `seed_rates`: Pipeline populates historical data about international exchange rates. You need to run the pipeline one time.
- `update_rates`: Pipeline populates delta data about international exchange rates. This pipelines is run every 3 hours.

## Setup pgAdmin (for validating the result of ETL process)
1. Navigate to `http://localhost:5050/browser` to view the pgAdmin UI (User: `pgadmin4@pgadmin.org`; Pwd: `admin1234`).
2. Register a new server with the following parameters: 
    - Server name: `postgres_server`
    - Host name/address: `postgresql_etl_server`
    - Port: `5432`
    - Maintenance database: `currency_db`
    - Username: `admin`
    - Password: `admin1234`
 3. Select data from the table `public.exchangerates`

## Important
All credentials are shared just for demo purposes. This approch is unsecure and is not used in real projects.
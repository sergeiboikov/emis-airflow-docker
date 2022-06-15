# About 

Deployment of local infrastructure for Airflow + PostgreSQL project.

## Installation

**Before anything else, you need Docker and `docker-compose` installed.*
(https://docs.docker.com/desktop/windows/install/)

1. Clone the repository in local folder.
2. Create a `.env` file in the project directory, and add the following variables:
    - `AIRFLOW_UID=50000`
    - `AIRFLOW_GID=0`
3. Execute the command `docker-compose up` from the root of the project directory.
4. Navigate to `localhost:8080/admin` to view the Airflow UI (User: `airflow`; Pwd: `airflow`).

## Setup pgAdmin (for validating the result of ETL process)
1. Navigate to `http://localhost:5050/browser` to view the pgAdmin UI (User: `pgadmin4@pgadmin.org`; Pwd: `admin1234`).
2. Register a new server with the following parameters: 
    - Server name: `postgres_server`
    - Host name/address: `postgresql_etl_server`
    - Port: `5432`
    - Maintenance database: `EMIS_DW`
    - Username: `admin`
    - Password: `admin1234`

## How to connect from local DBeaver
![alt text](/images/dbeaver.png "Title")

## Important
All credentials are shared just for demo purposes. This approch is unsecure and is not used in real projects.
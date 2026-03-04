#!/bin/bash

# Load the database with initial data
docker compose exec backend python -m ETL.data.load_db
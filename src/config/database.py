import os

# Database configuration
DATABASE_URL = "postgresql://user:pass@localhost/example_db"
DB_NAME = "example_db"

def get_connection():
    return DATABASE_URL

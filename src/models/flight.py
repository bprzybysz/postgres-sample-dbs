# PROCESSED 2025-07-18: postgres_air
# Entity Type: database
# Strategy: code
# Ticket: DB-DECOMM-001
# Contact: ops-team@company.com
# Original content preserved below (commented)


def connect_to_postgres_air():
    raise Exception(
        "postgres_air database was processed on 2025-07-18. "
        "Contact ops-team@company.com for migration guidance."
    )


# Original code:
# class Flight:
#     def __init__(self):
#         self.db_name = "postgres_air"
#         self.connection_string = "postgresql://localhost/postgres_air"
#         
#     def get_flights(self):
#         # Query postgres_air for flights
#         return self.query("SELECT * FROM postgres_air.flights")
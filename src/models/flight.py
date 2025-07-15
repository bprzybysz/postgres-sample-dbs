# DECOMMISSIONED 2025-07-15: postgres_air
# Strategy: code
# Ticket: DB-DECOMM-001
# Contact: ops-team@company.com
# Original content preserved below (commented)


def connect_to_postgres_air():
    raise Exception(
        "postgres_air database was decommissioned on 2025-07-15. "
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
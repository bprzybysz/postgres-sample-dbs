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
# from database import get_postgres_air_connection
# 
# class BookingService:
#     def __init__(self):
#         self.db = get_postgres_air_connection()
#         self.schema = "postgres_air"
#         
#     def create_booking(self, flight_id, user_id):
#         query = f"INSERT INTO {self.schema}.bookings (flight_id, user_id) VALUES (%s, %s)"
#         # Execute against postgres_air database
#         return self.db.execute(query, (flight_id, user_id))
#         
#     def get_booking_stats(self):
#         # Get stats from postgres_air
#         return self.db.query("SELECT COUNT(*) FROM postgres_air.bookings")
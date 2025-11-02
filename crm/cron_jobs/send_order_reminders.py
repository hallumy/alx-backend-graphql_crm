#!/usr/bin/env python3
import os
import sys
import logging
from datetime import datetime, timedelta

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_backend_graphql.settings")

import django
django.setup()

import logging
from datetime import datetime, timedelta
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


logging.basicConfig(
    filename="/tmp/order_reminders_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

transport = RequestsHTTPTransport(
    url="http://localhost:8000/graphql",
    verify=True,
    retries=3,
)
client = Client(transport=transport, fetch_schema_from_transport=True)

seven_days_ago = (datetime.now() - timedelta(days=7)).date()

query = gql("""
    query($startDate: DateTime!) {
      orders(orderDate_Gte: $startDate) {
      id
      customer {
        email
        }
      orderDate
      }
    }
""")
params = {"startDate": str(seven_days_ago)}

try:
    result = client.execute(query, variable_values=params)
    orders = result.get("orders", [])

    for order in orders:
        order_id = order["id"]
        email = order["customer"]["email"]
        logging.info(f"Reminder: Order ID{order_id} for {email}")

    print("Order reminders processed!")

except Exception as e:
    logging.error(f"Error fetching orders: {e}")
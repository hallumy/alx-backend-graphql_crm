from celery import shared_task
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from datetime import datetime
import requests

@shared_task
def generate_crm_report():
    transport = RequestsHTTPTransport(
        url="http://localhost:8000/graphql",
        verify=True
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # GraphQL query for totals
    query = gql("""
    query {
        totalCustomers: customersCount
        totalOrders: ordersCount
        totalRevenue: ordersTotalRevenue
    }
    """)

    result = client.execute(query)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = (
        f"{timestamp} - Report: "
        f"{result['totalCustomers']} customers, "
        f"{result['totalOrders']} orders, "
        f"{result['totalRevenue']} revenue"
    )

    # Log to file
    with open("/tmp/crm_report_log.txt", "a") as f:
        f.write(report + "\n")

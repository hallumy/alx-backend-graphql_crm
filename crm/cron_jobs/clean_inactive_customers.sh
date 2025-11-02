#!/bin/bash

# Navigate to the Django project root
cd /home/ahlam/alx-backend-graphql_crm

# Execute Django shell command to delete inactive customers
deleted_count=$(python manage.py shell -c "
from django.utils import timezone
from datetime import timedelta
from crm.models import Customer, Order

one_year_ago = timezone.now() - timedelta(days=365)
inactive_customers = Customer.objects.filter(order__isnull=True) | Customer.objects.filter(order__date__lt=one_year_ago)
count = inactive_customers.count()
inactive_customers.delete()
print(count)
" )

# Log deletion with timestamp
echo \"$(date '+%Y-%m-%d %H:%M:%S') - Deleted $deleted_count inactive customers\" >> /tmp/customer_cleanup_log.txt

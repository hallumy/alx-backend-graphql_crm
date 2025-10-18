# ALX Backend GraphQL CRM

A simple GraphQL API built with Django and Graphene for ALX backend CRM projects.  
This project demonstrates how to define a GraphQL schema using `graphene-django` and expose it through a `/graphql` endpoint.

---

## 🚀 Features

- GraphQL endpoint at `/graphql`
- Simple schema with a `hello` field that returns "Hello, GraphQL!"
- GraphiQL UI enabled for testing queries in the browser

---

## 🧱 Project Structure

alx-backend-graphql_crm/
├── manage.py
├── .venv/
├── crm/ # (Your Django app folder, optional)
├── alx_backend_graphql_crm/ # Django project folder
│ ├── settings.py
│ ├── urls.py
│ └── schema.py # ✅ GraphQL schema lives here


---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/alx-backend-graphql_crm.git
cd alx-backend-graphql_crm

2. Create & activate virtual environment

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt
# OR, if not using a requirements.txt yet:
pip install django graphene-django "graphene-django[debug]"

4. Apply migrations

python manage.py migrate

5. Run the development server

python manage.py runserver

⚙️ GraphQL Endpoint

Visit: http://localhost:8000/graphql

You should see the GraphiQL interface.
Try this query:

{
  hello
}

Expected response:

{
  "data": {
    "hello": "Hello, GraphQL!"
  }
}

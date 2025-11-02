import graphene
from crm.queries import CRMQuery

class Query(CRMQuery, graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(root, info):
        return "Hello,  GraphQL!"

schema = graphene.Schema(query=Query)

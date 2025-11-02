import graphene
from crm.models import Product

class UpdateLowStockProducts(graphene.Mutation):
    updated_products = graphene.List(graphene.String)
    message = graphene.String()

    def mutate(self, info):
        low_stock_products = Product.objects.filter(stock__lt=10)
        updated_names = []

        for product in low_stock_products:
            product.stock += 10  # Restock by 10
            product.save()
            updated_names.append(f"{product.name} (stock: {product.stock})")

        return UpdateLowStockProducts(
            updated_products=updated_names,
            message="Low stock products updated!"
        )

class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()

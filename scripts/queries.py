from inventory.models import Product, Category
from django.db.models import Avg, Sum, Max, Min, F, Count

def run():
    # 1. Average price of all products
    avg_price = Product.objects.aggregate(Avg('price'))['price__avg']
    print(f"Average Price of All Products: {avg_price}")

    # 2.
    avg_price_a = Product.objects.filter(name__startswith='A').aggregate(Avg('price'))['price__avg']
    print(f"Average Price of Products Starting with 'A': {avg_price_a}")

    # 3.
    total_price = Product.objects.aggregate(Sum('price'))['price__sum']
    print(f"Total Price of All Products: {total_price}")

    # 4.
    books_total_price = Product.objects.filter(category__name='Books').aggregate(Sum('price'))['price__sum']
    print(f"Total Price of 'Books' Category Products: {books_total_price}")

    # 5.
    price_stats = Product.objects.aggregate(Max('price'), Min('price'))
    print(f"Max Price: {price_stats['price__max']}, Min Price: {price_stats['price__min']}")

    # 6.
    categories_with_count = Category.objects.annotate(product_count=Count('products'))
    for category in categories_with_count:
        print(f"Category: {category.name}, Product Count: {category.product_count}")

    # 7.
    categories_with_avg_price = Category.objects.annotate(avg_price=Avg('products__price'))
    for category in categories_with_avg_price:
        print(f"Category: {category.name}, Average Price: {category.avg_price}")

    # 8.
    products_with_stock_value = Product.objects.annotate(stock_value=F('price') * F('stock_quantity'))
    for product in products_with_stock_value:
        print(f"Product: {product.name}, Stock Value: {product.stock_value}")

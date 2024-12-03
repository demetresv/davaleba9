import json
from inventory.models import Category, Product

def run():
    with open('data.json') as file:
        data = json.load(file)
        for item in data:
            model = item['model']
            fields = item['fields']
            if model == 'inventory.category':
                Category.objects.create(**fields)
            elif model == 'inventory.product':
                fields['category_id'] = fields.pop('category')
                Product.objects.create(**fields)
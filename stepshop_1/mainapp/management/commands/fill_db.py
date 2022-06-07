import json
import os.path

#from django.contrib.auth.models import User
from django.core import management
from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


JSON_PATH = 'mainapp/fixtures'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='UTF-8') as f:
        return json.load(f)


class Command(BaseCommand):
    def handle(self, *args, **options):
        management.call_command('flush', verbosity=0, interactive=False)

        categories = load_from_json('categories')
        products = load_from_json('products')

        for category in categories:
            _category = category.get('fields')
            _category['id'] = category.get('pk')
            #fields = category.get('fields')
            ##new_category = ProductCategory(**fields)
            #new_category.save()

            new_category = ProductCategory(**_category)
            new_category.save()

        for product in products:
            _product = product.get('fields')
            category_id = _product.get('category')
            _product['category'] = ProductCategory.objects.get(pk=category_id)
            new_product = Product(**_product)
            new_product.save()

            #fields = product.get('fields')
            #category_pk = fields['category']
            #_category = ProductCategory.objects.get(pk=category_pk)
            #fields['category'] = _category

            #new_product = Product(**fields)
            #new_product.save()

        ShopUser.objects.create_superuser('admin', 'admin@stepshop.kz', '123', age=16)



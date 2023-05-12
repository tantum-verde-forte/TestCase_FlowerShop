import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestCase_FlowersShop.settings")
django.setup()

from shop.models import Seller, Product, Deal

sellers_list = []
sellers = Seller.objects.all()
for x in sellers:
    seller = [x.username]
    deals_sum = 0
    consumers = []
    products = Product.objects.filter(seller=x.id)
    for i in products:
        deals = Deal.objects.filter(product=i.id)
        for j in deals:
            consumers.append(j.consumer.username)
            deals_sum += i.price
    seller.append(consumers)
    seller.append(deals_sum)
    sellers_list.append(seller)
print(sellers_list)




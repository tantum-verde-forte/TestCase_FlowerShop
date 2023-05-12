from django.db import models

class Consumer(models.Model):
    username = models.CharField(max_length=255, null=False, blank=False, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Seller(models.Model):
    username = models.CharField(max_length=255, null=False, blank=False, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Product(models.Model):
    COLOR_CHOICES = (
        ("WHITE", "White"),
        ("ReD", "Red"),
        ("YELLOW", "Yellow"),
        # ....
        ("PINK", "Pink"),
    )

    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    sort = models.CharField(max_length=255)
    color = models.CharField(max_length=9, choices=COLOR_CHOICES, default="WHITE")
    count = models.IntegerField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)


class Seller_review(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    review = models.TextField(max_length=500)


class Product_review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    review = models.TextField(max_length=500)


class Deal(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField()


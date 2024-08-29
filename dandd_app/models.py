from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    upc = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    product_name = models.CharField(max_length=200)
    title_english = models.CharField(max_length=200)
    color_english = models.CharField(max_length=50)
    size_english = models.CharField(max_length=20)
    images_link = models.URLField()
    english_description = models.TextField()
    msrp = models.DecimalField(max_digits=10, decimal_places=2)
    net_weight = models.DecimalField(max_digits=10, decimal_places=2)
    net_weight_unit = models.CharField(max_length=10)
    case_width = models.DecimalField(max_digits=10, decimal_places=2)
    case_length = models.DecimalField(max_digits=10, decimal_places=2)
    case_height = models.DecimalField(max_digits=10, decimal_places=2)
    case_unit = models.CharField(max_length=10)
    pieces_per_case = models.IntegerField()

    def __str__(self):
        return f"{self.product_name} - {self.color_english} - {self.size_english}"
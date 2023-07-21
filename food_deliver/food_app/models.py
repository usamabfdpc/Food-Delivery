from django.db import models

# Create your models here.

# Recipee Makers


class RecipeeCategory(models.Model):
    name = models.CharField(max_length=50)
    packing_fee = models.DecimalField(decimal_places=3,max_digits=10)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str( self.name)


class Ingredients(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self) -> str:
        return str( self.title)
        

class ExtraIngredients(models.Model):
    ingredient = models.OneToOneField(Ingredients,on_delete=models.CASCADE)        
    price = models.DecimalField(max_digits=10,decimal_places=3)

    def __str__(self) -> str:
        return str(f"{self.ingredient} ({self.price} $)")



class Recipee(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='recipy',blank=True)
    category = models.ManyToManyField(RecipeeCategory)
    ingredients = models.ManyToManyField(Ingredients,related_name='ingredients')
    extra_ingredients = models.ManyToManyField(ExtraIngredients,blank=True,related_name='extra_ingredients')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.BooleanField(default=True)
    featured_recipy = models.BooleanField()
    price_set_by_size = models.BooleanField()
    quantaty_to_order = models.IntegerField(default=1)


    def __str__(self) -> str:
        return str( self.name)

class RecipeeVarients(models.Model):
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    recipee = models.ForeignKey(Recipee,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str( self.size)
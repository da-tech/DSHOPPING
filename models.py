from django.db import models



class category(main):
    title = models.CharField(max_length=100)
    description = models.CharField( max_length=100)
    status = models.CharField( max_length=100)
    def __str__(self):
        return self.title

class country(main):
    title = models.CharField( max_length=100)
    abreviation = models.CharField(max_length=100)
    status = models.CharField( max_length=100)
    def __str__(self):
        return self.title

class gender(main):
    title = models.CharField(, max_length=100)
    description = models.CharField( max_length=100)
    status = models.CharField( max_length=100)
    def __str__(self):
        return self.title
        
class clients(main):
    id_client = models.CharField max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField( max_length=100)
    Gender = models.ForeignKey(gender, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, unique=True)
    email = models.EmailField( max_length = 15)               
    id_country = models.ForeignKey (country, on_delete=models.CASCADE)    
    image = models.ImageField (, null= True, blank=True, upload_to='authors/')
    message = models.TextField(,max_length=10)
    credit_card_number = models.CharField(,max_length=15)
        return '{0}{1}{2}'.format(self.first_name," ",self.last_name)

class products(main):
    title = models.CharField(max_length=100)
    description = models.CharField( max_length=100)
    id_category = models.ForeignKey (on_delete=models.CASCADE)
    id_country = models.ForeignKey ( on_delete=models.CASCADE)
    photo = models.ImageField ( null= True, blank=True, upload_to='products/')
    quantity = models.CharField( max_length=100)
    status = models.CharField( max_length=100)
   
    def __str__(self):
        return self.title


class shopping(main):
    id_product = models.ForeignKey (products, on_delete=models.CASCADE)
    id_client = models.ForeignKey (clients, on_delete=models.CASCADE)
    shopping_date = models.DateField('Shopping date', auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.id_product



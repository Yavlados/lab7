from django.db import models

# Create your models here.
class Users(models.Model):
    class Meta():
        db_table = "Users"
    email_user = models.EmailField(max_length=100)
    name_user = models.CharField(max_length=20)
    lastname_user = models.CharField(max_length=20)

class Tovar(models.Model):
    class Meta():
        db_table = "Tovar"
    id_tovar = models.AutoField(primary_key=True)
    name_tovar = models.CharField(max_length=50)
    type_tovar = models.CharField(max_length=50)

class Shop(models.Model):
    class Meta():
        db_table = "Table"
    id_shop =  models.AutoField(primary_key=True)
    name_shop = models.CharField(max_length=20)
    adr_shop = models.CharField(max_length=100)
    assort_shop = models.ManyToManyField(Tovar)

    def get_assort(self):
        return [{'id': tovar.id_tovar, 'name_tovar': tovar.name_tovar, 'type_tovar': tovar.type_tovar} for tovar in self.assort_shop.all()]

class Worker(models.Model):
    class Meta():
        db_table = "Worker"
    id_worker =  models.AutoField(primary_key=True)
    name_worker = models.CharField(max_length=20)
    lastname_worker = models.CharField(max_length=20)
    email_worker =  models.EmailField(max_length=100)
    workplace_worker = models.ForeignKey(Shop, on_delete=models.CASCADE)


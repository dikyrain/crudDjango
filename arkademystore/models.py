from django.db import models  

# class Employee(models.Model):  
#     eid = models.CharField(max_length=20)  
#     ename = models.CharField(max_length=100)  
#     eemail = models.EmailField()  
#     econtact = models.CharField(max_length=15)  
#     class Meta:  
#         db_table = "loyee"  
    
class ArkademyStore(models.Model):  
    nama_produk = models.CharField(max_length=20)  
    keterangan = models.CharField(max_length=100)  
    harga = models.IntegerField() 
    jumlah = models.IntegerField()  
    class Meta:  
        db_table = "arkademystore"  
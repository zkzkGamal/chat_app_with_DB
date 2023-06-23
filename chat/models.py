from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Static_Message(models.Model):
    name = models.TextField(max_length=20,null=True , blank=True)
    message = models.TextField( null=True , blank=True)
    company_name = models.TextField( null=True , blank=True)
    perant_id =  models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

class new_Static_Message(MPTTModel):
    name = models.TextField(max_length=20,null=True , blank=True)
    message = models.TextField( null=True , blank=True)
    company_name = models.TextField( null=True , blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    def __str__(self):
        return str(self.id)


class chat(models.Model):
    user =  models.ForeignKey(User , on_delete=models.CASCADE , blank=True,null=True)
    message = models.TextField( blank=True,null=True)
    server_message = models.TextField( blank=True,null=True)
    data_sended = models.DateField(auto_now_add=False)
    time_sended = models.TimeField(auto_now_add=True , null=True )
    message_id = models.IntegerField(null=True , blank=True)
    
    def __str__(self):
        return str(self.user.username)
    


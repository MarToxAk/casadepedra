from django.db import models


# Create your models here.
class DataAlteracao(models.Model):
    criado = models.DateTimeField(
        'Criado em',
        auto_now=False,
        auto_now_add=True
    )
    modificado = models.DateField(
        'Modificado em', 
        auto_now=True, 
        auto_now_add=False
    )
    
        
    class Meta:
        abstract = True
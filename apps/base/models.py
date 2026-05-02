from django.db import models

# Create your models here.

class BaseModel(models.Model):

    # TODO: Define fields here.
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('Estado',default = True)
    created_date = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    deleted_date = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for BaseModel"""

        abstract = True #No se crea una tabla en la base de datos para ese modelo.
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'
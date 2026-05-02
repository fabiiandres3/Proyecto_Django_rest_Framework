from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.

class MeasureUnit(BaseModel):

    # TODO : Define fields here.

    description = models.CharField('Descripcion',max_length=50, blank=False, null=False, unique=True)
    historical = HistoricalRecords() #History of who made the modification

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta Definition for MeasureUnit"""
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de Medidas'

    def __str__(self):
        return self.description
    

class CategoryProduct(BaseModel):

    # TODO : Define fields here.

    description = models.CharField('Descripcion', max_length=50, blank=False, null=False, unique=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name="Unidad de Medida")
    historical = HistoricalRecords() #History of who made the modification

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta Definition for CategoryProducts"""
        verbose_name = 'Categoria de Productos'
        verbose_name_plural = 'Categorias de Productos'

    def __str__(self):
        return self.description



class Indicador(BaseModel):

    # TODO : Define fields here.
    descount_value = models.PositiveSmallIntegerField()
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name="Indicador de Oferta")
    

    historical = HistoricalRecords() 

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value 

    class Meta:
        """Meta definition for Indicador."""

        verbose_name = 'Indicador de Oferta'
        verbose_name_plural = 'Indicadores de Ofertas'

    def __str__(self):
        return f'Oferta de la categoria {self.category_product} : {self.descount_value}%' 
    

class Product(BaseModel):

    # TODO : Define fields here.

    name = models.CharField('Nombre de Producto',max_length=150, unique=True, blank=False, null=False)
    Descripcion = models.TextField('Descripcion de Producto', blank=False, null=False)
    image = models.ImageField('Imagen del Producto',upload_to="products/", blank=True, null=True)

    historical = HistoricalRecords() 

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value 

    class Meta:
        """Meta definition for """
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

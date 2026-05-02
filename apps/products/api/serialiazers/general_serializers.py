from apps.products.models import MeasureUnit, CategoryProduct, Indicador
from rest_framework import serializers

class MeasureUnitSerializer(serializers.Serializer):

    class Meta:
        model = MeasureUnit #Modelo a serializar
        exclude = ('state',) #Campo no se serializar pq no se necesitaS retornar el Valor
        #Se serializa todo menos el campo state, que es un campo de control para saber si el registro esta activo o inactivo, pero no es necesario retornar ese valor al cliente.
        

    class CategoryProductSerializer(serializers.ModelSerializer):

        class  Meta:
            model = CategoryProduct
            exclude = ('state',)

    class IndicadorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Indicador
            exclude = ('state',)
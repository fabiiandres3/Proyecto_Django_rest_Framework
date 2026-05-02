from rest_framework import serializers
from apps.users.models import User

class UserSerializers(serializers.ModelSerializer): #Create and Update
    class Meta:
        model = User
        fields = '__all__'

    #se intersecta el metodo CREATE
    def create(self, validated_data): #Intersectamos el metodo create
        user = User(**validated_data) #Descomprime el diccionario validated_data que lleva los valores del modelo cuando son validados por is_valid() en la api y pasa los valores como parametros
        user.set_password(validated_data['password']) #Encripta el campo password
        user.save() #Guarda la info
        return user
    
    #Se intersecta el metodo PUT
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user


class UserListSerializer(serializers.ModelSerializer): #List JSON

    class Meta:
        model = User

    def to_representation(self, instance): #List what I want them to see
        return{
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }
        
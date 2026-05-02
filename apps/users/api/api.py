from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializers, UserListSerializer
from rest_framework.decorators import api_view
from rest_framework import status

"""class UserAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        users_serializers = UserSerializers(users,many=True)
        return Response(users_serializers.data)"""
    
@api_view(['GET','POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all().values('id','username','email','password') #Query
        users_serializers = UserListSerializer(users,many=True)   #instance
        return Response(users_serializers.data, status=status.HTTP_200_OK) #Response and status
    
    elif request.method == 'POST':
        users_serializers = UserSerializers(data=request.data)
        if users_serializers.is_valid():
            users_serializers.save()
            return Response({'message':'usuario creado correctamente'}, status=status.HTTP_200_OK)
        return Response(users_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk=None):
    #querySet
    user = User.objects.filter(id=pk).first()
    #validation
    if user:
        if request.method == 'GET':
            users_serializers = UserSerializers(user)
            return Response(users_serializers.data,status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            users_serializers = UserSerializers(user, data=request.data)
            if users_serializers.is_valid():
                users_serializers.save()
                return Response(users_serializers.data,status=status.HTTP_200_OK)
            return Response(users_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            user = User.objects.filter(id=pk).first()
            user.delete()
            return Response({'message':'Usuario Eliminado corectamente'})
        
    return Response({'message':'No se ha encontrado un Usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
    





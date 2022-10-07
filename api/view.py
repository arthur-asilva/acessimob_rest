from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.user.models import User
from apps.user.serializers import Serializer
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = Serializer(users, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def postData(request):
    request.data['name'] = f"{request.data['first_name']} {request.data['last_name']}"
    serializer = Serializer(data=request.data)
    if serializer.is_valid(): 
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def authUser(request):
    user = User.objects.filter(**request.data)
    if user.exists():
        token = Token.objects.get_or_create(user=user.first())[0]
        return Response({'token': token.key, 'success': True})
    return Response({'error': 'user not found'})
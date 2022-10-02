from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.user.models import User
from apps.user.serializers import Serializer


@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = Serializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = Serializer(data=request.data)
    if serializer.is_valid(): 
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
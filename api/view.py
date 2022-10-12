from datetime import date
from apps.post_location.models import PostLocation
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.user.models import User
from apps.user.serializers import Serializer
from rest_framework.authtoken.models import Token
import base64
import os
from tools.decorators import is_authenticate


@api_view(['POST'])
@is_authenticate
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
        # add last login update on token generation
        token = Token.objects.get_or_create(user=user.first())[0]
        return Response({'token': token.key, 'success': True})
    return Response({'error': 'user not found'})


@api_view(['PUT'])
@is_authenticate
def postLocation(request):
    user = Token.objects.get(key=request.data['token']).user
    photo = str.encode(request.data['photo'])
    path = f"media/{date.today().strftime('%Y/%m/%d')}/{user.id}/"

    if not os.path.isdir(path):
        os.makedirs(path)
    
    path += f"{len(os.listdir(path))}.jpeg"

    with open(path, "wb") as fh:
        fh.write(base64.decodebytes(photo))

    post = PostLocation(user=user, location=request.data['location'], photo=path, comments=request.data['comments'])
    post.save()

    return Response({'success': True})
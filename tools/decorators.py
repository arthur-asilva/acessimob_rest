from warnings import catch_warnings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

def is_authenticate(function):
    def wrap(request, *args, **kwargs):
        try:
            has_access = Token.objects.get(key=request.data['token'])
            request.data['user'] = has_access.user
            return function(request, *args, **kwargs)
        except:
            return Response({'error': 'unauthorized access'})
    return wrap
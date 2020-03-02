from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            {'username' : 'danny', 
            'password': '123456',
            'user_type': 'customer',
            'user_ip_address': '127.0.0.1',
            'last_activity' : 0
            }
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

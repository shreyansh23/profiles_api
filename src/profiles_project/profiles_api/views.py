from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class HelloApiView(APIView):
    """Test API view."""

    def get(self, request, format = None):
        """Returns a list of APIViews features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'It is similar to traditional django view',
            'Gives you the most control of your logic',
            'It is mapped manually to the URLs'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

class TestView(APIView):
    def get(self, request, *args, **kwargs):

        data = {
        'name': 'John',
        'age': 27
        }

        return Response(data)

    # def post(self, request, *args, **kwargs):
    #     serializer = PostSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)




# def test_view(request):
#     data = {
#         'name': 'John',
#         'age': 27
#     }

#     return JsonResponse(data)
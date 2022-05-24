from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

User = get_user_model()

@api_view(['POST'])
def profile(request):
    user_info = {
        'username': request.user.username,
        'age': request.user.age,
        'gender': request.user.gender,
        'occupation': request.user.occupation,
    }
    return JsonResponse(user_info)


@api_view(['PUT'])
def update(request):
    user = User.objects.get(username=request.user)
    user.age = request.data.get('age')
    user.gender = request.data.get('gender')
    user.occupation = request.data.get('occupation')
    user.save()
    user_info = {
        'username': user.username,
        'age': user.age,
        'gender': user.gender,
        'occupation': user.occupation,
    }

    return JsonResponse(user_info)

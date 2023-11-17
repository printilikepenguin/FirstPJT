from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User

@api_view(['GET'])
def duplicateID(request):
    if request.method == 'GET':
        name = request.GET.get('username')
        # existing_user = User.objects.filter(username=name)
        
        print(User)
        if User.objects.filter(username=name):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)

# def duplicateID(request):
#     if request.method == 'GET':
#         name = request.GET.get('username')
#         existing_user = User.objects.filter(username=name)

#         return Response(existing_user)

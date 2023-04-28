from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet 
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance,request.user)
        if request.user == instance:
            partial = kwargs.pop('partial', False)
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
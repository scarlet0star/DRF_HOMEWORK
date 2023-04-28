from rest_framework.viewsets import ModelViewSet
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.response import Response
from rest_framework import status


class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(uid_id=user.id)

    def perform_create(self, serializer):
        serializer.save(uid=self.request.user, is_completed=False)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user == instance.uid:
            partial = kwargs.pop('partial', False)
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user == instance.uid:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

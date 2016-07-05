from rest_framework.viewsets import ModelViewSet
from .serializers import CommandSerializer
from .models import Command


class CommandViewSet(ModelViewSet):
    serializer_class = CommandSerializer

    def get_queryset(self):
        return Command.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        We manually save the user based on who issued the request
        """
        serializer.save(user=self.request.user)

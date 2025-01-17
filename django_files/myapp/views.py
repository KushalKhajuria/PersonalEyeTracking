from rest_framework import viewsets
from .models import UserData
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all()
    serializer_class = MyModelSerializer

    @action(detail=False, methods=['delete'], url_path='delete-all', url_name='delete_all_users')
    def delete_all_users(self, request):
        """
        Deletes all users from the database.
        """
        UserData.objects.all().delete()
        return Response({"message": "All users have been deleted."}, status=status.HTTP_204_NO_CONTENT)
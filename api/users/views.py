from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views
from users.serializers import UserSerializer, GroupSerializer, UserPlayerSerializer
from users.models import UserPlayer

class PlayerEvolveView(views.APIView):
    queryset = UserPlayer.objects.all()

    def get(self, request, format=None):
        players = UserPlayer.objects.all()
        serializer = UserPlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        player = self.get_object(pk)
        xp = request.data
        player.xp += xp
        serializer = UserPlayerSerializer(player, many=False)
        return Response(serializer.data)


class UserPlayerViewSet(viewsets.ModelViewSet):
    queryset = UserPlayer.objects.all()
    serializer_class = UserPlayerSerializer

    def get(self, format=None):
        players = UserPlayer.objects.all()
        serializer = UserPlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserPlayerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, format=None):
        players = queryset
        serializer = UserSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

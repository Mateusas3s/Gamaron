from rest_framework import viewsets
from quests.serializers import QuestsSerializer
from quests.models import Quests


class QuestsViewSet(viewsets.ModelViewSet):

    queryset = Quests.objects.all()
    serializer_class = QuestsSerializer

    def get(self, format=None):
        queryset = queryset
        serializer = QuestsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = QuestsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

from avatar.models import Avatar
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.views import APIView
from avatar.serializers import AvatarSerializer

class AvatarViewSet(viewsets.ModelViewSet):

    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer

@permission_classes((IsAuthenticatedOrReadOnly,))
class getAvatarImageView(APIView):
    def getimage(request, format=None):
        # image_data = open("/avatar_images/download.jpeg", "rb").read()
        return Response(status=status.HTTP_200_OK)








#     def get(self, format=None):
#         queryset = queryset
#         serializer = ItenSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#
#         serializer = ItenSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=ValueError):
#             serializer.create(validated_data=request.data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error_messages,
#                         status=status.HTTP_400_BAD_REQUEST)
#
#
# class PlayerInvetoryViewSet(viewsets.ModelViewSet):
#     queryset = PlayerInventory.objects.all()
#     serializer_class = PlayerInventorySerializer

from quests.models import Quests
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import serializers


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class QuestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quests
        fields = ('id', 'title', 'description', 'reward_xp',
                  'reward_score', 'reward_iten', 'is_activated',
                  'url', 'creator')
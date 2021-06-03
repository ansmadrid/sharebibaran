from rest_framework import serializers
from share_detail.models import Share

#Share Serializer
class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'
from share_detail.models import Share
from rest_framework import viewsets,permissions
from .serializers import ShareSerializer

#Share Viewset
class ShareViewSet(viewsets.ModelViewSet):
    queryset = Share.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ShareSerializer

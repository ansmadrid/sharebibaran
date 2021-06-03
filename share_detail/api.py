from django.db.models.query import QuerySet
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

    # def get_queryset(self):
    #     sold = self.request.query_params.get("sold")
    #     queryset = self.queryset
    #     if sold == "true":
    #         queryset = queryset.filter(sold = True)
    #     if sold == "false":
    #         queryset = queryset.filter(sold = False)
    #     return queryset
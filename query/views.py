from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Query, Reply
from.serializers import QuerySerializer, ReplySerializer


class QueryViewset(viewsets.ModelViewSet):
    """
    View to create/update/delete/view queries. 
    """
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
    permission_classes = (IsAuthenticated,)


class ReplyViewset(viewsets.ModelViewSet):
    """
    View to create/update/delete/view replies. 
    """
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
    permission_classes = (IsAuthenticated,)

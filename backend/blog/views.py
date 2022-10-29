from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import mixins, generics


class PostView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView
    ):
    queryset = Client.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

post_view = PostView.as_view()
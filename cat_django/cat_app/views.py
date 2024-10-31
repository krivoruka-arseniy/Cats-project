from django.shortcuts import render, redirect
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from .models import Cats, Messages, Users
from .serializers import ListCatsSerializer, CatSerializer, UserMessagesSerializer, ListUserMessageSerializer, RegisterUsers


class PaginationsListCats(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5
    
    
class AllListCats(generics.ListAPIView):
    queryset = Cats.objects.all()
    serializer_class = CatSerializer
    pagination_class = PageNumberPagination
    
    
class ListCats(generics.ListAPIView):
    serializer_class = ListCatsSerializer
    pagination_class = PaginationsListCats
    
    def get_queryset(self):
        cats = Cats.objects.filter(cat_owner_id=self.request.user.pk)
        return cats
    
    
class CreateCats(generics.CreateAPIView):
    queryset = Cats.objects.all()
    serializer_class = CatSerializer
    
    def post(self, request, *args, **kwargs):
        Cats.objects.create(
            cat_owner_id=self.request.user.pk,
            cat_name=request.POST['cat_name'],
            cat_age=request.POST['cat_age'],
            cat_color=request.POST['cat_color'],
            cat_breed=request.POST['cat_breed']
        )
        return redirect('/')
    
    
class CatsAPIUpdate(generics.UpdateAPIView):
    queryset = Cats.objects.all()
    serializer_class = CatSerializer
    
    
class CatsAPIDestroy(generics.DestroyAPIView):
    queryset = Cats.objects.all()
    serializer_class = CatSerializer
    

class UserMessagesCreate(generics.CreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = UserMessagesSerializer
    
    def post(self, request, *args, **kwargs):
        Messages.objects.create(
            message_owner_id=self.request.user.pk,
            where_message_id=request.POST['where_message'],
            message_name=request.POST['message_name'],
            message_content=request.POST['message_content']
        )
        return redirect('messages')
    
    
class UserMessagesList(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = ListUserMessageSerializer
    pagination_class = PaginationsListCats
    
    def get_queryset(self):
        messages = Messages.objects.filter(where_message_id=self.request.user.pk)
        return messages
    
    
class UserMessagesDestroy(generics.DestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = ListUserMessageSerializer


class RegisterUsers(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = RegisterUsers
    
    def post(self, request, *args, **kwargs):
        user = Users(
            username=request.POST['username'],
            email=request.POST['email'],
            address=request.POST['address']
        )
        user.set_password(request.POST['password'])
        user.save()
        return redirect('/')
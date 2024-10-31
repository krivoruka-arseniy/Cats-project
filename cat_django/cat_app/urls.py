from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ListCats.as_view()),
    path('register/', views.RegisterUsers.as_view()),
    path('users/', include('rest_framework.urls')),
    path('create_cats/', views.CreateCats.as_view()),
    path('update/<int:pk>/', views.CatsAPIUpdate.as_view()),
    path('cats/destroy/<int:pk>/', views.CatsAPIDestroy.as_view()),
    path('create_messages/', views.UserMessagesCreate.as_view()),
    path('messages/', views.UserMessagesList.as_view(), name='messages'),
    path('messages/destroy/<int:pk>/', views.UserMessagesDestroy.as_view()),
    path('all_cats/', views.AllListCats.as_view())
]
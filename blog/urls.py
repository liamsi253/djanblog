from django.urls import path
from .views import Home, Show, Add, Edit, Delete

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('blog/<int:pk>', Show.as_view(), name="show"),
    path('blog/add/', Add.as_view(), name="add"),
    path('blog/edit/<int:pk>', Edit.as_view(), name="edit"),
    path('blog/<int:pk>/delete', Delete.as_view(), name="delete"),
]

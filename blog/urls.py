from django.urls import path
from .views import Home, Show, Add

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('blog/<int:pk>', Show.as_view(), name="show"),
    path('blog/add/', Add.as_view(), name="add")

]

from django.urls import path, re_path
from .views import home, single

urlpatterns = [
    path('', home, name='posts_archive'),
    path('<slug:pk>/', single, name='post_single'),
]

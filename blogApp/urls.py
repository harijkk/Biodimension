from django.urls import path
from . import views

urlpatterns = [
    path('blogs', views.home),
    path('blog/<slug:post_id>', views.post)
]

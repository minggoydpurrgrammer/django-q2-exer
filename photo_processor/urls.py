from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_view, name='upload'),
    path('status/<int:photo_id>/', views.status_view, name='status'),
]
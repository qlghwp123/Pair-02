from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:_id>/', views.detail, name='detail'),
    path('<int:_id>/update/', views.update, name='update'),
    path('<int:_id>/delete/', views.delete, name='delete'),
]
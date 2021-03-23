from django.urls import path
from . import views

urlpatterns = [
    path('', views.HookahListAPIView.as_view(), name = 'hookah_list'),
    path('<int:id>/', views.HookahRetrieveAPIView.as_view(), name = 'hookah_detail')
]
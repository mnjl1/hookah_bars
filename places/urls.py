from django.urls import path
from . import views

urlpatterns = [
    path('', views.HookahListAPIView.as_view(), name = 'hookah_list'),
    path('<int:id>/', views.HookahRetrieveAPIView.as_view(), name = 'hookah_detail'),
    path('create/', views.HookahCreateAPIView.as_view(), name = 'hookah_create'),
    path('update/<int:id>/', views.HookahRetrieveUpdateAPIView.as_view(), name = 'hookah_update'),
    path('delete/<int:id>/', views.HookahDestroyAPIView.as_view(), name = 'hookah_delete')
]
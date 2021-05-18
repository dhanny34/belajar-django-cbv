from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SekolahList.as_view(), name='list'),
    path('sekolah/<int:pk>', views.SekolahDetail.as_view(), name='sekolahdetail'),
]
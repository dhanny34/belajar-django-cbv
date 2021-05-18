from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SekolahListView.as_view(), name='list'),
    path('sekolah/<int:pk>', views.SekolahDetailView.as_view(), name='sekolahdetail'),
    path('buat/', views.SekolahCreateView.as_view(), name='buat'),
    path('update/<int:pk>', views.SekolahUpdateView.as_view(), name='update'),
    path('hapus/<int:pk>', views.SekolahHapusView.as_view(), name='hapus'),
]
from django.urls import path
from . import views
from .views import PickerView

app_name = 'benny'

urlpatterns = [

    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload_file'),
    path('files', views.files, name='files'),
    path('test', PickerView.as_view(), name='test_law'),

]

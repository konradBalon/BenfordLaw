from django.urls import path
from . import views

app_name = 'benny'

urlpatterns = [

    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload_file'),
    path('files', views.files, name='files'),
    path('test', views.test_law, name='test_law'),

]

from django.urls import path
from . import views
from .views import PickerView, HandleFileView

app_name = 'benny'

urlpatterns = [

    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload-file'),
    path('files', views.files, name='files'),
    path('pick-file', PickerView.as_view(), name='pick-file'),
    path('handle-file/<str:document>', HandleFileView.as_view(), name='handle-file'),

]

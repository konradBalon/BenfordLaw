from django.urls import path
from . import views
from .views import HeaderPickerView, FilePickerView, HandleFileView

app_name = 'benny'

urlpatterns = [

    path('', views.index, name='index'),
    path('upload', views.upload_file, name='upload-file'),
    path('files', views.files, name='files'),
    path('pick-file', FilePickerView.as_view(), name='file-picker'),
    path('pick-header/<str:document>', HeaderPickerView.as_view(), name='header-picker'),
    path('handle-file/<str:document>/<str:header>', HandleFileView.as_view(), name='file-handler'),

]

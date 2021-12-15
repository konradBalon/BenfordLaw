from http.client import HTTPResponse

from django.core.exceptions import ValidationError
from django.db.models import FilePathField
from django.shortcuts import render, redirect
from django.views import View

from .forms import DocumentForm

# Create your views here.
from .models import Document


def index(request):
    return render(request, 'benny/index.html')


def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect('home')
        print(form.errors)


    else:
        form = DocumentForm()

    return render(request, 'benny/upload.html', {
        'form': form
    })


def files(request):
    ctx = Document.objects.all()
    return render(request, 'benny/files.html', {"files": ctx})


class PickerView(View):

    def get(self, request):
        uploaded_files = Document.objects.all()
        return render(request, 'benny/TestTheLaw.html', {'files': uploaded_files})

    def post(self, request):
        selected_file = request.POST.get('selected_file')
        print(selected_file)

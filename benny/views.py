from http.client import HTTPResponse

from django.db.models import FilePathField
from django.shortcuts import render, redirect
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
    else:
        form = DocumentForm()
    return render(request, 'benny/upload.html', {
        'form': form
    })


def files(request):
    ctx = Document.objects.all()
    return render(request, 'benny/index.html', {"context": ctx})

def testLaw(request):
    path = FilePathField.path
    print(path)
    return HTTPResponse("ok")

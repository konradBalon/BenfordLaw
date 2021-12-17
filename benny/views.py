from http.client import HTTPResponse

import pandas as pd
from django.core.exceptions import ValidationError
from django.db.models import FilePathField
from django.http import HttpResponseRedirect
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
            return redirect('benny:index')
        print(form.errors)


    else:
        form = DocumentForm()

    return render(request, 'benny/upload.html', {
        'form': form
    })


def files(request):
    ctx = Document.objects.all()
    return render(request, 'benny/files.html', {"files": ctx})


class FilePickerView(View):

    def get(self, request):
        uploaded_files = Document.objects.all()
        return render(request, 'benny/file-picker.html', {'files': uploaded_files})

    def post(self, request):
        selected_file = request.POST.get('selected_file')
        return redirect('benny:header-picker', document=selected_file.split('/')[1])


class HeaderPickerView(View):

    def get(self, request, document):
        doc = Document.objects.filter(document=f'documents/{document}').first()
        handler = HandleFile(doc)
        handler.load_data_frame()

        return render(request, 'benny/header-picker.html',
                      {'document': doc, 'headers': handler.get_headers(), 'preview': handler.get_preview()})

    def post(self, request, document):
        selected_header = request.POST.get('selected_header')

        print(selected_header)
        return redirect('benny:file-handler', document=document, header=selected_header)


class HandleFileView(View):
    def get(self, request, document, header):
        print(document, header)
        document = Document.objects.filter(document=f'documents/{document}').first()
        handler = HandleFile(document=document)
        handler.load_data_frame()
        file_data = handler.get_benford_data(header)
        benford_data = [0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046]
        labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return render(request, 'benny/file-handler.html', {'labels': labels,
                                                           'benford_data': benford_data, 'file_data': file_data})


class HandleFile:

    def __init__(self, document):
        self.document = document
        self.df = None

    def load_data_frame(self):
        df = pd.read_csv(self.document.document.path, on_bad_lines='skip', sep=None, engine='python')
        self.df = df

    def get_headers(self):
        headers = self.df.columns
        return headers

    def get_preview(self):
        return self.df.head().to_html



    def get_benford_data(self, column):
        benford_data = []

        # convert to str and keep first character
        df = self.df[column].astype(str).str[:1]

        dframe = pd.DataFrame(data=df)

        for _ in range(1, 10):
            # count values for each number then divide by all rows count
            val = (dframe[dframe[column] == str(_)].shape[0]) / (df.shape[0])
            benford_data.append(val)

        return benford_data

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.conf import settings
import os
import shutil


def index(request):
#     folder = settings.MEDIA_ROOT
#     for the_file in os.listdir(folder):
#         file_path = os.path.join(folder, the_file)
#         try:
#             if os.path.isfile(file_path):
#                 os.unlink(file_path)
#                 # elif os.path.isdir(file_path): shutil.rmtree(file_path)
#         except Exception as e:
#             print(e)

#     file_name = 'Carte3.kml'
#     path = settings.MEDIA_ROOT
#     os.remove(os.path.join(path, file_name))

    return render(request, 'world/index.html')


def kml(request):
    template = loader.get_template('world/kml.html')
    context = {

    }

    return HttpResponse(template.render(context, request))


def answer_me(request):

    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)

    data = {
        'respond': uploaded_file_url,
        'file_name': myfile.name
    }
    return JsonResponse(data)

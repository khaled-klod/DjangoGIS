from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


def index(request):
    # if request.method == 'POST':
    #     print('POOOST')
    #     myfile = request.FILES['myfile']
    #     fs = FileSystemStorage()
    #     filename = fs.save(myfile.name, myfile)
    #     uploaded_file_url = fs.url(filename)
    #     return render(request, 'world/index.html', {
    #         'uploaded_file_url': uploaded_file_url
    #     })
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
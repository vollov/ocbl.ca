from django.shortcuts import render
from forms import UploadFileForm
from django.http import HttpResponseRedirect

def upload_photo(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        photo_form = UploadFileForm()
        page_title = 'File Upload'
        context = {
            'photo_form': photo_form,
            'page_title': page_title,
        }
        
        
    return render(request, 'upload.html', context)

def handle_uploaded_file(file):
    print file.name
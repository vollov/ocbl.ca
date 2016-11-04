from django.shortcuts import render
from forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.db.models import ImageField

def upload_photo(request):
    if request.method == 'POST':
        photo_form = UploadFileForm(request.POST, request.FILES)
        if photo_form.is_valid():
            image = photo_form.cleaned_data['image']
            albumn = photo_form.cleaned_data['albumn']
            photo_form.save()
            handle_uploaded_file(request.FILES['image'], albumn)
            return HttpResponseRedirect('/game/photos/')
    else:
        photo_form = UploadFileForm()
        page_title = 'File Upload'
        context = {
            'photo_form': photo_form,
            'page_title': page_title,
        }
        
        
    return render(request, 'upload.html', context)

def handle_uploaded_file(file, albumn):
    """upload_path = album_slug/f47ac10b-58cc-4372-a567-0e02b2c3d479.jpg"""
    
    print 'file.name={0}, albumn.slug={1}'.format(file.name, albumn.slug)
    
# use with to close the file automatically
#     try: 
#         with open('some/file/name.txt', 'wb+') as destination:
#             for chunk in f.chunks():
#                 destination.write(chunk)
#      
#     except IOError:
#         print "Could not read file:", fName
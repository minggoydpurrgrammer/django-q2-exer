from django.shortcuts import render, redirect
from django_q.tasks import async_task
from .models import Photo
from .forms import PhotoForm

def upload_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            # Offload to Django-Q2
            async_task('photo_processor.tasks.process_image_task', photo.id)
            return redirect('status', photo_id=photo.id)
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})

def status_view(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    return render(request, 'status.html', {'photo': photo})
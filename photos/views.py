from django.shortcuts import render,                 redirect


from .models import Photo
# Create your views here.
def gallery(request):
    photos = Photo.objects.all()
    context = {
        'photos':photos
    }
    return render(request,'photos/gallery.html',context)


def viewPhoto(request,pk):
    photos = Photo.objects.get(id = pk)
    return render(request,'photos/photo.html',{'photos':photos})


def addPhoto(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        photos = Photo.objects.create(
            image=image,
            description = data['description'],
        )

        return redirect('gallery')


    return render(request,'photos/add.html')
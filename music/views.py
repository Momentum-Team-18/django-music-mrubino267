from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlbumForm
from .models import Album
from django.utils import timezone

# Create your views here.


def post_album_list(request):
    albums = Album.objects.all()
    return render(request, 'index.html', {'albums': albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/album_detail.html', {'albums': album})


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST)
        form.save()
        return redirect('post-album-list')
    return render(request,'albums/add_album.html', {'form': form})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "GET":
        context = {'form': AlbumForm(instance=album), 'pk': pk}
    else:
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('post-album-list')
    return render(request,'albums/edit_album.html', context)


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('albums/post-album-list')
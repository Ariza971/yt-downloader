from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube

def home(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url :
            try : 
                yt = YouTube(url)
                stream = yt.streams.get_highest_resolution()
                stream.download(output_path='downloads/')
                return HttpResponse(f"Downloaded: {yt.title}")
            except Exception as e:
                return HttpResponse(f"Error: {str(e)}")
    return render(request, 'downloader/home.html')
            
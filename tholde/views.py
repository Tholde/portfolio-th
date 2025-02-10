from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def index(request):
    # return JsonResponse({"message": "Hello World"})
    return render(request, "index.html")


def redirect_linkedin(request):
    return HttpResponseRedirect("https://www.linkedin.com/in/tholde-rftn")
def redirect_github(request):
    return HttpResponseRedirect("https://github.com/tholde")
def redirect_twitter(request):
    return HttpResponseRedirect("https://x.com/tholde_rftn")
def redirect_facebook(request):
    return HttpResponseRedirect("https://www.facebook.com/ambanimaso.technology")
def redirect_instagram(request):
    return HttpResponseRedirect("https://www.instagram.com/tholde.rftn")
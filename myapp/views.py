from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import data
from django.http import HttpResponseRedirect

# Create your views here.


def scrape(request):
    if request.method == "POST":
        site = request.POST.get("site", "")
        page = requests.get(site)
        soup = BeautifulSoup(page.text, "html.parser")

        for link in soup.find_all("a"):
            address = link.get("href")
            name = link.string
            data.objects.create(address=address, name=name)
        return HttpResponseRedirect("/scrape")
    else:
        link_address = data.objects.all()
    return render(request, "myapp/result.html", {"link_address": link_address})


def clear(request):
    data.objects.all().delete()
    return render(request, "myapp/result.html")

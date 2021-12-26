from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ViewForm

# Create your views here.

def index(request):
    if request.method == "POST":
        form = ViewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")

    form = ViewForm()
    return render(request, "api_view/index.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "api_view/thank-you.html", {})
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View

from .forms import ViewForm

class ViewView(View):
    def get(self, request):
        form = ViewForm()

        return render(request, "api_view/index.html", {
            "form": form
        })

    def post(self, request):
        form = ViewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(request, "api_view/index.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "api_view/thank-you.html", {})
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views import View
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required


from .forms import ViewForm
from .serializers import ViewSerializer
from .models import ViewModel


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


class ViewModelView(viewsets.ModelViewSet):
    serializer_class = ViewSerializer
    queryset = ViewModel.objects.all()

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from app.forms import NumerologyForm


class NumerologyView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        form = NumerologyForm()
        return render(request, 'numerology.html', {'form': form})

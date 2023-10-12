from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from app.forms import NumerologyForm
from core.calculation import make_numerology
from core.models import Person


class NumerologyView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        form = NumerologyForm()
        person = request.session.get('person')
        request.session['person'] = None
        return render(request, 'numerology.html', {'form': form, 'person': person})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = NumerologyForm(request.POST)
        if form.is_valid():
            person = Person(**form.cleaned_data)
            person_with_numerology = make_numerology(person)
            request.session['person'] = person_with_numerology.model_dump_json()
            return redirect('numerology')

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from app.forms import NumerologyForm
from core.calculation import make_numerology
from core.models import Person


class NumerologyView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        person = request.session.get('person')
        person_dict = eval(person) if person else None
        numerology = person_dict.get('numerology') if person_dict else None
        if numerology:
            numerology['present_numbers'] = ''.join(f'{x}, ' for x in numerology['present_numbers'])[:-2]
            numerology['missing_numbers'] = ''.join(f'{x}, ' for x in numerology['missing_numbers'])[:-2]
        request.session['person'] = None
        form = NumerologyForm(
            initial={
                'first_name': person_dict.get('first_name'),
                'last_name': person_dict.get('last_name'),
                'birth': person_dict.get('birth')
            } if person_dict is not None else {}
        )
        return render(request, 'numerology.html', {'form': form, 'numerology': numerology})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = NumerologyForm(request.POST)
        if form.is_valid():
            person = Person(**form.cleaned_data)
            person_with_numerology = make_numerology(person)
            request.session['person'] = person_with_numerology.model_dump_json()
            return redirect('numerology')

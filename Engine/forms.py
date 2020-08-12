from django.forms import Form
from django import forms
from django.forms.widgets import Select,CheckboxSelectMultiple
from .models import seat
class SeatBookingForm(Form):
    s = seat.objects.all()
    OPTS = []
    for i, x in enumerate(s):
        OPTS.append((i+1, x.id))
    seats = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'id': x}), choices=OPTS)
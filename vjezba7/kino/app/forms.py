from email.policy import default
from random import choices
from django.forms import ModelForm
from django import forms
from .models import Projection,Ticket
from django.contrib.admin.widgets import AdminTimeWidget

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['movieName','seatNumber']


class CreateProjectionForm(forms.Form):
    movieName = forms.CharField(label='Movie name', max_length=100)
    screeningTime = forms.TimeField(label='Screening time',widget=AdminTimeWidget(format='%H:%M'))
    movieSeats = forms.IntegerField(label='Seats available')


class UpdateProjectionForm(forms.Form):

    projSelect = forms.ModelChoiceField(label="Select delete movie",queryset = Projection.objects.all())
    newMovieName = forms.CharField(label="New movie name", max_length=100)
    newScreeningTime = forms.TimeField(label='New movie time',widget=AdminTimeWidget(format='%H:%M'))
    newMovieSeats = forms.IntegerField(label='Seats available')

class DeleteProjectionForm(forms.Form):
    projSelect = forms.ModelChoiceField(label="Select to delete",queryset = Projection.objects.all())

    

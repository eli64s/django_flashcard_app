from django.forms import ModelForm 
from django import forms
from .models import Card_Set, Card

class Card_Set_Form(ModelForm):
    '''
    Form mapping to the Card_Set model
    '''
    class Meta:
        model = Card_Set
        fields = ['topic', 'description']
        #fields = ['topic', 'description', 'is_active']


class Card_Form(ModelForm):
    '''
    Form mapping to the Card model
    '''
    class Meta:
        model = Card
        fields = ['parent_card_set', 'word', 'definition', 'sentences']


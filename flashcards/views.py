# flashcards views
from django.shortcuts import (
    HttpResponseRedirect,
	get_object_or_404,
    render
)
from django.urls import reverse
from .models import Card_Set, Card
from .forms import Card_Set_Form, Card_Form
from PyDictionary import PyDictionary

# Views for the 'flashcards' app
def flashcards(request):
    '''
    Renders the flashcard app's flashcards.html template
    '''
    # Card_Set.objects.all() returns all cards in the database
    topic_query_set = Card_Set.objects.all().order_by('topic').filter(is_active = True) 
    context = {'topics': topic_query_set}   # Dictionary{} rendered for flashcards/flashcards.html
    return render(request, 'flashcards/flashcards.html', context)


def create_card_set(request):
    '''
    Renders a template used to create POST requests to create a new card set
    '''
    # Create the form instance and populate data from the request
    if request.method == 'POST':
        form = Card_Set_Form(request.POST)

        if form.is_valid():                                               # Check if form is valid
            form.save()                                                   # Save form - object saved to database                                                                          
            return HttpResponseRedirect(reverse('flashcards:flashcards')) # Redirect to the flashcards view

    else:
        form = Card_Set_Form()

    context = {'form': form}
    return render(request, 'flashcards/create_card_set.html', context)


def create_card(request, card_set_id):
    '''
    View to create a new card in the given card set id
    '''
    # get_object_or_404() displays '404 error' if it fails to get object 
    card_set_object = get_object_or_404(Card_Set, id = card_set_id)

    if request.method == 'POST':
        form = Card_Form(request.POST)

        if form.is_valid():                                                 
            form.save()                                                     
            return HttpResponseRedirect(reverse('flashcards:flashcards'))            

    else:
        form = Card_Form(initial = {'parent_card_set': card_set_object})

    context = {'form': form}
    return render(request, 'flashcards/add_edit_cards.html', context)


def delete_card(request, card_id):
    '''
    Deletes card whose id == card_id
    '''
    card_object = get_object_or_404(Card, id = card_id)
    card_object.delete()
    return HttpResponseRedirect(reverse('flashcards:flashcards'))        


def delete_card_set(request, card_set_id):
	'''
	Deletes card set whose id == card_set_id
	'''
	card_set_object = get_object_or_404(Card_Set, id = card_set_id)
	card_set_object.delete()										
	return HttpResponseRedirect(reverse('flashcards:flashcards'))     


def edit_card(request, card_id):
    '''
    View that renders a form to edit the card object's information
    '''
    card_object = get_object_or_404(Card, id = card_id)

    if request.method == 'POST':
        form = Card_Form(request.POST, instance = card_object)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flashcards:flashcards'))     
    
    else:
        form = Card_Form(instance = card_object)
    
    context = {'form': form, 'edit_mode': True, 'card_object': card_object}
    return render(request, 'flashcards/add_edit_cards.html', context)
    

def edit_card_set(request, card_set_id):
	'''
	View that renders a form to edit the card set object's information
    '''

	card_set_object = get_object_or_404(Card_Set, id = card_set_id)

	if request.method == 'POST':
		form = Card_Set_Form(request.POST, instance = card_set_object)

		if form.is_valid():                 
			form.save()                     
		return HttpResponseRedirect(reverse('flashcards:flashcards'))     

	else:
		form = Card_Set_Form(instance = card_set_object)

	context = {'form': form, 'edit_mode': True, 'card_set_object': card_set_object}
	return render(request, 'flashcards/create_card_set.html', context)


def view_card_set(request, card_set_id):
    '''
    View to get card set from the database -
    returns the first card in card set - 
    unless a card_id is defined in the url
    '''
    card_set_object = get_object_or_404(Card_Set, id = card_set_id)
    card_list = card_set_object.card_set.all()	# Returns all cards in respective card set
    card_object = card_list.first()			    # Returns the first card in the set

    # Condition to get the next/previous card in the set
    if request.method == 'GET' and 'card' in request.GET:
        card_object = get_object_or_404(Card, id = request.GET['card'])

    context = {'card_set_object': card_set_object, 'card_object': card_object}
    return render(request, 'flashcards/view_cards.html', context)


def dictionary(request):
    '''
    View for the 'search bar' in the
    navbar - a page is rendered that 
    displays the searched word and its
    definition using PyDictionary
    '''

    try:
        if request.method == 'GET':
            word_searched = request.GET.get('word_searched')
            dictionary = PyDictionary()                  # PyDictionary module 
            word_def = dictionary.meaning(word_searched) # Get definition of word searched
            word_def = list(word_def.values())[0][0]     # Extract definition as a string
        
    except:
        word_def = 'This word does not exist in the database'

    context = {'word_searched': word_searched, 'word_def': word_def}
    return render(request, 'flashcards/dictionary.html', context)

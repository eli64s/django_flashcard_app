# flashcards views
from django.shortcuts import (
    HttpResponseRedirect,
	get_object_or_404,
    render
)
from django.urls import reverse
from .models import Card_Set, Card
from .forms import Card_Set_Form, Card_Form

# Create your views here.
def flashcards(request):
    '''
    Renders the flashcards app flashcards.html template
    '''
    # This returns all cards in the database
    topic_query_set = Card_Set.objects.all().order_by('topic').filter(is_active = True) 
    context = {'topics': topic_query_set}   # Dictionary passed that will be rendered for flashcards/home.html
    return render(request, 'flashcards/flashcards.html', context)


def create_card_set(request):
    '''
    Renders a template used to create POST requests
    to create a new card set
    '''
    # Create the form instance, and populate data from the request
    if request.method == 'POST':
        form = Card_Set_Form(request.POST)

        if form.is_valid():                                # Check if the form is valid
            form.save()                                    #Save the form, saves the object to the database
            return HttpResponseRedirect(reverse('flashcards:flashcards'))   

    else:
        form = Card_Set_Form()

    context = {'form': form}
    return render(request, 'flashcards/create_card_set.html', context)


def create_card(request, card_set_id):
    '''
    Used to create a new card for the given card set id
    '''
    card_set_object = get_object_or_404(Card_Set, id = card_set_id)

    if request.method == 'POST':
        form = Card_Form(request.POST)

        if form.is_valid():                                                 # Check if the form is valid
            form.save()                                                     # Save the form, saves the object to the database
            return HttpResponseRedirect(reverse('flashcards:flashcards'))   # Redirect user back to the flashcards view card set page         

    else:
        form = Card_Form(initial = {'parent_card_set': card_set_object})

    context = {'form': form}
    return render(request, 'flashcards/add_edit_cards.html', context)


def delete_card(request, card_id):
    '''
    Deletes the cards whose id == card_id
    '''
    card_object = get_object_or_404(Card, id = card_id)
    card_object.delete()
    return HttpResponseRedirect(reverse('flashcards:flashcards'))        


def delete_card_set(request, card_set_id):
	'''
	Deletes the card set whose id == card_set_id
	'''
	card_set_object = get_object_or_404(Card_Set, id = card_set_id)
	card_set_object.delete()										
	return HttpResponseRedirect(reverse('flashcards:flashcards'))     


def edit_card(request, card_id):
    '''
    Renders the form to edit information on the card
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
	Renders the form to edit infomration about the card set object
	'''

	# If this statement does not get the object, it displays a 404 error
	card_set_object = get_object_or_404(Card_Set, id = card_set_id)

    # Create the form instance, and populate data from the request
	if request.method == 'POST':
		form = Card_Set_Form(request.POST, instance = card_set_object)

		if form.is_valid():                 # Check if the form is valid
			form.save()                     # Save the form, saves the object to the database
		return HttpResponseRedirect(reverse('flashcards:flashcards'))     

	else:
		form = Card_Set_Form(instance = card_set_object)

	context = {'form': form, 'edit_mode': True, 'card_set_object': card_set_object}
	return render(request, 'flashcards/create_card_set.html', context)


def view_card_set(request, card_set_id):
    '''
    Get card set from the database,
    returns first card in card set unless card_id is specified in the url
    '''
    card_set_object = get_object_or_404(Card_Set, id = card_set_id)
    card_list = card_set_object.card_set.all()		# Returns all cards in respective card set
    card_object = card_list.first()			        # Returns the first card in the set

    # Functionality to get the next/previous card in set
    if request.method == 'GET' and 'card' in request.GET:
        card_object = get_object_or_404(Card, id = request.GET['card'])

    '''
    # Form for writing the vocabulary word in a sentence
    if request.method == 'POST':
        form = Card_Form(request.POST, instance = card_object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('flashcards:flashcards')) 

    else:
        form = Card_Form(instance = card_object)
    '''

    context = {'card_set_object': card_set_object, 'card_object': card_object}
    return render(request, 'flashcards/view_cards.html', context)


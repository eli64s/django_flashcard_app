import random
from django.db import models

# Models for the 'flashcards' app
class Card_Set(models.Model):
    '''
    Card_Set model functions as the deck that a card belongs to
    A deck has a topic and description
    '''                                                        
    topic = models.CharField(max_length = 50, null = False, blank = False)       # Topic of the Deck
    description = models.CharField(max_length = 300, null = False, blank = True) # Description of topic
    is_active = models.BooleanField(default = True)   # When Card_Set is created, it will default to 
                                                      # being inactive as no cards will exist in the set
    # __str__ is a function that modifies string representation
    # When Cards.objects.all() is run, the name of the word will be displayed
    # Without this function, Cards.objects.all() would return [<Cards: Cards object (1)>]
    def __str__(self):
        return self.topic


    def get_card_count(self):
        '''
        Returns the card count in each deck as an integer
        '''
        return self.card_set.count()
    get_card_count.short_description = 'Card Count'  # Card Count is the column header in Admin Panel


    def get_random_card(self):
        '''
        Returns a random card from the deck 
        '''
        random_number = random.randint(0, self.card_set.count() - 1)    # Return random card from deck
        random_card = self.card_set.all()[random_number]
        return random_card


class Card(models.Model):
    '''
    Card model for the cards in the deck 
    Parent is the Card_Set model
    Each card has word, definition, and sentence
    '''
    parent_card_set = models.ForeignKey(Card_Set, on_delete = models.CASCADE)
    
    word = models.CharField(max_length = 50, null = False, blank = False)         # Vocabulary word
    definition = models.TextField(max_length = 500, null = False, blank = False)  # Word's definition
    sentences = models.TextField(max_length = 500, null = False, blank = True)    # Word used in sentence
    

    def __str__(self):
        return self.word


    def is_there_previous_card(self):
        '''
        Returns True if card is not the frist card in the deck
        '''
        first_card_in_set = self.parent_card_set.card_set.first()
        if self == first_card_in_set:
            return False
        else:
            return True


    def get_previous_card(self):
        '''
        Returns the previous card in the deck
        '''
        first_card_in_set = self.parent_card_set.card_set.first()

        if self == first_card_in_set:
            return self.parent_card_set.card_set.last()
        else:
            return self.parent_card_set.card_set.filter(id__lt = self.id).last()


    def is_there_a_next_card(self):
        '''
        Returns True if the card is not last in the deck
        '''
        last_card_in_set = self.parent_card_set.card_set.last()
        if self == last_card_in_set:
            return False
        else:
            return True


    def get_next_card(self):
        '''
        Returns the next card in the deck
        '''
        last_card_in_set = self.parent_card_set.card_set.last()
        if self == last_card_in_set:
            return self.parent_card_set.card_set.first()
        else:
            return self.parent_card_set.card_set.filter(id__gt = self.id).first()


from django.contrib import admin
from .models import Card_Set, Card

def push_live(modeladmin, request, query_set):
    '''
    In the Action: dropdown on the Admin Panel -
    Let's admin select multiple card sets at once to push to active
    '''
    rows_updated = query_set.update(is_active = True)

    # Message sent to admin - displaying how many sets were updated as active
    if rows_updated == 1:
        message = '1 set was'

    else:
        message = '%s were' % rows_updated
    modeladmin.message_user(request, '%s sucessfully updated' % message)  

push_live.short_description = 'Select card sets as active.'

# Customizing the Admin Panel
class Card_Set_Admin(admin.ModelAdmin):

     # 'is_active' adds column to the Admin Panel - displaying if topic is active (inactive means there are no cards in the card set)
     # 'get_card_count' adds column to the Admin Panel - displaying total number of cards in each card set
    list_display = ('topic', 'is_active', 'get_card_count')  

    # Add filter box on the Admin Panel, letting admin filter to active/inactive card sets
    list_filter = ('is_active',)

    # Admin can search for topic or description
    search_fields = ['topic', 'description']

    actions = [push_live]

class Card_Admin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Card_Set, Card_Set_Admin)
admin.site.register(Card, Card_Admin)
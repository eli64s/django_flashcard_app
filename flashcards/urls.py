# flashcards app urls conf
from django.conf.urls import url, include
from . import views # . means we are in the same directory (views is in same directory as urls)

urlpatterns = [ 
    url(r'^$', views.flashcards, name = 'flashcards'), 
    url(r'create/', views.create_card_set, name = 'create_card_set'), 
    url(r'create_card/(?P<card_set_id>[\d]+)', views.create_card, name = 'create_card'), 
    url(r'delete/(?P<card_set_id>[\d]+)', views.delete_card_set, name = 'delete_card_set'), 
    url(r'delete_card/(?P<card_id>[\d]+)', views.delete_card, name = 'delete_card'), 
    url(r'edit/(?P<card_set_id>[\d]+)', views.edit_card_set, name = 'edit_card_set'),
    url(r'edit_card/(?P<card_id>[\d]+)', views.edit_card, name = 'edit_card'), 
    url(r'view/(?P<card_set_id>[\d]+)', views.view_card_set, name = 'view_card_set'), 
    url(r'dictionary/', views.dictionary, name = 'dictionary'), 
]
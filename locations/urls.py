from django.urls import path
from .views import *

urlpatterns = [
    # Terminals
    path('terminals/', terminals, name='terminals'),
    path('search_terminals/', search_terminals, name='search_terminals'),
    path('create_terminal/', create_terminal, name='create_terminal'),
    path('update_terminal/<int:pk>', update_terminal, name='update_terminal'),
    path('delete_terminal/<int:pk>', delete_terminal, name='delete_terminal'),
    # Gates
    path('gates/', gates, name='gates'),
    path('search_gates/', search_gates, name='search_gates'),
    path('create_gate/', create_gate, name='create_gate'),
    path('update_gate/<int:pk>', update_gate, name='update_gate'),
    path('delete_gate/<int:pk>', delete_gate, name='delete_gate'),
    # Stands
    path('stands/', stands, name='stands'),
    path('search_stands/', search_stands, name='search_stands'),
    path('create_stand/', create_stand, name='create_stand'),
    path('update_stand/<int:pk>', update_stand, name='update_stand'),
    path('delete_stand/<int:pk>', delete_stand, name='delete_stand'),
    # PBBs
    path('pbbs/', pbbs, name='pbbs'),
    path('search_pbbs/', search_pbbs, name='search_pbbs'),
    path('create_pbb/', create_pbb, name='create_pbb'),
    path('update_pbb/<int:pk>', update_pbb, name='update_pbb'),
    path('delete_pbb/<int:pk>', delete_pbb, name='delete_pbb'),
]
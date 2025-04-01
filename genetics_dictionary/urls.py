from django.urls import path
#from config.urls import urlpatterns
from .views import add_term, term_list

urlpatterns = [
    path('add/', add_term, name='add_term'),
    path('list/', term_list, name="terms_list")
]
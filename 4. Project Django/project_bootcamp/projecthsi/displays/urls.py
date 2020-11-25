from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('participant', views.participant, name='participant'),
    path('participant-table', views.participant_table, name='participant_table'),
    path('add-participant', views.add_participant, name='add_participant'),
]

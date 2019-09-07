from django.urls import path
from .views import *

app_name='flags'

urlpatterns =[
	path('all', SignalsListView.as_view()),
	path('detail/<int:pk>', SignalDetailView.as_view())
	]
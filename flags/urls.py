from django.urls import path
from .views import *

app_name='flags'

urlpatterns =[
	path('all', FlagsListView.as_view()),
	path('flag/detail/<int:pk>', FlagDetailView.as_view())
	]
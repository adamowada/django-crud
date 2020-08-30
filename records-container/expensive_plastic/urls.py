from .views import HomePageView, CreatePageView
from django.urls import path, include

urlpatterns = [
    path('', HomePageView.as_view(), name='Plastic'),
    path('create/', CreatePageView.as_view(), name='Make_Plastic')
]
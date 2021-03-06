from django.urls import path, re_path, include
from .api import views


urlpatterns = [

	path('home/', views.HomePage.as_view(), name="home"),
    path('create/', views.FestCreate.as_view(), name="create"),
    path('update/', views.FestUpdate.as_view(), name="update"),
    path('delete/', views.FestDelete.as_view(), name="delete"),
    path('event/delete/', views.EventDelete.as_view(), name="eventDelete"),
    path('sponsor/delete/', views.SponsorDelete.as_view(), name="sponsorDelete"),
    path('details/', views.FestDetails.as_view(), name="details"),
    path('liked/', views.FestLiked.as_view(), name="liked")
]

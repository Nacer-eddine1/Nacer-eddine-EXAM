from django.urls import path
from .views import (
    CustomLoginView,
    JokeListView,
    JokeCreateView,
    JokeDetailView,
    JokeUpdateView,
    JokeDeleteView,
    SignupView
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', JokeListView.as_view(), name='joke_list'),
    path('joke/new/', JokeCreateView.as_view(), name='joke_create'),
    path('joke/<int:pk>/', JokeDetailView.as_view(), name='joke_detail'),
    path('joke/<int:pk>/edit/', JokeUpdateView.as_view(), name='joke_update'),
    path('joke/<int:pk>/delete/', JokeDeleteView.as_view(), name='joke_delete'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

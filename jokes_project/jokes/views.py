from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Joke
from .forms import SignUpForm, JokeForm
from django.contrib.auth.mixins import LoginRequiredMixin

class JokeListView(ListView):
    model = Joke
    template_name = 'list_jokes.html'

class JokeDetailView(DetailView):
    model = Joke
    template_name = 'joke_detail.html'

class JokeCreateView(LoginRequiredMixin, CreateView):
    model = Joke
    form_class = JokeForm
    template_name = 'create_joke.html'
    success_url = reverse_lazy('joke_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeUpdateView(LoginRequiredMixin, UpdateView):
    model = Joke
    form_class = JokeForm
    template_name = 'update_joke.html'
    success_url = reverse_lazy('joke_list')

class JokeDeleteView(LoginRequiredMixin, DeleteView):
    model = Joke
    template_name = 'delete_joke.html'
    success_url = reverse_lazy('joke_list')

class SignupView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'login.html'

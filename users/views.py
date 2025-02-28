from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import UserProfile
from .forms import userform, userupdateform
from django.contrib.auth.models import User
from django.urls import reverse_lazy

    
class userlistview(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

class usercreateview(CreateView):
    model = User
    form_class = userform
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:user_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        UserProfile.objects.create(user=user, date_of_birth=form.cleaned_data['date_of_birth'])
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class userupdateview(UpdateView):
    model = User
    form_class = userupdateform
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('users:user_list')

@method_decorator(login_required, name='dispatch')
class userdeleteview(DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('users:user_list')

def location_view(request):
    return render(request, 'location.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'users/login.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('users:user_list')

def signout(request):
    logout(request)
    return redirect('users:login')  # Redirige a la página de inicio de sesión
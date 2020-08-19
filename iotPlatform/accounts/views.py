from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

from django.contrib.auth import authenticate , logout

def registration_view(request):
    save = False
    form = UserForm1(request.POST or None)
    form1 = ProprietaireForm1(request.POST or None, request.FILES)
    if request.method  == 'POST':
        proprietaire = Proprietaire()
        user = User()
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = form.save(commit=False)
            user.set_password(password)
            user.save()

            proprietaire = form1.save(commit=False)
            proprietaire.user = user
            proprietaire.save()
            save = True
            return redirect('login')
    return render(request, 'accounts/register.html', {'form':form, 'form1':form1})


"""def registration_view(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'accounts/register.html', context)

"""
class LoginUser(LoginView):
    model = User
    fields = ['username', 'password']
    template_name = "accounts/login.html"


def logout_view(request):
	logout(request)
	return redirect('/iotCloud/')


@login_required(redirect_field_name='accounts/login')
def mon_profil(request):
    user = User()
    if user.is_authenticated:
        reseaux = Reseau.objects.filter(proprietaire_id = request.user.id)
        proprietaire = Proprietaire.objects.filter(user_id = request.user.id)
        #print(proprietaire.telephone_proprio)
    return render(request, 'gestionIoT/votre_profil.html', {"reseaux": reseaux, "proprietaire": proprietaire})

def login_view_(request):
	context = {}
	user = request.user
	if user.is_authenticated: 
		return redirect("home")

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect("home")
	else:
		form = AccountAuthenticationForm()
	context['login_form'] = form

	return render(request, "accounts/login.html", context)


def account_view(request):

	if not request.user.is_authenticated:
			return redirect("login")

	context = {}
	if request.POST:
		form = AccountUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.initial = {
					"email": request.POST['email'],
					"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Updated"
	else:
		form = AccountUpdateForm(

			initial={
					"email": request.user.email, 
					"username": request.user.username,
				}
			)

	context['account_form'] = form
	return render(request, "accounts/account.html", context)


def must_authenticate_view(request):
	return render(request, 'accounts/must_authenticate.html', {})

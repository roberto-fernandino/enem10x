from django.shortcuts import render, redirect
from usuarios.funcs import MediaChart
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from usuarios.forms import AccountCreationForm as signup_form
from django.contrib import messages
# Create your views here.


# CACHE AQUI
@login_required()
def user_view(request):
    data_mat, data_nat, data_lin, data_hum, months = MediaChart(request.user)
    context = {
        "data_mat": data_mat,
        "months": months,
        "data_nat": data_nat,
        "data_lin": data_lin,
        "data_hum": data_hum,
    }
    return render(request, "usuarios/user.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("usuarios:user")
    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home:home")
        else:
            messages.error(request,'Email ou senha invalidos')
            return render(request, "usuarios/login.html")
        
    return render(request, "usuarios/login.html")


def signup(request, *args, **kwargs):
    if request.method == "POST":
        form = signup_form(request.POST)
        if form.is_valid():
            # Cria conta com Account Form
            form.save()
            email = form.cleaned_data["email"]
            nome = form.cleaned_data["nome"]
            password = form.cleaned_data["password2"]
            auth_user = authenticate(request, email=email, password=password)
            if auth_user is not None:
                # Se o usuario foi criado com sucesso ja loga
                login(request, auth_user)
                return redirect("usuarios:signup-sucess")
        else:
            context = {"form": form}
            return render(request, "usuarios/signup.html", context)
    form = signup_form()

    context = {
        "form": form,
    }
    return render(request, "usuarios/signup.html", context)


@login_required
def signupsucess(request):
    return render(request, "usuarios/signup-sucess.html")


def logout_view(request):
    logout(request)
    return redirect("home:home")

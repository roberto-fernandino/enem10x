from django.shortcuts import render, redirect
from usuarios.funcs import MediaChart
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from usuarios.forms import AccountCreationForm
from django.contrib import messages
from materiais.models import ProvaCompleta
# Create your views here.


# CACHE AQUI
@login_required()
def user_view(request):
    data_mat, data_nat, data_lin, data_hum, months_mat, months_nat, months_lin, months_hum = MediaChart(request.user)
    provas_completas = ProvaCompleta.objects.filter(usuario=request.user)
    context = {
        "data_mat": data_mat,
        "months_mat": months_mat,
        "data_nat": data_nat,
        "months_nat": months_nat,
        "data_lin": data_lin,
        "months_lin": months_lin,
        "data_hum": data_hum,
        "months_hum": months_hum,
        "provas_completas": provas_completas,
    }
    return render(request, "usuarios/user.html", context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("usuarios:user")
    elif request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("home:home")
        return render(request, "usuarios/login.html", {"message": "Email ou senha inválidos"})
    return render(request, "usuarios/login.html")


def signup(request, *args, **kwargs):
    if request.method == "POST":
        form = AccountCreationForm(request.POST)
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
        context = {"form": form}
        return render(request, "usuarios/signup.html", context)
    
    form = AccountCreationForm()
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

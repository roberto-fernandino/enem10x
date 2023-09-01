from django.shortcuts import render, redirect
from usuarios.funcs import NotaChart, NotaFilteredChart, MediaQuery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from usuarios.forms import AccountCreationForm
from django.contrib import messages
from materiais.models import ProvaCompleta
from django.http import JsonResponse
from usuarios.models import MediaGeral

# Create your views here.


# CACHE AQUI
@login_required()
def notas_graph(request):
    if request.user.is_aluno or request.user.is_admin:
        (
            data_mat,
            data_nat,
            data_lin,
            data_hum,
            months_mat,
            months_nat,
            months_lin,
            months_hum,
        ) = NotaChart(request.user)
        media_mat, media_nat, media_lin, media_hum = MediaQuery(request.user)
        context = {
            "data_mat": data_mat,
            "months_mat": months_mat,
            "data_nat": data_nat,
            "months_nat": months_nat,
            "data_lin": data_lin,
            "months_lin": months_lin,
            "data_hum": data_hum,
            "months_hum": months_hum,
            "media_mat": media_mat,
            "media_nat": media_nat,
            "media_lin": media_lin,
            "media_hum": media_hum,
        }
        return render(request, "usuarios/notas-graph.html", context)
    else:
        return redirect('usuarios/assinar-aluno.html')

@login_required()
def filter_graph_time(request):
    months = request.GET.get("filter", None)
    months = int(months) if months else None
    result = NotaFilteredChart(request.user, months)
    print(result)
    data_mat = result["data_mat"]
    data_nat = result["data_nat"]
    data_lin = result["data_lin"]
    data_hum = result["data_hum"]
    months_mat = result["months_mat"]
    months_nat = result["months_nat"]
    months_lin = result["months_lin"]
    months_hum = result["months_hum"]
    context = {
        "graph_mat": {"newLabels": months_mat, "newData": data_mat},
        "graph_nat": {"newLabels": months_nat, "newData": data_nat},
        "graph_lin": {"newLabels": months_lin, "newData": data_lin},
        "graph_hum": {"newLabels": months_hum, "newData": data_hum},
    }
    return JsonResponse(context)


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
        return render(
            request, "usuarios/login.html", {"message": "Email ou senha inválidos"}
        )
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
                MediaGeral.objects.create(
                    usuario=request.user,
                    media_matematica=0,
                    media_ciencias_natureza=0,
                    media_ciencias_humanas=0,
                    media_linguagens=0,
                )
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

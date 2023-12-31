from django.shortcuts import render, redirect
from usuarios.funcs import NotaChart, NotaFilteredChart, MediaQuery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from usuarios.forms import AccountCreationForm, CriarTurmaForm
from django.contrib import messages
from materiais.models import ProvaCompleta
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse
from usuarios.models import Turma, Professor, Aluno
from usuarios.decorators import user_has_tag
from uuid import uuid4
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.urls import reverse

# Create your views here.


# CACHE AQUI
@login_required
@user_has_tag("is_aluno")
def notas_graph(request):
    if request.user.is_aluno or request.user.is_admin:
        aluno = request.user.aluno
        cache_key = f"notas_graph_{aluno.id}"
        cached_page = cache.get(cache_key)
        if cached_page:
            return HttpResponse(cached_page)
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
        media_mat, media_nat, media_lin, media_hum = MediaQuery(aluno)
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
        response = render(request, "usuarios/notas-graph.html", context)
        cache.set(cache_key, response.content, 60 * 10)
        return response
    else:
        return HttpResponseForbidden("403 forbidden")


@login_required
def platform_view(request):
    if request.user.is_authenticated:
        return render(request, "static/platform-base.html")
    else:
        return redirect("usuarios:login")


@login_required
def filter_graph_time(request):
    months = request.GET.get("filter", None)
    months = int(months) if months else None
    result = NotaFilteredChart(request.user, months)
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
        return redirect("usuarios:plataforma")
    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("usuarios:plataforma")
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
def professor_turmas_view(request):
    if request.user.is_professor:
        professor = request.user.professor
        cache_key = f"professor_turmas_view_{professor.id}"
        cached_page = cache.get(cache_key)
        if cached_page:
            return HttpResponse(cached_page)
        turmas_1 = Turma.objects.filter(criador=professor)
        turmas_2 = professor.turmas.all()
        turmas = set(turmas_1) | set(turmas_2)
        context = {"turmas": turmas, "professor": professor}
        response = render(request, "usuarios/turmas.html", context)
        cache.set(cache_key, response.content, 60 * 10)
        return response
    else:
        return HttpResponseForbidden("saia")


@login_required
@user_has_tag("is_aluno")
def aluno_turmas_view(request):
    if request.user.is_aluno:
        aluno = request.user.aluno
        cache_key = f"aluno_turmas_view_{aluno.id}"
        cached_page = cache.get(cache_key)
        if cached_page:
            return HttpResponse(cached_page)

        turmas = Turma.objects.filter(alunos=aluno)
        context = {"turmas": turmas, "aluno": aluno}
        response = render(request, "usuarios/turmas.html", context)
        cache.set(cache_key, response.content, 60 * 10)
        return response
    else:
        return HttpResponseForbidden("Forbidden, don't try again.")


@login_required
@user_has_tag("is_professor")
def criar_turma_view(request):
    professor_criador = Professor.objects.get(usuario=request.user)
    if request.method == "POST":
        form = CriarTurmaForm(professor_criador, request.POST)
        if form.is_valid():
            turma = form.save(commit=False)
            turma.codigo = uuid4()
            turma.criador = professor_criador
            turma.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                f'{professor_criador.usuario.nome} meus parabens "{turma.nome}" criada com sucesso! ',
            )
            cache.delete(f"professor_turmas_view_{professor_criador.id}")
            return redirect(reverse("usuarios:professor-turmas"))
    form = CriarTurmaForm(professor_criador)
    context = {"form": form}
    return render(request, "usuarios/create-turma.html", context)


@login_required
@user_has_tag("is_professor")
def professor_turma_view(request, turma_id):
    professor = Professor.objects.get(usuario=request.user)
    turma = get_object_or_404(Turma, id=turma_id)

    if (
        not turma.professores.filter(id=professor.id).exists()
        and turma.criador != professor
    ):
        return HttpResponseForbidden("403 Forbidden")

    context = {
        "turma": turma,
        "professor": professor,
    }
    return render(request, "usuarios/turma.html", context)


@login_required
@user_has_tag("is_aluno")
def aluno_turma_view(request, turma_id):
    aluno = Aluno.objects.get(usuario=request.user)
    turma = get_object_or_404(Turma, id=turma_id)
    if not turma.alunos.filter(id=aluno.id).exists():
        return HttpResponseForbidden("403 Forbidden")
    context = {
        "turma": turma,
        "aluno": aluno,
    }
    return render(request, "usuarios/turma.html", context)


@login_required
def signupsucess(request):
    return render(request, "usuarios/signup-sucess.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("home:home")


@login_required
def entra_turma(request):
    if request.user.is_aluno or request.user.is_professor:
        usuario = request.user
        if request.method == "POST":
            codigo = request.POST["codigo"]
            turma = get_object_or_404(Turma, codigo=codigo)
            if request.user.is_aluno:
                if turma.criador.get_remaining_alunos() <= 0:
                    messages.add_message(
                        request,
                        messages.ERROR,
                        "Esse professor ja atingiu seu limite de alunos.",
                    )
                    return render(request, "usuarios/erro.html")
                else:
                    aluno = request.user.aluno
                    cache_key = f"aluno_turmas_{aluno.id}"
                    turma.alunos.add(aluno)
                    turma.criador.alunos += 1
                    turma.criador.save()
                    cache.delete(cache_key)
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        f"{usuario.nome} voce entrou na {turma.nome} com sucesso!",
                    )
                    return redirect("usuarios:aluno-turmas")
            if request.user.is_professor:
                professor = request.user.professor
                cache_key = f"professor_turmas_{professor.id}"
                turma.professores.add(professor)
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    f"{usuario.nome} você entrou na {turma.nome} com sucesso !",
                )
                cache.delete(cache_key)
                return redirect("usuarios:professor-turmas")
        return render(request, "usuarios/entrar-turma.html")
    else:
        return HttpResponseForbidden(
            "Você não tem permissão para acessar esta página. Esse acesso será rastreado.."
        )


@login_required
def delete_turma(request, turma_id):
    turma = Turma.objects.get(id=turma_id)
    messages.add_message(
        request,
        messages.SUCCESS,
        f"{request.user.nome} você apagou a turma {turma.nome} com suceso!",
    )
    turma.delete()
    return redirect("usuarios:professor-turmas")


@login_required
@user_has_tag("is_professor")
def remover_aluno(request, turma_id, aluno_id):
    """
    View, usada como botao para remover um aluno de uma uma turma como um professor.
    """
    usuario = request.user
    turma = get_object_or_404(Turma, id=turma_id)
    criador = turma.criador
    if usuario == criador.usuario:
        aluno = Aluno.objects.get(id=aluno_id)
        turma.alunos.remove(aluno)
        criador.alunos -= 1
        criador.save()
    else:
        return HttpResponseForbidden("Usuario nao é o criador da turma.")
    messages.add_message(request, messages.SUCCESS, "Aluno removido com sucesso.")
    return redirect("usuarios:professor-turma", turma_id)


@login_required
@user_has_tag("is_aluno")
def sair_turma_aluno(request, turma_id, aluno_id):
    """
    View, usada como botao para sair de uma turma como um aluno.
    """
    aluno = Aluno.objects.get(id=aluno_id)
    turma = Turma.objects.get(id=turma_id)
    turma.alunos.remove(aluno)
    turma.criador.alunos -= 1
    turma.criador.save()
    messages.add_message(
        request, messages.SUCCESS, f"Voce saiu da turma {turma.nome} com sucesso!"
    )
    return redirect("usuarios:aluno-turmas")


@login_required
@user_has_tag("is_aluno")
def aluno_provas_feitas(request):
    """
    Tela com todas as provas feitas para o aluno e a opcao de realizar novas provas.
    """
    aluno = request.user.aluno
    cache_key = f"aluno_provas_feitas_{aluno.id}"
    cached_page = cache.get(cache_key)
    if cached_page:
        return HttpResponse(cached_page)

    provas_feitas_do_usuario = ProvaCompleta.objects.filter(aluno=aluno)
    context = {"provas_feita_do_usuario": provas_feitas_do_usuario}
    response = render(request, "usuarios/provas-feitas.html", context)
    cache.set(cache_key, response.content, 60 * 10)
    return response


@login_required
def user_profile(request):
    """
    Tela de Perfil do usuario.
    """

    # Dados do usuario
    email = request.user.email
    cpf_escondido = request.user.esconde_cpf
    cpf = request.user.cpf
    nome = request.user.nome
    data_criacao_conta = request.user.data_criacao
    telefone = request.user.telefone

    cache_key = f"user_profile_{request.user.id}"
    cached_page = cache.get(cache_key)
    if cached_page:
        return HttpResponse(cached_page)

    context = {
        "data_criacao_conta": data_criacao_conta,
        "idade": request.user.retorna_idade(),
        "nome": nome,
        "email": email,
        "cpf_escondido": cpf_escondido,
        "telefone": telefone,
    }
    response = render(request, "usuarios/user-profile.html", context)
    cache.set(cache_key, response.content, 60 * 5)
    return response

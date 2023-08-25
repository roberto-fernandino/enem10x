from django.shortcuts import render
from usuarios.funcs import MediaChart
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
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

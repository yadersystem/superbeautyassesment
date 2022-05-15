from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from inventario.models import Equipo, EquipoUsuario



def filtros(request):
    return render(request, 'inventario/elegir_filtros.html')


@csrf_exempt
def equipo(request):
    """Nos permite ver el formualrio del filtro y renderizar esa informacion
    a una vista que nos ayuda a procesarla"""

    if request.method == 'POST':
        tipo = request.POST.get('tipo', '')
        referencia = request.POST.get('referencia', '')

        return redirect('/inventario/equipo_details/?tipo=' + tipo + '&referencia=' + referencia)

    return render(request, 'inventario/equipo.html')


def equipo_details(request):
    """controlamos los posibles errores que se presenten a la hora de hacer los filtros con los
    valores optenidos y luego esa informacion es enviada a la plantilla """
    tipo = request.GET.get('tipo')
    referencia = request.GET.get('referencia')
    equipo = None

    if tipo or referencia:
        try:
            equipo = Equipo.objects.filter(tipo=tipo) | \
                     Equipo.objects.filter(referencia=referencia)
        except equipo:
            msg = "Error de Servidor"
            raise msg

    return render(request, 'inventario/details.html', {'equipos': equipo})


def equipousuario(request):
    """Nos permite ver el formulario del filtro y renderizar esa informacion
        a una vista que nos ayuda a procesarla"""

    if request.method == 'POST':
        usuario = request.POST.get('usuario', '')
        fecha = request.POST.get('fecha', '')

        return redirect('/inventario/usuarios_details/?usuario=' + usuario + '&fecha=' + fecha)

    return render(request, 'inventario/equipousuario.html')


def usuarios_details(request):
    """"
    controlamos los posibles errores que se presenten a la hora de hacer los filtros con los
    valores optenidos y luego esa informacion es enviada a la plantilla
    """
    usuario = request.GET.get('usuario')
    fecha = request.GET.get('fecha')
    user = None
    msg = None
    result = None

    if usuario or fecha:
        try:
            user = User.objects.filter(username=usuario)
        except user:
            msg = "Usuario No encontrado"
            raise msg

        if user and fecha is not '':
            try:
                result = EquipoUsuario.objects.filter(usuario=user[0].id) | \
                         EquipoUsuario.objects.filter(fechaasignacion=fecha)
            except result:
                msg = "El usuario o fecha no ha sido encontrado"
                raise msg
        elif fecha is not '':
            result = EquipoUsuario.objects.filter(fechaasignacion=fecha)
        elif user:
            result = EquipoUsuario.objects.filter(usuario=user[0].id)

    return render(request, 'inventario/usuarios_details.html', {'results': result, 'msg': msg})

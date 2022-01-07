from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from core.forms import FormCliente, FormVeiculo, FormRotativo, FormMensalista, FormParametro
from core.models import Cliente, Veiculo, Parametro, Mensalista, Rotativo
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'core/index.html')

class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


@login_required
def cadastro_cliente(request):
   if request.user.is_staff and request.user.is_active:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid(): #pega o formulario e verifica se tem valores nos campos preechidos
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso.")
            return redirect('url_listagem_clientes')
        contexto = {'form': form,'texto_titulo': 'Cadastro de Cliente', 'texto_botao': 'Cadastrar',
                    'texto_cancelar': 'url_principal'}
        return render(request, 'core/cadastro.html', contexto)
   else:
       return render(request, 'core/nao-autorizado.html')


@login_required
def listagem_clientes(request):
    if request.user.is_staff and request.user.is_active:
        dados = Cliente.objects.all()
        if request.POST:
           if request.POST['pesquisar_input']:
                dados = Cliente.objects.filter(nome=request.POST['pesquisar_input'])

        contexto = {'dados': dados,'listagem': 'listagem'}
        return render(request, 'core/listagem_clientes.html', contexto)
    else:
        return render(request, 'core/nao-autorizado.html')


@login_required
def cadastro_veiculo(request):
    if request.user.is_staff and request.user.is_active:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():  # pega o formulario e verifica se tem valores nos campos preechidos
            form.save()
            messages.success(request, "Veículo cadastrado com sucesso.")
            return redirect('url_listagem_veiculos')
        contexto = {'form': form, 'texto_titulo': 'Cadastro de Veiculo', 'texto_botao': 'Cadastrar',
                    'texto_cancelar': 'url_principal'}
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/nao-autorizado.html')


@login_required
def listagem_veiculos(request):
    if request.user.is_staff and request.user.is_active:
        dados = Veiculo.objects.all()
        if request.POST:
            if request.POST['pesquisar_input']:
                dados = Veiculo.objects.filter(placa=request.POST['pesquisar_input'])

        contexto = {'dados': dados,'listagem': 'listagem'}
        return render(request, 'core/listagem_veiculos.html', contexto)
    else:
        return render(request, 'core/nao-autorizado.html')


@login_required
def atualiza_cliente(request, id):
    if request.user.is_staff and request.user.is_active:
        obj = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente atualizado com sucesso.")
            return redirect('url_listagem_clientes')
        else:
            contexto = {'form': form, 'texto_titulo': 'Atualização de Cliente', 'texto_botao': 'Atualizar',
                        'texto_cancelar': 'url_listagem_clientes'}
            return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/nao-autorizado.html')


@login_required
def exclui_cliente(request, id):
    if request.user.is_staff and request.user.is_active:
        obj = Cliente.objects.get(id=id)
        if request.POST:
            obj.delete()
            messages.success(request, "Cliente excluído com sucesso.")
            return redirect('url_listagem_clientes')
        else:
            contexto = {'dado': obj.nome, 'id': id, 'url': 'url_listagem_clientes'}
            return render(request, 'core/confirma_exclusao.html', contexto)
    else:
        return render(request, 'core/nao-autorizado.html')

@login_required
def atualiza_veiculo(request, id):
    if request.user.is_staff and request.user.is_active:
        obj = Veiculo.objects.get(id=id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Veículo atualizado com sucesso.")
            return redirect('url_listagem_veiculos')
        else:
            contexto = {'form': form, 'texto_titulo': 'Atualização de Veiculo', 'texto_botao': 'Atualizar',
                        'texto_cancelar': 'url_listagem_veiculos'}
            return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/nao-autorizado.html')


@login_required
def exclui_veiculo(request, id):
    if request.user.is_staff and request.user.is_active:
        obj = Veiculo.objects.get(id=id)
        if request.POST:
            obj.delete()
            messages.success(request, "Veículo excluído com sucesso.")
            return redirect('url_listagem_veiculos')
        else:
            contexto = {'dado': obj.modelo, 'id': obj.placa, 'url': 'url_listagem_veiculos'}
            return render(request, 'core/confirma_exclusao.html', contexto)
    else:
        return render(request, 'core/nao-autorizado.html')


@login_required
def listagem_parametros(request):
    dados = Parametro.objects.all()
    contexto = {'dados': dados, 'listagem': 'listagem'}
    return render(request, 'core/listagem_parametros.html', contexto)


@login_required
def cadastro_rotativo(request):
    if request.user.is_staff and request.user.is_active:
        form = FormRotativo(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Rotativo cadastrado com sucesso.")
            return redirect('url_listagem_rotativos')
        contexto = {'form': form, 'texto_botao': 'Cadastrar', 'texto_titulo': 'Cadastro de Rotativos',
                    'texto_cancelar': 'url_principal'}
        return render(request, 'core/cadastro.html', contexto)
    else:
        return render(request, 'core/nao-autorizado.html')


@login_required
def listagem_rotativos(request):
    if request.user.is_staff and request.user.is_active:
        dados = Rotativo.objects.all()
        if request.POST:
            if request.POST['pesquisar_input']:
                dados = Rotativo.objects.filter(id_veiculo__placa=request.POST['pesquisar_input'])
        contexto = {'dados': dados, 'listagem': 'listagem'}
        return render(request, 'core/listagem_rotativos.html', contexto)
    else:
        return render(request, 'core/nao-autorizado.html')


@login_required
def atualiza_rotativo(request, id):
   if request.user.is_staff and request.user.is_active:
        obj = Rotativo.objects.get(id=id) #buscar objeto no banco
        form = FormRotativo(request.POST or None, instance=obj)  #preparar o formuçário
        if form.is_valid():
            obj.calculo_total()
            obj.pago = True
            form.save()
            messages.success(request, "Rotativo atualizado com sucesso.")
            return redirect('url_listagem_rotativos')
        contexto = {'form': form, 'texto_titulo': ' Atualiza Rotativos', 'texto_botao': 'Atualizar',
                    'texto_cancelar': 'url_listagem_rotativos'}
        return render(request, 'core/cadastro.html', contexto)
   else:
       return render(request, 'core/nao-autorizado.html')
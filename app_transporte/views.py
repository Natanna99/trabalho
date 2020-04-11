from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Veiculo
from .models import Solicitacao
from .models import Funcionario
from .models import Cargo

def todas_solicitacao(request):
    total= Solicitacao.objects.all()
    return render(request,'app/lista.html' , {'total': total})

def dtl_solicitacao(request, id_solicitacao):
    try:
        dtlsolicitacao= Solicitacao.objects.get(pk= id_solicitacao)

    except Exception:
        raise Http404('Solicitação não encontrada')
  
    return render(request, 'app/detalheSolicitacao.html', {'dtlsolicitacao': dtlsolicitacao})

def carros_cadastrados(request):
    carros= Veiculo.objects.all()
    return render(request, 'app/todos_carros.html', {'carros': carros})

def dtl_carros(request, id_carro):
    try:
        dtlCarros= Veiculo.objects.get(pk= id_carro)
    
    except Exception:
        raise Http404("Veiculo não encontrado")
    
    return render(request, 'app/detalheCarros.html', {'dtlCarros':dtlCarros})

def todos_funcionarios(request):
    funcionarios= Funcionario.objects.all()
    return render(request, 'app/todos_funcionarios.html', {'funcionario':funcionarios})

def dtl_Funcionario(request, id_funcionario):
    try:
        dtlFuncionario= Funcionario.objects.get(pk= id_funcionario)
    
    except Exception:
        raise Http404("Funcionario não encontrado")
    
    return render(request, 'app/detalheFuncionario.html', {'dtlFuncionario':dtlFuncionario})

    



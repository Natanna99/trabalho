from django.urls import path
from .views import todas_solicitacao, dtl_solicitacao, carros_cadastrados, dtl_carros, todos_funcionarios, dtl_Funcionario

urlpatterns = [
     path('listaSolicitação', todas_solicitacao, name='lista'),
     path('solicitacoes/<int:id_solicitacao>/', dtl_solicitacao, name= 'solicitações'),

     path('todos_carros', carros_cadastrados, name= 'carros'),
     path('descrição_carro/<int:id_carro>/', dtl_carros, name= 'carro'),

     path('funcionarios', todos_funcionarios, name= 'funcionarios' ),
     path('detalheFuncionario/<int:id_funcionario>/', dtl_Funcionario, name= 'funcionario' ),

]

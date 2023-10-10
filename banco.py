'''
#DESAFIO // Faça um código que simula um banco.

grave os dados em memoria.
Esse banco tem que ter as funções, 
'saque','deposito','saldo','extrato','transfência'.

Faça esse código com POO.
Exiba o horário do sanque no extrato.
'''

from random import choice, randint


class Banco:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
        
    def __repr__(self):
        return f'conta:{self.nome} || CPF:{self.cpf}'
    
    def _extrato(self,conta):
        pass
    
    def _saque(self,conta,valor_do_saque):
        pass
    
    def _deposito(self,conta,valor_do_deposito):
        pass
    
    def _saldo(self,conta):
        pass
    
    def _trasnferencia(self,conta,conta_a_receber,valor_transferencia):
        pass
    
    def _pix(self,conta,chave_pix,valro_de_trasnferencia):
        pass
    
    def _chave_pix(self,conta):
        pass
    

    
NupaG = Banco(nome='Matheus',cpf=114755741)
print(NupaG)
  

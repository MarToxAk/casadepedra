class Tarefas():
    def __init__(self, autor, nome, telefone, check_in, check_out, num_adultos, num_criancas, idade_crianca1, idade_crianca2, idade_crianca3, idade_crianca4):
        self.__autor = autor
        self.__nome = nome
        self.__telefone = telefone
        self.__check_in = check_in
        self.__check_out = check_out
        self.__num_adultos = num_adultos
        self.__num_criancas= num_criancas
        self.__idade_crianca1 = idade_crianca1
        self.__idade_crianca2 = idade_crianca2
        self.__idade_crianca3 = idade_crianca3
        self.__idade_crianca4 = idade_crianca4

        

    @property
    def nome(self,):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome

    @property
    def autor(self,):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor

    @property
    def telefone(self,):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone

    @property
    def check_in(self,):
        return self.__check_in

    @check_in.setter
    def check_in(self, check_in):
        self.__check_in

    @property
    def check_out(self,):
        return self.__check_out

    @check_out.setter
    def check_out(self, check_out):
        self.__check_out

    @property
    def num_adultos(self,):
        return self.__num_adultos

    @num_adultos.setter
    def num_adultos(self, num_adultos):
        self.__num_adultos

    @property
    def num_criancas(self,):
        return self.__num_criancas

    @num_criancas.setter
    def num_criancas(self, num_criancas):
        self.__num_criancas

    @property
    def idade_crianca1(self,):
        return self.__idade_crianca1

    @idade_crianca1.setter
    def idade_crianca1(self, idade_crianca1):
        self.__idade_crianca1

    @property
    def idade_crianca2(self,):
        return self.__idade_crianca2

    @idade_crianca2.setter
    def idade_crianca2(self, idade_crianca2):
        self.__idade_crianca2

    @property
    def idade_crianca3(self,):
        return self.__idade_crianca3

    @idade_crianca3.setter
    def idade_crianca3(self, idade_crianca3):
        self.__idade_crianca3

    @property
    def idade_crianca4(self,):
        return self.__idade_crianca4

    @idade_crianca4.setter
    def idade_crianca4(self, idade_crianca4):
        self.__idade_crianca4
        
        
class TarefasEdicao():
    def __init__(self, autor, nome, telefone, check_in, check_out, num_adultos, num_criancas, crianca1, crianca2, crianca3, crianca4, parcela, disconto, pk):
        self.__autor = autor
        self.__nome = nome
        self.__telefone = telefone
        self.__check_in = check_in
        self.__check_out = check_out
        self.__num_adultos = num_adultos
        self.__num_criancas= num_criancas
        self.__crianca1 = crianca1
        self.__crianca2 = crianca2
        self.__crianca3 = crianca3
        self.__crianca4 = crianca4
        self.__disconto = disconto
        self.__parcela = parcela
        self.__pk = pk
        

    @property
    def nome(self,):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome

    @property
    def autor(self,):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor

    @property
    def telefone(self,):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone

    @property
    def check_in(self,):
        return self.__check_in

    @check_in.setter
    def check_in(self, check_in):
        self.__check_in

    @property
    def check_out(self,):
        return self.__check_out

    @check_out.setter
    def check_out(self, check_out):
        self.__check_out

    @property
    def num_adultos(self,):
        return self.__num_adultos

    @num_adultos.setter
    def num_adultos(self, num_adultos):
        self.__num_adultos

    @property
    def num_criancas(self,):
        return self.__num_criancas

    @num_criancas.setter
    def num_criancas(self, num_criancas):
        self.__num_criancas

    @property
    def crianca1(self,):
        return self.__crianca1

    @crianca1.setter
    def crianca1(self, crianca1):
        self.__crianca1

    @property
    def crianca2(self,):
        return self.__crianca2

    @crianca2.setter
    def crianca2(self, crianca2):
        self.__crianca2

    @property
    def crianca3(self,):
        return self.__crianca3

    @crianca3.setter
    def crianca3(self, crianca3):
        self.__crianca3

    @property
    def crianca4(self,):
        return self.__crianca4

    @crianca4.setter
    def crianca4(self, crianca4):
        self.__crianca4


    @property
    def disconto(self,):
        return self.__disconto

    @disconto.setter
    def disconto(self, disconto):
        self.__disconto


    @property
    def parcela(self,):
        return self.__parcela

    @parcela.setter
    def parcela(self, parcela):
        self.__parcela
    
    @property
    def pk(self,):
        return self.__pk

    @pk.setter
    def pk(self, pk):
        self.__pk
    

class TarefasConfiguracao():
    def __init__(self,
    texto_whatsapp,
    nome_cotacao,
    check_in_cotacao, 
    check_out_cotacao, 
    num_pessoas_cotacao, 
    num_criancas_cotacao, 
    valor_cotacao, 
    parcela_cotacao, 
    parcela_1opc_cotacao, 
    valor_4opc_cotacao, 
    deconto_4opc_cotacao):
        self.__texto_whatsapp = texto_whatsapp
        self.__nome_cotacao = nome_cotacao
        self.__check_in_cotacao = check_in_cotacao
        self.__check_out_cotacao = check_out_cotacao
        self.__num_pessoas_cotacao = num_pessoas_cotacao
        self.__num_criancas_cotacao = num_criancas_cotacao
        self.__valor_cotacao = valor_cotacao
        self.__parcela_cotacao = parcela_cotacao
        self.__parcela_1opc_cotacao = parcela_1opc_cotacao
        self.__valor_4opc_cotacao = valor_4opc_cotacao
        self.__deconto_4opc_cotacao = deconto_4opc_cotacao

    @property
    def texto_whatsapp(self,):
        return self.__texto_whatsapp

    @texto_whatsapp.setter
    def texto_whatsapp(self, texto_whatsapp):
        self.__texto_whatsapp

    @property
    def nome_cotacao(self,):
        return self.__nome_cotacao

    @nome_cotacao.setter
    def nome_cotacao(self, nome_cotacao):
        self.__nome_cotacao

    @property
    def check_in_cotacao(self,):
        return self.__check_in_cotacao

    @check_in_cotacao.setter
    def check_in_cotacao(self, check_in_cotacao):
        self.__check_in_cotacao

    @property
    def check_out_cotacao(self,):
        return self.__check_out_cotacao

    @check_out_cotacao.setter
    def check_out_cotacao(self, check_out_cotacao):
        self.__check_out_cotacao

    @property
    def num_pessoas_cotacao(self,):
        return self.__num_pessoas_cotacao

    @num_pessoas_cotacao.setter
    def num_pessoas_cotacao(self, num_pessoas_cotacao):
        self.__num_pessoas_cotacao

    @property
    def num_criancas_cotacao(self,):
        return self.__num_criancas_cotacao

    @num_criancas_cotacao.setter
    def num_criancas_cotacao(self, num_criancas_cotacao):
        self.__num_criancas_cotacao

    @property
    def valor_cotacao(self,):
        return self.__valor_cotacao

    @valor_cotacao.setter
    def valor_cotacao(self, valor_cotacao):
        self.__valor_cotacao
    
    @property
    def parcela_cotacao(self,):
        return self.__parcela_cotacao

    @parcela_cotacao.setter
    def parcela_cotacao(self, parcela_cotacao):
        self.__parcela_cotacao
    
    @property
    def parcela_1opc_cotacao(self,):
        return self.__parcela_1opc_cotacao

    @parcela_1opc_cotacao.setter
    def parcela_1opc_cotacao(self, parcela_1opc_cotacao):
        self.__parcela_1opc_cotacao
    
    @property
    def valor_4opc_cotacao(self,):
        return self.__valor_4opc_cotacao

    @valor_4opc_cotacao.setter
    def valor_4opc_cotacao(self, valor_4opc_cotacao):
        self.__valor_4opc_cotacao

    @property
    def deconto_4opc_cotacao(self,):
        return self.__deconto_4opc_cotacao

    @deconto_4opc_cotacao.setter
    def deconto_4opc_cotacao(self, deconto_4opc_cotacao):
        self.__deconto_4opc_cotacao


class TarefasConfiguracao():
    def __init__(self,
    texto_whatsapp,
    nome_cotacao,
    check_in_cotacao, 
    check_out_cotacao, 
    num_pessoas_cotacao, 
    num_criancas_cotacao, 
    valor_cotacao, 
    parcela_cotacao, 
    parcela_1opc_cotacao, 
    valor_4opc_cotacao, 
    deconto_4opc_cotacao):
        self.__texto_whatsapp = texto_whatsapp
        self.__nome_cotacao = nome_cotacao
        self.__check_in_cotacao = check_in_cotacao
        self.__check_out_cotacao = check_out_cotacao
        self.__num_pessoas_cotacao = num_pessoas_cotacao
        self.__num_criancas_cotacao = num_criancas_cotacao
        self.__valor_cotacao = valor_cotacao
        self.__parcela_cotacao = parcela_cotacao
        self.__parcela_1opc_cotacao = parcela_1opc_cotacao
        self.__valor_4opc_cotacao = valor_4opc_cotacao
        self.__deconto_4opc_cotacao = deconto_4opc_cotacao

    @property
    def texto_whatsapp(self,):
        return self.__texto_whatsapp

    @texto_whatsapp.setter
    def texto_whatsapp(self, texto_whatsapp):
        self.__texto_whatsapp

    @property
    def nome_cotacao(self,):
        return self.__nome_cotacao

    @nome_cotacao.setter
    def nome_cotacao(self, nome_cotacao):
        self.__nome_cotacao

    @property
    def check_in_cotacao(self,):
        return self.__check_in_cotacao

    @check_in_cotacao.setter
    def check_in_cotacao(self, check_in_cotacao):
        self.__check_in_cotacao

    @property
    def check_out_cotacao(self,):
        return self.__check_out_cotacao

    @check_out_cotacao.setter
    def check_out_cotacao(self, check_out_cotacao):
        self.__check_out_cotacao

    @property
    def num_pessoas_cotacao(self,):
        return self.__num_pessoas_cotacao

    @num_pessoas_cotacao.setter
    def num_pessoas_cotacao(self, num_pessoas_cotacao):
        self.__num_pessoas_cotacao

    @property
    def num_criancas_cotacao(self,):
        return self.__num_criancas_cotacao

    @num_criancas_cotacao.setter
    def num_criancas_cotacao(self, num_criancas_cotacao):
        self.__num_criancas_cotacao

    @property
    def valor_cotacao(self,):
        return self.__valor_cotacao

    @valor_cotacao.setter
    def valor_cotacao(self, valor_cotacao):
        self.__valor_cotacao
    
    @property
    def parcela_cotacao(self,):
        return self.__parcela_cotacao

    @parcela_cotacao.setter
    def parcela_cotacao(self, parcela_cotacao):
        self.__parcela_cotacao
    
    @property
    def parcela_1opc_cotacao(self,):
        return self.__parcela_1opc_cotacao

    @parcela_1opc_cotacao.setter
    def parcela_1opc_cotacao(self, parcela_1opc_cotacao):
        self.__parcela_1opc_cotacao
    
    @property
    def valor_4opc_cotacao(self,):
        return self.__valor_4opc_cotacao

    @valor_4opc_cotacao.setter
    def valor_4opc_cotacao(self, valor_4opc_cotacao):
        self.__valor_4opc_cotacao

    @property
    def deconto_4opc_cotacao(self,):
        return self.__deconto_4opc_cotacao

    @deconto_4opc_cotacao.setter
    def deconto_4opc_cotacao(self, deconto_4opc_cotacao):
        self.__deconto_4opc_cotacao
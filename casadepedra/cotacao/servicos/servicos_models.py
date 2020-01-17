from pprint import pprint
from string import Template
from datetime import date
import locale
from casadepedra.configuracao.models import ConfiguracaoTexto, Configuracao
from django.db.models import Q



locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class TextoWppCotacao():
    def __init__(self, check_in, check_out, num_adultos, num_criancas, idade_crianca1, idade_crianca2, idade_crianca3, idade_crianca4, valor_cotacao):
        self.check_in = check_in
        self.check_out = check_out
        self.num_adultos = num_adultos
        self.num_criancas = num_criancas
        self.idade_crianca1 = idade_crianca1
        self.idade_crianca2 = idade_crianca2
        self.idade_crianca3 = idade_crianca3
        self.idade_crianca4 = idade_crianca4
        self.valor_cotacao = valor_cotacao

        
    
    def verificador_datas(self, dados):
        padrao = ConfiguracaoTexto.objects.filter(padrao=True)
        buscador_data = ConfiguracaoTexto.objects.filter(Q(data_inicial__range=(dados.check_in,dados.check_out))|Q(data_inicial__range=(dados.check_in,dados.check_out))|Q(data_inicial__lt=dados.check_in,data_final__gt=dados.check_out))
        pprint(f'{dados.check_in} á {dados.check_out}')
        if buscador_data.count() == 0:
            check_in = padrao.values()[0]['check_in']
            check_out = padrao.values()[0]['check_out']
            num_dias = padrao.values()[0]['num_dias']
            num_criancas = padrao.values()[0]['num_criancas']
            idade_crianca = padrao.values()[0]['idade_crianca']
            num_pessoas = padrao.values()[0]['num_pessoas']
            valor_total = padrao.values()[0]['valor_total']
            valor_real = padrao.values()[0]['valor_real']
            valor_desconto = padrao.values()[0]['check_in']
            valor_da_parcelas = padrao.values()[0]['valor_da_parcelas']
            valor_da_parcelas_menos_etrada = padrao.values()[0]['valor_da_parcelas_menos_etrada']           
            valor_50porc = padrao.values()[0]['valor_50porc']
            num_parcela = padrao.values()[0]['num_parcela']
            num_parcela_mais_1 = padrao.values()[0]['num_parcela_mais_1']
            porcentagem = padrao.values()[0]['porcentagem']
            porcentagem_mais_5 = padrao.values()[0]['porcentagem_mais_5']
            cotacao_texto = padrao.values()[0]['cotacao_texto']
            desconto = padrao.values()[0]['desconto']
            valor_da_entrada = padrao.values()[0]['valor_da_entrada']
            valores = self.verificacao_bool(dados, check_in, check_out, num_dias, num_criancas, idade_crianca, num_pessoas, valor_total, valor_real, valor_desconto, valor_da_parcelas, valor_50porc, num_parcela_mais_1, porcentagem, porcentagem_mais_5, desconto, valor_da_parcelas_menos_etrada, num_parcela, cotacao_texto, valor_da_entrada)
            return valores

        elif buscador_data.count() > 1:
            check_in = padrao.values()[0]['check_in']
            check_out = padrao.values()[0]['check_out']
            num_dias = padrao.values()[0]['num_dias']
            num_criancas = padrao.values()[0]['num_criancas']
            idade_crianca = padrao.values()[0]['idade_crianca']
            num_pessoas = padrao.values()[0]['num_pessoas']
            valor_total = padrao.values()[0]['valor_total']
            valor_real = padrao.values()[0]['valor_real']
            valor_desconto = padrao.values()[0]['check_in']
            valor_da_parcelas = padrao.values()[0]['valor_da_parcelas']
            valor_da_parcelas_menos_etrada = padrao.values()[0]['valor_da_parcelas_menos_etrada']           
            valor_50porc = padrao.values()[0]['valor_50porc']
            num_parcela = padrao.values()[0]['num_parcela']
            num_parcela_mais_1 = padrao.values()[0]['num_parcela_mais_1']
            porcentagem = padrao.values()[0]['porcentagem']
            porcentagem_mais_5 = padrao.values()[0]['porcentagem_mais_5']
            cotacao_texto = padrao.values()[0]['cotacao_texto']
            desconto = padrao.values()[0]['desconto']
            valor_da_entrada = padrao.values()[0]['valor_da_entrada']
            valores = self.verificacao_bool(dados, check_in, check_out, num_dias, num_criancas, idade_crianca, num_pessoas, valor_total, valor_real, valor_desconto, valor_da_parcelas, valor_50porc, num_parcela_mais_1, porcentagem, porcentagem_mais_5, desconto, valor_da_parcelas_menos_etrada, num_parcela, cotacao_texto, valor_da_entrada)
            return valores

        elif buscador_data.count() == 1:         
            check_in = buscador_data.values()[0]['check_in']
            check_out = buscador_data.values()[0]['check_out']
            num_dias = buscador_data.values()[0]['num_dias']
            num_criancas = buscador_data.values()[0]['num_criancas']
            idade_crianca = buscador_data.values()[0]['idade_crianca']
            num_pessoas = buscador_data.values()[0]['num_pessoas']
            valor_total = buscador_data.values()[0]['valor_total']
            valor_real = buscador_data.values()[0]['valor_real']
            valor_desconto = buscador_data.values()[0]['check_in']
            valor_da_parcelas = buscador_data.values()[0]['valor_da_parcelas']
            valor_da_parcelas_menos_etrada = buscador_data.values()[0]['valor_da_parcelas_menos_etrada']           
            valor_50porc = buscador_data.values()[0]['valor_50porc']
            num_parcela = buscador_data.values()[0]['num_parcela']
            num_parcela_mais_1 = buscador_data.values()[0]['num_parcela_mais_1']
            porcentagem = buscador_data.values()[0]['porcentagem']
            porcentagem_mais_5 = buscador_data.values()[0]['porcentagem_mais_5']
            cotacao_texto = buscador_data.values()[0]['cotacao_texto']
            desconto = buscador_data.values()[0]['desconto']
            valor_da_entrada = buscador_data.values()[0]['valor_da_entrada']
            valores = self.verificacao_bool(dados, check_in, check_out, num_dias, num_criancas, idade_crianca, num_pessoas, valor_total, valor_real, valor_desconto, valor_da_parcelas, valor_50porc, num_parcela_mais_1, porcentagem, porcentagem_mais_5, desconto, valor_da_parcelas_menos_etrada, num_parcela, cotacao_texto, valor_da_entrada)
            return valores
            
            
    def dias_alfa(self, check_in, check_out):
            dialy = int((check_out - check_in).days)
            if dialy == 1:
                return 'Uma Diária'
            elif dialy == 2:
                return 'Duas Diárias'
            elif dialy == 3:
                return 'Três Diárias'
            elif dialy == 4:
                return 'Quatro Diárias'
            elif dialy == 5:
                return 'Cinco Diárias'
            elif dialy == 6:
                return 'Seis Diárias'
            elif dialy == 7:
                return 'Sete Diárias'
            elif dialy == 8:
                return 'Oito Diárias'
            elif dialy == 9:
                return 'Nove Diárias'
            elif dialy == 10:
                return 'Dez Diárias'
            elif dialy == 11:
                return 'Onze Diárias'
            elif dialy == 12:
                return 'Doze Diárias'
            elif dialy == 13:
                return 'Treze Diárias'
            elif dialy == 14:
                return 'Quatoze Diárias'
            elif dialy == 15:
                return 'Quinze Diárias'
            elif dialy == 16:
                return 'Dezesseis Diárias'
            elif dialy == 17:
                return 'Dezessete Diárias'
            elif dialy == 18:
                return 'Dezoito Diárias'
            elif dialy == 19:
                return 'Dezenove Diárias'
            elif dialy == 20:
                return 'Vinte Diárias'
            elif dialy == 21:
                return 'Vinte e Um Diárias'
            elif dialy == 22:
                return 'Vinte e Dois Diárias'
            elif dialy == 23:
                return 'Vinte e Três Diárias'
            elif dialy == 24:
                return 'Vinte e Quatro Diárias'
            elif dialy == 25:
                return 'Vinte e Cinco Diárias'
            elif dialy == 26:
                return 'Vinte e Seis Diárias'
            elif dialy == 27:
                return 'Vinte e Sete Diárias'
            elif dialy == 28:
                return 'Vinte e Oito Diárias'
            elif dialy == 29:
                return 'Vinte e Nove Diárias'
            elif dialy == 30:
                return 'Trinta Diárias'
            elif dialy == 31:
                return 'Trinta e Uma Diárias'
            else:
                return f'{dialy} Diárias'


    def alfa_num_criancas(self, num_criancas):
        if num_criancas == 0:
            return ''
        elif num_criancas == 1:
            return 'Uma Criança'
        elif num_criancas == 2:
            return 'Duas Crianças'
        elif num_criancas == 3:
            return 'Três Crianças'
        elif num_criancas == 4:
            return 'Quatro Crianças'
        else:
            'Erro'


    def idades(self, idade1, idade2, idade3, idade4, num_criancas):
        def alfa_idades(idade):
            if idade == 0:
                return '0 Ano'
            elif idade == 1:
                return '1 Ano'
            elif idade == 2:
                return '2 Anos'
            elif idade == 3:
                return '3 Anos'
            elif idade == 4:
                return '4 Anos'
            elif idade == 5:
                return '5 Anos'
            elif idade == 6:
                return '6 Anos'
            elif idade == 7:
                return '7 Anos'
            elif idade == 8:
                return '8 Anos'
            elif idade == 9:
                return '9 Anos'
            elif idade == 10:
                return '10 Anos'
            elif idade == 11:
                return '11 Anos'
            elif idade == 12:
                return '12 Anos'
            elif idade == 13:
                return '13 Anos'
            elif idade == 14:
                return '14 Anos'
            elif idade == 15:
                return '15 Anos'
            elif idade == 16:
                return '16 Anos'
            elif idade == 17:
                return '17 Anos'

        if num_criancas == 0:
            return ''
        elif num_criancas == 1:
            return (f'{alfa_idades(idade1)} (Cortesia)' if idade1 <=6 else alfa_idades(idade1))
        elif num_criancas == 2:
            idade1 = f'{alfa_idades(idade1)} (Cortesia)' if idade1 <=6 else alfa_idades(idade1)
            idade2 = alfa_idades(idade2)
            return f'{idade1}/{idade2}'


    def configuracao_geral_parcela(self, valor_total):
        configuracao = Configuracao.objects.filter(valor_final__gte=valor_total).filter(valor_inicial__lte=valor_total)
        return configuracao.values()[0]['parcela']

    def configuracao_geral_entrada(self, valor_total):
        configuracao = Configuracao.objects.filter(valor_final__gte=valor_total).filter(valor_inicial__lte=valor_total)
        entrada = configuracao.values()[0]['entrada']
        if entrada is True:
            parcela = configuracao.values()[0]['parcela']
            return parcela+1
        else:
            parcela = configuracao.values()[0]['parcela']
            return parcela

    def verificacao_bool(self, dados, check_in, check_out, num_dias, num_criancas, idade_crianca, num_pessoas, valor_total, valor_real, valor_desconto, valor_da_parcelas, valor_50porc, num_parcela_mais_1, porcentagem, porcentagem_mais_5, desconto, valor_da_parcelas_menos_etrada, num_parcela, cotacao_texto, valor_da_entrada):

        if check_in is True:
            check_in = (dados.check_in.strftime('%d de %B de %Y (%a)').title())
        else:
            check_in = ''
        if check_out is True:
            check_out = (dados.check_out.strftime('%d de %B de %Y (%a)').title())
        else:
            check_out = ''
        if num_dias is True:
            num_dias = (self.dias_alfa(dados.check_in, dados.check_out))
        else:
            num_dias = ''
        if num_criancas is True:
            num_criancas = (self.alfa_num_criancas(dados.num_criancas))
        else:
            num_criancas = ''
        if idade_crianca is True:
            idade_crianca = (self.idades(dados.idade_crianca1, dados.idade_crianca2, dados.idade_crianca3, dados.idade_crianca4, dados.num_criancas))
        else:
            idade_crianca = ''
        if num_pessoas is True:
            num_pessoas = f'{dados.num_adultos} Pessoa(s)'
        else:
            '' 
        if valor_total is True:
            valor_total = locale.currency(dados.valor_cotacao, grouping=True)
        else: 
            valor_total = ''
        if valor_real is True:
            valor_real = (dados.valor_cotacao*100)/95
            valor_real = locale.currency(valor_real, grouping=True)
        else:
            valor_real = ''
        if valor_desconto is True:
            valor_desconto = (dados.valor_cotacao-(dados.valor_cotacao*desconto)/100)
            valor_desconto = locale.currency(valor_desconto, grouping=True)
        else:
            valor_desconto = ''
        if valor_da_parcelas is True:
            parcela = self.configuracao_geral_parcela(dados.valor_cotacao)
            valor_da_parcelas = dados.valor_cotacao/parcela
            valor_da_parcelas = locale.currency(valor_da_parcelas, grouping=True)
        else: 
            valor_da_parcelas = ''
        if valor_da_parcelas_menos_etrada is True:
            parcela = self.configuracao_geral_parcela(dados.valor_cotacao)
            parcela_entrada = self.configuracao_geral_entrada(dados.valor_cotacao)
            valor_da_parcelas_menos_etrada = locale.currency((dados.valor_cotacao-(dados.valor_cotacao/parcela_entrada))/parcela, grouping=True)
        else:
            valor_da_parcelas_menos_etrada = ''
        if valor_50porc is True:
            valor_50porc = locale.currency(dados.valor_cotacao/2, grouping=True)
        else:
            valor_50porc = ''
        if num_parcela is True:
            num_parcela = self.configuracao_geral_parcela(dados.valor_cotacao)
            num_parcela = f'{num_parcela}x'
        else:
            num_parcela = ''
        if num_parcela_mais_1 is True:
            num_parcela_mais_1 = self.configuracao_geral_entrada(dados.valor_cotacao)
            num_parcela_mais_1 = f'{num_parcela_mais_1}x'
        else:
            num_parcela_mais_1 
        if porcentagem is True:
            porcentagem = desconto
            porcentagem = f'{desconto}%'

        else:
            porcentagem = ''
        if porcentagem_mais_5 is True:
            porcentagem_mais_5 = desconto+5
            porcentagem_mais_5 = f'{desconto+5}%'
        else:
            porcentagem_mais_5 = ''
        if valor_da_entrada is True:
            parcela = self.configuracao_geral_parcela(dados.valor_cotacao)
            parcela_entrada = self.configuracao_geral_entrada(dados.valor_cotacao)
            conta = dados.valor_cotacao/parcela_entrada
            valor_da_entrada =  locale.currency(conta, grouping=True)
        else:
            valor_da_entrada = ''

        cotacao_texto = Template(cotacao_texto).substitute(
            Check_In=check_in,
            Check_Out=check_out,
            Num_Dias=num_dias,
            Valor_Total=valor_total,
            Valor_Real=valor_real,
            Valor_Desconto=valor_desconto,
            Valor_Da_Parcelas=valor_da_parcelas,
            Valor_Da_Parcelas_Menos_Etrada=valor_da_parcelas_menos_etrada,
            Valor_50Porc=valor_50porc,
            Num_Parcela=num_parcela,
            Num_Parcela_Mais_1=num_parcela_mais_1,
            Porcentagem=porcentagem,
            Porcentagem_mais_5=porcentagem_mais_5,
            Num_Criancas=num_criancas,
            Idade_Crianca=idade_crianca,
            Valor_Da_Entrada=valor_da_entrada,
            Porcentagem_Mais_5=porcentagem_mais_5,
            Num_Pessoas=num_pessoas
        )
        return str(cotacao_texto)
class ServicoModels():
    def texto_whatsapp_detalhe_view(self, nome, telefone, check_in, check_out, num_adultos, num_criancas, idade_crianca1, idade_crianca2, idade_crianca3, idade_crianca4, valor_cotacao):

        def nome_funcao(nome_cotacao, nome):
            if nome_cotacao == True:
                nome = nome
            else:
                nome = ''

            return nome
        
        def person_alfa():
            if num_adultos == 1:
                return 'Uma Pessoa'
            elif num_adultos == 2:
                return 'Duas Pessoas'
            elif num_adultos == 3:
                return 'Três Pessoas'
            elif num_adultos == 4:
                return 'Quatro Pessoas'
            elif num_adultos == 5:
                return 'Cinco Pessoas'
            elif num_adultos == 6:
                return 'Seis Pessoas'
        
        def criancas_func():
            for crianca in range(num_criancas):
                crianca = crianca+1
                if crianca == 1:
                    if idade_crianca1 <= 6:
                        idade_crianca1_func = f'{idade_crianca1} Anos (Cortesia)'
                    else:
                        idade_crianca1_func = f'{idade_crianca1} Anos'
                if crianca == 2:
                    if idade_crianca2 <= 6:
                        idade_crianca2_func = f'{idade_crianca2} Anos (Cortesia)'
                    else:
                        idade_crianca2_func = f'{idade_crianca2} Anos'
                if crianca == 3:
                    if idade_crianca3 <= 6:
                        idade_crianca3_func = f'{idade_crianca3} Anos (Cortesia)'
                    else:
                        idade_crianca3_func = f'{idade_crianca3} Anos'
                if crianca == 4:
                    if idade_crianca4 <= 6:
                        idade_crianca4_func = f'{idade_crianca4} Anos (Cortesia)'
                    else:
                        idade_crianca4_func = f'{idade_crianca4} Anos'
            return f'{idade_crianca1_func}{idade_crianca2_func}{idade_crianca3_func}{idade_crianca4_func}'
                

        def check_in_funcao(check_in_cotacao, check_in):
            if check_in_cotacao == True:
                check_in = ''

        return 'dasdasdadsa'

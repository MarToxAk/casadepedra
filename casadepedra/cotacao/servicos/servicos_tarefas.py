from ..models import CotacaoModels
import requests
import json
from pprint import pprint
import datetime

class ServicoCotacao():

    def valor_diaria_api_omnibees(self, check_in, check_out, num_adultos, num_criancas, idade_crianca1, idade_crianca2, idade_crianca3, idade_crianca4):
        dict_json_idade_crianca1 = None if idade_crianca1 == None else {'Age': idade_crianca1, 'AgeQualifyCode': 7 if idade_crianca1 <= 11 else 8 , 'Count': 1} 
        dict_json_idade_crianca2 = None if idade_crianca2 == None else {'Age': idade_crianca2, 'AgeQualifyCode': 7 if idade_crianca2 <= 11 else 8 , 'Count': 1} 
        dict_json_idade_crianca3 = None if idade_crianca3 == None else {'Age': idade_crianca3, 'AgeQualifyCode': 7 if idade_crianca3 <= 11 else 8 , 'Count': 1}
        dict_json_idade_crianca4 = None if idade_crianca4 == None else {'Age': idade_crianca4, 'AgeQualifyCode': 7 if idade_crianca4 <= 11 else 8 , 'Count': 1} 

        headers = {'content-type': 'application/json'}

        json_dict = {'EchoToken': 'b892b6f6-aba5-9616-2002-ef1bb1d142f2', 'TimeStamp': str(datetime.datetime.today()) , 'Target': 0, 'Version': 0, 'PrimaryLangID': 8, 'AvailRatesOnly': False, 'BestOnly': False, 'IsModify': False, 'RequestedCurrency': 16, 'HotelSearchCriteria': {'AvailableOnlyIndicator': False, 'Criterion': {'RoomStayCandidatesType': {'RoomStayCandidates': [{'GuestCountsType': {'GuestCounts': [
            {'Age': None, 'AgeQualifyCode': 10, 'Count': num_adultos}, dict_json_idade_crianca1, dict_json_idade_crianca2, dict_json_idade_crianca3, dict_json_idade_crianca4]}, 'Quantity': 1, 'RPH': 0, 'BookingCode': ''}]}, 'HotelRefs': [{'ChainCode': None, 'HotelCode': 3661}], 'GetPricesPerGuest': True, 'StayDateRange': {'Duration': None, 'Start': str(check_in), 'End': str(check_out)}, 'RatePlanCandidatesType': {'RatePlanCandidates': [{'GroupCode': None, 'PromotionCode': None}]}, 'TPA_Extensions': {'IsForMobile': True, 'RatePlanID': '', 'RoomTypeID': ''}}}}

        dict_json = json.dumps(json_dict)
        r = requests.post(
            'https://beapi.omnibees.com/api/BE/GetHotelAvail?v=2.0.2&api=7af21027-ca43-736b-ec40-074418ac55dd&t=aab46c45b97d059671359e9bf122cc4a', data=dict_json, headers=headers)
        js = r.json()
        pp = json.dumps(js)
        valor_diaria = json.loads(pp)
        return valor_diaria


    def servico_criar_cotacao(self, cotacao):
        CotacaoModels.objects.create(autor=cotacao.autor, nome=cotacao.nome, telefone=cotacao.telefone, check_in=cotacao.check_in, check_out=cotacao.check_out, num_adultos=cotacao.num_adultos, num_criancas=cotacao.num_criancas,
                                    idade_crianca1=cotacao.idade_crianca1, idade_crianca2=cotacao.idade_crianca2, idade_crianca3=cotacao.idade_crianca3, idade_crianca4=cotacao.idade_crianca4, valor_cotacao=self.valor_diaria_api_omnibees(cotacao.check_in, cotacao.check_out, cotacao.num_adultos, cotacao.num_criancas, cotacao.idade_crianca1, cotacao.idade_crianca2, cotacao.idade_crianca3, cotacao.idade_crianca4)['HotelStaysType']['HotelStays'][0]['Price']['AmountBeforeTax'])

    def servico_edicao_cotacao(self, cotacao):
        CotacaoModels.objects.filter(pk=cotacao.pk).update(autor=cotacao.autor, nome=cotacao.nome, telefone=cotacao.telefone, check_in=cotacao.check_in, check_out=cotacao.check_out, num_adultos=cotacao.num_adultos, num_criancas=cotacao.num_criancas,
                                                  crianca1=cotacao.crianca1, crianca2=cotacao.crianca2, crianca3=cotacao.crianca3, crianca4=cotacao.crianca4, valor_cotacao=self.valor_diaria_api_omnibees(cotacao.check_in, cotacao.check_out, cotacao.num_adultos, cotacao.num_criancas, cotacao.crianca1, cotacao.crianca2, cotacao.crianca3, cotacao.crianca4), parcela=cotacao.parcela, disconto=cotacao.disconto)

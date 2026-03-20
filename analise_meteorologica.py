# Projeto acadêmico de análise de dados meteorológicos
# Data:13/11/2025
# Cria classes para processar e armazenar informações meteorológicas de
# instituições de ensino, IEs.

#######################################################################
# Coloque aqui as definições das classes EstacaoMeteorologica e       #
# GestorMeteorologico.                                                #
#######################################################################
class EstacaoMeteorologica:
    def __init__(self, ie, temp, precip):
        self.ie = ie # String ('IFMG', 'UFMG', 'UFV' etc.)
        self.temp = temp # Lista de floats
        self.precip = precip # Lista de floats
        
    def inserir_medicao(self, temp, precip):
        # Adiciona novas medições nas listas de temperaturas e
        # precipitações armazenadas nos atributos da classe.
        self.temp.append(temp)
        self.precip.append(precip)
       
    def calcular_medias_anuais(self):
        # Calcula as médias das temperaturas e precipitações
        # para os últimos 12 meses
        tempFat = self.temp
        precipFat = self.precip
        somaTemp = 0
        cont = 0
        for i in range(len(self.temp)-12,len(self.temp)):
            somaTemp += self.temp[i]
            cont += 1
            temp_media_12 = somaTemp / cont
        somaPrecip = 0
        for j in range(len(self.precip)-12,len(self.precip)):
            somaPrecip += self.precip[j]
            precip_media_12 = somaPrecip / cont
       
        
        return (temp_media_12, precip_media_12)


class GestorMeteorologico:
    def __init__(self):
        self.dict_ies = {}
    def inserir_estacao(self, estacao):
        self.dict_ies[estacao.ie] = estacao
        
        


def main():
    import random
    
    random.seed(167)
    nmed = 2003 # n > 10; neste caso, número de medições de 166 anos e 11 meses
    
    temps = [random.uniform(0.0, 40.00) for _ in range(nmed)]
    precips = [random.uniform(0.0, 300.0) for _ in range(nmed)]
    
    # Cria a estacao_ufv.
    estacao_ufv = EstacaoMeteorologica('UFV', temps, precips)
    # Insere a temperatura média mensal 25.0° e a respectiva precipitação
    # média mensal 53.6 mm na estacao_ufv.
    estacao_ufv.inserir_medicao(25.0, 53.6)
    # Calcula a temperatura média e a precipitação média dos últmos 12 meses.
    (temp_media_12, precip_media_12) = estacao_ufv.calcular_medias_anuais()

    # Cria um gestor meteorológico.
    gestor = GestorMeteorologico()
    # Insere a estacao_ufv no gestor meteorológico.
    gestor.inserir_estacao(estacao_ufv)
    
    print('Temperatura média dos últimos 12 meses na estação %s: %.1f °C' %
          (gestor.dict_ies[estacao_ufv.ie].ie, temp_media_12))
    print('Precipitação média dos últimos 12 meses na estação %s: %.0f mm' %
          (gestor.dict_ies[estacao_ufv.ie].ie, precip_media_12))


if __name__ == '__main__':
    main()

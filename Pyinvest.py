import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#entradas
capital = float(input('Capital inicial: '))
aporte = float(input('Aporte Mensal: '))
meses = int(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual (%)')) / 100
perc_cdb = float(input('Percentual do CDI (%)')) / 100
perc_lci = float(input('Percentual do LCI (%)')) / 100
taxa_fii = float(input('Rentabilidade mensal do FII (%)')) / 100
meta = float(input('Meta financeira (R$) ')) 

#conversão cdi
cdi_mensal = math.pow(1+cdi_anual, 1/12) -1

#total investido
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1 + taxa_cdb), meses) + (aporte *meses))
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.05)

#LCI
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1 + taxa_lci), meses) + (aporte *meses) )

#POUPANÇA
taxa_poupança = 0.005 
montante_poupanca = (capital *math.pow((1 + taxa_poupança), meses) + (aporte * meses) )

#FII - SIMULAÇÕES
valor_base_fii = (capital * math.pow((1 + taxa_fii), meses) + (aporte * meses))

fii1 = valor_base_fii * (1 + random.uniform(-0.03, 0.03))
fii2 = valor_base_fii * (1 + random.uniform(-0.03, 0.03))
fii3 = valor_base_fii * (1 + random.uniform(-0.03, 0.03))
fii4 = valor_base_fii * (1 + random.uniform(-0.03, 0.03))
fii5 = valor_base_fii * (1 + random.uniform(-0.03, 0.03))

lista_fii = [fii1, fii2, fii3, fii4, fii5]

media_fii = statistics.mean(lista_fii)
mediana_fii = statistics.median(lista_fii)
desvio_fii = statistics.stdev(lista_fii)

# DATA
data_simulacao = datetime.datetime.now()
data_resgate = data_simulacao + datetime.timedelta(days = meses * 30)

# META
meta_atingida = media_fii >= meta

# GRÁFICOS ASCII

graf_cdb = "█" * int(montante_cdb_liquido / 1000)
graf_lci = "█" * int(montante_lci / 1000)
graf_poup = "█" * int(montante_poupanca / 1000)
graf_fii = "█" * int(media_fii / 1000)

# RELATÓRIO FINAL

print("\n===================================")
print("PyInvest - Simulador de Investimentos")
print("===================================")

print("\nData da simulação:", data_simulacao.strftime("%d/%m/%Y"))
print("Data estimada de resgate:", data_resgate.strftime("%d/%m/%Y"))

print("\nTotal investido:", locale.currency(total_investido, grouping=True))

print("\n--- RESULTADOS FINANCEIROS ---")

print("\nCDB:", locale.currency(montante_cdb_liquido, grouping=True))
print(graf_cdb)

print("\nLCI/LCA:", locale.currency(montante_lci, grouping=True))
print(graf_lci)

print("\nPoupança:", locale.currency(montante_poupanca, grouping=True))
print(graf_poup)

print("\nFII (média):", locale.currency(media_fii, grouping=True))
print(graf_fii)

print("\n--- ESTATÍSTICAS FII ---")

print("Mediana:", locale.currency(mediana_fii, grouping=True))
print("Desvio padrão:", locale.currency(desvio_fii, grouping=True))

print("\nMeta atingida:", meta_atingida)

print("===================================")

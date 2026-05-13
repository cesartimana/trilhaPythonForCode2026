# Presentación inicial

print('Calculadora de viagem! Será que a viagem é viável??')
print('---------------------------------------------------')
print('\nIMPORTANTE: Usar PONTO como separador decimal. NÃo usar separador de milhares. Exemplo: 48659.12')

def check_value(val):
    if val < 0:
        raise Exception('Valor negativo (inadequado). Calculo encerrado')
    return

#Solicitud de inputs y restricciones
presupuesto = float(input("\nIndique o orcamento disponivel, em Reais: "))
check_value(presupuesto)
destino = input('Indique o nome da cidade ou pais do destino: ')
pasaje = float(input('Indique o custo da passagem, em Reais: '))
check_value(pasaje)
hosp = float(input('Indique o custo diário de hospedagem, em Euros: '))
check_value(hosp)
dias = int(input('Indique os días de viagem, sem decimais: '))
check_value(dias)

#Constante
conv_EU_BR = 6.1 #1 Euro = 6.1 Reais

#Cálculos
total_hosp = hosp * conv_EU_BR * dias
custo_total = total_hosp + pasaje


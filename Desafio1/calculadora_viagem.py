# 1) Presentación inicial

print('\nCalculadora de viagem! Será que a viagem é viável??')
print('---------------------------------------------------')
print('\nIMPORTANTE: Usar PONTO como separador decimal. NÃo usar separador de milhares. ')
print('Exemplo: 48659.12')

def check_value(val):
    #para revisar negativos
    if val < 0:
        raise Exception('Valor negativo (inadequado). Calculo encerrado')
    return

# 2) Solicitud de inputs y restricciones
presupuesto = float(input("\nIndique o orcamento disponivel, em Reais: "))
check_value(presupuesto)
destino = input('Indique o nome da cidade ou pais do destino: ')
pasaje = float(input('Indique o custo da passagem, em Reais: '))
check_value(pasaje)
hosp = float(input('Indique o custo diário de hospedagem, em Euros: '))
check_value(hosp)
dias = int(input('Indique os días de viagem, sem decimais: '))
check_value(dias)

# 3) Calculos
#Constante
conv_EU_BR = 6.1 #1 Euro = 6.1 Reais

#Cálculos
total_hosp = hosp * conv_EU_BR * dias
custo_total = total_hosp + pasaje

# 4) Validacion y exhibicion de resultados
#A partir de aqui, informacion que obtengo, informacion que se muestra

print('\nResultados da calculadora!!!')
print('------------------------------')
print('\nSe eu quero viagar a ' + destino + ' com ' + str(round(presupuesto,2)) + ' reais...')
print('\nValor total da hospedagem: ' + str(round(total_hosp,2)) + ' reais')
print('Custo total da viagem: ' + str(round(custo_total,2)) + ' reais')

#Validacion de presupuesto
diff = presupuesto - custo_total
if diff > 0:
    print('Orcamento possivel. Sobrará ' + str(round(diff,2)) + ' reais')
else:
    print('Orcamento NÃO possivel. Falta ' + str(round(-diff,2)) + ' reais')

#Viavilidad
#Lo escribi así para forzarme a usar BOOL, AND. Pero no seria como normalmente lo haria

bool_viavel = False

if diff > 0 and dias > 0:
    bool_viavel = True

if bool_viavel:
    print('Status da viagem: VIAVEL')
else:
    print('Status da viagem: INVIAVEL')

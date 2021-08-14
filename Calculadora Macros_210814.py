"""
Calculadora de Macros baseada no trabalho de Michael Matthews (BLS e TLS)
"""

# BMR = Taxa Metabólica Basal
# TDEE = Total de Energia Gasta Diariamente

sexo = input('Você é homem ou mulher? ').capitalize()
while not (sexo=='Homem') and not (sexo=='Mulher'):
    sexo = input('PQP, você é homem ("Homem") ou mulher ("Mulher")? ').capitalize()
w = float(input('Qual seu peso (kg)? '))
h = float(input('Qual sua altura (cm)? '))
if(h<=2.50) and h>1:
    h=h*100
age = int(input('Quantos anos você tem? '))
f = int(input('Quantas horas por semana você faz exercício? '))
fator_freq=[1.15,1.2,1.275,1.35,1.4,1.475,1.55,1.6,1.675,1.75,1.85]

if(sexo=='Homem'):
    BMR = 10 * w + 6.25 * h - 5 * age + 5

elif (sexo == 'Mulher'):
    BMR = 10 * w + 6.25 * h - 5 * age - 161

TDEE = BMR * fator_freq[f]

print()
print(f'Taxa Metabólica Basal estimada:{BMR:.0f}kCal')
print()
print(f'Gasto Energético Diário estimado: {TDEE:.0f}kCal')
print()

obj=input('Qual seu objetivo atual (Secar, Manter ou Crescer)? ').capitalize()

while not (obj=="Secar") and not (obj=="Manter") and not (obj=="Crescer"):
    print('Responda com "Secar", "Manter" ou "Crescer" apenas!')
    obj = input('Qual seu objetivo atual (Secar, Manter ou Crescer)? ').capitalize()

if(obj=='Secar'):
    cal=TDEE*0.75
    proteínas=0.4*cal/4
    carbos=0.4*cal/4
    gorduras=0.2*cal/9
elif(obj=='Manter'):
    cal=TDEE
    proteínas=0.3*cal/4
    carbos=0.45*cal/4
    gorduras=0.25*cal/9
elif (obj=='Crescer'):
    cal=TDEE*1.1
    proteínas=0.25*cal/4
    carbos=0.55*cal/4
    gorduras=0.2*cal/9

print()
print(f'Calorias estimadas: {cal:.0f}kCal por dia')
print(f'proteínas: {proteínas:.0f}g')
print(f'carbos: {carbos:.0f}g')
print(f'gorduras: {gorduras:.0f}g')
print()

if(obj=='Secar'):
    print('Obs.: Caso seu peso não mude em 02 semanas, corte em 25g seus carbos')
if(obj=='Crescer'):
    print('Obs.: Caso seu peso não mude em 02 semanas, aumente em 30g seus carbos')

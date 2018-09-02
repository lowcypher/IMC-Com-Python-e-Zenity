#! /usr/bin/env python
#-*- coding: UTF-8 -*-

from zenipy import entry
from zenipy import message

peso = entry(text='Peso - Use ponto como separador do Peso', placeholder='Digite O Peso', title='IMC')
altura = entry(text='Altura - Use ponto como separador da Altura', placeholder='Digite A Altura', title='IMC')
imc = float (peso) / (float(altura)*float(altura)) 

if imc < 17:
   message(title='IMC', text="%s " '\nIMC Excessivamente Baixo' %(imc))
elif (17 < imc < 18.49):
   message(title='IMC', text="%s " '\nIMC Baixo' %(imc))
elif (18.5 < imc < 24.99):
   message(title='IMC', text="%s " '\nIMC Normal' %(imc))
elif (25 < imc < 29.99):
   message(title='IMC', text="%s " '\nIMC Sobrepeso' %(imc))
elif (30 < imc < 34.99):
   message(title='IMC', text="%s " '\nIMC Obesidade I' %(imc))
elif (35 < imc < 39.99):
   message(title='IMC', text="%s " '\nIMC Obesidade II (Severa)' %(imc))
elif imc > 40:
   message(title='IMC', text="%s " '\nIMC Obesidade III (Móbida)' %(imc))

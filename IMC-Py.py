#! /usr/bin/env python
#-*- coding: UTF-8 -*-
'''
Nome: IMC-Py
Autor: Mario Medeiros
Data: 2016-10-19
Versão: 0.1
Feito em:
Python 2.7.6
GNU/Linux
--------------------------------------------------------------------------------
Programa em Python que calcula o IMC - Índice de Massa Corpórea, de uma pessoa.
Dado o seu peso e altura usando a fórmula do IMC = peso divido pelo quadrado da
altura e em seguida mostra a mensagem de acordo com tabela abaixo:

Tabela de Referência - IMC
Fonte: http://www.calculoimc.com.br/tabela-de-imc
-----------------------------------------------
Resultado 	       |  Situação                |
----------------------------------------------|
Abaixo de 17 	   |  Muito abaixo do peso    |
Entre 17 e 18,49   |  Abaixo do peso          |
Entre 18,5 e 24,99 |  Peso normal             |
Entre 25 e 29,99   |  Acima do peso           |
Entre 30 e 34,99   |  Obesidade I             |
Entre 35 e 39,99   |  Obesidade II (severa)   |
Acima de 40 	   |  Obesidade III (mórbida) |
-----------------------------------------------

                Altura (em metros)
Peso (em kg) |	1,5 	1,55 	1,6 	1,65 	1,7 	1,75 	1,8 	1,85 	1,9 	1,95 	2
-----------------------------------------------------------------------------------------------------
50 	         |  22,22 	20,81 	19,53 	18,37 	17,30 	16,33 	15,43 	14,61 	13,85 	13,15 	12,50
55 	         |  24,44 	22,89 	21,48 	20,20 	19,03 	17,96 	16,98 	16,07 	15,24 	14,46 	13,75
60 	         |  26,67 	24,97 	23,44 	22,04 	20,76 	19,59 	18,52 	17,53 	16,62 	15,78 	15,00
65 	         |  28,89 	27,06 	25,39 	23,88 	22,49 	21,22 	20,06 	18,99 	18,01 	17,09 	16,25
70 	         |  31,11 	29,14 	27,34 	25,71 	24,22 	22,86 	21,60 	20,45 	19,39 	18,41 	17,50
75 	         |  33,33 	31,22 	29,30 	27,55 	25,95 	24,49 	23,15 	21,91 	20,78 	19,72 	18,75
80 	         |  35,56 	33,30 	31,25 	29,38 	27,68 	26,12 	24,69 	23,37 	22,16 	21,04 	20,00
85 	         |  37,78 	35,38 	33,20 	31,22 	29,41 	27,76 	26,23 	24,84 	23,55 	22,35 	21,25
90 	         |  40,00 	37,46 	35,16 	33,06 	31,14 	29,39 	27,78 	26,30 	24,93 	23,67 	22,50
95 	         |  42,22 	39,54 	37,11 	34,89 	32,87 	31,02 	29,32 	27,76 	26,32 	24,98 	23,75
100 	     |  44,44 	41,62 	39,06 	36,73 	34,60 	32,65 	30,86 	29,22 	27,70 	26,30 	25,00
105 	     |  46,67 	43,70 	41,02 	38,57 	36,33 	34,29 	32,41 	30,68 	29,09 	27,61 	26,25
110 	     |  48,89 	45,79 	42,97 	40,40 	38,06 	35,92 	33,95 	32,14 	30,47 	28,93 	27,50
115 	     |  51,11 	47,87 	44,92 	42,24 	39,79 	37,55 	35,49 	33,60 	31,86 	30,24 	28,75
120 	     |  53,33 	49,95 	46,88 	44,08 	41,52 	39,18 	37,04 	35,06 	33,24 	31,56 	30,00
125 	     |  55,56 	52,03 	48,83 	45,91 	43,25 	40,82 	38,58 	36,52 	34,63 	32,87 	31,25
130 	     |  57,78 	54,11 	50,78 	47,75 	44,98 	42,45 	40,12 	37,98 	36,01 	34,19 	32,50
135 	     |  60,00 	56,19 	52,73 	49,59 	46,71 	44,08 	41,67 	39,44 	37,40 	35,50 	33,75
140 	     |  62,22 	58,27 	54,69 	51,42 	48,44 	45,71 	43,21 	40,91 	38,78 	36,82 	35,00
-----------------------------------------------------------------------------------------------------
'''
print
print
print ('   ==================== { IMC-Py - Versão 0.1} ====================')
print ('   ======= { Cáculo do IMC - Índice de Massa Corpórea } =======')
print ('   ======= { Obs: o separador valor peso/altura é o ponto } ======= ')
print ('   ======= { Exemplo: peso 75.7 - altura 1.75 } =======')
print ('   =================== { Data Release: 2016-10-19 } ===============')
print
peso = raw_input ('   Digite o peso: ')
print
altura = raw_input ('   Digite a altura: ')
print
imc = float (peso) / (float(altura)*float(altura))

if imc < 17:
 print '   IMC Excessivamente Baixo ' , imc
elif (17 < imc < 18.49):
 print '   IMC Baixo ' , imc
elif (18.5 < imc < 24.99):
 print '   IMC Normal ' , imc
elif (25 < imc < 29.99):
 print '   IMC Sobrepeso ' , imc
elif (30 < imc < 34.99):
 print '   IMC Obesidade I ' , imc
elif (35 < imc < 39.99):
 print '   IMC Obesidade II (Severa) ' , imc
elif imc > 40:
 print '   IMC Obesidade III (Mórbida) ' , imc
print

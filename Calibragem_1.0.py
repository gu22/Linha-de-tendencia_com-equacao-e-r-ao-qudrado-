# -*- coding: utf-8 -*-
#import xlsxwriter
import os
import shutil
import decimal
from datetime import *


def frange(x,y,jump):
    while x< y:
        yield x
        x += jump

dir_padrao=os.path.dirname(os.path.abspath(__file__))

"""======================================================================"""

print (('CALIBRAGEM DE PONTAS - v1.0')+('\n')+('Desenvolvido por: Gustavo dos Santos'))
hj = date.today()
hora = datetime.now()

print ('\n')
print (hj)


print ("\n")




sim = ['s','sim']
nao = ['n','nao','não']
cm = 1
bk = sim + nao



verb = list(frange(-8,8,decimal.Decimal("0.01")))
vere = [float(i) for i in verb]

print (('Para corrigir valor anterior')+('\n')+('Aperte a letra c ')+('\n'))
valores = {}
while True:
    cver = 00

    while cver < 61:


        avar = (input("%d: "%cver).replace(",","."))
        correcao ="c"
        if avar != correcao:
            avar = float((avar).replace(",","."))
            if avar in vere:
                valores[cver]= avar
                cver = cver + 10
        else:
            cver = cver - 10
            valores[cver] = float(input("%d: "%cver).replace(",","."))
            cver = cver + 10



##            if avar == correcao:
##                cver = cver - 10
##                valores[cver] = (input("%d: "%cver).replace(",","."))
##                cver = cver + 10
##            elif avar in vere:
##                valores[cver]= float((avar).replace(",","."))
##                cver = cver + 10
##            try:
##                avar = float(input("%d: "%cver).replace(",","."))
##                break
##            except ValueError:
##                print ('Valor não é aceito')

        #if
##        if avar  in vere:
##            valores[cver]= avar
##            cver = cver + 10


    else:
        pass

    print ('\n')

    print ('Valores Registrados:')
    for pontas in sorted(valores.items()):

        print (pontas)
################################################################################
    cop = (input ('Valores estao corretos? (Sim: s / Nao: n): '))


    while cop in nao :

        if cop in nao:
            print ('Pontos: ')
            for pc in sorted(valores):
                print (pc)

            while True:
                try:
                    copc = int(input ('Qual ponto está incorreto: '))
                    while copc not in valores:
                        print ('Valor não é aceito')
                    else:
                        print ('Correcão do ponto %d'%copc)
                        break
                except ValueError:
                    print ('Valor não é aceito')

            while True:
                try:
                    valores[copc] = float(input("Valor de Correção: ").replace(",","."))
                    break
                except ValueError:
                    print ('Valor não é aceito')


            for xyz in sorted(valores.items()):

                print (xyz)


            while True:
                cop = (input ('Valores estão corretos? (Sim: s / Nao: n): ').lower())
                if cop in sim:
                    break
                else:
                    print ('Valor não é aceito')

    print('\n')


####################################################################################
    #print (valores[10])
    #Calculando a 1° parte equacao
    a = 7*(0*(valores[0]) + 10*(valores[10]) + 20*(valores[20]) + 30*(valores[30]) + 40*(valores[40]) + 50*(valores[50]) + 60*(valores[60]))
    b = ((0+10+20+30+40+50+60)*((valores[0])+(valores[10])+(valores[20])+(valores[30])+(valores[40])+(valores[50])+(valores[60])))
    c = 7*((valores[0])**2+(valores[10])**2+(valores[20])**2+(valores[30])**2+(valores[40])**2+(valores[50])**2+(valores[60])**2)
    d = ((valores[0])+(valores[10])+(valores[20])+(valores[30])+(valores[40])+(valores[50])+(valores[60]))**2
    m = (a-b)/(c-d)
    #Calculando a 2° parte equacao
    e = (0+10+20+30+40+50+60)
    f = m * ((valores[0])+(valores[10])+(valores[20])+(valores[30])+(valores[40])+(valores[50])+(valores[60]))
    i = (e-f)/7
    print ('Equação:')
    print ('%.4f'%m)
    print ('%.4f'%i)

#Calculando coeficiente de determinaçao (r ao quadrado)
    sereta = ((((0*(valores[0]))+i)**2)+(((10*(valores[10]))+i)**2)+(((20*(valores[20]))+i)**2)+(((30*(valores[30]))+i)**2)+(((40*(valores[40]))+i)**2)+(((50*(valores[50]))+i)**2)+(((60*(valores[60]))+i)**2))
    #print (sereta)



    ymedia = ((1/7)*((7**7/7)+7)-0)
    #print (ymedia)

    semedia = (((0-ymedia)**2)+((10-ymedia)**2)+((20-ymedia)**2)+((30-ymedia)**2)+((40-ymedia)**2)+((50-ymedia)**2)+((60-ymedia)**2))
    #print (semedia)

    rquadrado = float(1-(sereta/semedia))

    print ('R ao quadrado:')
    print ('%.4f'%rquadrado)








################################################################################################################################
    x = ''

    while True:
        y = x
        l = (input('Entre com o valor para verificação (Para finalizar aperte a tecla f ): ').lower())
        w = l

        finalizacao = "f"

        #eq = ((m*l)+i)
        if l == 'f':
            if y == '':
                print ('Valor do campo não pode esta vazio'+('\n'))
            else:
                break
        elif w == '':
            print ('Valor do Ajuste não pode ser vazio')
        else:
            l=float((l).replace(',','.'))
            eq = ((m*l)+i)
            print('%.4f'%eq)
            x = l
            z = eq












#############################################################################################################

    dia = (hj.day)
    mes = (hj.month)

    pasta = ('%d-%d'%(mes,dia))

    if not os.path.exists(pasta):
        os.mkdir(pasta)
        print ('Pasta %d-%d criada'%(mes,dia))
    else:
        #print ('Pasta com data de hoje ja existe')
        pass


    narquivo = (input("Nome:").capitalize()+'.txt')

    #Criando arquivo txt
    os.chdir(pasta)

    arq = open((narquivo),'w')
    arq.write('Pontos:')
    arq.write("\n")

    c = 0
    while c < 61:
        arq.write(str((valores[c])).replace('.',','))
        arq.write("\n")
        c = c+10

    arq.write("\n")
    arq.write("\n")
    arq.write("Ajuste")
    arq.write("\n")
    arq.write('Ponto: '+(str(x).replace('.',',')))
    arq.write("\n")
    arq.write('Resultado: '+(str(z).replace('.',',')))
    arq.write("\n")
    arq.write("\n")
    arq.write('Equação')
    arq.write("\n")
    arq.write('y = '+(str(m).replace('.',',')+'* X'))
    arq.write("\n")
    arq.write(str(i).replace('.',','))
    arq.write("\n")
    arq.write('R²= '+ (str(rquadrado).replace('.',',')))

    arq.close()

    cp = (input('Gostaria de calibrar outra ponta?(Sim: s / Nao: n): ').lower())

    if cp in sim :
        os.chdir(dir_padrao)
        continue
    else:
        os.system = ('Pause')
        input = ("Pressione Enter para finalizar")
        break



os.system = ('Pause')
input = ("Pressione Enter para finalizar")
#print (sorted(valores.items()))

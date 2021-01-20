
Cont_intervalo_1 = 0
Cont_intervalo_2 = 0
Cont_intervalo_3 = 0
Cont_intervalo_4 = 0
Cont_intervalo_5 = 0
Cont_intervalo_6 = 0
Cont_intervalo_7 = 0
Cont_intervalo_8 = 0
Cont_intervalo_9 = 0
Cont_intervalo_10 = 0

cont_while = 0
vendedores = float(input("Digite o numero de vendedores"))

while(True):
    cont_while = cont_while +1


    salario = float(input("Digite o salario"))
    salario_novo = salario+200

    # cada intervalo
    if (salario >= 200 and salario <= 299):
        Cont_intervalo_1 = Cont_intervalo_1+1

    if (salario >= 300 and salario <= 399):

        Cont_intervalo_2 = Cont_intervalo_2+1

    if (salario >= 400 and salario <= 499):

        Cont_intervalo_3 = Cont_intervalo_3+1

    if (salario >= 500 and salario <= 599):

        Cont_intervalo_4 = Cont_intervalo_4+1

    if (salario >= 600 and salario <= 699):

        Cont_intervalo_5 = Cont_intervalo_5+1

    if (salario >= 700 and salario <= 799):

        Cont_intervalo_6 = Cont_intervalo_6+1

    if (salario >= 800 and salario <= 899):

        Cont_intervalo_7 = Cont_intervalo_7+1

    if (salario >= 900 and salario <= 999):

        Cont_intervalo_8 = Cont_intervalo_8+1
    if (salario>1000):
        Cont_intervalo_9 = Cont_intervalo_9 + 1

    if(cont_while == vendedores):
        break

print("Numero de Funcionarios no Intevalo 1:"+str(Cont_intervalo_1))
print("Numero de Funcionarios no Intevalo 2:"+str(Cont_intervalo_2))
print("Numero de Funcionarios no Intevalo 3:"+str(Cont_intervalo_3))
print("Numero de Funcionarios no Intevalo 4:"+str(Cont_intervalo_4))
print("Numero de Funcionarios no Intevalo 5:"+str(Cont_intervalo_5))
print("Numero de Funcionarios no Intevalo 6:"+str(Cont_intervalo_6))
print("Numero de Funcionarios no Intevalo 7:"+str(Cont_intervalo_7))
print("Numero de Funcionarios no Intevalo 8:"+str(Cont_intervalo_8))
print("Numero de Funcionarios no Intevalo 9:"+str(Cont_intervalo_9))
print("Numero de Funcionarios no Intevalo 10:"+str(Cont_intervalo_10))

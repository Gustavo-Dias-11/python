#idade = int(input('digite sua idade: '))

#if idade >= 18:
    #print('permitido')
#else:
    #print('bloqueado')
salario = float(input('digite seu salario: '))

if salario <= 3000:
    print('programador junior')
elif salario > 300 and salario <= 6000:
    print('pregramdor pleno')
elif salario > 6000 and salario <= 15000:
    print('programdor senior')
else: 
    print('gerente de projetos')

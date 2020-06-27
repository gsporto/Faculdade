try:
    num1=int(input("Digite o primeiro valor inteiro: "))
    num2=int(input("Digite o segundo valor inteiro: "))

    result=float(num1/num2)

    print("Resultado: %f" % result)
except ValueError as ve:
    print("Erro1: Voce deve digitar valores inteiros: %s" % ve)
except ZeroDivisionError as zde:
    print("Erro 2: Divisao por zero: %s" % zde)
except Exception as ex:
    print("Erro3: Erro inexperado: %s" % ex)

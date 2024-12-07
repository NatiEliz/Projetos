print("")
valor = input ("Qual valor Fibonacci que você deseja?: ")
print("")
num = int(valor)

if num == 0 or num == 1:
    print (f'O Fibonacci de {valor} é 1')
    
else:
    fibonacci = [0, 1]
    
    for volta in range (2, num):
        proximo = fibonacci[- 1] +fibonacci[- 2]
        fibonacci.append(proximo)
        
    print ("Olá, segue a sua sequencia de Fibonacci:")
    print("")
    print (fibonacci)
    print("")
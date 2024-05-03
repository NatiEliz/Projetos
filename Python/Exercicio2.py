### Criando uma Concessionária

###################################################################### Dados Carros
carros = []
def cadastrarCarro():
    try:
        carro = {
            "codigo": 0,
            "marca": "",
            "ano": "",
            "quantidade": 0,
            "valor": "",
        }
        carro["codigoCarro"] = len(carros) + 1
        carro["marca"] = input("Digite a marca/modelo do carro: ")
        carro["ano"] = int(input("Digite o ano do carro (yyyy): "))
        carro["quantidade"] = int(input("Quantidade comprada: "))
        carro["valor"] = (input ("Valor R$: "))
        carros.append(carro)
        print("")
        print("                      🎉🎉🎉 CARRO CADASTRADO COM SUCESSO!!! 🎉🎉🎉")
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")
    except:
        print("")
        print("ERRO AO EFETUAR O CADASTRO!")
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")
def visualizarCarros():
    try:
        for carro in carros:
            print(f'Código: {carro["codigoCarro"]}')
            print(f'    Marca/Modelo: {carro["marca"]}')
            print(f'    Ano: {carro["ano"]}')
            print(f'    Valor: R$ {carro["valor"]};')
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")
    except:
        print("")
        print("ERRO AO VISUALIZAR O ESTOQUE DE CARROS!")
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")
def estoqueCarros():
    print("")
    for quantidade in carros:
        if estoqueCarros <= len(carros):
            quantidade = list(filter(lambda e: ["quantidade"] == quantidade, carros))
        print (quantidade)
    print("")
    input("Clique qualquer tecla para retornar ao menu inicial")
    print("")
def alterarCarros():
    try:
        
        for carro in carros:
            print(f'Código: {carro["codigoCarro"]} - Marca: {carro["marca"]};')
        print("")
        print("")
        codigo = int(input("Digite o código do Carro que você deseja alterar: "))
        print ("")
        if codigo <= len(carros):
            carro = list(filter(lambda c: c["codigoCarro"] == codigo, carros))[0]
            carros.remove(carro)
            if carro:
                carro["marca"] = input("Digite a marca/modelo do carro: ")
                carro["ano"] = int(input("Digite o ano do carro (yyyy): "))
                carro["valor"] = (input ("Valor R$: "))
                carros.append(carro)
                print("")
                print("                      🎉🎉🎉 CADASTRO ALTERADO COM SUCESSO!!! 🎉🎉🎉")
                print("")
                input ("Clique qualquer tecla para retornar ao menu inicial")
                print("")
        else:
            print("")
            print("CÓDIGO INVÁLIDO!")
            print("")
            input("Clique qualquer tecla para retornar ao menu inicial.")
            print("")
    
    except:
        print("")
        print("ERRO AO ALTERAR OS DADOS!")
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")

###################################################################### Dados Clientes
clientes = []
def cadastrarCliente():
    try:
        cliente = {
            "codigo": 0,
            "nomeCliente": "",
            "dataNascimento": "",
            "documento": 0,
        }
        cliente["codigoCliente"] = len(clientes) + 1
        cliente["nomeCliente"] = str(input("Digite nome completo do cliente: "))
        cliente["dataNascimento"] = input("Digite a data de nascimento do cliente (xx/xx/xxxx): ")
        cliente["documento"] = int(input("Digite o número RG do cliente (apenas nº): "))
        clientes.append(cliente)
        print("")
        print("                    🎉🎉🎉 CLIENTE CADASTRADO COM SUCESSO!!! 🎉🎉🎉 ")
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")
    except:
        print("")
        print("ERRO AO CADASTRAR O CLIENTE!")
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")
def alterarClientes():
    try:
        for cliente in clientes:
            print(f'Código: {cliente["codigoCliente"]} - Nome Cliente: {cliente["nomeCliente"]};')
        print ("")
        print ("")
        codigo = int(input("Digite o código do Cliente que você deseja alterar: "))
        print ("")
        if codigo <= len(clientes): 
            
            cliente = list(filter(lambda c: c["codigoCliente"] == codigo, clientes))[0]
            clientes.remove(cliente)
            if cliente:
                cliente["nomeCliente"] = input("Digite o nome completo do cliente: ")
                cliente["dataNascimento"] = input("Digite a data de nascimento do cliente (xx/xx/xxxx): ")
                cliente["documento"] = int(input("Digite o número RG do cliente (apenas nº): "))
                clientes.append(cliente)
                
                print("")
                print("                      🎉🎉🎉 CADASTRO ALTERADO COM SUCESSO!!! 🎉🎉🎉")
                print("")
                input("Clique qualquer tecla para retornar ao menu inicial")
                print("")
        else:
            print("")
            print("CÓDIGO INVÁLIDO!")
            print("")
            input("Clique qualquer tecla para retornar ao menu inicial.")
            print("")
    except:
        print("")
        print("ERRO AO ALTERAR OS DADOS!")
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")

###################################################################### Dados Vendas
vendas = []
def cadastrarVenda():
    try:
        for cliente in clientes:
            print(f'Código: {cliente["codigoCliente"]} - Nome Cliente: {cliente["nomeCliente"]}')
        codigoCliente = int(input("Digite o código do cliente que realizará a compra: "))
        print("")
        if codigoCliente <= len(clientes): 
            cliente = list(filter(lambda c: c["codigoCliente"] == codigoCliente, clientes))[0]
            
            for carro in carros:
                print(f'Código: {carro["codigoCarro"]} - Marca: {carro["marca"]} - Estoque: {carro["quantidade"]}')
            codigoCarro = int(input("Digite o código do carro a ser comprado: "))
            print("")
            if codigoCarro <= len(carros):
                carro = list(filter(lambda c: c["codigoCarro"] == codigoCarro, carros))[0]
                if carro ["quantidade"] >= 1:
                    print("")
                    print("Deseja confirmar a compra? ")
                    print("(1) Sim")
                    print("(2) Não")
                    print("")
                    opcao = int(input("Informe a opção desejada (x): "))
                    print("")
                    if opcao == 1:
                        venda = {
                        "codigoVenda": 0,
                        "clienteVenda": cliente["nomeCliente"],
                        "carroVenda": carro["marca"],
                        "valor": carro["valor"],
                        "quantidade": 0,
                        }
                        venda["codigoVenda"] = len(vendas) + 1
                        venda["quantidade"] = int(carro["quantidade"] - 1)
                        vendas.append(venda)
                        print("")
                        print("                    🎉🎉🎉 VENDA CADASTRADA COM SUCESSO!!! 🎉🎉🎉 ")
                        print("")
                        input("Clique qualquer tecla para retornar ao menu inicial")
                        print("")
                    elif opcao == 2:
                        print("")
                        print("VENDA CANCELADA.")
                        print("")
                        input("Clique qualquer tecla para retornar ao menu inicial.")
                        print("")
                    else:
                        print("")
                        print("OPÇÃO INVÁLIDA.")
                        print("")
                        input("Clique qualquer tecla para retornar ao menu inicial.")
                        print("")
                else:
                    print("")
                    print("INFELIZMENTE NÃO TEMOS ESTE CARRO EM ESTOQUE.")
                    print("")
                    input("Clique qualquer tecla para retornar ao menu inicial.")
                    print("")
            else:
                print("")
                print("OPÇÃO INVÁLIDA.")
                print("")
                input("Clique qualquer tecla para retornar ao menu inicial.")
                print("")
        else:
            print("")
            print("OPÇÃO INVÁLIDA.")
            print("")
            input("Clique qualquer tecla para retornar ao menu inicial.")
            print("")
    except:
        print("")
        print("ERRO AO CADASTRAR A VENDA!")
        print("")
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")
def visualizarVendas():
    try:
        for venda in vendas:
            print(f'Código: {venda["codigoVenda"]}')
            print(f'    Cliente: {venda["clienteVenda"]}')
            print(f'    Carro: {venda["carroVenda"]}')
            print(f'    Valor da Venda R$: {venda["valor"]}')
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")
    except:
        print("")
        print("ERRO!")
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")

###################################################################### Opção Alterar dados
def opcaoAlterarDados():
    print ("(1) Alterar dados dos Carros")
    print ("(2) Alterar dados dos Clientes")
    print("")
    try:
        opcao1 = int(input("Informe a opção desejada (1 ou 2)?: "))
        print("")
        match opcao1:
            case 1:
                alterarCarros()
            case 2:
                alterarClientes()
            case _:
                print("")
                print("OPÇÃO INVÁLIDA!")
                print("")
                input("Clique qualquer tecla para retornar ao menu inicial.")
                print("")
    except:
        print("")
        print("OPÇÃO INVÁLIDA!")
        print("")
        input("Clique qualquer tecla para retornar ao menu inicial.")
        print("")

###################################################################### Menu de opções
def iniciar():
    print ("======================================================")
    print ("======== Sistema de Compra e Venda - Carros ==========")
    print ("======================================================")
    print ("")
    print ("(1) Inserir um novo carro")
    print ("(2) Inserir um novo cliente")
    print ("(3) Alterar dados já inseridos")
    print ("(4) Inserir uma nova venda")
    print ("(5) Visualizar vendas efetuadas")
    print ("(6) Visualizar estoque de carros")
    print ("(7) Sair")
    print ("")
    
    sair = False
    try:
        opcao = int(input("Informe a opção desejada (x): "))
        print("")
        
        match opcao:
            case 1:
                cadastrarCarro()
            case 2:
                cadastrarCliente()
            case 3:
                opcaoAlterarDados()
            case 4:
                cadastrarVenda()
            case 5:
                visualizarVendas()
            case 6:
                visualizarCarros()
            case 7:
                print ("SAINDO DO SISTEMA...")
                print ("")
                sair = True
            case _:
                print("")
                print ("OPÇÃO INVÁLIDA!")
    except:
        print("")
        print ("OPÇÃO INVÁLIDA!")
    return sair

while iniciar() == False:
    print ("")
    print ("")
    print ("=================== REINICIANDO... ===================")
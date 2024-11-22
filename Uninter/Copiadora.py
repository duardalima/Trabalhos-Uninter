ef escolha_servico():
    while True:
        servico = input("Escolha o serviço desejado (dig/ico/ipb/fot): ").lower()
        if servico == 'dig':
            return 1.10
        elif servico == 'ico':
            return 1.00 
        elif servico == 'ipb':
            return 0.40 
        elif servico == 'fot':
            return 0.20 
        else:
            print("Opção inválida. Por favor, escolha entre dig/ico/ipb/fot.") 
def num_pagina():
    while True:
        try:
            num_paginas = int(input("Digite o número de páginas: "))
            if num_paginas >= 20000:
                print("Número de páginas inválido. Máximo permitido é 19999.") 
            elif num_paginas < 0:
                print("Número de páginas inválido. Não pode ser negativo.")
            else:
                if num_paginas < 20:
                    return num_paginas
                elif 20 <= num_paginas < 200:
                    return num_paginas * 0.85  
                elif 200 <= num_paginas < 2000:
                    return num_paginas * 0.80  
                elif 2000 <= num_paginas < 20000:
                    return num_paginas * 0.75  
        except ValueError:
            print("Valor não numérico. Por favor, digite um número válido.") 
def servico_extra():
    while True:
        try:
            extra = int(input("Escolha o serviço extra (1 - Encadernação simples, 2 - Capa dura, 0 - Nenhum): "))
            if extra == 1:
                return 15.00 
            elif extra == 2:
                return 40.00 
            elif extra == 0:
                return 0.00 
            else:
                print("Opção inválida. Por favor, escolha entre 1, 2 ou 0.")
        except ValueError:
            print("Valor não numérico. Por favor, digite um número válido.") 
print("Bem-vindo ao sistema de cobrança da copiadora da Maria!")  

custo_por_pagina = escolha_servico()  
num_paginas = num_pagina() 
valor_extra = servico_extra()

total = (custo_por_pagina * num_paginas) + valor_extra  

print(f"Pedido realizado com sucesso!")
print(f"Serviço escolhido: {custo_por_pagina:.2f} por página")
print(f"Número de páginas (com desconto se aplicável): {num_paginas:.2f}")
print(f"Custo adicional: {valor_extra:.2f}")
print(f"Total a pagar: {total:.2f} reais") 

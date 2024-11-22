print("Bem-vindo à Loja de Açaí e Cupuaçu da Maria!")  
total = 0  

while True:  
 
    sabor = input("Digite o sabor (CP para Cupuaçu ou AC para Açaí): ").upper()  
    if sabor not in ['CP', 'AC']:  
        print("Sabor inválido. Tente novamente")  
        continue  
  
    tamanho = input("Digite o tamanho (P/M/G): ").upper()  
    if tamanho not in ['P', 'M', 'G']:  
        print("Tamanho inválido. Tente novamente")  
        continue 
      
    if sabor == 'CP':  
        if tamanho == 'P':  
            preco = 9  
        elif tamanho == 'M':  
            preco = 14  
        elif tamanho == 'G':  
            preco = 18  
    elif sabor == 'AC':  
        if tamanho == 'P':  
            preco = 11  
        elif tamanho == 'M':  
            preco = 16  
        elif tamanho == 'G':  
            preco = 20  

    total += preco  
    print(f"Adicionado ao pedido: {sabor} tamanho {tamanho} - R${preco:.2f}")  
 
    mais_alguma_coisa = input("Deseja pedir mais alguma coisa? (S/N): ").upper()  
    if mais_alguma_coisa == 'N':  
        break 

print(f"Valor total do pedido: R${total:.2f}")  
print("Obrigado por comprar na loja da Maria!")  
def simula_saida_console():  
  
    print("\n--- Exigência de Saída de Console 1 de 4 ---")  
    print("Bem-vindo à Loja de Açaí e Cupuaçu da Maria!")  
   
    print("\n--- Exigência de Saída de Console 2 de 4 ---")  
    print("Digite o sabor (CP para Cupuaçu ou AC para Açaí): XX")  
    print("Sabor inválido. Tente novamente")  
    
    print("\n--- Exigência de Saída de Console 3 de 4 ---")  
    print("Digite o sabor (CP para Cupuaçu ou AC para Açaí): CP")  
    print("Digite o tamanho (P/M/G): X")  
    print("Tamanho inválido. Tente novamente")  
      
    print("\n--- Exigência de Saída de Console 4 de 4 ---")  
    print("Digite o sabor (CP para Cupuaçu ou AC para Açaí): CP")  
    print("Digite o tamanho (P/M/G): M")  
    print("Adicionado ao pedido: CP tamanho M - R$14.00")  
    print("Deseja pedir mais alguma coisa? (S/N): S")  
    print("Digite o sabor (CP para Cupuaçu ou AC para Açaí): AC")  
    print("Digite o tamanho (P/M/G): G")  
    print("Adicionado ao pedido: AC tamanho G - R$20.00")  
    print("Deseja pedir mais alguma coisa? (S/N): N")  
    print("Valor total do pedido: R$34.00")  
    print("Obrigada por comprar na loja da Maria!")

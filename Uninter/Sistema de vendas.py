# Exigência de Código 1 de 6: Mensagem de boas-vindas com o meu nome. 
print("Bem-vindo a loja da Maria Eduarda") 

# Exigência de Código 2 de 6: Input do valor unitário e da quantidade do produto. 
valor_unitario = float(input("Digite o valor unitário do produto: ")) 
quantidade = int(input("Digite a quantidade do produto: ")) 

# Cálculo do valor total sem desconto 
valor_total_sem_desconto = valor_unitario * quantidade 

# Exigência de Código 3 de 6: Implementação do desconto conforme a listagem. 
if valor_total_sem_desconto < 2500: 
 desconto = 0 # Exigência de Código 5 de 6: Uso da estrutura if 
elif 2500 <= valor_total_sem_desconto < 6000: 
 desconto = 4 # Exigência de Código 5 de 6: Uso da estrutura elif 
elif 6000 <= valor_total_sem_desconto < 10000: 
 desconto = 7 # Exigência de Código 5 de 6: Uso da estrutura elif 
else: 
 desconto = 11 # Exigência de Código 5 de 6: Uso da estrutura else 

# Cálculo do valor total com desconto 
valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto / 100) 

# Exigência de Código 4 de 6: Exibição dos valores totais 
print(f"Valor total sem desconto: R${valor_total_sem_desconto:.2f}") 
print(f"Valor total com desconto: R${valor_total_com_desconto:.2f}") 

# Exigência de Saída de Console 1 de 2: Mensagem de boas-vindas com o meu nome. 
print("Obrigada por comprar na loja da Maria") 

# Exigência de Saída de Console 2 de 2: Mensagem indicando que um pedido recebeu desconto. 
if valor_total_sem_desconto >= 2500: 
 print("Parabéns! Seu pedido recebeu um desconto.") 
else: 
 print("Seu pedido não atingiu o valor necessário para receber um desconto.")
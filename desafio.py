CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome:")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario_usuario = float(input("Digite o valor do seu salário:"))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

bonus_usuario = float(input("Digite o valor do bônus recebido:"))

# 4) Calcule o valor do bônus final

valor_final = (CONSTANTE_BONUS + salario_usuario) * bonus_usuario



# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus

print(f"Olá {nome_usuario} o seu valor de bônus é {valor_final}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
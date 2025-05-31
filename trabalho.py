

print("Bem-vindo(a) ao Guia Básico de Enchentes!")
print("Aqui você encontrará informações importantes para sua segurança.")

areas_de_risco = [ #lista usada para armazenar as areas de risco
    "Áreas próximas a rios e córregos.",
    "Regiões de encosta com risco de deslizamento.",
    "Bairros com histórico de alagamentos frequentes.",
    "Locais com sistemas de drenagem deficientes."
]

sinais_de_alerta = [ #lista usada para armazenar os sinais de alerta
    "Aumento rápido do nível da água em rios ou córregos.",
    "Água turva ou barrenta vindo de ralos ou bueiros.",
    "Barulho alto de água corrente vindo de locais inesperados.",
    "Chuva muito forte e contínua por várias horas."
]

acoes_de_emergencia = [ #lista usada para armazenar as ações de emergencia
    "Vá para um local alto e seguro imediatamente.",
    "Desligue a energia elétrica e o gás da sua casa.",
    "Não tente atravessar áreas alagadas, mesmo de carro.",
    "Mantenha-se informado(a) por rádio ou celular (se seguro).",
    "Tenha seus documentos importantes em um saco plástico."
]

contatos_de_emergencia = [ #lista usada para armazenar os contatos de emergência
    {"nome": "Bombeiros", "numero": "193"},
    {"nome": "Defesa Civil", "numero": "199"},
    {"nome": "SAMU (Ambulância)", "numero": "192"}
]
     

opcao = '' #variavel para armazenar a opção escolhida pelo usuario

while opcao != '0': #usando while para fazer um loop, com !="0" para só sair quando o usuario digitar 0
    print("\n--- MENU PRINCIPAL ---")
    print("1. Ver Áreas de Risco")
    print("2. Ver Sinais de Alerta")
    print("3. Ver Ações de Emergência")
    print("4. Ver Contatos de Emergência")
    print("0. Sair da Aplicação")

    opcao = input("Digite o número da opção desejada: ") #variavel com input para receber a opção do usuario

    if opcao == '1': #verifica se a opção é igual a 1, se for, a lista de areas de risco é mostrada
        print("\n--- ÁREAS DE RISCO DE ENCHENTE ---")
        for area in areas_de_risco:
            print(f"- {area}")
        print("----------------------------------")
        print("*Sempre observe as informações da Defesa Civil local.*")

    elif opcao == '2': #verifica se a opção é igual a 2, se for, a lista de sinais de alerta é mostrada
        print("\n--- SINAIS DE ALERTA DE ENCHENTE ---")
        for sinal in sinais_de_alerta:
            print(f"- {sinal}")
        print("----------------------------------")
        print("*Fique atento e aja rapidamente ao identificar estes sinais.*")

    elif opcao == '3': #verifica se a opção é igual a 3, se for, a lista de ações de emergencia é mostrada
        print("\n--- AÇÕES DE EMERGÊNCIA EM CASO DE ENCHENTE ---")
        for acao in acoes_de_emergencia:
            print(f"- {acao}")
        print("----------------------------------------------")
        print("*A segurança é prioridade. Não se arrisque.*")

    elif opcao == '4': #verifica se a opção é igual a 4, se for, a lista de contatos de emergencia é mostrada
        print("\n--- CONTATOS DE EMERGÊNCIA ---")
        for contato in contatos_de_emergencia:
            print(f"- {contato['nome']}: {contato['numero']}")
        print("------------------------------")
        print("*Ligue apenas em caso de emergência real.*")

    elif opcao == '0': #verifica se a opção é igual a 0, se for, o programa é encerrado.
        print("\nSaindo do Guia de Enchentes. Mantenha-se seguro(a)!")
    else: # caso o usuario não insira uma opção valida
        print("\nOpção inválida. Por favor, digite um número de 0 a 4.")
        print("Tente novamente.")
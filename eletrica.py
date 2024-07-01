# apresentacao.py

def main():
    print("### Bem-vindo à Calculadora de Projetos Elétricos ###\n")

    # Solicita ao usuário o tipo de projeto
    tipo_projeto = input("Qual tipo de projeto você deseja realizar? (iluminação / tomada): ")

    # Importa e executa o projeto escolhido
    if tipo_projeto.lower() == "iluminação":
        import iluminacao
        iluminacao.main()
    elif tipo_projeto.lower() == "tomada":
        import tomada
        tomada.main()
    else:
        print("Tipo de projeto não reconhecido. Por favor, escolha 'iluminação' ou 'tomada'.")

if __name__ == "__main__":
    main()

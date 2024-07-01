import math
import pandas as pd

class NBR5410:
    def __init__(self, lado1, lado2):
        self.lado1 = lado1  # Primeiro lado do ambiente
        self.lado2 = lado2  # Segundo lado do ambiente

    def calcular_perimetro(self):
        return 2 * (self.lado1 + self.lado2)

    def calcular_area(self):
        return self.lado1 * self.lado2

    def calcular_numero_iluminacao(self):
        # Calcula o número de pontos de iluminação de acordo com a NBR 5410
        area = self.calcular_area()
        if area <= 6:
            return 1
        else:
            num_iluminacao = 1  # Pelo menos um ponto de iluminação para os primeiros 6m²
            area_restante = area - 6
            # Adiciona 1 ponto de iluminação a cada 4m² adicionais, com potência de 60VA
            num_iluminacao += math.floor(area_restante / 4)
            return num_iluminacao

    def calcular_potencia_total_iluminacao(self):
        # Calcula a potência total da iluminação de acordo com a NBR 5410
        num_iluminacao = self.calcular_numero_iluminacao()
        potencia_total = 100 + (num_iluminacao - 1) * 60  # 100VA para o primeiro ponto, 60VA para os seguintes
        return potencia_total

def solicitar_dados_ambiente(num_ambiente):
    # Lista de opções de ambientes
    opcoes_ambiente = {
        1: "Sala",
        2: "Dormitório 1",
        3: "Dormitório 2",
        4: "Dormitório 3",
        5: "Dormitório 4",
        6: "Quarto Suíte",
        7: "Banheiro Suíte",
        8: "Banheiro Social",
        9: "Banheiro Dependência",
        10: "Quarto Dependência",
        11: "Cozinha",
        12: "Área de Serviço",
        13: "Varanda",
        14: "Varanda Suíte"
    }

    print(f"### Ambiente {num_ambiente} ###")
    print("Escolha o tipo de ambiente:")
    for key, value in opcoes_ambiente.items():
        print(f"{key}. {value}")
    
    escolha = int(input("Digite o número correspondente ao tipo de ambiente: "))
    tipo_ambiente = opcoes_ambiente.get(escolha, "Outros")

    lados = input("Informe os lados do ambiente separados por vírgula (Exemplo: 5, 4): ").split(',')
    lado1, lado2 = map(float, lados)

    nbr = NBR5410(lado1, lado2)

    # Calcula o número de pontos de iluminação e a potência total de iluminação
    num_iluminacao = nbr.calcular_numero_iluminacao()
    potencia_iluminacao = nbr.calcular_potencia_total_iluminacao()

    return tipo_ambiente, lado1, lado2, nbr.calcular_perimetro(), nbr.calcular_area(), num_iluminacao, potencia_iluminacao

def main():
    print("### Calculadora de Iluminação por Ambiente - NBR 5410 ###\n")

    # Solicita ao usuário o número de ambientes
    num_ambientes = int(input("Informe o número de ambientes: "))

    # Listas para armazenar os dados de cada ambiente
    ambientes = []
    lados1 = []
    lados2 = []
    perimetros = []
    areas = []
    num_iluminacao_list = []
    potencia_iluminacao_list = []

    # Para cada ambiente, solicita os dados e calcula o número de pontos de iluminação e potência total
    total_num_iluminacao = 0
    total_potencia_iluminacao = 0
    for i in range(1, num_ambientes + 1):
        tipo_ambiente, lado1, lado2, perimetro, area, num_iluminacao, potencia_iluminacao = solicitar_dados_ambiente(i)

        # Armazena os dados do ambiente
        ambientes.append(tipo_ambiente)
        lados1.append(lado1)
        lados2.append(lado2)
        perimetros.append(perimetro)
        areas.append(area)
        num_iluminacao_list.append(num_iluminacao)
        potencia_iluminacao_list.append(potencia_iluminacao)

        # Atualiza os totais de pontos de iluminação e potência
        total_num_iluminacao += num_iluminacao
        total_potencia_iluminacao += potencia_iluminacao

    # Adiciona os totais à lista de dados
    ambientes.append("Total")
    lados1.append("")
    lados2.append("")
    perimetros.append("")
    areas.append("")
    num_iluminacao_list.append(total_num_iluminacao)
    potencia_iluminacao_list.append(total_potencia_iluminacao)

    # Cria um DataFrame com os dados coletados
    data = {
        'Ambiente': ambientes,
        'Lado 1 (m)': lados1,
        'Lado 2 (m)': lados2,
        'Perímetro (m)': perimetros,
        'Área (m²)': areas,
        'Nº de Pontos de Iluminação': num_iluminacao_list,
        'Potência Iluminação (VA)': potencia_iluminacao_list
    }
    df = pd.DataFrame(data)

    # Exibe a tabela
    print("\n### Tabela de Dados por Ambiente ###")
    print(df)

if __name__ == "__main__":
    main()

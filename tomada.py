import math
import pandas as pd  # Importa a biblioteca pandas para trabalhar com DataFrames

class NBR5410:
    def __init__(self, perimetro, area):
        self.perimetro = perimetro  # Perímetro do ambiente
        self.area = area  # Área do ambiente

    def calcular_numero_tomadas_tug(self, tipo_ambiente):
        # Calcula o número de tomadas TUG conforme as regras da NBR 5410
        if tipo_ambiente == "Banheiro" or tipo_ambiente == "Varanda":
            return 1
        elif tipo_ambiente in ["Sala", "Dormitório 1", "Dormitório 2", "Dormitório 3", "Dormitório 4", "Quarto Suíte"]:
            num_tomadas = self.perimetro / 5
        elif tipo_ambiente in ["Cozinha", "Área de Serviço"]:
            num_tomadas = self.perimetro / 3.5
            # Limita o número de tomadas a 4
            num_tomadas = min(num_tomadas, 4)
        else:
            # Para outros ambientes, aplica regra específica baseada no perímetro
            if self.perimetro < 6:
                return 1
            else:
                num_tomadas = self.perimetro / 5
        
        # Arredonda para cima para incluir frações
        num_tomadas = math.ceil(num_tomadas)
        return num_tomadas

    def calcular_numero_tomadas_tue(self, tipo_ambiente):
        # Calcula o número de tomadas TUE para casos específicos
        if tipo_ambiente in ["Banheiro Social", "Banheiro Suíte"]:
            return 1, "Chuveiro Elétrico"
        elif tipo_ambiente == "Área de Serviço":
            return 1, "Máquina de lavar roupa"
        elif tipo_ambiente in ["Dormitório 1", "Dormitório 2", "Dormitório 3", "Dormitório 4", "Quarto Suíte"]:
            return 1, "Ar condicionado"
        elif tipo_ambiente == "Cozinha":
            return 1, "Geladeira"
        else:
            return 0, ""  # Retorna 0 tomadas TUE e uma string vazia para evitar "(para )" quando não houver tomadas TUE

    def potencia_tomada_tug(self, tipo_ambiente):
        # Retorna a potência das tomadas TUG de acordo com o tipo de ambiente
        if tipo_ambiente in ["Cozinha", "Área de Serviço"]:
            return 600
        else:
            return 100

    def potencia_tomada_tue(self, tipo_ambiente):
        # Retorna a potência das tomadas TUE de acordo com o tipo de ambiente
        if tipo_ambiente in ["Banheiro Social", "Banheiro Suíte"]:
            return 5600
        elif tipo_ambiente == "Área de Serviço":
            return 1000
        elif tipo_ambiente in ["Dormitório 1", "Dormitório 2", "Dormitório 3", "Dormitório 4", "Quarto Suíte"]:
            return 1600
        elif tipo_ambiente == "Cozinha":
            return 500
        else:
            return 0

    def calcular_potencia_total_tug(self, tipo_ambiente, num_tomadas_tug):
        # Calcula a potência total das tomadas TUG em um ambiente
        potencia_por_tomada = self.potencia_tomada_tug(tipo_ambiente)
        potencia_total = min(num_tomadas_tug, 3) * potencia_por_tomada
        # Para tomadas excedentes, adiciona 100VA para cada uma
        if num_tomadas_tug > 3:
            potencia_total += (num_tomadas_tug - 3) * 100
        return potencia_total

    def calcular_potencia_total_tue(self, tipo_ambiente, num_tomadas_tue):
        # Calcula a potência total das tomadas TUE em um ambiente
        potencia_por_tomada = self.potencia_tomada_tue(tipo_ambiente)
        return potencia_por_tomada * num_tomadas_tue

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

    nbr = NBR5410(lado1 + lado2, lado1 * lado2)
    
    return tipo_ambiente, lado1, lado2

def main():
    print("### Calculadora de Número de Tomadas por Ambiente - NBR 5410 ###\n")

    # Solicita ao usuário o número de ambientes
    num_ambientes = int(input("Informe o número de ambientes: "))

    # Listas para armazenar os dados de cada ambiente
    ambientes = []
    lados1 = []
    lados2 = []
    perimetros = []
    areas = []
    num_tomadas_tug_list = []
    potencia_tug_list = []
    num_tomadas_tue_list = []
    potencia_tue_list = []
    equipamento_tue_list = []

    # Para cada ambiente, solicita os dados e calcula o número de tomadas TUG e TUE recomendadas
    total_tug = 0
    total_tue = 0
    total_potencia_tug = 0
    total_potencia_tue = 0
    for i in range(1, num_ambientes + 1):
        tipo_ambiente, lado1, lado2 = solicitar_dados_ambiente(i)

        nbr = NBR5410(lado1 + lado2, lado1 * lado2)
        num_tomadas_tug = nbr.calcular_numero_tomadas_tug(tipo_ambiente)
        num_tomadas_tue, equipamento_tue = nbr.calcular_numero_tomadas_tue(tipo_ambiente)

        potencia_total_tug = nbr.calcular_potencia_total_tug(tipo_ambiente, num_tomadas_tug)
        potencia_total_tue = nbr.calcular_potencia_total_tue(tipo_ambiente, num_tomadas_tue)

        # Armazena os dados do ambiente
        ambientes.append(tipo_ambiente)
        lados1.append(lado1)
        lados2.append(lado2)
        perimetros.append(lado1 + lado2)
        areas.append(lado1 * lado2)
        num_tomadas_tug_list.append(num_tomadas_tug)
        potencia_tug_list.append(potencia_total_tug)
        num_tomadas_tue_list.append(num_tomadas_tue)
        potencia_tue_list.append(potencia_total_tue)
        equipamento_tue_list.append(equipamento_tue)

        # Atualiza os totais de TUG e TUE
        total_tug += num_tomadas_tug
        total_tue += num_tomadas_tue
        total_potencia_tug += potencia_total_tug
        total_potencia_tue += potencia_total_tue

    # Adiciona uma linha adicional para os totais na tabela
    ambientes.append("Total")
    lados1.append("")
    lados2.append("")
    perimetros.append("")
    areas.append("")
    num_tomadas_tug_list.append(total_tug)
    potencia_tug_list.append(total_potencia_tug)
    num_tomadas_tue_list.append(total_tue)
    potencia_tue_list.append(total_potencia_tue)
    equipamento_tue_list.append("")

    # Cria um DataFrame com os dados coletados
    data = {
        'Ambiente': ambientes,
        'Lado 1 (m)': lados1,
        'Lado 2 (m)': lados2,
        'Perímetro (m)': perimetros,
        'Área (m²)': areas,
        'Nº de Tomadas TUG': num_tomadas_tug_list,
        'Potência TUG (W)': potencia_tug_list,
        'Nº de Tomadas TUE': num_tomadas_tue_list,
        'Equipamento TUE': equipamento_tue_list,
        'Potência TUE (W)': potencia_tue_list
    }
    df = pd.DataFrame(data)

    # Exibe a tabela
    print("\n### Tabela de Dados por Ambiente ###")
    print(df)

if __name__ == "__main__":
    main()

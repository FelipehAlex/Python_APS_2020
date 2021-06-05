import coletas as ct
import math


# def funções
def ListaMaterias(mat):
    res = []
    for i in range(len(ct.material)):
        if mat in ct.material[i]:
            res.append([ct.nome[i], ct.endereco[i]])

    return res


def PontoColeta(lat, lon, mat):
    res = ['.', '.', 0]
    res[2] = 1000000000000
    for i in range(len(ct.material)):
        dist = abs(
            math.sqrt((ct.latitude[i] - lat)**2 + (ct.longitude[i] - lon)**2))
        if mat in ct.material[i] and dist < res[2]:
            res = [ct.nome[i], ct.endereco[i], dist]
    res.pop(2)
    return res


def Raio(lat, lon, raio, mat):
    res = []

    for i in range(len(ct.material)):
        dist = abs(
            math.sqrt((ct.latitude[i] - lat)**2 + (ct.longitude[i] - lon)**2))
        dist *= 111.12
        if mat in ct.material[i] and dist < raio:
            res.append([ct.nome[i], ct.endereco[i]])
    else:
        print('Nenhum ponto de coleta encontrado apartir do raio selecionado!')

    return res

# setup
# programa principal


print("Reciclagem")
print("+", "-"*60, "+")

opcao_menu_principal = 0
# Menu Principal
print("1-Informações sobre os materias reciclaveis"
      "\n2-Pontos de coleta por material"
      "\n3-A partir de sua posição, veja o local de coleta mais próximo"
      "\n4-Sair")
print("+", "-"*60, "+")

while (opcao_menu_principal != 4):
    opcao_menu_principal = int(input("Selecione uma opção: "))
    if opcao_menu_principal == 1:

        # Menu Informações
        print("Informações sobre os materiais")
        print("+", "-"*60, "+")
        print("1-Plastico" "\n2-Papel" "\n3-Metal" "\n4-Vidro" "\n5-Lixo Eletronico" "\n6-Sair")

        while (opcao_menu_principal != 6):
            opcao_menu_info = int(input("Selecione uma opção: "))
            print()

            if opcao_menu_info == 1:
                print("A reciclagem do Plastico tem seu foco na reciclagem de objetos feitos a partir de polímeros vindos do petróleo.")
                print("+", "_"*130, "+")
                print()

            elif opcao_menu_info == 2:
                print("A reciclagem do Papel é um processo que visa utilizar papéis velhos com o aproveitamento"
                      "\ndas fibras celulósicas dos papéis e cartões já utilizados, para produção de papéis novos.")
                print("+", "_"*130, "+")
                print()

            elif opcao_menu_info == 3:
                print("A reciclagem de Metal consiste no reaproveitamento do aço contido em objetos obsoletos,"
                      "\nsendo usado em vários materiais, como carros, latas, suportes de concreto, "
                      "\ntendo sua reciclagem com custos baixos o mantém facilmente reciclável.")
                print("+", "_"*130, "+")
                print()

            elif opcao_menu_info == 4:
                print("A reciclagem do Vidro é um processo aonde o vidro é reaproveitado,"
                      "\nsendo utilizado para formação de novos materiais, isso acontece através do derretimento do vidro. "
                      "\nA separação do vidro em cores pode ser necessária, dependendo da sua utilização final. "
                      "\nAs três cores principais são Verde, Marrom ou Âmbar e o Vidro Incolor.")
                print("+", "_"*130, "+")
                print()

            elif opcao_menu_info == 5:
                print("Resíduo de computadores, conhecido como Lixo Eletrônico, tem seu nome por serem equipamentos eletrônicos descartados."
                      "\nEles constituem um risco grande para o meio ambiente, por conterem metais tóxicos ou substâncias nocivas como Mercúrio,"
                      "\nChumbo, Berílio e Bário, entre outros.")
                print("+", "_"*130, "+")
                print()

            elif opcao_menu_info == 6:
                print("1-Informações sobre os materias reciclaveis"
                      "\n2-Pontos de coleta por material"
                      "\n3-A partir de sua posição, veja o local de coleta mais próximo"
                      "\n4-Sair")
                print("+", "-"*60, "+")
                print()

                opcao_menu_principal = int(input("Selecione uma opção: "))
                break
            else:
                print("Opção Invalida")

    if opcao_menu_principal == 2:
        # Menu Pontos de Coleta
        print("Pontos de coleta por material")
        print("+", "-"*60, "+")
        print()

        print("1-Plastico" "\n2-Papel" "\n3-Metal" "\n4-Vidro" "\n5-Lixo Eletronico" "\n6-Sair")
        print("+", "_"*60, "+")
        print()

        while (opcao_menu_principal != 6):
            opcao_menu_coleta = int(input("Selecione uma opção: "))
            print()

            if opcao_menu_coleta == 1:
                print(ListaMaterias('plástico'))

            elif opcao_menu_coleta == 2:
                print(ListaMaterias('papel/papelão'))

            elif opcao_menu_coleta == 3:
                print(ListaMaterias('metal'))

            elif opcao_menu_coleta == 4:
                print(ListaMaterias('vidro'))

            elif opcao_menu_coleta == 5:
                print(ListaMaterias('lixo eletronico'))

            elif opcao_menu_coleta == 6:
                print("1-Informações sobre os materias reciclaveis"
                      "\n2-Pontos de coleta por material"
                      "\n3-A partir de sua posição, veja o local de coleta mais próximo"
                      "\n4-Sair")
                print("+", "_"*60, "+")
                opcao_menu_principal = int(input("Selecione uma opção: "))
                break
            else:
                print("Opção Invalida")
    if opcao_menu_principal == 3:

        # Menu Posição
        print("Ponto de coleta por material mais próximo a partir de sua localização")
        print("+", "-"*60, "+")
        print()
        print("1-Plastico" "\n2-Papel" "\n3-Metal" "\n4-Vidro" "\n5-Lixo Eletronico" "\n6-Sair")

        while (opcao_menu_principal != 6):
            opcao_menu_posicao = int(input("Selecione uma opção: "))
            if opcao_menu_posicao == 1:
                print(Raio(float(input('Latitude: ')), float(
                    input('Logitude: ')), float(input('Raio: ')), 'plástico'))

            elif opcao_menu_posicao == 2:
                print(Raio(float(input('Latitude: ')), float(
                    input('Logitude: ')), float(input('Raio: ')), 'papel/papelão'))

            elif opcao_menu_posicao == 3:
                print(Raio(float(input('Latitude: ')), float(
                    input('Logitude: ')), float(input('Raio: ')), 'metal'))

            elif opcao_menu_posicao == 4:
                print(Raio(float(input('Latitude: ')), float(
                    input('Logitude: ')), float(input('Raio: ')), 'vidro'))

            elif opcao_menu_posicao == 5:
                print(Raio(float(input('Latitude: ')), float(
                    input('Logitude: ')), float(input('Raio: ')), 'lixo eletronico'))

            elif opcao_menu_posicao == 6:
                print("1-Informações sobre os materias reciclaveis"
                      "\n2-Pontos de coleta por material"
                      "\n3-A partir de sua posição, veja o local de coleta mais próximo"
                      "\n4-Sair")
                print()
                opcao_menu_principal = int(input("Selecione uma opção: "))
                break
            else:
                print("Opção Invalida")

    if opcao_menu_principal == 4:
        break
    else:
        print("Opção Invalida")

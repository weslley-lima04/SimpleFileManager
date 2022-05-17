"""
Versão com openpyxl. Funciona desde que os arquivos no excel sejam diretórios.

v10/01/22 3.58
"""

import openpyxl
import shutil
import os
from PySimpleGUI import popup, OneLineProgressMeter


def import_img(way_xls, source):
    # print("import_img v09/01/22 4.32 beta_version")
    # print("build by @manxell \n")
    #
    # print("Digite o caminho do excel com as cores.")
    # print("Exemplo: C:/Users/Meu Computador/Desktop/lista_cores.xlsx")
    caminho_excel = way_xls

    cores = openpyxl.load_workbook(caminho_excel)

    # print("Digite o caminho da pasta de origem das imagens:")
    fonte = source

    # print("Digite o caminho da pasta na qual as imagens serão salvas:")
    destino = f"{os.path.dirname(fonte)}/cores_separadas"

    arquivos = os.listdir(fonte)

    planilha = cores.active

    qtd_cores = len(planilha['a'])

    progresso_barra = 0
    achado = 0
    for valor in planilha['a']:
        progresso_barra += 1
        for arquivo in arquivos:
            if valor.value in arquivo:
                # print(valor.value)
                achado += 1
                shutil.copytree(f'{fonte}/{arquivo}', f'{destino}/{valor.value}/{arquivo}')

            elif valor.value not in arquivos:
                pass

        global barra
        barra = OneLineProgressMeter('Trabalhando...', progresso_barra, qtd_cores, key="bar", orientation='h', size=(20, 20))
        if not barra:
            break

    return achado, barra, qtd_cores

    # print("Recomeçar? Digite s para sim e n para não.")
    # print("Dica: limpe a pasta ou a exclua antes de reiniciar.")
    # restart = input()
    # if restart == "s":
    #     import_img(way_xls, source)

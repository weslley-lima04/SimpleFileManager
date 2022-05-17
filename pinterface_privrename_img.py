"""
renomeia uma pasta de acordo com uma coluna do excel adjacente.
funciona desde que sejam todos diretórios.

v10/01/22 3.46
"""
from PySimpleGUI import popup, OneLineProgressMeter
import openpyxl
import shutil
import os


def rename_dir(way_xls, source):
    # print("rename_img v10/01/22 3.46 beta_version")
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

    achado = 0
    progresso_barra = 0
    for cor in planilha['b']:
        progresso_barra += 1
        for arquivo in arquivos:
            linha = cor.row
            if planilha[f'a{linha}'].value in arquivo:
                achado += 1
                shutil.copytree(f'{fonte}/{arquivo}', f"{destino}/{arquivo}_{cor.value}")

        global barra
        barra = OneLineProgressMeter('Trabalhando...', progresso_barra, qtd_cores, key="bar", orientation='h',
                                     size=(20, 20))
        if not barra:
            break

    return achado, barra, qtd_cores

    # print("Recomeçar? Digite s para sim e n para não.")
    # print("Dica: limpe a pasta ou a exclua antes de reiniciar.")
    # restart = input()
    # if restart == "s":
    #     rename_img()

# rename_img()

from PySimpleGUI import *
from openpyxl import utils
from entrar_e_renomear_pastas import renomear_img
from pinterface_privimport_img import import_img
from pinterface_privrename_img import rename_dir

theme('Dark Grey 13')

layout = [[Combo(['Separar imagens de acordo com determinada cor',
                  'Renomear pastas de acordo com determinada cor'],
                 default_value="Escolha uma função...", size=(60, 10),
                 key="func", enable_events=True, bind_return_key=True)],
          [Text('Procurar excel')],
          [Input(default_text="Selecione o excel com as cores...", enable_events=True, key="xls"),
           FileBrowse(button_text="Procurar")],
          [Text('Procurar imagens')],
          [Input(default_text="Selecione a pasta de imagens...", enable_events=True, key="colors"),
           FolderBrowse(button_text="Procurar")],
          [Checkbox("Renomear imagens?", default=False, enable_events=True, key="ckbx", disabled=False)],
          [OK(key="Ok"), Cancel(key="Cancel")]]

janela = Window("Escolher arquivos", layout, margins=(20, 20))
# event, values = janela.read()

# mantém o programa aberto
while True:
    event, values = janela.read()
    if event in (WIN_CLOSED, 'Exit'):
        popup("", "Bye!")
        break

    # inicio do programa
    if values["func"] == 'Separar imagens de acordo com determinada cor':
        janela['ckbx'].update(disabled=False)
        # pegando valor do input a partir do values + key
        if event == "Ok":
            xls = values['xls']
            pasta_cores = values['colors']
            try:
                img_achada, stats_barra, qtdcor = import_img(xls, pasta_cores)
                if stats_barra:
                    popup("", f'{img_achada} arquivos copiados relativos a {qtdcor} cor(es).')
                else:
                    popup("", "Função interrompida.")
            except FileExistsError:
                popup("", "Você precisa excluir a pasta antiga primeiro!")
            except utils.exceptions.InvalidFileException:
                popup("", "Isso não parece um excel...")

            if values["ckbx"]:
                renomear_img(f"{os.path.dirname(values['colors'])}/cores_separadas")
                popup("", "Imagens renomeadas!")

    if values["func"] == 'Renomear pastas de acordo com determinada cor':
        janela['ckbx'].update(disabled=True)

        if event == "Ok":
            xls = values['xls']
            pasta_cores = values['colors']
            try:
                img_achada, stats_barra, qtdcor = rename_dir(xls, pasta_cores)
                if stats_barra:
                    popup("", f'{img_achada} arquivos renomeados de acordo com {qtdcor} cor(es).')
                else:
                    popup("", "Função interrompida.")
            except utils.exceptions.InvalidFileException:
                popup("", "Isso não parece um excel...")

    # saída do programa
    if event == "Cancel":
        popup("", "Bye!")
        break


# pesquisar: enable_events, key


janela.close()

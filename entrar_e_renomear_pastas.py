import os


# print("Digite o caminho dos arquivos")
# caminho = input()


def renomear_img(caminho):
    # pegando o caminho até a pasta final onde estão os arquivos(mas não os arquivos)
    def file_dir(way):
        filedir = []
        for raiz, diretorios, arquivos in os.walk(way):
            for arquivo in arquivos:
                caminho_arquivos = raiz
                filedir.append(caminho_arquivos)
        return filedir

    # removendo as duplicatas geradas pela lista acima
    def remov_dp(lista_alvo):
        new_list = list(dict.fromkeys(lista_alvo))
        return new_list

    pastas_dup = file_dir(caminho)
    fullpath = remov_dp(pastas_dup)

    for i in fullpath:
        path_cor = os.path.dirname(i)  # variável meramente intermediária
        cor = os.path.basename(path_cor)  # aqui pega o nome da pasta, que é uma cor
        files = os.listdir(i)  # aqui lista os arquivos dentro da pasta i
        ext = os.path.splitext(files[0])[1]  # aqui pega a extensão
        count = -1  # para os arquivos ficarem em 1, 2, 3...
        for k in files:
            count += 1
            os.rename(f"{i}/{k}", f"{i}/{cor}{count}{ext}")
            # i/k pois é o caminho total + o arquivo

import os
import zipfile


caminhoPasso2 = r'C:\Users\nando.DESKTOP-599MFJB\OneDrive\Área de Trabalho\Automatizar\2 Criar pastas OK'
caminhoPasso4 = r'C:\Users\nando.DESKTOP-599MFJB\OneDrive\Área de Trabalho\Automatizar\4 Arquivos recebidos'

def descompactar(Caminho1,Caminho2):
    if os.listdir(Caminho2) != []:
        # ***ler os arquivos da pasta criada e salvar em uma lista***

        arquivos=[arq for arq in os.listdir(Caminho1)]
        novoNome = [arq.replace("(","").replace(")","") for arq in arquivos]
        caminhoArquivo = [os.path.join(Caminho1,var) for var in arquivos]

        # ***Ler os arquivos zipados recebidos e salvar em uma lista***

        arquivozip = [arqz for arqz in os.listdir(Caminho2)]
        novoNomezip = [arqzi.split(".")[0] for arqzi in arquivozip]
        caminhoArquivozip = [os.path.join(Caminho2,va) for va in arquivozip]

        # ***Colocar o arquivo Zipado dentro da sua pasta e descompactar o arquivo***
        tem = 0
        for zip in (novoNomezip):
            if zip in novoNome:
                vai = os.path.join(caminhoArquivo[tem],zip)+'7z'
                os.rename(caminhoArquivozip[tem],vai)
                with zipfile.ZipFile(vai,'r') as zip_ref:
                    ab = [ar for ar in caminhoArquivo]
                    zip_ref.extractall(ab[tem])
                tem += 1
            else:
                print(f'Não encontrei a pasta do arquivo {zip}')
                tem += 1
    else:
        print("Pasta esta vazia")



if __name__ == '__main__':
    descompactar(caminhoPasso2, caminhoPasso4)

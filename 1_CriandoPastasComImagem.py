import pandas as pd
import os
import gspread
import shutil

caminhoImagem = r'C:\Users\nando.DESKTOP-599MFJB\OneDrive\Área de Trabalho\Automatizar\1 Imagens OK'
def CriarPasta(nome):
    #                                   Verificar se a pasta tem imagem, se não tiver, avisa e para

    nomeimagem = [var for var in os.listdir(nome)]
    if nomeimagem ==[]:
            print('Não tem imagens para trabalhar')
    else:
        #                               Variaveis com os caminho na maquina

        caminhoPasta = r'C:\Users\nando.DESKTOP-599MFJB\OneDrive\Área de Trabalho\Automatizar\2 Criar pastas OK'
        caminhoimg5e6 = r'C:\Users\nando.DESKTOP-599MFJB\OneDrive\Área de Trabalho\Automatizar\copias'
        CODE = '15IZ30KR8CH66QZkxy7P-ICHLFL5IuqBmyonpCWmoq6A'
        key = ''
        for pasta, subpasta, arquivo in os.walk(
                r'C:\Users\nando.DESKTOP-599MFJB\OneDrive\Área de Trabalho\Automatizar\Automatiza_temporario\Projeto automatizar castro'):
            for arq in arquivo:
                if 'key' in arq:
                    key = os.path.join(pasta, arq)
                    break
            break

        #                               Entra no google planilhas e salvar em um dataframe

        gc = gspread.service_account(filename=key)
        sh = gc.open_by_key(CODE)
        ws = sh.worksheet('Página1')
        PLanilhaProdutos = pd.DataFrame(ws.get_all_values()[1:], columns=ws.get_all_values()[0])
        novo_cabecalho = PLanilhaProdutos.iloc[0]
        PLanilhaProdutos.columns = novo_cabecalho
        PLanilhaProdutos = PLanilhaProdutos.drop(0)
        PLanilhaProdutos = PLanilhaProdutos.reset_index(drop=True)
        #                               Variaveis de validação

        nomePasta = [var.split('.')[0] for var in os.listdir(nome)]
        novoNomePasta = [PLanilhaProdutos[PLanilhaProdutos['Pasta/Nome do Arquivo'].str.match('.*' + arq)][
                'Nome do produto'].values[0] for arq in nomePasta]
        caminhoarquivo = [os.path.join(nome,var) for var in nomeimagem]
        todos = [os.path.join(caminhoimg5e6, var) for var in os.listdir(caminhoimg5e6)]
        ArquivoJPG5e6 = os.listdir(caminhoimg5e6)
        contar = 0
        #                               Criar nova pasta com o nome do arquivo que está no google planilhas

        os.chdir(caminhoPasta)
        for criar in nomePasta:
            nomedapasta = f'Can {criar} - {novoNomePasta[contar]}'
            os.mkdir(nomedapasta)
            os.rename(caminhoarquivo[contar],f'{caminhoPasta}/{nomedapasta}/{nomeimagem[contar]}')
            shutil.copyfile(todos[0],f'{caminhoPasta}/{nomedapasta}/{ArquivoJPG5e6[0]}')
            shutil.copyfile(todos[1], f'{caminhoPasta}/{nomedapasta}/{ArquivoJPG5e6[1]}')
            contar += 1
        print(f'{contar} Pastas criadas e renomeadas')



if __name__ == '__main__':
    CriarPasta(caminhoImagem)
    #teste()
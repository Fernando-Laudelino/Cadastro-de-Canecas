from zipfile import ZipFile                                                     # Biblioteca para zipar os arquivos
import os
import os.path
from os.path import basename                                                    # OS é a biblioteca para navegar entre as pastas
import time                                                                     # Biblioteca Time é para controlar o tempo entre uma tela e outra
from EnvioWhatsap import navegar

caminho = r'C:\Users\nando.DESKTOP-599MFJB\OneDrive\Área de Trabalho\Automatizar\2 Criar pastas OK' # o caminho da pasta para zipar os arquivos
vai = r'C:\Users\nando.DESKTOP-599MFJB\OneDrive\Área de Trabalho\Automatizar\3 zipa e enviar por whats OK'
contato = "https://web.whatsapp.com/send?phone=5511942339979&text= "            # Essa variaveu está com o endereço para ir direto ao numero desejado

def compactar(diretorio):                                                       # Crie o metodo compactar para ficar mais organizado e chamando só no final do código
    if os.listdir(diretorio)==[]:                                               # Verificar na pasta se tem alguma pasta para ser compactada
        print('Não tem pasta')                                                  # Se não tiver pasta é enviado a mensagem que não tem pasta
    else:
        for pasta, subpasta, arquivos in os.walk(diretorio):                    # Se tiver aqui separamos pasta de subpasta e arquivo com o caminho completo
            if subpasta == []:                                                  # Desse if até o else é para fazer a contagem das pastas existente e exclui arquivos
                break
            else:
                qnt = len(subpasta)
            for nomeSubpasta in subpasta:                                       # Aqui eu pego o nome da Pasta para nomear as novas pastas zipadas
                os.chdir(vai)                                                   # Vou até onde eu quero criar as novas pastas zipadas
                with ZipFile(f'{nomeSubpasta}.7z', 'w') as zip:       # Crio a pasta zipada com o mesmo nome da pasta original
                    arq = os.path.join(pasta, nomeSubpasta)                     # Aqui eu crio o caminho até a pasta onde está os arquivos
                    arq1 = os.listdir(arq)                                      # Aqui eu entro dentro da pasta onde está os arquivos para jogar na pasta zipada
                    for arq2 in arq1:                                           # Pego o nome de todos os arquivos dentro da pasta
                        arq3 = os.path.join(arq, arq2)                          # junto o caminho da pasta com o nome do arquivo
                        zip.write(arq3, basename(arq3))                         # Entro dentro da pasta zipada e colo o arquivo ou o caminho completo do arquivo
            print(f'{qnt} Pastas compactadas')                                  # E aviso a quantidade de arquivos que foram compactados


if __name__ == '__main__':                                                      # Esse metodo é para informa o programa que ele tem que começar a rodar aparti da qui
    compactar(caminho)                                                          # Função zipa os arquivos e envia para pastar enviar whatsapp
    time.sleep(1)
    print(f'{navegar(contato, vai)} arquivos enviado no Whatsapp')              # Envia os arquivos zipados por whatsapp
># Automatizar o cadastro de produtos 
>> Tenho que pegar a imagem dentro de uma drive compartilhado, salvar a imagem no meu PC criar uma pasta com o nome da imagem.<br>
Entra no site colocar a imagem na caneca e criar duas imagens e um video da caneca girando em 360 graus, pegar as 2 imagens e o video e colocar dentro da pasta nova criada, compactar e enviar para uma outra pessoa para tratar o tamanho das imagens e adicionar mais 4 imagens novoas.<br>
Vou receber o arquivo compactado com o mesmo nome, salvo a pasta compactada dentro da pasta e descompacto ela com as 6 imagens e o video, 
>---
>>## **classe** 
>>
>> ### Produto.
>>* ### nome
>>* ### caminho
>>
>> ### Pasta.
>>* ### nome
>>* ### caminho
>---
>>## **Funções** 
>>
>>### CaminhoPasta
>>###
>---
>### Ferramentas e Bibliotecas
> __Python__
>~~~Python
>import pandas as pd
>import os
>import gspread
>import shutil
>from os.path import basename                                                  
>import time                                                                    
>from EnvioWhatsap import navegar   
>from zipfile import ZipFile
>from selenium import webdriver
>from selenium.webdriver.common.by import By
>

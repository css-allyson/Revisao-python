# %%
# para manipular arquivos em python é necessário inicialmente abrir com a função open()
# e ao final fechar os arquivos com close()

file =  open("exemplo.txt","r")
# manipulação do arquivo
file.close()

# %%
#existem diferentes modos de abrir um arquivo:
# r abre arquivo somente para leitura
file =  open("exemplo.txt","r")
# w abre arquivo para modificar
file =  open("exemplo.txt","w")
# a abre arquivo para acrescentar informação
file =  open("exemplo.txt","a")

# %%
#Método read() retorna o conteúdo do arquivo como string
file = open("exemplo.txt", "r")
print(file.read())
file.close()


# %%
#Método readline() lê uma linha por vêz do arquivo
file = open("exemplo.txt", "r")
print(file.readline())
file.close()

# %%
#Para iterar por todas as linhas utilizamos o método readlines()
file = open("exemplo.txt", "r")
for linha in file.readlines():
    print(linha)
file.close()
# %%
#Outra alternativa para iterar por todas as linhas é utilizar o método readline com while:
file = open("exemplo.txt", "r")
while len(linha := file.readline()):
    print(linha)
file.close()
# %%
# Para escrever em um arquivo abrimos ele com a permissão de escrita w, depois utilizamos o método write()
file = open("exemplo.txt", "W")
file.write("Hello world!")
file.close()
# %%
# Também podemos utilizar o método writelines() para escrever várias linhas, esse método difere
# porque precisamos passar uma lista de strings
file = open("exemplo.txt", "W")
file.writelines(["Hello world!","segunda linha","Terceira linha"])
#Contudo o código gerado não pula linhas, para pular linhas precisamos incluir \n
file.writelines(["Hello world!","\n","segunda linha","\n","Terceira linha"])
file.close()

#%%
# Para gerenciar arquivos e diretórios utilizamos os módulos os e shutil
import os
import shutil

#%%
#funcionalidades básicas dos módulos
#cria pasta
os.mkdir("exemplo")
#renomeia arquivos
os.rename("old.txt","new.txt")
# remove arquivos
os.remove("unwanted.txt")
#move arquivos
shutil.move("source.txt","destination.txt")

# %%
#utilizamos a biblioteca pathlib e Path para armazenar o diretório atual do projeto
from pathlib import Path
ROOT_PATH = Path(__file__).parent
#agora podemos criar uma nova pasta no diretório atual
os.mkdir(ROOT_PATH / 'novo_diretorio')


# %%
#exceções mais comuns ao trabalhar com arquivos:
#FileNotFoundError quando o arquivo não é encontrado no diretório
#PermissionError quando ocorre uma tentativa de manipular um arquivo sem permissão adequada
#IOError erro geral na entrada ou saída
#UnicodeDecodeError lançado quando ocorre erro ao tentar decodificar um arquivo
#usando uma codificação inadequada

# %%
#Utilizando try except para tentar abrir um arquivo inexistente e levantar o erro FileNotFoundError
try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print("Arquivo inexistente")

# %%
#Também podemos capturar os detalhes da exceção

try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError as exc:
    print("Arquivo inexistente")
    print(exc)

# %%
try:
    arquivo = open(ROOT_PATH / 'novo-diretorio')
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquovo: {exc}")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")

# %%
#uma boa prática é abrir o arquivo da seguinte maneira para evitar que o arquivo não seja fechado
try:
    with open('arquivo.txt', 'r') as arquivo:
      print(arquivo.read())
except IOError as exc:
    print(f"Erro ao ler o arquivo:{exc}")

# %%
#outra boa prática é especificar a codificação no parâmetro encoding:
arquivo = open("arquivo.txt", 'r', encoding='utf-8')

# %%
#Para lidar com arquivos .csv o python conta com o módulo csv
import csv
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# %%
#Para escrever em arquivo csv podemos utilizar o método writerow()
import csv
with open("example.csv", "w",newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["nome","idade"])
    writer.writerow(["Ana","30"])
    writer.writerow(["João","22"])
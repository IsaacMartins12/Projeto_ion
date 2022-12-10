import sqlite3
import matplotlib.pyplot as pl
from PIL import Image
from glob import glob
import os

potencia = []
corrente = []
valor = []
tensao = []
tempo = []
dados_tratados = []

cnx = sqlite3.connect('projeto_ion.db')
cursor = cnx.cursor()

comando = "SELECT * FROM Registros"

dados = cursor.execute(comando)

dados_lidos = dados.fetchall()

for i in range(0,len(dados_lidos)) :
  dados_tratados.append(dados_lidos[i])

for i in range(0,len(dados_lidos)) :
  potencia.append(dados_tratados[i][0])
  tensao.append(dados_tratados[i][1])
  corrente.append(dados_tratados[i][2])
  valor.append(dados_tratados[i][3])
  tempo.append(dados_tratados[i][4])

pl.title("GRÁFICO DE RENDIMENTO")
pl.ylim(0, 2)
pl.xlim(0,tempo[len(tempo)-1])
pl.xlabel('Tempo')
pl.ylabel('Valor')
pl.plot(tempo,valor,color="red") # Responsável por colocar legenda
pl.grid(True)   
pl.savefig('valor.png')

# gera gráfico 2

pl.title("GRÁFICO DE TENSAO DA REDE")
pl.ylim(80, 140)
pl.xlim(0,tempo[len(tempo)-1])
pl.xlabel('Tempo')
pl.ylabel('Tensao')
pl.plot(tempo,tensao,color="red") # Responsável por colocar legenda
pl.grid(True)   
pl.savefig('tensao.png')

# gera gráfico 3

pl.title("GRÁFICO DE CORRENTE DA REDE")
pl.ylim(0, 1)
pl.xlim(0,tempo[len(tempo)-1])
pl.xlabel('Tempo')
pl.ylabel('Corrente')
pl.plot(tempo,corrente,color="red") # Responsável por colocar legenda
pl.grid(True)   
pl.savefig('corrente.png')

iml = []

files = glob("*.png")
# rgb.save(PDF_FILE, 'PDF', resoultion=100.0)
for f in files:
    print(f)
    print(f[:-4])
    newname = f[:-4] + ".png"
    print(newname)
    os.rename(f, newname)
files = glob("*.png")
print(files)

# rgba = Image.open(PNG_FILE)
# To avoid ValueError: cannot save mode RGBA 

rgba = Image.open(glob("*.png")[0])
rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
rgb.paste(rgba, mask=rgba.split()[3])               # paste using alpha channel as mask
for img in files:
    rgba2 = Image.open(img)
    rgb2 = Image.new('RGB', rgba2.size, (255, 255, 255))  # white background
    rgb2.paste(rgba2, mask=rgba2.split()[3])               # paste using alpha channel as mask
    iml.append(rgb2)
pdf = "ALL.pdf"

rgb.save(pdf, "PDF" ,resolution=100.0, save_all=True, append_images=iml)
# Esse código dever ser alterado de acordo com a necessidade do projeto

# Deve-se trocar os comandos de mysql pra Sqlite

# E checar a possibilidade de gerar um txt com a biblioteca Canvas sem necessariamente mandar os dados pra um BD

import serial 
import sqlite3
comport = serial.Serial('COM6', 9600)   
print ('Serial Iniciada...\n')

cnx = sqlite3.connect('projeto_ion.db')
cursor = cnx.cursor()

serialValue = str(comport.readline())

while (serialValue) :
   
  serialValue = str(comport.readline())
  dados = serialValue.split("|")
  dados_potencia = dados[0][2::]
  dados_tensao = dados[1]
  dados_corrente = dados[2]
  dados_valor = dados[3]
  dados_tempo = dados[4][0:4]
  
  comando = f'INSERT INTO Registros (Potencia,Tensao,Corrente,Valor,Tempo) VALUES ({dados_potencia},{dados_tensao},{dados_corrente},{dados_valor},{dados_tempo})'

  cursor.execute(comando)
  dados.clear()  
  cnx.commit() 

cursor.close()
cnx.close()
comport.close()
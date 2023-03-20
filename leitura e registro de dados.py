'''
Código raiz de leitura serial do arduino em python a partir deste código é possível
desenvolver códigos derivados de maiores aplicações
'''

import serial as arduino

com = str(input("Digite qual a COM"))
velSerial = int(input("Qual a Baudrate: "))
nomeArquivo = str(input("Digite o nome para o arquivo em txt: "))

porta = "COM" + com
conexao = arduino.Serial(porta, velSerial)
arquivo = open(nomeArquivo + ".txt", "a")


while True:
    leituraSerial = conexao.readline()
    print(type(leituraSerial))
    conversao_serial = leituraSerial.decode("utf-8")
    print("Arduino diz:", conversao_serial)
    with open(nomeArquivo + ".txt", "a") as arquivo: #abre o arquivo para poder escrever
        arquivo.write(conversao_serial) #escreve os dados já convertidos em Strings
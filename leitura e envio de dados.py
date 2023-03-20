'''
Código que recebe e envia comandos pela serial
'''
from numpy import complex64
import serial as arduino

porta = 'COM3'
velSerial = 9600
conexao = arduino.Serial(porta, velSerial)

opcao = "0";    #opção pré-definida

while opcao != '2':
    opcao = input("Digite 1 para ligar\nDigite 0 para desligar\nDigite 2 para sair\n")
    if opcao !=2:
        conexao.write(bytes(opcao, 'utf-8')); #b"1"
        leituraSerial = conexao.readline()
        print("Arduino diz:", leituraSerial)

conexao.close()
print("Arduino diz: off")
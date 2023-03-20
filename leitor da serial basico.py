import serial as arduino

com = str(input("Digite qual a COM"))
velSerial = int(input("Qual a Baudrate: "))

porta = "COM" + com
conexao = arduino.Serial(porta, velSerial)


while True:
    leituraSerial = conexao.readline()
    print(leituraSerial)
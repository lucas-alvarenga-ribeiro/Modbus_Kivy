from clientemodbus import ClienteMODBUS

def main():
    cliente = ClienteMODBUS('localhost', 502)
    if cliente.connect():
        addr = 100
        val = 40.5
        print(f"Escrevendo valor float {val} no seguinte endereço {addr}...")
        cliente.escreveFloat(addr, val)
        lido = cliente.lerFloat(addr)
        print(f"Valor lido: {lido}")
        cliente.close()
    else:
        print("Sem conexão")
if __name__ == '__main__':
    main()
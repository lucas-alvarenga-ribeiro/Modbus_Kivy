from clientemodbus import ClienteMODBUS

def main():
    cliente = ClienteMODBUS('localhost', 502)
    if cliente.connect():
        addr = 100
        cliente.escreveDado(1, addr, 0)
        print("Ligando bit 2 e bit 7...")
        cliente.escreveBits(addr, 1, 14)
        cliente.escreveBits(addr, 1, 3)
        bits = cliente.lerBitsHolding(addr)
        print("Estado atual dos bits:")
        for i, b in enumerate(bits):
            if b:
                print(f"Bit {i} = 1")   
        cliente.close()
    else:
        print("Sem conexão")
if __name__ == '__main__':
    main()
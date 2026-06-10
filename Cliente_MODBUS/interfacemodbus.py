from pymodbus.client import ModbusTcpClient
from time import sleep

class ClienteInterface():
    def __init__(self, cliente, scan_time=1):
        self._cliente = cliente
        self._scan_time = scan_time  

    
    def atendimento(self):
        """
        Método para atendimento do usuário
        """
        # Abre a conexão com o servidor MODBUS 
        try:
            atendimento = True
            while atendimento:
                sel = input("Deseja realizar uma leitura, escrita ou configuração? (1- Leitura | 2- Escrita | 3- Configuração | 4- Sair): ")
                
                "Adicionando float como opção de leitura"
                if sel == '1':
                    tipo = input("""Qual tipo de dado deseja ler? (1- Holding Register | 2- Coil | 3- Input Register | 4- Discrete Input | 5- Float | 6- Ler Bit): """)
                    if(tipo == '1' or tipo == '2' or tipo == '3' or tipo == '4'):
                        addr = input("Digite o endereço da tabela MODBUS: ")
                        nvezes = input("Digite o número de vezes que deseja ler: ")
                        for i in range(0, int(nvezes)):
                            print(f"Leitura {i+1}: {self._cliente.lerDado(int(tipo), int(addr))}")
                            sleep(self._scan_time)
                    elif tipo == '5':
                        addr = input("Digite o endereço da tabela MODBUS: ")
                        nvezes = input("Digite o número de vezes que deseja ler: ")
                        for i in range(0, int(nvezes)):
                            print(f"Leitura {i+1}: {self._cliente.lerFloat(int(addr))}")
                            sleep(self._scan_time)
                    elif tipo == '6':
                        addr = input("Digite o endereço da tabela MODBUS: ")
                        print(f"Leitura {1}: {self._cliente.lerBitsHolding(int(addr))}")
                elif sel == '2':
                    tipo = input("""Qual tipo de dado deseja escrever? (1- Holding Register | 2- Coil | 3- Float | 4- Bit): """)
                    if(tipo == '1' or tipo == '2'):
                        addr = input("Digite o endereço da tabela MODBUS: ")
                        valor = input("Digite o valor que deseja escrever: ")
                        ok = self._cliente.escreveDado(int(tipo), int(addr), int(valor))
                        print("Escrita realizada." if ok else "Falha na escrita.")
                    elif tipo == '3':
                        addr = input("Digite o endereço da tabela MODBUS: ")
                        valor = input("Digite o valor float que deseja escrever: ")
                        self._cliente.escreveFloat(int(addr), float(valor))
                        print("Escrita realizada.")
                    elif tipo == '4':
                        addr = input("Digite o endereço da tabela MODBUS: ")
                        posicao = input("Digite qual bit quer acessar: ")
                        bit = input("Digite o valor do bit que deseja escrever: ")
                        self._cliente.escreveBits(int(addr), int(bit), int(posicao))
                        print("Escrita realizada.")

                elif sel == '3':
                    scant = input("Digite o tempo de varredura desejado [s]: ")
                    self._scan_time = float(scant)

                elif sel == '4':
                    atendimento = False
                else:
                    print("Seleção inválida")
        except Exception as e:
            print('Erro no atendimento: ', e.args)
        finally:
            # Fecha a conexão ao sair
            self._cliente.close()


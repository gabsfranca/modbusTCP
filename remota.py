from pyModbusTCP.client import ModbusClient
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

host = "192.168.0.101"
port = 502

while True: 
    modbusClient = ModbusClient(host = host , port = port, auto_open= True)

    logging.info(f'tentando conectar: {host}:{port}')

    if modbusClient.open():
        logging.info(f'conectado: {host}:{port}')
    else:
        logging.error(f'falha ao conectar em {host}:{port}')

    valor = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
    primeiraMemoria = 0

    logging.info(f'tentando escrever o valor {valor} comecando da memoria {primeiraMemoria}')

    success = modbusClient.write_multiple_coils(primeiraMemoria, valor)

    if success:
        logging.info(f'valor {valor} escrito com sucesso')
    else:
        logging.info('falha ao escrever valor ')

    logging.info(f'tentando ler as coils a partir da {primeiraMemoria}')

    sucessoLeitura = modbusClient.read_coils(0, 10)

    if sucessoLeitura:
        logging.info(f'valor {sucessoLeitura}, lido com sucesso')
    else:
        logging.info(f'num deu p le ')

#modbusClient.close()
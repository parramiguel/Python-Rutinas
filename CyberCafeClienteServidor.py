# servidor_cybercafe.py
import socket
import threading
import json
import time
from datetime import datetime

class ServidorCyberCafe:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.clientes = {}
        self.computadoras = {
            i: {'estado': 'libre', 'cliente': None, 'tiempo_inicio': None, 'costo_total': 0}
            for i in range(1, 11)  # 10 computadoras
        }
        self.tarifa_por_minuto = 0.10  # $0.10 por minuto
        self.lock = threading.Lock()
        
    def iniciar_servidor(self):
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.socket_servidor.listen(5)
        print(f"🖥️ Servidor CyberCafe iniciado en {self.host}:{self.port}")
        
        while True:
            cliente_socket, direccion = self.socket_servidor.accept()
            print(f"📱 Nueva conexión desde {direccion}")
            threading.Thread(target=self.manejar_cliente, args=(cliente_socket,)).start()
    
    def manejar_cliente(self, cliente_socket):
        try:
            while True:
                mensaje = cliente_socket.recv(1024).decode('utf-8')
                if not mensaje:
                    break
                
                datos = json.loads(mensaje)
                respuesta = self.procesar_comando(datos)
                cliente_socket.send(json.dumps(respuesta).encode('utf-8'))
                
        except Exception as e:
            print(f"Error con cliente: {e}")
        finally:
            cliente_socket.close()
    
    def procesar_comando(self, datos):
        comando = datos.get('comando')
        
        if comando == 'obtener_estado':
            return self.obtener_estado_computadoras()
        
        elif comando == 'ocupar_computadora':
            computadora_id = datos['computadora_id']
            nombre_cliente = datos['nombre_cliente']
            return self.ocupar_computadora(computadora_id, nombre_cliente)
        
        elif comando == 'liberar_computadora':
            computadora_id = datos['computadora_id']
            return self.liberar_computadora(computadora_id)
        
        elif comando == 'calcular_costo':
            computadora_id = datos['computadora_id']
            return self.calcular_costo(computadora_id)
        
        else:
            return {'estado': 'error', 'mensaje': 'Comando no reconocido'}
    
    def obtener_estado_computadoras(self):
        with self.lock:
            estado_actual = {}
            for comp_id, info in self.computadoras.items():
                estado_actual[comp_id] = {
                    'estado': info['estado'],
                    'cliente': info['cliente'],
                    'tiempo_transcurrido': self.calcular_tiempo_transcurrido(info['tiempo_inicio']),
                    'costo_actual': info['costo_total']
                }
            return {'estado': 'ok', 'computadoras': estado_actual}
    
    def ocupar_computadora(self, computadora_id, nombre_cliente):
        with self.lock:
            if computadora_id not in self.computadoras:
                return {'estado': 'error', 'mensaje': 'Computadora no existe'}
            
            comp = self.computadoras[computadora_id]
            if comp['estado'] == 'ocupada':
                return {'estado': 'error', 'mensaje': 'Computadora ya está ocupada'}
            
            comp['estado'] = 'ocupada'
            comp['cliente'] = nombre_cliente
            comp['tiempo_inicio'] = time.time()
            comp['costo_total'] = 0
            
            return {'estado': 'ok', 'mensaje': f'Computadora {computadora_id} ocupada por {nombre_cliente}'}
    
    def liberar_computadora(self, computadora_id):
        with self.lock:
            if computadora_id not in self.computadoras:
                return {'estado': 'error', 'mensaje': 'Computadora no existe'}
            
            comp = self.computadoras[computadora_id]
            if comp['estado'] == 'libre':
                return {'estado': 'error', 'mensaje': 'Computadora ya está libre'}
            
            costo_final = self.calcular_costo_actual(computadora_id)
            nombre_cliente = comp['cliente']
            
            comp['estado'] = 'libre'
            comp['cliente'] = None
            comp['tiempo_inicio'] = None
            comp['costo_total'] = 0
            
            return {
                'estado': 'ok', 
                'mensaje': f'Computadora {computadora_id} liberada',
                'costo_final': costo_final,
                'cliente': nombre_cliente
            }
    
    def calcular_costo(self, computadora_id):
        costo = self.calcular_costo_actual(computadora_id)
        return {'estado': 'ok', 'costo_actual': costo}
    
    def calcular_costo_actual(self, computadora_id):
        comp = self.computadoras[computadora_id]
        if comp['estado'] == 'libre':
            return 0
        
        tiempo_minutos = self.calcular_tiempo_transcurrido(comp['tiempo_inicio'])
        return round(tiempo_minutos * self.tarifa_por_minuto, 2)
    
    def calcular_tiempo_transcurrido(self, tiempo_inicio):
        if tiempo_inicio is None:
            return 0
        return (time.time() - tiempo_inicio) / 60  # Convertir a minutos

if __name__ == "__main__":
    servidor = ServidorCyberCafe()
    servidor.iniciar_servidor()
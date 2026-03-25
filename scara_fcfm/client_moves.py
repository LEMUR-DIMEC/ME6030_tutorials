from client_moves_class import MoveClient
import time
# Example usage
url = 'http://192.168.1.100:5000'
move_sender = MoveClient(url)
move_sender.send_move(-357, 296, 170.0)
time.sleep(1)
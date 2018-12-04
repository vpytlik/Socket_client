import socket
import pickle
import logging


logger = logging.getLogger()
s_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
s_handler.setFormatter(formatter)
logger.addHandler(s_handler)
logger.setLevel(logging.DEBUG)

socket = socket.socket()
socket.connect(('127.0.0.1', 9091))


class FootballPlayer:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def move(self):
        x = int(input())
        y = int(input())
        dict_ = {'Name': self.name, 'x': x, 'y': y}
        # print(dict_)
        socket.send(pickle.dumps(dict_))
        logger.debug('Sending data to server')
        data = socket.recv(1024)
        socket.close()
        new_dict = pickle.loads(data)
        logger.debug('Receiving data from server')
        self.x = new_dict['x']
        self.y = new_dict['y']

    def print_(self):
        print(self.name, self.x, self.y)


def main():
    goalkeeper = FootballPlayer("Akinfeev", 0, 10)
    defender = FootballPlayer("Granat", 0, 5)
    midfielder = FootballPlayer("Cheryshev", 5, 0)
    forward = FootballPlayer("Dzyuba", 0, -5)
    defender.print_()
    defender.move()
    defender.print_()



if __name__ == "__main__":
    main()

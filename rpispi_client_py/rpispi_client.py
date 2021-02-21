import sys

from rpispi.srv import Spixfer
import rclpy
from rclpy.node import Node

class RpiSpiClientAsyc( Node ):
    
    def __init__( self ):
        super().__init__('rpi_spi_client_async')
        self.cli = self.create_client(Spixfer, 'spi')



def main():
    print('Hi from rpispi_client_py.')


if __name__ == '__main__':
    main()

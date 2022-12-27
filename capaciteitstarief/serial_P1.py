import serial.tools.list_ports
import time


class Connection:
    def __init(self):
        self.ser = None

    def find_serial(self):
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in ports:
            return port

    def serial_settings(self):
        self.ser = serial.Serial()
        self.ser.port = self.find_serial()
        self.ser.baudrate = 115200
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.xonxoff = 1
        self.ser.rtscts = 0
        self.ser.timeout = 12
        print(f"poort: {self.ser.port}")

    def open_connection(self):
        try:
            self.ser.open()
        except:
            time.sleep(1.5)
            self.serial_settings()
            self.open_connection()

    def connection_main(self):
        self.serial_settings()
        self.open_connection()
from dsmr_parser import telegram_specifications
from dsmr_parser import obis_references
from dsmr_parser.clients import SerialReader, SERIAL_SETTINGS_V5
import os

class DSMR:
    def __init__(self):
        self.all_telegrams = None

    def reader(self):
        self.all_telegrams = SerialReader(
            device='/dev/ttyUSB0',
            serial_settings=SERIAL_SETTINGS_V5,
            telegram_specification=telegram_specifications.V5)
    
    def telegram_object(self):
        for telegram in self.all_telegram.read_as_object():
            os.system('clear')
            print(telegram)

    def obis(self):
        for telegram in self.all_telegrams.read():
            # The telegram message timestamp.
            message_datetime = telegram[obis_references.P1_MESSAGE_TIMESTAMP]

            # Using the active tariff to determine the electricity being used and
            # delivered for the right tariff.
            tariff = telegram[obis_references.ELECTRICITY_ACTIVE_TARIFF]
            tariff = int(tariff.value)

            electricity_used_total \
                = telegram[obis_references.ELECTRICITY_USED_TARIFF_ALL[tariff - 1]]
            electricity_delivered_total = \
                telegram[obis_references.ELECTRICITY_DELIVERED_TARIFF_ALL[tariff - 1]]

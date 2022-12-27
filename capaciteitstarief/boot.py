#import wifi
import serial_P1
import excel
#import dsmr

if __name__ == "__main__":
    #wifi_connection = wifi.Wifi('Orange-95a56', '528sv7FC')
    #wifi_connection.wlan()

    serial_connection = serial_P1.Connection()
    serial_connection.connection_main()

    excel_file = excel.Excel()

    while True:
        #####
        # todo
        # get values from dsmr
        #######
        excel_file.excel_main(None)
        break

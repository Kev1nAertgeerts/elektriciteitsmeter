from openpyxl import load_workbook
from datetime import datetime as dt

class Excel:
    def __init__(self):
        self.path = r"C:\Users\Kevin\Dropbox\documenten\python\opleidingen\Syntra\capaciteitstarief\capaciteits_tarief.xlsx"
        self.wb = load_workbook(filename=self.path)
        self.sheet = self.wb["piekvermogen"]

    def date(self):
        nu = dt.now()
        month = nu.strftime("%m")
        year = nu.strftime("%Y")
        return [month, year]

    def piekvermogen_schrijven(self, input=list()):
        #bepalen celnummer
        date = self.date()
        cel = chr(int(date[1])-1955)+str(int(date[0])+2)

        # vorige waarde bepalen, mag niet 'None' zijn
        if self.sheet[cel].value == None:
            old_value = 0
        else:
            old_value = float(self.sheet[cel].value)

        #oud en nieuw vergelijken
        new_value = input[0]
        if float(new_value) > old_value:
            self.sheet[cel] = input[0]

        #meterstand injectie & consumptie invullen
        self.sheet["C17"] = input[1]
        self.sheet["D17"] = input[2]

        #save excel
        self.wb.save(self.path)

    def excel_main(self, dsmr_input):
        self.piekvermogen_schrijven(dsmr_input)

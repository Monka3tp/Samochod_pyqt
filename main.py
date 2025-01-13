import sys

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog

class MyForm(QDialog):

    prices = {
        'miejski': 80,
        'kompakt:': 120,
        'van': 140,
        'suv': 160
    }

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.endDate.setDate(QDate.currentDate())
        self.ui.startDate.setSelectedDate(QDate.currentDate())
        self.ui.calculateButton.clicked.connect(self.calculate)
        self.show()

    def calculate(self):
        start_date = self.ui.startDate.selectedDate()
        end_date = self.ui.endDate.date()

        #legalność dat
        if start_date.daysTo(end_date) < 0 and start_date.daysTo(QDate.currentDate()) >= 0:
            message_box = QMessageBox()
            message_box.setWindowTitle('Błąd')
            message_box.setInformativeText("Data rozpoczęcia najmu jest późniejsza niż data jego zakończenia")
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
            message_box.exec()
            return

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())
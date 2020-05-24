from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QPushButton,
    QLineEdit
)
import sys


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Qt Calculator")

        main_layout = QVBoxLayout(self)
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        main_layout.addWidget(self.display)

        button_grid = QGridLayout()
        main_layout.addLayout(button_grid)

        button_list = [
            ["C", "+/-", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "="],
        ]

        for row, character_list in enumerate(button_list):
            for col, character in enumerate(character_list):
                button = QPushButton(character)
                button.setMinimumSize(50, 50)
                button.clicked.connect(self.click_action)  #new line
                button_grid.addWidget(button, row, col)

    def click_action(self):
        button = self.sender()
        character = button.text()

        if character != "=" and character != "+/-":  # fixed line
            self.display.insert(character)

        if character == "C":
            self.clear_action()

        if character == "=":
            self.calc()

        if character == "+/-":  # new block
            self.change_sign()

    def clear_action(self):
        self.display.clear()

    def calc(self):
        expression = self.display.text()
        if "%" in expression:
            result = self.percentage()
        else:
            result = eval(expression)

        self.display.setText(str(result))

    def change_sign(self):
        expression = self.display.text()

        if expression:
            if expression[0] == "-":
                self.display.setText(expression[1:])
            else:
                self.display.setText(f"-{expression}")

    def percentage(self):
        expression = self.display.text()

        num1, num2 = expression.split("%")

        num1 = self.coerce(num1)
        num2 = self.coerce(num2)
        return num1 * (num2/100)

    @staticmethod
    def coerce(x):
        a = float(x)
        try:
            b = int(x)
        except:
            return a

        return b

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    app.exec_()
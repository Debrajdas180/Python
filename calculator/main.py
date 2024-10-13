from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def create_button(parent, text, x, y, width, height, on_click_func):
    button = QPushButton(text, parent)  # Create a button with the given text
    button.setGeometry(x, y, width, height)  # Set its position and size
    button.clicked.connect(on_click_func)  # Connect the button to the provided function
    return button


# To store input from the user
operator = ""
x = ""
y = ""
result = 0


def operation(op):
    global operator
    if x:  # Ensure there is already an operand before selecting an operator
        operator = op


def add(num):
    # Append the number to the current input
    global x, y, operator
    if operator == "":
        # If no operator is selected, we are entering the first operand
        x += str(num)
        print(x)
        result_label.setText(x)
        result_label.text
        
    else:
        # After an operator is selected, we are entering the second operand
        y += str(num)
        print(y)
        result_label.setText(y)


def calculation():
    global x, y, operator, result
    try:
        if x and y and operator:
            if operator == "+":
                result = float(x) + float(y)
            elif operator == "-":
                result = float(x) - float(y)
            elif operator == "*":
                result = float(x) * float(y)
            elif operator == "/":
                result = float(x) / float(y)
            print(result)
            result_label.setText(str(result))
    except Exception as e:
        print()


def Clear():
    global x, y, operator
    x, y, operator = "", "", ""
    result_label.setText("0")


def window():
    global result_label
    app = QApplication([])
    window = QWidget(windowTitle="Calculator")
    # create_button(window,'0',50,50,200,50,add_0)
    result_label = QLabel("0", window)
    result_label.setGeometry(50, 20, 800, 40)
    result_label.setStyleSheet("font-size: 24px;")
    create_button(window, "1", 50, 50, 200, 50, lambda: add(1))
    create_button(window, "2", 250, 50, 200, 50, lambda: add(2))
    create_button(window, "3", 450, 50, 200, 50, lambda: add(3))
    create_button(window, "4", 50, 100, 200, 50, lambda: add(4))
    create_button(window, "5", 250, 100, 200, 50, lambda: add(5))
    create_button(window, "6", 450, 100, 200, 50, lambda: add(6))
    create_button(window, "7", 50, 150, 200, 50, lambda: add(7))
    create_button(window, "8", 250, 150, 200, 50, lambda: add(8))
    create_button(window, "9", 450, 150, 200, 50, lambda: add(9))
    create_button(window, "+", 650, 50, 200, 50, lambda: operation("+"))
    create_button(window, "-", 650, 100, 200, 50, lambda: operation("-"))
    create_button(window, "*", 650, 150, 200, 50, lambda: operation("*"))
    create_button(window, "/", 650, 200, 200, 50, lambda: operation("/"))
    create_button(window, "Enter", 50, 200, 400, 50, calculation)
    create_button(window, "Clear", 450, 200, 200, 50, Clear)

    window.show()
    app.exec()


window()

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QListWidget,
    QMessageBox,
)
from PyQt5.QtGui import QIcon


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("To-Do List")
        self.setGeometry(100, 100, 300, 400)

        # Set application icon (logo)
        self.setWindowIcon(
            QIcon("D:\Repo\My_python\TO-DO\logo.png")
        )  # Replace with your logo's path

        # Layout
        layout = QVBoxLayout()

        # Input field to add tasks
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a new task...")
        layout.addWidget(self.task_input)

        # Button to add tasks
        add_button = QPushButton("Add Task", self)
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)

        # List widget to show tasks
        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)

        # Button to remove selected task
        remove_button = QPushButton("Remove Task", self)
        remove_button.clicked.connect(self.remove_task)
        layout.addWidget(remove_button)

        # Set layout
        self.setLayout(layout)

    def add_task(self):
        task = self.task_input.text()
        if task:  # Check if the task is not empty
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Please enter a task!")

    def remove_task(self):
        selected_task = self.task_list.currentRow()
        if selected_task >= 0:  # Check if a task is selected
            self.task_list.takeItem(selected_task)
        else:
            QMessageBox.warning(self, "Error", "Please select a task to remove!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())

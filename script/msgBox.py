from PyQt5.QtWidgets import QMessageBox, QPushButton

# simple message according a choice
class FreeWill(QMessageBox):
    def __init__(self, parent, message, action):
        super().__init__(parent)
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Confirmation")
        self.setText(message)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.No)
        self.action = action

    def exec_and_call_action(self):
        result = self.exec_()
        if result == QMessageBox.Yes:
            self.action()
        elif result == QMessageBox.No:
            pass

# Message to display before closing the program during a loop
class tripleChoice(QMessageBox):
    def __init__(self, parent, message, action_yes, action_no, custom_action_text, custom_action):
        super().__init__(parent)
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Loop Warning")
        self.setText(message)

        self.yes_button = self.addButton("Yes", QMessageBox.YesRole)
        self.no_button = self.addButton("No", QMessageBox.NoRole)
        self.custom_button = self.addButton(custom_action_text, QMessageBox.RejectRole)

        self.action_yes = action_yes
        self.action_no = action_no
        self.custom_action = custom_action

    def exec_and_call_actions(self):
        result = self.exec_()

        if self.clickedButton() == self.yes_button:
            self.action_yes()
            return True
        elif self.clickedButton() == self.no_button:
            self.action_no()
            return True
        elif self.clickedButton() == self.custom_button:
            self.custom_action()
            return True

        return False

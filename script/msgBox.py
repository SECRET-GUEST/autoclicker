from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QPushButton, QButtonGroup,QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


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

# Theme configuration
class ThemeSelector(QDialog):
    def __init__(self, parent=None, logger=None):
        super().__init__(parent)
        self.logger = logger

class ThemeSelector(QDialog):
    def __init__(self, parent=None, logger=None):
        super().__init__(parent)
        self.logger = logger

        self.setWindowTitle("Themes")

        # Hide context help button
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)


        self.init_ui()

    def init_ui(self):
        # Create a vertical layout for the dialog
        layout = QVBoxLayout()

        # Create a button group for the radio buttons
        self.button_group = QButtonGroup(self)

        # Add radio buttons for each theme
        for i in range(1, 6):
            # Create a horizontal layout for the theme row
            theme_layout = QHBoxLayout()

            # Add an image label for the theme preview
            image_label = QLabel(self)
            image_path = self.logger.ressource_path(f"ico/theme{i}.png")
            image_label.setPixmap(QPixmap(image_path).scaled(108, 108))
            theme_layout.addWidget(image_label)

            # Add a radio button for the theme
            radio_button = QRadioButton(self)
            self.button_group.addButton(radio_button, i)
            theme_layout.addWidget(radio_button)

            # Add the theme row layout to the dialog layout
            layout.addLayout(theme_layout)

        # Set the first radio button as checked by default
        self.button_group.button(1).setChecked(True)

        # Add an "OK" button to accept the user selection
        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

        # Set the dialog layout
        self.setLayout(layout)

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,pyqtSignal,QSize

from functools import partial

# simple message according a choice
class FreeWill(QMessageBox):
    def __init__(self, parent, message, action,logger=None):
        super().__init__(parent)
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Confirmation")
        self.setText(message)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.No)
        self.action = action
        
        self.logger = logger
        self.selected_theme = None
        
        self.setWindowIcon(QIcon(self.logger.ressource_path("assets/ico/autoclicker.png")))
    def exec_and_call_action(self):
        result = self.exec_()
        if result == QMessageBox.Yes:
            self.action()
        elif result == QMessageBox.No:
            pass



# Message to display before closing the program during a loop
class tripleChoice(QMessageBox):
    def __init__(self, parent, message, action_yes, action_no, custom_action_text, custom_action,logger=None):
        super().__init__(parent)

        self.logger = logger
        self.selected_theme = None
        
        self.setWindowIcon(QIcon(self.logger.ressource_path("assets/ico/autoclicker.png")))

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

    theme_selected = pyqtSignal(int)  # signal to refresh themes on title bar

    def __init__(self, parent=None, logger=None):
        super().__init__(parent)
        
        self.logger = logger
        self.selected_theme = None

        self.setWindowIcon(QIcon(self.logger.ressource_path("assets/ico/autoclicker.png")))

        self.setWindowTitle("Themes")

        # Hide context help button
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.init_ui()


    def on_theme_button_clicked(self, theme_id):
        self.selected_theme = theme_id
        self.theme_selected.emit(theme_id)
        self.accept()


    def init_ui(self):
        # Fisrt we make a vertical grid
        layout = QVBoxLayout()

        # Add buttons for each theme
        for i in range(1, 6):
            # Create a horizontal layout for the theme row
            theme_layout = QHBoxLayout()

            # Add an image button for the theme
            theme_button = QPushButton(self)
            image_path = self.logger.ressource_path(f"assets/ico/theme{i}.png")
            theme_button.setIcon(QIcon(image_path))
            theme_button.setIconSize(QSize(108, 108))
            theme_button.clicked.connect(partial(self.on_theme_button_clicked, i))
            theme_layout.addWidget(theme_button)

            # Add the theme row layout to the dialog layout
            layout.addLayout(theme_layout)

        # Set the dialog layout
        self.setLayout(layout)


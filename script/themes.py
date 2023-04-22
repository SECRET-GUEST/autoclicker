from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QColorDialog, QApplication

class ThemeSelector(QDialog):
    def __init__(self):
        super().__init__()

        # Create labels and color frames for each theme option
        self.button_label = QLabel("Button")
        self.button_color = QFrame()
        self.button_color.setFixedSize(20, 20)
        self.button_color.setStyleSheet("background-color: #F2E2BA;")
        self.check_box_label = QLabel("Checkbox")
        self.check_box_color = QFrame()
        self.check_box_color.setFixedSize(20, 20)
        self.check_box_color.setStyleSheet("background-color: #B0F2B4;")
        # Add more options as needed

        # Create buttons to set each theme option
        self.button_button = QPushButton("Set Button Color")
        self.check_box_button = QPushButton("Set Checkbox Color")
        # Add more buttons as needed

        # Connect each button to its respective method to set the theme
        self.button_button.clicked.connect(self.set_button_theme)
        self.check_box_button.clicked.connect(self.set_check_box_theme)
        # Add more connections as needed

        # Create layout for labels and buttons
        option_layout = QVBoxLayout()
        option_layout.addWidget(self.button_label)
        option_layout.addWidget(self.button_color)
        option_layout.addWidget(self.button_button)
        option_layout.addWidget(self.check_box_label)
        option_layout.addWidget(self.check_box_color)
        option_layout.addWidget(self.check_box_button)
        # Add more options to layout as needed

        # Create layout for buttons to apply or cancel theme changes
        button_layout = QHBoxLayout()
        self.apply_button = QPushButton("Apply")
        self.cancel_button = QPushButton("Cancel")
        self.apply_button.clicked.connect(self.apply_theme)
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.apply_button)
        button_layout.addWidget(self.cancel_button)

        # Create main layout for dialog and add sub-layouts
        main_layout = QVBoxLayout()
        main_layout.addLayout(option_layout)
        main_layout.addLayout(button_layout)

        # Set main layout for dialog
        self.setLayout(main_layout)

    def set_button_theme(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.button_color.setStyleSheet("background-color: " + color.name() + ";")

    def set_check_box_theme(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.check_box_color.setStyleSheet("background-color: " + color.name() + ";")

    def apply_theme(self):
        # Set application stylesheet based on selected colors for each theme option
        app = QApplication.instance()
        app.setStyleSheet("""
            QPushButton {
                background-color: """ + self.button_color.palette().button().color().name() + """;
                color: #023047;
                border-top-right-radius: 10px;
                border-bottom-left-radius: 10px;
                padding: 5px 10px;
            }
            
            QPushButton:hover {                background-color: """ + self.button_color.palette().button().color().lighter(120).name() + """;
            }
            
            QPushButton:pressed {
                background-color: """ + self.button_color.palette().button().color().darker(120).name() + """;
            }

            QCheckBox::indicator {
                border: 0.5px solid """ + self.check_box_color.palette().button().color().name() + """;
                border-radius: 50%; 
                width: 10px;
                height: 10px;
            }

            QCheckBox::indicator:checked {
                background-color: """ + self.check_box_color.palette().button().color().name() + """;
                border-color: """ + self.check_box_color.palette().button().color().name() + """;
            }

            QCheckBox::indicator:hover {
                border-color: """ + self.check_box_color.palette().button().color().lighter(120).name() + """;
            }

            QCheckBox::indicator:checked:hover {
                background-color: """ + self.check_box_color.palette().button().color().lighter(120).name() + """;
                border-color: """ + self.check_box_color.palette().button().color().lighter(120).name() + """;
            }
            """)

        # Close dialog box
        self.accept()

               

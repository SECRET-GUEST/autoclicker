#     |               |                                 |
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  |                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    |
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                                                        |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                       |                    |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                |                                        |
                
#                 |                     |
#  |                                |                       |                    |            |                                |                       |                    |     |                                |                       |                    |     |                                |                       |                              |                                |
#          |                               |                                         |                              |                       |                    |                           |                       |                    |                           |                       |                    |                                |                       |                    |
                
#  |         |                                   PRESENTATION                                                |                                |                    |   |                                |                    |   |                                |                    |        |                                |                    |
#                                                                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#               |                             /                 \                          |                                                                              |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
                
#       |                            A cyberpunk graphical interface for                    |                                           |               |                                           |               |                                           |                    |                                           |
                
#                          /                      |    v    |                    \
                
#               your app, you just have to import the class, you have an example of use downside      |                                |                                          |      |                                |                                          |      |                                |                                          |           |                                |  
#     |                  !      |                                   |     |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
#                               |                                   |     |                  
#                  |            |                   Anyway          !                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |
                
#             |                      |                 have                                                 |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                     |                                           |
                

#                |                                  FUN         |                        |                                         |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                                                      |
                
#                                                        =)
                
#
#                               |                      or                                       |                                                            |                    |                |                       |                    |                |                       |                    |                    |                                           |
                

#             |                              |       DIE ! ! !        |                       |                            |                |                       |                    |                |                       |                    |                    |                                           |#     |                        |                                         |                                |
                
#
#                                                    !                                       |                                |                    |  |                                |                    |  |                                |                    |       |                                |                    |
                
#     |               |                                 !
                
#                 |                                                |            |                                   |                               |                           |                               |                           |                               |                                |                               |
#          |                                  !                                     |
                
#                 |                     |                                                     |                                   |                               |     |                                   |                               |     |                                   |                               |          |                                   |                               |
#  |                          |                       |                    !
#          |                                    |                                         |     |                    |                                    | |     |                    |                                    | |     |                    |                                    |      |     |                    |                                    |
#     |                        |                                 |      |                                |                       |                    |                |                       |                    |                |                       |                    |                    |                                           |
                
#                     |                                                |      |                                   |                               |                         |                               |                         |                               |                              |                               |
#          |                                   |                               |                   |                                |                       |                    |          |                                |                       |                    |          |                                |                       |                    |               |                                                                |
              
#_ _  _ ____ ___ ____ _    _    ____ ___ _ ____ _  _
#| |\ | [__   |  |__| |    |    |__|  |  | |  | |\ |
#| | \| ___]  |  |  | |___ |___ |  |  |  | |__| | \|
        
import os,sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QFrame, QLabel, QVBoxLayout, QSizeGrip
from PyQt5.QtGui import QIcon, QPainterPath, QRegion, QPainterPath
from PyQt5.QtCore import Qt, QPoint,pyqtSignal

#___  ____ _ _ _ ____ ____    ___  _    ____ _  _ ___
#|__] |  | | | | |___ |__/    |__] |    |__| |\ |  |
#|    |__| |_|_| |___ |  \    |    |___ |  | | \|  |
                

#OPENING | https://www.youtube.com/watch?v=_85LaeTCtV8 :3


#function to make an exe file with py to exe
def ressource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # The application is frozen (compiled)
        app_path = sys._MEIPASS
    else:
        # The application is not frozen (running from source)
        app_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(app_path, relative_path)
#to make it works, you have to rename all your path with ressource_path (/path/) WHEN YOU WILL TURN THE SCRIPT TO EXE
#Example : /icon/lol.png  BECOME  ressource_path(/icon/lol.png)





#_  _ ____ _ _  _    _ _ _ _ _  _ ___  ____ _ _ _ 
#|\/| |__| | |\ |    | | | | |\ | |  \ |  | | | | 
#|  | |  | | | \|    |_|_| | | \| |__/ |__| |_|_| 
                                                 



# Class for hide the title bar ( A simple QWidget isn't working for some reasons)
class cypunkTitle1(QWidget):
    def __init__(self, parent):
        super().__init__(parent)


class cypunk1Window(QMainWindow):
    resized = pyqtSignal()

    def __init__(self, title, window_size, btn_minimize=None, btn_show=None, stylesheet_path=None):
        super().__init__()

        self.setMouseTracking(True)

        self.resizing_right = False
        self.resizing_bottom = False
        self.resizing_left = False
        self.resizing_top = False

        self.mouse_pressed = False
        self.mouse_position = QPoint()  # initialize mouse position variable

        self.mwgui(title, window_size, btn_minimize, btn_show, stylesheet_path)



    # Graphical user interface of main window
    def mwgui(self, title, window_size, btn_minimize, btn_show, stylesheet_path):
        self.title = title  # initialize window title in a variable that can be used in another page
        self.btn_minimize = ressource_path(btn_minimize) 
        self.btn_show = ressource_path(btn_show)

        # Set Layout for the title (you can add self.vlay_cypunk1.addWidget(YOUR_WIDGET) directly in other pages  )
        self.init_Vlayout()



        #Load stylesheet if available
        if stylesheet_path:
            with open(stylesheet_path, "r") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)  # set stylesheet for the window


        self.minimize_icon = QIcon(btn_minimize)
        self.show_icon = QIcon(btn_show)

        width, height = map(int, window_size.split("x"))  # parse window size from string



        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)  # set window flags
        self.setAttribute(Qt.WA_NoSystemBackground, True)  # set widget attribute for no system background
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # set widget attribute for translucent background



        self.central_widget = QFrame()  # create a central widget to let set the rgba(transparency) in your other page
        self.setMinimumSize(width, height)  # set minimum size for the window (updated line)
        self.setCentralWidget(self.central_widget)




        # create title bar widget
        self.title_bar = cypunkTitle1(self)  
        self.title_bar.setGeometry(0, 0, self.width(), 30) 

        self.hide_button = QPushButton(self.title_bar)  # create minimize button

        #Use this to minimize the window with an image
        if btn_minimize:
            self.hide_button.setIcon(QIcon(btn_minimize)) 


        self.hide_button.setGeometry(0, 5, 30, 20) 
        self.hide_button.setStyleSheet("background-color: transparent;") 
        self.hide_button.clicked.connect(self.toggle_window) 

        self.title_label = QLabel(title, self.title_bar, objectName="title")  
        self.title_label.setGeometry(28, 5, 200, 20)  
        self.title_label.setStyleSheet("background-color: transparent; padding-right: 20px;")




        # The close button inside the window
        self.close_button = QPushButton(self.title_bar)  # create close button
        self.close_button.setGeometry(width - 30 - 8, 15, 20, 20)  # Place it 8 px before the hexagonal mask
        self.close_button.setStyleSheet("QPushButton {"
                                         "background-color: #D00000;"
                                         "border: none;"
                                         "width: 20px;"
                                         "height: 10px;"
                                         "}"
                                         "QPushButton:hover {"
                                         "background-color: #DC2F02;"
                                         "}")
        self.close_button.clicked.connect(self.close_application)


        # Maximize button
        self.maximize_button = QPushButton(self.title_bar) 
        self.maximize_button.setGeometry(width - 60 - 8, 5, 20, 20) 
        self.maximize_button.setStyleSheet("QPushButton {"
                                         "background-color: #E85D04;"
                                         "border: none;"
                                         "width: 20px;"
                                         "height: 10px;"
                                         "}"
                                         "QPushButton:hover {"
                                         "background-color: #F48C06;"
                                         "}")
        self.maximize_button.clicked.connect(self.toggle_maximize)


        # Minimize button
        self.micromize_button = QPushButton(self.title_bar) 
        self.micromize_button.setGeometry(width - 90 - 8, 5, 20, 20) #Replace 60 by 90 iff you're using maximization
        self.micromize_button.setStyleSheet("QPushButton {"
                                         "background-color: #FFBA08;"
                                         "border: none;"
                                         "width: 20px;"
                                         "height: 10px;"
                                         "}"
                                         "QPushButton:hover {"
                                         "background-color: #FAA307;"
                                         "}")
        self.micromize_button.clicked.connect(self.showMinimized)




        # Add size grip
        self.size_grip = QSizeGrip(self.central_widget)
        self.size_grip.setGeometry(self.width() - 20, self.height() - 20, 20, 20)

        # Ajoutez ces lignes à la fin de la méthode mwgui
        self.resized.connect(self.update_central_widget_geometry)
        self.update_central_widget_geometry()







    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resized.emit() 

        self.size_grip.setGeometry(self.width() - 20, self.height() - 20, 20, 20)

        # move the close button widget with the window
        new_pos = self.mapToGlobal(QPoint(self.width() - 30, 5))

        # Adjust the position of the close/max/min button
        self.close_button.move(self.width() - 30 - 8, 5)
        self.maximize_button.move(self.width() - 60 - 8, 5)
        self.micromize_button.move(self.width() - 90 - 8, 5) #Replace 60 by 90 iff you're using maximization

        self.title_bar.setGeometry(0, 0, self.width(), 30)  # set geometry for title bar widget
        self.central_widget.setGeometry(0, 0, self.width(), self.height())  # update central widget geometry

        self.frameGeometry().setWidth(self.width())  # update frame geometry width
        self.frameGeometry().setHeight(self.height())  # update frame geometry height

        self.set_hexagon_shape()






    def update_central_widget_geometry(self):
        self.central_widget.setGeometry(0, 0, self.width(), self.height())






    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = True
            self.mouse_position = event.globalPos() - self.pos()

            if abs(self.width() - event.pos().x()) <= 10:
                self.resizing_right = True
            elif abs(self.height() - event.pos().y()) <= 10:
                self.resizing_bottom = True
            elif abs(event.pos().x()) <= 10:
                self.resizing_left = True
            elif abs(event.pos().y()) <= 10:
                self.resizing_top = True

            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = False
            self.resizing_right = False
            self.resizing_bottom = False
            self.resizing_left = False
            self.resizing_top = False
            self.update_cursor(event)  
            event.accept()


    def mouseMoveEvent(self, event):
        self.update_cursor(event)

        if self.mouse_pressed:
            if self.resizing_right:
                self.resize(event.pos().x(), self.height())
            elif self.resizing_bottom:
                self.resize(self.width(), event.pos().y())
            elif self.resizing_left:
                new_width = self.width() - (event.globalX() - self.pos().x())
                self.setGeometry(event.globalX(), self.pos().y(), new_width, self.height())
            elif self.resizing_top:
                new_height = self.height() - (event.globalY() - self.pos().y())
                self.setGeometry(self.pos().x(), event.globalY(), self.width(), new_height)
            else:
                self.move(event.globalPos() - self.mouse_position)
            event.accept()






    def update_cursor(self, event):
        if self.mouse_pressed:
            if abs(self.width() - event.pos().x()) <= 10 or abs(event.pos().x()) <= 10:
                self.setCursor(Qt.SizeHorCursor)
            elif abs(self.height() - event.pos().y()) <= 10:
                self.setCursor(Qt.SizeVerCursor)
            elif abs(self.height() - event.pos().y()) <= 10 or abs(event.pos().y()) <= 10:
                self.setCursor(Qt.SizeVerCursor)
            else:
                self.setCursor(Qt.ArrowCursor)
        else:
            self.setCursor(Qt.ArrowCursor)  






    def init_Vlayout(self):
        # Apply a vertical layout to the central widget
        self.vlay_cypunk1 = QVBoxLayout(self.centralWidget())
        self.vlay_cypunk1.setContentsMargins(0, 30, 0, 0)


    def Vlayout(self, widget):
        # Add the given widget to the layout
        self.vlay_cypunk1.addWidget(widget)


    def moveEvent(self, event):
        super().moveEvent(event)
        new_pos = self.mapToGlobal(QPoint(self.width() - 10, 0))
        self.set_hexagon_shape()







    def set_hexagon_shape(self):
        # create QPainterPath for a hexagon shape
        path = QPainterPath()
        path.moveTo(30, 0)
        path.lineTo(self.width() - 20, 0)
        path.lineTo(self.width(), 20)
        path.lineTo(self.width(), self.height() - 0)
        path.lineTo(self.width() - 20, self.height())
        path.lineTo(20, self.height())
        path.lineTo(0, self.height() - 20)
        path.lineTo(0, 0)
        path.closeSubpath()

        # create QRegion from hexagon shape and set it as the mask for the window
        region = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(region)




    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


    def toggle_window(self):
        if self.central_widget.isVisible():  # check if central widget is visible
            # hide central widget, title label, buttons close max min
            self.central_widget.hide()
            self.title_label.hide()
            self.close_button.hide()
            self.micromize_button.hide()
            self.maximize_button.hide()
            self.hide_button.setIcon(self.show_icon)  # set icon for minimize button to show icon

        else:
            # Show all
            self.close_button.show()
            self.central_widget.show()
            self.title_label.show()
            self.micromize_button.show()
            self.maximize_button.show()
            self.hide_button.setIcon(self.minimize_icon) 




    def close_application(self):
        os._exit(0)  # close EVERYTHING



#
##_  _ ____ ____ ____ ____ ____ ____    ___  ____ _  _ 
##|\/| |___ [__  [__  |__| | __ |___    |__] |  |  \/  
##|  | |___ ___] ___] |  | |__] |___    |__] |__| _/\_ 
#                              
#                                                     
#class Cypunk1MessageBox(QMessageBox):
#    def __init__(self,stylesheet_path=None, *args, **kwargs): # pass stylesheet as argument
#        super().__init__(*args, **kwargs)
#
#        self.mbGui(stylesheet_path)  
#
#
#    def mbGui(self,stylesheet_path):
#        #Load stylesheet if available
#        if stylesheet_path:
#            with open(stylesheet_path, "r") as file:
#                stylesheet = file.read()
#                self.setStyleSheet(stylesheet)  
#     
#     
#        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)  # set window flags
#        self.setAttribute(Qt.WA_NoSystemBackground, True)  # set widget attribute for no system background
#        self.setAttribute(Qt.WA_TranslucentBackground, True)  # set widget attribute for translucent background
#   
#
#
#    # This function is similar to the Hexagon function you saw before, but
#    # here you can also assign and use colours for the message box
#    def paintEvent(self, event):
#        # Create a QPainter object to paint on the widget
#        painter = QPainter(self)
#
#        # Set the brush color to the background color of the widget
#        painter.setBrush(self.palette().brush(QPalette.Background))
#
#        # Create a QPainterPath object to define the shape of the widget
#        path = QPainterPath()
#        path.moveTo(30, 0)
#        path.lineTo(self.width() - 20, 0)
#        path.lineTo(self.width(), 20)
#        path.lineTo(self.width(), self.height() - 0)
#        path.lineTo(self.width() - 20, self.height())
#        path.lineTo(20, self.height())
#        path.lineTo(0, self.height() - 20)
#        path.lineTo(0, 0)
#
#        # Close the subpath to complete the shape
#        path.closeSubpath()
#
#        # Draw the shape using the QPainter object
#        painter.drawPath(path)
#
#
#
#
##Functions to move the window by holding left mouse button
#    def mousePressEvent(self, event):
#        if event.button() == Qt.LeftButton:
#            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
#            event.accept()
#
#    def mouseMoveEvent(self, event):
#        if event.buttons() == Qt.LeftButton:
#            self.move(event.globalPos() - self.dragPosition)
#            event.accept()
#
#
#
#
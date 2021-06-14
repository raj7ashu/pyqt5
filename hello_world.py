import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

#Create an Instance of Application
app = QApplication(sys.argv)

#Create an instance of application's GUI
window = QWidget()
window.setWindowTitle("Mail Explode")
window.setGeometry(100, 100, 280, 80) # First two argument window position on screen. Last to for  window wdth and height.  
window.move(60, 15)

hello_msg = QLabel("<h1>Hello World</h1>",parent=window)
hello_msg.move(60, 15) # Place the msg at given coordinates

#Show your application GUI
window.show()

#Run your application's event loop (or main loop)
sys.exit(app.exec_())

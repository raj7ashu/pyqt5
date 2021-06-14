import sys
from PyQt5.QtCore import QLine
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QFormLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("QFormaLayout")

layout = QFormLayout()
layout.addRow("Name: ",QLineEdit()) # First argument is the label and 2nd arg is widget(like textedit)
layout.addRow("Age: ",QLineEdit())
layout.addRow("Jobs: ",QLineEdit())
layout.addRow("Hobbies: ",QLineEdit())

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
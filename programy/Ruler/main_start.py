import sys
from force_handler.handler import MainWindowForce
from PyQt5.QtWidgets import *

__version__ = '0.1'
__author__ = 'Karol Ziobro'

class OneToRule(QMainWindow):
    """GUI class"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ruler')
        self.setFixedSize(800,500)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self.layout = QGridLayout()
        self.skeleton()

    def skeleton(self):
        main_label = QLabel(self)
        main_label.setText('Ruler')
        main_label.move(400,7)
        button1 = QPushButton(self)
        button1.setText("Button1")
        button1.move(100,32)
        button1.clicked.connect(MainWindowForce)

def main():
    stylesheet = """OneToRule {
        background-image: url(background.png);
        background-repeat: no-repeat; 
        background-position: center;}"""
    ruler = QApplication(sys.argv)
    ruler.setStyleSheet(stylesheet)
    viev = OneToRule()
    viev.show()
    sys.exit(ruler.exec())

if __name__ == '__main__':
    main()
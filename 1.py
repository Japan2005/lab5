import sys
from PySide6.QtCore import * 
from PySide6.QtWidgets import * 
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__ (self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap(r"SEP/lab5/rabbit.png")
        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
    
        p.setPen(QColor(0, 0, 0))  
        
        p.setBrush(QColor(255, 255, 255))  

        p.drawRect(70, 150, 100, 100)

        p.setBrush(QColor(255, 0, 0)) 
        p.drawPolygon([
            QPoint(70, 150), QPoint(170, 150), QPoint(120, 100)
        ])
        
        p.setBrush(QColor(100, 50, 0))  
        p.drawRect(110, 200, 20, 50)
        
        p.setBrush(QColor(0, 255, 255))  
        p.drawRect(80, 170, 20, 20)
        p.drawRect(140, 170, 20, 20)

        p.drawPixmap(QRect(220, 140, 100, 100), self.rabbit) 


        p.end()
        
def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())

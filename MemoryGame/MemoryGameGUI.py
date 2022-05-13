import sys, random
from PyQt5.QtWidgets import *
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class Worker(QObject):
    btnStatus = pyqtSignal(bool)
    finished = pyqtSignal()
    progress = pyqtSignal(int, int, str)
    def __init__(self, flipTiles):
        super().__init__()
        self.flipTiles = flipTiles

    def run(self):
        self.btnStatus.emit(False)
        # change colors of flipped buttons
        for flipTilePos in self.flipTiles:
            # thread
            self.progress.emit(flipTilePos[0], flipTilePos[1], "background-color : yellow")
            time.sleep(1)
            self.progress.emit(flipTilePos[0], flipTilePos[1], "background-color : grey")
            time.sleep(1)
        self.btnStatus.emit(True)
        self.finished.emit()

class basicWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 600)
        self.grid_layout = QGridLayout()

        self.gridNum = 16
        
        for x in range(self.gridNum):

            for y in range(self.gridNum):
                button = QPushButton(str(self.gridNum*x + y))
                button.setStyleSheet("background-color : grey")
                button.clicked.connect(lambda _, r=x, c=y: self.btnClick(r, c))
                
                self.grid_layout.addWidget(button, x, y, 1, 1)

        self.setLayout(self.grid_layout)
        self.flipTiles = []
        self.pointer = 0
        self.gameOn = True

    def threadInitialize(self):
        self.thread = QThread()
        self.worker = Worker(self.flipTiles)
        self.worker.moveToThread(self.thread)
     
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.switch)
        self.worker.btnStatus.connect(self.disableOrEnableAllBtn)

        # final reset
        self.thread.start()

    def disableOrEnableAllBtn(self, on):
          for x in range(self.gridNum):
            for y in range(self.gridNum):
                self.grid_layout.itemAtPosition(x, y).widget().setEnabled(on)

    def addNewFlipTile(self):
        row = random.randrange(0, self.gridNum)
        col = random.randrange(0, self.gridNum)
        self.flipTiles.append([row, col])

    def btnClick(self, r, c):
        
        if self.pointer < len(self.flipTiles):
            if r == self.flipTiles[self.pointer][0] and c == self.flipTiles[self.pointer][1]:
                self.pointer += 1
            else:
                print("game over")
                sys.exit()
        if self.pointer == len(self.flipTiles):
            self.pointer = 0
            # show tiles
            self.addNewFlipTile()
            self.threadInitialize()
        
    def switch(self, r, c, color):
        self.grid_layout.itemAtPosition(r, c).widget().setStyleSheet(color)

        
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windowExample = basicWindow()
    windowExample.show()
    sys.exit(app.exec_())


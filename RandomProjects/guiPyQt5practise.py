import sys
from tkinter import Y
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGraphicsEllipseItem, QGraphicsView, \
QGraphicsScene, QGraphicsLineItem

from PyQt5.QtCore import Qt, QLine

"""
    TODO
    set center position


"""


class Vertex (QGraphicsEllipseItem):
    def __init__(self, x, y, r, color, value):

        super().__init__(0,0,r,r)

        self.r = r
        self.buffer = (2**0.5) * r  / 2

        self.value = value
        self.setPos(x + self.buffer,y+self.buffer)
        self.setBrush(color)
        self.lines = dict()


    def addLine(self, qLine):
        
        qLinePoint = qLine.getPoint(self.pos().x() + self.buffer, self.pos().y()+ self.buffer)
        print(qLinePoint)
        self.lines[qLine] = qLinePoint
        
    def movePos(self, x, y):
        self.setPos(x, y)

    def updateLinePosition(self):
        for qLine in self.lines.keys():
            
            yPos = self.pos().y()
            xPos = self.pos().x()
            if self.lines[qLine] == 1:
                qLine.setp1(xPos, yPos)
            else:
                # point 2
                qLine.setp2(xPos, yPos)


class Line(QGraphicsLineItem):
    def __init__(self, x1, y1, x2, y2, color, radius):
        # pass in x1, y1, x2, y2 to parent class

        # add the position of point1 and point2 at the top left part of circle object
        # meaning that the position is not the center of circle

        self.buffer = (2**0.5) * radius  / 2
        super().__init__(x1 + self.buffer, y1+self.buffer, x2+self.buffer, y2+self.buffer)
        # setLine takes 4 positional arguments
        self.setPen(color)

    def setp1(self, x1, y1):
        self.setLine(x1 + self.buffer, y1 + self.buffer, self.line().x2(), self.line().y2())
        
    def setp2(self, x2, y2):
        self.setLine(self.line().x1(), self.line().y1(), x2+self.buffer, y2+self.buffer)
        
    def getPoint(self, xVertex, yVertex):
        x1 = self.line().x1() + self.buffer
        x2 = self.line().x2() + self.buffer
        y1 = self.line().y1() + self.buffer
        y2 = self.line().y2() + self.buffer
        if (abs(xVertex - x1) <= abs(xVertex - x2) and abs(yVertex - y1) <= abs(yVertex - y2)):
            return 1
        return 2

class GraphicView(QGraphicsView):
    def __init__(self, graph, vertices):
        super().__init__()
        self.graph = graph
        self.vertices = vertices
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setSceneRect(0, 0, 600, 600)
        
        self.radius = 20
        self.selectedNode = None
        self.createVertexInstances()
        self.createNeighborConnections()



    def createVertexInstances(self):
        for i in range(len(self.vertices)):
            # TODO change to random color and change starting value of vertex

            # changes self.vertices list of values to list of instances
            vertexValue = self.vertices[i]
            self.vertices[i] = Vertex(i * 40, 0, self.radius, Qt.white, vertexValue)
            self.scene.addItem(self.vertices[i])
        
        
    def createNeighborConnections(self):
        for i, relationList in enumerate(self.graph):
            # create line
            vertex1 = self.vertices[i]
            for j in range(len(relationList)):
                if relationList[j] == 1:
                    vertex2 = self.vertices[j]
                    line = Line(vertex1.pos().x(), vertex1.pos().y(), vertex2.pos().x(), vertex2.pos().y(), Qt.white , self.radius)
                    vertex1.addLine(line)
                    vertex2.addLine(line)
                    self.scene.addItem(line)
    def mousePressEvent(self, e):
        for vertex in self.vertices:
            # check for math
            if (vertex.x() <= e.x() <= vertex.x() + self.radius and vertex.y() <= e.y() <= vertex.y() + self.radius):
                self.selectedNode = vertex
                break


    def mouseMoveEvent(self, e):
        if self.selectedNode:
            self.selectedNode.movePos(e.x(), e.y())
            self.selectedNode.updateLinePosition()


    def mouseReleaseEvent(self, e):
        self.selectedNode = None

graph = [
    [0,1,0,1,0,0],
    [1,0,1,0,0,0],
    [0,1,0,1,0,1],
    [1,0,1,0,1,0],
    [0,0,0,1,0,1],
    [0,0,1,0,1,0]
]
vertex = [5,7,1,10,3,5]
app = QApplication(sys.argv)
window = GraphicView(graph, vertex)
window.show()

app.exec()

import sys
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QVBoxLayout, QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets
import os
import pandas as pd
from GUI import *
from sqltest import*

class Main():

    def __init__(self):
        self.ui = Ui_MainWindow()
        self.mainWindow = QMainWindow()
        self.ui.setupUi(self.mainWindow)

        self.connect()
        self.ui.Stack.setCurrentIndex(1)


        #self.loop()
        self.studentNameClicked = None
        self.populateTree()

    def connect(self):
        self.ui.treeWidget.clicked.connect(self.onClicked)
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.actionRoom.triggered.connect(lambda: self.ui.Stack.setCurrentIndex(1))
        self.ui.actionStudent.triggered.connect(self.newStudent)

    def onClicked(self):
        itemSelected = self.ui.treeWidget.selectedItems()
        self.nameSelected = itemSelected[0].text(0)

        """if self.name in self.turmaNames:
            self.readRoom(itemSelected)
        else:
            self.readStudents(itemSelected)"""

        if itemSelected[0].parent() == None:
            self.readRoom(itemSelected)
        else:
            self.readStudents(itemSelected)

    def newStudent(self):
        self.ui.Stack.setCurrentIndex(0)
        self.name = self.ui.nameEdit.clear()
        self.age = self.ui.ageEdit.clear()
        self.job = self.ui.jobEdit.clear()
        self.interests = self.ui.interestsEdit.clear()
        self.friends = self.ui.friendsEdit.clear()
        self.notes = self.ui.studentNotes.clear()
        self.room = self.ui.studentRoomEdit.clear()

        self.newStudent = True

    def newRoom(self):
        self.ui.roomEdit.clear()
        self.ui.attributesEdit.clear()
        self.ui.notesEdit.clear()
        self.ui.dateTimeEdit.clear()

        self.newRoom = True


    def saveStudents(self):
        name = self.ui.nameEdit.text()
        age = self.ui.ageEdit.text()
        room = self.ui.studentRoomEdit.text()
        job = self.ui.jobEdit.text()
        interests = self.ui.interestsEdit.text()
        #friends = self.ui.friendsEdit.toPlainText()
        notes = self.ui.studentNotes.toPlainText()

        if self.newStudent == False:
            V = (name,age,room,job,interests,notes,self.studentNameClicked)
            print(self.studentNameClicked)
            print(V)
            updateStudent(V)

        else:
            V = (name,age,room,job,interests,notes)
            insertNewStudent(V)
        self.newStudent = False
        self.populateTree()

    def saveRoom(self):
        room = self.ui.roomEdit.text()
        attributes = self.ui.attributesEdit.toPlainText()
        notes = self.ui.notesEdit.toPlainText()
        dateTime = self.ui.dateTimeEdit.text()
        V = (room,attributes,notes,dateTime)

        if self.newRoom == False:
            updateRoom()
        else:
            insertNewRoom()

        self.newRoom = False
        self.populateTree()

    def save(self):
        if self.ui.Stack.currentIndex() == 0:
            self.saveStudents()
        else:
            self.saveRoom()


    def readStudents(self,itemSelected):
        self.ui.Stack.setCurrentIndex(0)
        nameDisplay = itemSelected[0].text(0)
        self.studentNameClicked = nameDisplay
        studentData = getSpecificStudent(nameDisplay).fetchone()

        name = studentData[1]
        age = studentData[2]
        room = studentData[3]
        job = studentData[4]
        interests = studentData[5]
        #self.friends = studentData[6]
        notes = studentData[6]

        self.ui.nameEdit.setText(str(name))
        self.ui.ageEdit.setText(age)
        self.ui.jobEdit.setText(job)
        self.ui.interestsEdit.setText(interests)
        #self.ui.friendsEdit.setText(friends)
        self.ui.studentRoomEdit.setText(room)
        self.ui.studentNotes.setText(notes)

    def readRoom(self,itemSelected):
        self.ui.Stack.setCurrentIndex(1)
        roomName = itemSelected[0].text(0)
        self.roomNameClicked = roomName
        roomData = getSpecificRoom(roomName).fetchone()

        name = roomData[1]
        time = roomData[2]
        teacher = roomData[3]
        notes = roomData[4]

        self.ui.roomEdit.setText(name)
        self.ui.dateTimeEdit.setText(time)
        self.ui.classTeacherEdit.setText(teacher)
        self.ui.notesEdit.setText(notes)


    def populateRoom(self,parent):
        for row in getStudentsFromRoom(parent.text(0)):
            item = QTreeWidgetItem()
            item.setText(0,row[1])
            parent.addChild(item)

    def populateTree(self):
        self.ui.treeWidget.clear()
        for row in list(getRoomData().fetchall()):
            #print("Room:", row[1])
            folder = QTreeWidgetItem()
            folder.setText(0,row[1])
            folder.setIcon(0, QIcon("icon2.png"));
            folder.setExpanded(True)
            self.ui.treeWidget.addTopLevelItem(folder)
            self.populateRoom(folder)
            #self.studentData.move




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.mainWindow.show()
    sys.exit(app.exec_())

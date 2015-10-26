# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created: Sat Oct 24 19:02:45 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os
lib_path = os.path.abspath('..')
sys.path.append(lib_path)
from Search import *
from heur import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PuzzleInput(QtGui.QWidget):
    def __init__(self):
	    QtGui.QWidget.__init__(self)
	    self.setupUi(self)

    def setupUi(self, PuzzleInput):
        PuzzleInput.setObjectName(_fromUtf8("PuzzleInput"))
        PuzzleInput.setEnabled(True)
        PuzzleInput.setMinimumSize(QtCore.QSize(500, 400))
        PuzzleInput.setMaximumSize(QtCore.QSize(500, 400))
        PuzzleInput.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        PuzzleInput.setWindowOpacity(1.0)
        self.verticalLayout_2 = QtGui.QVBoxLayout(PuzzleInput)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Algoritmo = QtGui.QGroupBox(PuzzleInput)
        self.Algoritmo.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Algoritmo.setObjectName(_fromUtf8("Algoritmo"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.Algoritmo)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bfsOpt = QtGui.QRadioButton(self.Algoritmo)
        self.bfsOpt.setChecked(True)
        self.bfsOpt.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.bfsOpt.setObjectName(_fromUtf8("bfsOpt"))
        self.horizontalLayout.addWidget(self.bfsOpt)
        self.aStarOpt = QtGui.QRadioButton(self.Algoritmo)
        self.aStarOpt.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.aStarOpt.setObjectName(_fromUtf8("aStarOpt"))
        self.horizontalLayout.addWidget(self.aStarOpt)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.Algoritmo)
        self.Heuristica = QtGui.QGroupBox(PuzzleInput)
        self.Heuristica.setEnabled(False)
        self.Heuristica.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Heuristica.setObjectName(_fromUtf8("Heuristica"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.Heuristica)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.dMinOpt = QtGui.QRadioButton(self.Heuristica)
        self.dMinOpt.setChecked(True)
        self.dMinOpt.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.dMinOpt.setObjectName(_fromUtf8("dMinOpt"))
        self.horizontalLayout_4.addWidget(self.dMinOpt)
        self.dManOpt = QtGui.QRadioButton(self.Heuristica)
        self.dManOpt.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.dManOpt.setObjectName(_fromUtf8("dManOpt"))
        self.horizontalLayout_4.addWidget(self.dManOpt)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.Heuristica)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(PuzzleInput)
        self.line.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        spacerItem = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.initialStateLbl = QtGui.QLabel(PuzzleInput)
        self.initialStateLbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.initialStateLbl.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.initialStateLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.initialStateLbl.setObjectName(_fromUtf8("initialStateLbl"))
        self.verticalLayout_7.addWidget(self.initialStateLbl)
        self.initialStateTable = QtGui.QTableWidget(PuzzleInput)
        self.initialStateTable.setEnabled(True)
        self.initialStateTable.setAlternatingRowColors(False)
        self.initialStateTable.setIconSize(QtCore.QSize(0, 0))
        self.initialStateTable.setRowCount(3)
        self.initialStateTable.setColumnCount(3)
        self.initialStateTable.setObjectName(_fromUtf8("initialStateTable"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.initialStateTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.initialStateTable.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.initialStateTable.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.initialStateTable.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.initialStateTable.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.initialStateTable.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.initialStateTable.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.initialStateTable.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.initialStateTable.setItem(2, 2, item)
        self.initialStateTable.horizontalHeader().setVisible(False)
        self.initialStateTable.horizontalHeader().setCascadingSectionResizes(True)
        self.initialStateTable.horizontalHeader().setDefaultSectionSize(79)
        self.initialStateTable.horizontalHeader().setMinimumSectionSize(0)
        self.initialStateTable.horizontalHeader().setSortIndicatorShown(False)
        self.initialStateTable.horizontalHeader().setStretchLastSection(True)
        self.initialStateTable.verticalHeader().setVisible(False)
        self.initialStateTable.verticalHeader().setCascadingSectionResizes(True)
        self.initialStateTable.verticalHeader().setDefaultSectionSize(58)
        self.initialStateTable.verticalHeader().setMinimumSectionSize(0)
        self.initialStateTable.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_7.addWidget(self.initialStateTable)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.finalStateLbl = QtGui.QLabel(PuzzleInput)
        self.finalStateLbl.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.finalStateLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.finalStateLbl.setObjectName(_fromUtf8("finalStateLbl"))
        self.verticalLayout_6.addWidget(self.finalStateLbl)
        self.finalStateTable = QtGui.QTableWidget(PuzzleInput)
        self.finalStateTable.setAutoFillBackground(False)
        self.finalStateTable.setIconSize(QtCore.QSize(0, 0))
        self.finalStateTable.setRowCount(3)
        self.finalStateTable.setColumnCount(3)
        self.finalStateTable.setObjectName(_fromUtf8("finalStateTable"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.finalStateTable.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.finalStateTable.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.finalStateTable.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.finalStateTable.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.finalStateTable.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.finalStateTable.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.finalStateTable.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.finalStateTable.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.finalStateTable.setItem(2, 2, item)
        self.finalStateTable.horizontalHeader().setVisible(False)
        self.finalStateTable.horizontalHeader().setDefaultSectionSize(79)
        self.finalStateTable.horizontalHeader().setStretchLastSection(True)
        self.finalStateTable.verticalHeader().setVisible(False)
        self.finalStateTable.verticalHeader().setCascadingSectionResizes(False)
        self.finalStateTable.verticalHeader().setDefaultSectionSize(58)
        self.finalStateTable.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_6.addWidget(self.finalStateTable)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.resolverBtn = QtGui.QPushButton(PuzzleInput)
        self.resolverBtn.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.resolverBtn.setObjectName(_fromUtf8("resolverBtn"))
        self.horizontalLayout_3.addWidget(self.resolverBtn)
        self.solucaoBtn = QtGui.QPushButton(PuzzleInput)
        self.solucaoBtn.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.solucaoBtn.setObjectName(_fromUtf8("solucaoBtn"))
        self.horizontalLayout_3.addWidget(self.solucaoBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(PuzzleInput)
        QtCore.QMetaObject.connectSlotsByName(PuzzleInput)

    def retranslateUi(self, PuzzleInput):
        PuzzleInput.setWindowTitle(_translate("PuzzleInput", "puzzle8", None))
        self.Algoritmo.setTitle(_translate("PuzzleInput", "Algoritmo", None))
        self.bfsOpt.setText(_translate("PuzzleInput", "Busca em Largura", None))
        self.aStarOpt.setText(_translate("PuzzleInput", "A*", None))
        self.Heuristica.setTitle(_translate("PuzzleInput", "Heurística", None))
        self.dMinOpt.setText(_translate("PuzzleInput", "Distância Mínima", None))
        self.dManOpt.setText(_translate("PuzzleInput", "Distância Manhattan", None))
        self.initialStateLbl.setText(_translate("PuzzleInput", "Estado Inicial", None))
        __sortingEnabled = self.initialStateTable.isSortingEnabled()
        self.initialStateTable.setSortingEnabled(False)
        self.initialStateTable.setSortingEnabled(__sortingEnabled)
        self.finalStateLbl.setText(_translate("PuzzleInput", "Estado Final", None))
        __sortingEnabled = self.finalStateTable.isSortingEnabled()
        self.finalStateTable.setSortingEnabled(False)
        self.finalStateTable.setSortingEnabled(__sortingEnabled)
        self.resolverBtn.setText(_translate("PuzzleInput", "Resolver", None))
        self.solucaoBtn.setText(_translate("PuzzleInput", "Ver Solução", None))


        self.resolverBtn.clicked.connect(self.checkAndSolve)

        self.aStarOpt.toggled.connect(self.activateHeur)
        self.bfsOpt.toggled.connect(self.disableHeur)

    def disableHeur (self):
    	self.Heuristica.setEnabled(False)

    def activateHeur (self):
    	self.Heuristica.setEnabled(True)

    def readFromTable(self,table):
    	r = []
    	for row in xrange(0,3):
    		c = []
	        for column in xrange(0,3):
	        	try:
	        		c.append(int(table.item(row,column).text()))
	        	except ValueError:
	        		if (table.item(row,column).text() == ''):
	        			c.append(0)
    		r.append(c)
    	return r

    def checkState(self,state):
    	stateflat = [item for sublist in state for item in sublist]
    	stateflat.sort()
    	for a,b in enumerate(stateflat):
    		if (a!=b):
    			return False
    	return True

    def findEmpty(self, state):
    	for i,x in enumerate(state):
    		for j,y in enumerate(x):
    			if (y == 0):
    				return (i,j)


    def checkAndSolve(self):
    	a = self.readFromTable(self.initialStateTable)
        b =  self.readFromTable(self.finalStateTable)

        if (self.checkState(a) and self.checkState(b)):
        	if self.bfsOpt.isChecked():
        		bfs = BFSearch(State(a,self.findEmpty(a)),State(b,self.findEmpty(b)))
        		l = bfs.runSearch()
        		for i in l:
        			i.printState()
        		print len(l)
        	elif self.aStarOpt.isChecked():
        		l = []
        		if self.dMinOpt.isChecked():
        			astar = AStarSearch(State(a,self.findEmpty(a)),State(b,self.findEmpty(b)),heur_min)
        			l = astar.runSearch()
        		elif self.dManOpt.isChecked():
        			astar = AStarSearch(State(a,self.findEmpty(a)),State(b,self.findEmpty(b)),heur_man)
        			l = astar.runSearch()
        		for i in l:
        			i.printState()
        		print len(l)

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Ui_PuzzleInput()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
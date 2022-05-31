

from new1 import Ui_MainWindow as createTeam
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
#from Score import Ui_ScoreWindow


class Ui_MainWindow(object):
    conScore = sqlite3.connect('game.db')
    curScore = conScore.cursor()
    bat = bow = all = wk = a = 0
    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = createTeam()
        self.ui.setupUi(self.window)
       
       
        self.window.show()
        
    #def create(self):
        #team_name = self.your_plugin_dlg.ui.yourLineEdit.text()
     #   team_name = self.lineEdit.text()
      #  print(team_name)
       # return team_name    
    def openWindow(self):
        from evaluatescore import Ui_Dialog
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
            #print("effieh")
        ret=Dialog.exec()
            
        """self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ScoreWindow()
        self.ui.setupUi(self.window)
        self.window.show()"""


    def setWindow(self):
        self.Batsman_2.setEnabled(True)
        self.Bowlers_2.setEnabled(True)
        self.Allrounder_3.setEnabled(True)
        self.Wicketkeeper.setEnabled(True)
        self.Batsman_2.setCheckable(True)
        self.Bowlers_2.setCheckable(True)
        self.Allrounder_3.setCheckable(True)
        self.Wicketkeeper.setCheckable(True)

        self.Batcount.setText('0')
        self.Bowlcount.setText('0')
        self.Alrcount.setText('0')
        self.Wkcount.setText('0')
        self.playerscount.setText('1000')
        self.name.setText('0')
       
        
       
        #self.label_3.setText(self.create)
        #print(teamName)
        #self.label_3.text()
      

    def radio1(self):
        
        f= open("guru99.txt",'r')
        tean_name=f.read()
        self.label_3.setText(tean_name)
        f.close()
        cur=self.curScore.execute("Select player from stats where ctg = 'batsman';")
        for row in cur:
            selected=[]
            for i in range(self.listWidget.count()):
                selected.append(self.listWidget.item(i).text())
            if row[0] not in selected:self.listWidget_2.addItem(row[0])
            


    def radio2(self):
        f= open("guru99.txt",'r')
        tean_name=f.read()
        self.label_3.setText(tean_name)
        f.close()
        cur=self.curScore.execute("Select player from stats where ctg = 'bowler';")
        for row in cur:
            selected=[]
            for i in range(self.listWidget.count()):
                selected.append(self.listWidget.item(i).text())
            if row[0] not in selected:self.listWidget_2.addItem(row[0])
       

    def radio3(self):
        
        f= open("guru99.txt",'r')
        tean_name=f.read()
        self.label_3.setText(tean_name)
        f.close()
        cur=self.curScore.execute("Select player from stats where ctg = 'all rounder';")
        for row in cur:
            selected=[]
            for i in range(self.listWidget.count()):
                selected.append(self.listWidget.item(i).text())
            if row[0] not in selected:self.listWidget_2.addItem(row[0])
            

    def radio4(self):
        f= open("guru99.txt",'r')
        tean_name=f.read()
        self.label_3.setText(tean_name)
        f.close()
        cur=self.curScore.execute("Select player from stats where ctg = 'wicket keeper';")
        for row in cur:
            selected=[]
            for i in range(self.listWidget.count()):
                selected.append(self.listWidget.item(i).text())
           # print(selected)
            if row[0] not in selected:self.listWidget_2.addItem(row[0])
    def showdlg(self,msg):
        #print("ecb")
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Dream Team selector")
        ret=Dialog.exec()
            
        

    def removelist1(self, item):
        try:
            pl = item.text()
            self.curScore.execute("select value from stats where player ='" + pl + "';")
            vl = int(self.curScore.fetchone()[0])
            if int(self.name.text())+vl < 1000:
                self.curScore.execute("select ctg from stats where player ='" + pl + "';")
                ctg = self.curScore.fetchone()[0]
                if ctg == 'batsman':
                    self.bat = self.bat + 1
                    self.Batcount.setText(str(self.bat))
                elif ctg == 'bowler':
                    self.bow = self.bow + 1
                    self.Bowlcount.setText(str(self.bow))
                elif ctg == 'all rounder':
                    self.all = self.all + 1
                    self.Alrcount.setText(str(self.all))
                elif ctg == 'wicket keeper'and self.wk < 1:
                    self.wk = self.wk + 1
                    self.Wkcount.setText(str(self.wk))
                elif ctg == 'wicket keeper' :
                    self.showdlg("Eror!: Can't Select More Than One Wicket Keeper")
                    return
                elif ((self.bat+self.bow+self.all+self.wk)>12) :
                    self.showdlg("Eror!: Can't Select More Than 11 players")
                    return
                self.listWidget_2.takeItem(self.listWidget_2.row(item))
                leftvl = str(int(self.name.text()) + vl)
                rightvl = str(int(self.playerscount.text())-vl)
                self.playerscount.setText(rightvl)
                self.name.setText(leftvl)
                self.a=leftvl
                self.listWidget.addItem(item.text())
            else:
                self.showdlg("Not Enough Points!")
        except Exception as e:
            print(e)


    def removelist2(self, item):
        try:
            pl = item.text()
            self.curScore.execute("select ctg from stats where player ='" + pl + "';")
            ctg = self.curScore.fetchone()[0]
            if ctg == 'batsman':
                self.bat = self.bat - 1
                self.Batcount.setText(str(self.bat))
            elif ctg == 'bowler':
                self.bow = self.bow - 1
                self.Bowlcount.setText(str(self.bow))
            elif ctg == 'all rounder':
                self.all = self.all - 1
                self.Alrcount.setText(str(self.all))
            elif ctg == 'wicket keeper' and self.wk < 1:
                self.wk = self.wk - 1
                self.Wkcount.setText(str(self.wk))
            self.listWidget.takeItem(self.listWidget.row(item))
            self.curScore.execute("select value from stats where player ='"+pl+"';")
            vl = int(self.curScore.fetchone()[0])
            leftvl = str(int(self.name.text()) - vl)
            rightvl = str(int(self.playerscount.text()) + vl)
            self.playerscount.setText(rightvl)
            self.name.setText(leftvl)
            self.a=leftvl
            self.listWidget_2.addItem(item.text())
        except Exception as e:
            print(e)


    def saveteam(self,nm,ply,val):
        if self.bat+self.bow+self.all+self.wk!=11:
            self.showdlg("Insufficient players")
            return
        try:
        #print("frbfj")
            sql="INSERT INTO teams (name,players,value) VALUES ('"+nm+"','"+ply+"','"+str(val)+"');"
        #print("f3f4")
        
            #print("bjr")
            cur=self.curScore.execute(sql)
            #print("dehe")
            self.showdlg("Team Saved Succesfully")
            self.conScore.commit()
        except:
            self.showdlg("Error in Operation")
            self.conScore.rollback()   
       

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 786)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1021, 91))
        self.frame.setStyleSheet("QFrame { \n"
"   border: 5px solid Cyan\n"
"} ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 1011, 95))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 20, 0, 20)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Batsman = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Batsman.setFont(font)
        self.Batsman.setIndent(1)
        self.Batsman.setObjectName("Batsman")
        self.horizontalLayout.addWidget(self.Batsman)
        self.Batcount = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Batcount.setFont(font)
        self.Batcount.setObjectName("Batcount")
        self.horizontalLayout.addWidget(self.Batcount)
        self.Bowlers = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Bowlers.setFont(font)
        self.Bowlers.setObjectName("Bowlers")
        self.horizontalLayout.addWidget(self.Bowlers)
        self.Bowlcount = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Bowlcount.setFont(font)
        self.Bowlcount.setIndent(10)
        self.Bowlcount.setObjectName("Bowlcount")
        self.horizontalLayout.addWidget(self.Bowlcount)
        self.Allrounder = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Allrounder.setFont(font)
        self.Allrounder.setObjectName("Allrounder")
        self.horizontalLayout.addWidget(self.Allrounder)
        self.Alrcount = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Alrcount.setFont(font)
        self.Alrcount.setIndent(10)
        self.Alrcount.setObjectName("Alrcount")
        self.horizontalLayout.addWidget(self.Alrcount)
        self.Wicketkeeepr = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Wicketkeeepr.setFont(font)
        self.Wicketkeeepr.setObjectName("Wicketkeeepr")
        self.horizontalLayout.addWidget(self.Wicketkeeepr)
        self.Wkcount = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Wkcount.setFont(font)
        self.Wkcount.setIndent(10)
        self.Wkcount.setObjectName("Wkcount")
        self.horizontalLayout.addWidget(self.Wkcount)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(17, 110, 1011, 91))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Totalplayers = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Totalplayers.setFont(font)
        self.Totalplayers.setIndent(30)
        self.Totalplayers.setObjectName("Totalplayers")
        self.horizontalLayout_5.addWidget(self.Totalplayers)
        self.playerscount = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.playerscount.setFont(font)
        self.playerscount.setIndent(-10)
        self.playerscount.setObjectName("playerscount")
        self.horizontalLayout_5.addWidget(self.playerscount)
        self.TeamName = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.TeamName.setFont(font)
        self.TeamName.setIndent(100)
        self.TeamName.setObjectName("TeamName")
        self.horizontalLayout_5.addWidget(self.TeamName)
        self.name = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setIndent(60)
        self.name.setObjectName("name")
        self.horizontalLayout_5.addWidget(self.name)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(16, 220, 1021, 361))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_4.setContentsMargins(0, 20, -1, 20)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Batsman_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Batsman_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Batsman_2.setFont(font)
        self.Batsman_2.setTabletTracking(False)
        self.Batsman_2.setAcceptDrops(False)
        self.Batsman_2.setToolTipDuration(20)
        self.Batsman_2.setStyleSheet("Batmans")
        self.Batsman_2.setObjectName("Batsman_2")
        self.horizontalLayout_4.addWidget(self.Batsman_2)
        self.Bowlers_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Bowlers_2.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Bowlers_2.setFont(font)
        self.Bowlers_2.setObjectName("Bowlers_2")
        self.horizontalLayout_4.addWidget(self.Bowlers_2)
        self.Allrounder_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Allrounder_3.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Allrounder_3.setFont(font)
        self.Allrounder_3.setChecked(False)
        self.Allrounder_3.setObjectName("Allrounder_3")
        self.horizontalLayout_4.addWidget(self.Allrounder_3)
        self.Wicketkeeper = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.Wicketkeeper.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Wicketkeeper.setFont(font)
        self.Wicketkeeper.setObjectName("Wicketkeeper")
        self.horizontalLayout_4.addWidget(self.Wicketkeeper)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 130, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(160, 610, 701, 22))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(100, 100, 190, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 26))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Team = QtWidgets.QAction(MainWindow)
        self.actionNew_Team.setObjectName("actionNew_Team")
        self.actionOpen_Team = QtWidgets.QAction(MainWindow)
        self.actionOpen_Team.setObjectName("actionOpen_Team")
        self.actionsave_Team = QtWidgets.QAction(MainWindow)
        self.actionsave_Team.setObjectName("actionsave_Team")
        self.actionEvaluate_Team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_Team.setObjectName("actionEvaluate_Team")
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        self.Batsman_2.toggled['bool'].connect(self.listWidget_2.clear)
        self.Bowlers_2.toggled['bool'].connect(self.listWidget_2.clear)
        self.Allrounder_3.toggled['bool'].connect(self.listWidget_2.clear)
        self.Wicketkeeper.toggled['bool'].connect(self.listWidget_2.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menu)
        
        self.Batsman_2.toggled.connect(self.radio1)
        self.Bowlers_2.toggled.connect(self.radio2)
        self.Allrounder_3.toggled.connect(self.radio3)
        self.Wicketkeeper.toggled.connect(self.radio4)
        self.listWidget_2.itemDoubleClicked.connect(self.removelist1)
        self.listWidget.itemDoubleClicked.connect(self.removelist2)
        

       

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Batsman.setText(_translate("MainWindow", "Batsman(Bat)"))
        self.Batcount.setText(_translate("MainWindow", "##"))
        self.Bowlers.setText(_translate("MainWindow", "Bowlers (Bowl)"))
        self.Bowlcount.setText(_translate("MainWindow", "##"))
        self.Allrounder.setText(_translate("MainWindow", "Allrounder (ALR)"))
        self.Alrcount.setText(_translate("MainWindow", "##"))
        self.Wicketkeeepr.setText(_translate("MainWindow", "WicketKeeper(WK)"))
        self.Wkcount.setText(_translate("MainWindow", "##"))
        self.Totalplayers.setText(_translate("MainWindow", "Points Available: "))
        self.playerscount.setText(_translate("MainWindow", "1000"))
        self.TeamName.setText(_translate("MainWindow", "Points Used :"))
        self.name.setText(_translate("MainWindow", "00"))
        self.Batsman_2.setText(_translate("MainWindow", "Batsman"))
        self.Bowlers_2.setText(_translate("MainWindow", "Bowlers"))
        self.Allrounder_3.setText(_translate("MainWindow", "AllRounder"))
        self.Wicketkeeper.setText(_translate("MainWindow", "WicketKeeper"))
        self.label_2.setText(_translate("MainWindow", "Team    name"))
        self.label_3.setText(_translate("MainWindow", "##"))
        self.label.setText(_translate("MainWindow", "your Selection"))
        self.label_6.setText(_translate("MainWindow", "Available Players"))
        self.label_7.setText(_translate("MainWindow", "Selected Players"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_Team.setText(_translate("MainWindow", "New Team"))
        self.actionOpen_Team.setText(_translate("MainWindow", "Open Team"))
        self.actionsave_Team.setText(_translate("MainWindow", "save Team"))
        self.actionEvaluate_Team.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        
    def show(self):
        #print("vvrv")
        self.Batcount.setText(str(self.bat))
        self.Bowlcount.setText(str(self.bwl))
        self.Wkcount.setText(str(self.wk))
        self.Alrcount.setText(str(self.ar))
        #print("rrrr")
        #self.playerscount.setText(self.avl)
        #self.name.setText(self.used)
        #print("efef")
    
    def openTeam(self):
       
       
        sql="select name from teams;"
       
        cur=self.curScore.execute(sql)
        
        teams=[]
        #print("rrr")
        #cur=mycur.fetchall()
        for row in cur:
            teams.append(row[0])
        
        team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Dream","Choose A Team",teams,0,False)
        if ok and team:
            self.label_3.setText(team)
        
        sql1="SELECT players,value from teams where name='"+team+"';"
        cur=self.curScore.execute(sql1)
        row=cur.fetchone()
        #print("ooo")
        selected=row[0].split(',')
        #print(selected)
        self.listWidget.addItems(selected)
        a=str(row[1])

        self.name.setText(a)
    
        b=(1000-row[1])
        self.playerscount.setText(str(b))
    
        count=self.listWidget.count()

        ##iterate to count no. of specific players

        for i in range(count-1):
            ply=self.listWidget.item(i).text()
            #print(ply)
            sql="select ctg from stats where player='"+ply+"';"
            
            cur=self.curScore.execute(sql)
            
            row=cur.fetchone()
            #print(row)
            ctgr=row[0]
            #print("ej")
            if ctgr=="batsman":
                self.bat+=1
                self.Batcount.setText(str(self.bat))
            if ctgr == 'bowler':
                self.bwl+=1
                self.Bowlcount.setText(str(self.bwl))
            if ctgr == 'all rounder':
                self.ar+=1
                self.Alrcount.setText(str(self.ar))
            if ctgr == 'wicket keeper':
                self.wk+=1
                self.Wkcount.setText(str(self.wk))    

        #print("vdkn")
        self.show()
        #print("fece")
        
    
        
    def menu(self, action):
        txt = action.text()
        if txt == 'EVALUATE Team':
            
            self.openWindow()
        elif txt == 'NEW Team':
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.playerscount.setText('1000')
            self.name.setText('0')
            self.listWidget_2.clear()
            self.listWidget.clear()
            self.listWidget_2.setEnabled(True)

            self.openWindow1()
            self.setWindow()
            
        elif txt == 'SAVE Team':
            
            count=self.listWidget.count()
            selected=""
            for i in range(count):
                selected+=self.listWidget.item(i).text()
                if i<count:
                    selected+=","
            self.saveteam(self.label_3.text(),selected,self.a)
            
        elif txt == 'OPEN Team':
            
           
            self.bat=0
            self.bwl=0
            self.ar=0
            self.wk=0
            self.playerscount.setText('1000')
            self.name.setText('0')
            #self.playerscount=1000
            #self.name=0
            self.listWidget_2.clear()
            self.listWidget.clear()
            self.listWidget_2.setEnabled(False)
            self.show()
            self.openTeam()
                    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

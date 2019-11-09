from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic
import os,sys
from file_navigator import file_navigator

class MyMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow,self).__init__(parent)
        uic.loadUi("./walker.ui",self)
        self.setWindowTitle("File Navigation system")
        self.lineEdit_root.setText("/Users/cqiu/app/file_walker/root")
        self.lineEdit_tagname.setText(".file_tag.txt")
        self.walker = file_navigator()
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_clear.clicked.connect(self.clear)

    def search(self):
        self.walker.reset_tag(self.lineEdit_tagname.text())
        self.walker.reset_root([self.lineEdit_root.text()])
        conditions={}
        project = self.lineEdit_project.text()
        beamline = self.lineEdit_beamline.text()
        year = self.lineEdit_year.text()
        dataid = self.lineEdit_dataid.text()
        participants = self.lineEdit_participants.text()
        keys=['project','beamline','year','dataid','participants']
        for key in keys:
            if locals()[key]!="":
                conditions[key]=locals()[key]
        self.walker.reset_search_condition(conditions)
        self.walker.reset_root(self.lineEdit_root.text().rsplit(","))
        self.walker.reset_tag(self.lineEdit_tagname.text())
        self.walker.search_file()
        text_output=''
        for each in self.walker.location_box:
            tag_file = os.path.join(each,self.walker.tag_file)
            with open(tag_file,'r') as f:
                text_output=text_output+each+"\n"+f.read()+"\n"
        self.textEdit_location_box.setText(text_output)

    def clear(self):
        self.textEdit_location_box.setText("")
        self.lineEdit_project.setText("")
        self.lineEdit_year.setText("")
        self.lineEdit_beamline.setText("")
        self.lineEdit_dataid.setText("")
        self.lineEdit_participants.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())




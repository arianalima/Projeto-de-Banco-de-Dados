#coding: utf-8
from PyQt4 import QtCore, QtGui
import CRUD_Clinica

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

class Ui_DialogCli(object):
    def setupUi(self, DialogCli,codCli):
        DialogCli.setObjectName(_fromUtf8("DialogCli"))
        DialogCli.resize(320, 200)
        DialogCli.setStyleSheet(_fromUtf8("background:rgb(90, 181, 134)"))
        self.formLayoutWidget = QtGui.QWidget(DialogCli)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 300, 91))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayoutCli = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayoutCli.setObjectName(_fromUtf8("formLayoutMed"))

        self.labelCodCLi = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodCLi.setObjectName(_fromUtf8("labelCodCli"))
        self.formLayoutCli.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelCodCLi)
        self.campoCodCli = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodCli.setObjectName(_fromUtf8("campoCodCli"))
        self.formLayoutCli.setWidget(1, QtGui.QFormLayout.FieldRole, self.campoCodCli)
        self.labelNomeCli = QtGui.QLabel(self.formLayoutWidget)
        self.labelNomeCli.setObjectName(_fromUtf8("labelNomeCli"))
        self.formLayoutCli.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelNomeCli)
        self.campoNomeCli = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoNomeCli.setObjectName(_fromUtf8("campoNomeCli"))
        self.formLayoutCli.setWidget(2, QtGui.QFormLayout.FieldRole, self.campoNomeCli)
        self.labelLocalCli = QtGui.QLabel(self.formLayoutWidget)
        self.labelLocalCli.setObjectName(_fromUtf8("labelLocalCli"))
        self.formLayoutCli.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelLocalCli)
        self.campoLocalCli = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoLocalCli.setObjectName(_fromUtf8("campoLocalCli"))
        self.formLayoutCli.setWidget(3, QtGui.QFormLayout.FieldRole, self.campoLocalCli)
        self.labelCli = QtGui.QLabel(DialogCli)
        self.labelCli.setGeometry(QtCore.QRect(100, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelCli.setFont(font)
        self.labelCli.setObjectName(_fromUtf8("labelCli"))
        self.btnExcluir = QtGui.QPushButton(DialogCli)
        self.btnExcluir.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.btnExcluir.setObjectName(_fromUtf8("btnExcluir"))
        self.btnCancelar = QtGui.QPushButton(DialogCli)
        self.btnCancelar.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.retranslateUi(DialogCli)
        QtCore.QMetaObject.connectSlotsByName(DialogCli)
        self.setCamposClinica(codCli)
        self.btnRun()

    def retranslateUi(self, DialogCli):
        DialogCli.setWindowTitle(_translate("DialogCli", "Excluir Clínica", None))

        self.labelCodCLi.setText(_translate("DialogCli", "Código", None))
        self.labelNomeCli.setText(_translate("DialogCli", "Nome", None))
        self.labelLocalCli.setText(_translate("DialogCli", "Local", None))
        self.labelCli.setText(_translate("DialogCli", "Excluir Clínica", None))
        self.btnExcluir.setText(_translate("DialogCli", "Excluir", None))
        self.btnCancelar.setText(_translate("DialogCli", "Cancelar", None))


    def run(self,codCli):
        DialogCli = QtGui.QDialog()
        ui = Ui_DialogCli()
        ui.setupUi(DialogCli,codCli)
        DialogCli.show()
        sys.exit(app.exec_())

    def Close(self):
        DialogCli = QtGui.QDialog()
        ui = Ui_DialogCli()
        ui.setupUi(DialogCli,0)
        DialogCli.close()
        sys.exit(app.exec_())

    def setCamposClinica(self,codCli):
        clinica,boolean,menssagem = CRUD_Clinica.BuscarClinicaCod(codCli)
        nome,local = clinica[1][0],clinica[2][0]
        self.campoCodCli.setText(codCli)
        self.campoCodCli.setReadOnly(True)
        self.campoNomeCli.setText(nome)
        self.campoNomeCli.setReadOnly(True)
        self.campoLocalCli.setText(local)
        self.campoLocalCli.setReadOnly(True)

    def Excluir(self):
        cod = self.campoCodCli.text()
        if len(cod)!= 0:
            cod = int(cod)
            operacao = CRUD_Clinica.ApagarClinica(cod)

            self.popUp(operacao)


    def btnRun(self):
        self.btnExcluir.clicked.connect(self.Excluir)
        self.btnCancelar.clicked.connect(self.Close)

    def popUp(self,msg,tipo=None):
        mensagem = QtGui.QMessageBox()
        mensagem.setWindowTitle("Aviso")
        mensagem.setText(msg)
        mensagem.setStandardButtons(mensagem.Ok)
        if tipo is None:
            mensagem.buttonClicked.connect(self.Close)
        mensagem.exec_()

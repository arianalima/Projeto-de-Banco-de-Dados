#coding: utf-8
import sys
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
    def setupUi(self, DialogCli):
        DialogCli.setObjectName(_fromUtf8("DialogCli"))
        DialogCli.resize(317, 200)
        DialogCli.setStyleSheet(_fromUtf8("background:rgb(90, 181, 134)"))
        self.labelCli = QtGui.QLabel(DialogCli)
        self.labelCli.setGeometry(QtCore.QRect(60, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelCli.setFont(font)
        self.labelCli.setObjectName(_fromUtf8("labelCli"))
        self.formLayoutWidget = QtGui.QWidget(DialogCli)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 301, 91))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayoutEspec = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayoutEspec.setObjectName(_fromUtf8("formLayoutEspec"))

        self.labelNomeCli = QtGui.QLabel(self.formLayoutWidget)
        self.labelNomeCli.setObjectName(_fromUtf8("labelNomeCli"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelNomeCli)
        self.campoNomeCli = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoNomeCli.setObjectName(_fromUtf8("campoNomeCli"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.FieldRole, self.campoNomeCli)
        self.labelLocalCli = QtGui.QLabel(self.formLayoutWidget)
        self.labelLocalCli.setObjectName(_fromUtf8("labelLocalCli"))
        self.formLayoutEspec.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelLocalCli)
        self.campoLocalCli = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoLocalCli.setObjectName(_fromUtf8("campoLocalCli"))
        self.formLayoutEspec.setWidget(2, QtGui.QFormLayout.FieldRole, self.campoLocalCli)
        self.btnCancelar = QtGui.QPushButton(DialogCli)
        self.btnCancelar.setGeometry(QtCore.QRect(230, 170, 75, 23))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.btnCadastrar = QtGui.QPushButton(DialogCli)
        self.btnCadastrar.setGeometry(QtCore.QRect(140, 170, 75, 23))
        self.btnCadastrar.setObjectName(_fromUtf8("btnCadastrar"))

        self.retranslateUi(DialogCli)
        QtCore.QMetaObject.connectSlotsByName(DialogCli)

        self.BtnRun()

    def retranslateUi(self, DialogCli):
        DialogCli.setWindowTitle(_translate("DialogCli", "Cadastro de Clínica", None))
        self.labelCli.setText(_translate("DialogCli", "Cadastro de Clínicas", None))

        self.labelNomeCli.setText(_translate("DialogCli", "Nome", None))
        self.labelLocalCli.setText(_translate("DialogCli", "Local", None))
        self.btnCancelar.setText(_translate("DialogCli", "Cancelar", None))
        self.btnCadastrar.setText(_translate("DialogCli", "Cadastrar", None))


    def Inserir(self):
        nome = self.campoNomeCli.text()
        local = self.campoLocalCli.text()
        if len(nome)!=0 and len(local) != 0:
            operacao = CRUD_Clinica.InserirClinica(nome,local)
            self.popUp(operacao)

        else:
            self.popUp("Campo(s) Vazio(s)!", 1)

    def Close(self):
        DialogCli = QtGui.QDialog()
        ui = Ui_DialogCli()
        ui.setupUi(DialogCli)
        DialogCli.close()
        sys.exit(app.exec_())

    def Run(self):
        DialogCli = QtGui.QDialog()
        ui = Ui_DialogCli()
        ui.setupUi(DialogCli)
        DialogCli.show()
        sys.exit(app.exec_())

    def BtnRun(self):
        self.btnCadastrar.clicked.connect(self.Inserir)
        self.btnCancelar.clicked.connect(self.Close)

    def popUp(self,msg,tipo=None):
        mensagem = QtGui.QMessageBox()
        mensagem.setWindowTitle("Aviso")
        mensagem.setText(msg)
        mensagem.setStandardButtons(mensagem.Ok)
        if tipo is None:
            mensagem.buttonClicked.connect(self.Close)
        mensagem.exec_()

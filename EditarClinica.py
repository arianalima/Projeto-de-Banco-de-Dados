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
    def setupUi(self, DialogCli,codCli):
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

        self.labelCodCli = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodCli.setObjectName(_fromUtf8("labelCodCli"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelCodCli)
        self.campoCodCli = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodCli.setObjectName(_fromUtf8("campoCodCli"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.FieldRole, self.campoCodCli)
        self.labelNomeCli = QtGui.QLabel(self.formLayoutWidget)
        self.labelNomeCli.setObjectName(_fromUtf8("labelNomeCli"))
        self.formLayoutEspec.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelNomeCli)
        self.campoNomeCli = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoNomeCli.setObjectName(_fromUtf8("campoNomeCli"))
        self.formLayoutEspec.setWidget(2, QtGui.QFormLayout.FieldRole, self.campoNomeCli)
        self.labelLocalCli = QtGui.QLabel(self.formLayoutWidget)
        self.labelLocalCli.setObjectName(_fromUtf8("labelLocalCli"))
        self.formLayoutEspec.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelLocalCli)
        self.campoLocalCli = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoLocalCli.setObjectName(_fromUtf8("campoLocalCli"))
        self.formLayoutEspec.setWidget(3, QtGui.QFormLayout.FieldRole, self.campoLocalCli)
        self.btnCancelar = QtGui.QPushButton(DialogCli)
        self.btnCancelar.setGeometry(QtCore.QRect(230, 170, 75, 23))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.btnEditar = QtGui.QPushButton(DialogCli)
        self.btnEditar.setGeometry(QtCore.QRect(140, 170, 75, 23))
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))

        self.retranslateUi(DialogCli)
        QtCore.QMetaObject.connectSlotsByName(DialogCli)
        self.setCamposClinica(codCli)
        self.BtnRun()

    def retranslateUi(self, DialogCli):
        DialogCli.setWindowTitle(_translate("DialogCli", "Editar Clínica", None))
        self.labelCli.setText(_translate("DialogCli", "Editar Clínica", None))

        self.labelCodCli.setText(_translate("DialogCli", "Código", None))
        self.labelNomeCli.setText(_translate("DialogCli", "Nome", None))
        self.labelLocalCli.setText(_translate("DialogCli", "Local", None))
        self.btnCancelar.setText(_translate("DialogCli", "Cancelar", None))
        self.btnEditar.setText(_translate("DialogCli", "Editar", None))


    def Editar(self):
        codCli = self.campoCodCli.text()
        nome = self.campoNomeCli.text()
        local = self.campoLocalCli.text()
        if len(nome)!=0 and len(local) != 0:
            codCli = int(codCli)
            operacao = CRUD_Clinica.AlterarClinica(codCli,nome,local)
            self.popUp(operacao)

        else:
            self.popUp("Campo(s) Vazio(s)!", 1)

    def Close(self):
        DialogCli = QtGui.QDialog()
        ui = Ui_DialogCli()
        ui.setupUi(DialogCli,0)
        DialogCli.close()
        sys.exit(app.exec_())

    def run(self,codCli):
        DialogCli = QtGui.QDialog()
        ui = Ui_DialogCli()
        ui.setupUi(DialogCli,codCli)
        DialogCli.show()
        sys.exit(app.exec_())

    def setCamposClinica(self,codCli):
        clinica,boolean,menssagem = CRUD_Clinica.BuscarClinicaCod(codCli)
        nome,local = clinica[1][0],clinica[2][0]
        self.campoCodCli.setText(codCli)
        self.campoCodCli.setReadOnly(True)
        self.campoNomeCli.setText(nome)
        self.campoLocalCli.setText(local)

    def BtnRun(self):
        self.btnEditar.clicked.connect(self.Editar)
        self.btnCancelar.clicked.connect(self.Close)

    def popUp(self,msg,tipo=None):
        mensagem = QtGui.QMessageBox()
        mensagem.setWindowTitle("Aviso")
        mensagem.setText(msg)
        mensagem.setStandardButtons(mensagem.Ok)
        if tipo is None:
            mensagem.buttonClicked.connect(self.Close)
        mensagem.exec_()

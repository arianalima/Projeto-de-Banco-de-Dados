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

class Ui_DialogEspec(object):
    def setupUi(self, DialogEspec,codEspec):
        DialogEspec.setObjectName(_fromUtf8("DialogEspec"))
        DialogEspec.resize(319, 194)
        DialogEspec.setStyleSheet(_fromUtf8("background:rgb(90, 181, 134)"))

        self.formLayoutWidget = QtGui.QWidget(DialogEspec)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 301, 91))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayoutEspec = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayoutEspec.setObjectName(_fromUtf8("formLayoutEspec"))

        self.labelCodEspec = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodEspec.setObjectName(_fromUtf8("labelCodEspec"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelCodEspec)
        self.campoCodEspec = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodEspec.setObjectName(_fromUtf8("campoCodEspec"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.FieldRole, self.campoCodEspec)
        self.labelNomeEspec = QtGui.QLabel(self.formLayoutWidget)
        self.labelNomeEspec.setObjectName(_fromUtf8("labelNomeEspec"))
        self.formLayoutEspec.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelNomeEspec)
        self.campoNomeEspec = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoNomeEspec.setObjectName(_fromUtf8("campoNomeEspec"))
        self.formLayoutEspec.setWidget(2, QtGui.QFormLayout.FieldRole, self.campoNomeEspec)
        self.labelCodEspecGen = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodEspecGen.setObjectName(_fromUtf8("labelCodEspecGen"))
        self.formLayoutEspec.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelCodEspecGen)
        self.campoCodEspecGen = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodEspecGen.setObjectName(_fromUtf8("campoCodEspecGen"))
        self.formLayoutEspec.setWidget(3, QtGui.QFormLayout.FieldRole, self.campoCodEspecGen)
        self.labelEspec = QtGui.QLabel(DialogEspec)
        self.labelEspec.setGeometry(QtCore.QRect(50, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelEspec.setFont(font)
        self.labelEspec.setObjectName(_fromUtf8("labelEspec"))

        self.btnCancelar = QtGui.QPushButton(DialogEspec)
        self.btnCancelar.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.btnExcluir = QtGui.QPushButton(DialogEspec)
        self.btnExcluir.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.btnExcluir.setObjectName(_fromUtf8("btnExcluir"))

        self.retranslateUi(DialogEspec)
        QtCore.QMetaObject.connectSlotsByName(DialogEspec)
        self.setCamposEspecialidade(codEspec)
        self.btnRun()

    def retranslateUi(self, DialogEspec):
        DialogEspec.setWindowTitle(_translate("DialogEspec", "Excluir Especialidade", None))
        self.btnExcluir.setText(_translate("DialogEspec", "Confirmar", None))
        self.labelNomeEspec.setText(_translate("DialogEspec", "Nome", None))
        self.labelCodEspec.setText(_translate("DialogEspec", "Código", None))
        self.labelCodEspecGen.setText(_translate("DialogEspec", "Código Especialidade Genérica", None))
        self.labelEspec.setText(_translate("DialogEspec", "Excluir Especialidade", None))
        self.btnCancelar.setText(_translate("DialogEspec", "Cancelar", None))

    def run(self,codEspec):
        DialogEspec = QtGui.QDialog()
        ui = Ui_DialogEspec()
        ui.setupUi(DialogEspec,codEspec)
        DialogEspec.show()
        sys.exit(app.exec_())

    def Close(self):
        DialogEspec = QtGui.QDialog()
        ui = Ui_DialogEspec()
        ui.setupUi(DialogEspec,0)
        DialogEspec.close()
        sys.exit(app.exec_())

    def setCamposEspecialidade(self, codEspec):
        especialidade,boolean,menssagem = CRUD_Clinica.BuscarCodEspecialidade(codEspec)
        nome,codEspecGen = especialidade[1][0],str(especialidade[2][0])
        self.campoCodEspec.setText(codEspec)
        self.campoCodEspec.setReadOnly(True)
        self.campoNomeEspec.setText(nome)
        self.campoNomeEspec.setReadOnly(True)
        self.campoCodEspecGen.setText(codEspecGen)
        self.campoCodEspecGen.setReadOnly(True)

    def Excluir(self):
        cod = self.campoCodEspec.text()
        if len(cod)!= 0:
            cod = int(cod)
            operacao = CRUD_Clinica.ApagarEspecialidade(cod)
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

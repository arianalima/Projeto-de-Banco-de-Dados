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
    def setupUi(self, DialogEspec):
        DialogEspec.setObjectName(_fromUtf8("DialogEspec"))
        DialogEspec.resize(319, 194)
        DialogEspec.setStyleSheet(_fromUtf8("background:rgb(90, 181, 134)"))
        self.btnCadastrar = QtGui.QPushButton(DialogEspec)
        self.btnCadastrar.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.btnCadastrar.setObjectName(_fromUtf8("btnCadastrar"))
        self.formLayoutWidget = QtGui.QWidget(DialogEspec)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 301, 91))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayoutEspec = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayoutEspec.setObjectName(_fromUtf8("formLayoutEspec"))

        self.labelNomeEspec = QtGui.QLabel(self.formLayoutWidget)
        self.labelNomeEspec.setObjectName(_fromUtf8("labelNomeEspec"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelNomeEspec)
        self.campoNomeEspec = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoNomeEspec.setObjectName(_fromUtf8("campoNomeEspec"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.FieldRole, self.campoNomeEspec)
        self.labelCodEspecGen = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodEspecGen.setObjectName(_fromUtf8("labelCodEspecGen"))
        self.formLayoutEspec.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelCodEspecGen)
        self.campoCodEspecGen = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodEspecGen.setObjectName(_fromUtf8("campoCodEspecGen"))
        self.formLayoutEspec.setWidget(2, QtGui.QFormLayout.FieldRole, self.campoCodEspecGen)
        self.labelEspec = QtGui.QLabel(DialogEspec)
        self.labelEspec.setGeometry(QtCore.QRect(30, 10, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelEspec.setFont(font)
        self.labelEspec.setObjectName(_fromUtf8("labelEspec"))
        self.btnCancelar = QtGui.QPushButton(DialogEspec)
        self.btnCancelar.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.retranslateUi(DialogEspec)
        QtCore.QMetaObject.connectSlotsByName(DialogEspec)

        self.btnRun()

    def retranslateUi(self, DialogEspec):
        DialogEspec.setWindowTitle(_translate("DialogEspec", "Cadastro de Especialidade", None))
        self.btnCadastrar.setText(_translate("DialogEspec", "Cadastrar", None))

        self.labelNomeEspec.setText(_translate("DialogEspec", "Nome", None))
        self.labelCodEspecGen.setText(_translate("DialogEspec", "Código Especialidade Genérica", None))
        self.labelEspec.setText(_translate("DialogEspec", "Cadastro de Especialidade", None))
        self.btnCancelar.setText(_translate("DialogEspec", "Cancelar", None))

    def Run(self):
        DialogEspec = QtGui.QDialog()
        ui = Ui_DialogEspec()
        ui.setupUi(DialogEspec)
        DialogEspec.show()
        sys.exit(app.exec_())

    def Close(self):
        DialogEspec = QtGui.QDialog()
        ui = Ui_DialogEspec()
        ui.setupUi(DialogEspec)
        DialogEspec.close()
        sys.exit(app.exec_())

    def Inserir(self):
        nome = self.campoNomeEspec.text()
        codEspecGen = self.campoCodEspecGen.text()
        if len(nome) != 0:
            if len(codEspecGen) != 0:
                try:
                    codEspecGen = int(codEspecGen)
                    operacao = CRUD_Clinica.InserirEspecialidade(nome,codEspecGen)
                    self.popUp(operacao)
                except:
                    self.popUp("Código deve conter apenas números!",1)
            else:
                operacao = CRUD_Clinica.InserirEspecialidade(nome)
                self.popUp(operacao)
        else:
            self.popUp("Insira um nome!",1)

    def btnRun(self):
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

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

class Ui_DialogMed(object):
    def setupUi(self, DialogMed):
        DialogMed.setObjectName(_fromUtf8("DialogMed"))
        DialogMed.resize(320, 193)
        DialogMed.setStyleSheet(_fromUtf8("background:rgb(90, 181, 134)"))
        self.formLayoutWidget = QtGui.QWidget(DialogMed)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 301, 91))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayoutMed = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayoutMed.setObjectName(_fromUtf8("formLayoutMed"))

        self.labelNomeMed = QtGui.QLabel(self.formLayoutWidget)
        self.labelNomeMed.setObjectName(_fromUtf8("labelNomeMed"))
        self.formLayoutMed.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelNomeMed)
        self.campoNomeMed = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoNomeMed.setObjectName(_fromUtf8("campoNomeMed"))
        self.formLayoutMed.setWidget(1, QtGui.QFormLayout.FieldRole, self.campoNomeMed)
        self.labelCodEspecMed = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodEspecMed.setObjectName(_fromUtf8("labelCodEspecMed"))
        self.formLayoutMed.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelCodEspecMed)
        self.campoCodEspecMed = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodEspecMed.setObjectName(_fromUtf8("campoCodEspecMed"))
        self.formLayoutMed.setWidget(2, QtGui.QFormLayout.FieldRole, self.campoCodEspecMed)
        self.labelMed = QtGui.QLabel(DialogMed)
        self.labelMed.setGeometry(QtCore.QRect(50, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelMed.setFont(font)
        self.labelMed.setObjectName(_fromUtf8("labelMed"))
        self.btnCadastrar = QtGui.QPushButton(DialogMed)
        self.btnCadastrar.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.btnCadastrar.setObjectName(_fromUtf8("btnCadastrar"))
        self.btnCancelar = QtGui.QPushButton(DialogMed)
        self.btnCancelar.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.retranslateUi(DialogMed)
        QtCore.QMetaObject.connectSlotsByName(DialogMed)

        self.btnRun()

    def retranslateUi(self, DialogMed):
        DialogMed.setWindowTitle(_translate("DialogMed", "Cadastro de Médico", None))

        self.labelNomeMed.setText(_translate("DialogMed", "Nome", None))
        self.labelCodEspecMed.setText(_translate("DialogMed", "Código Especialidade", None))
        self.labelMed.setText(_translate("DialogMed", "Cadastro de Médico", None))
        self.btnCadastrar.setText(_translate("DialogMed", "Cadastrar", None))
        self.btnCancelar.setText(_translate("DialogMed", "Cancelar", None))


    def run(self):
        DialogMed = QtGui.QDialog()
        ui = Ui_DialogMed()
        ui.setupUi(DialogMed)
        DialogMed.show()
        sys.exit(app.exec_())

    def Close(self):
        DialogMed = QtGui.QDialog()
        ui = Ui_DialogMed()
        ui.setupUi(DialogMed)
        DialogMed.close()
        sys.exit(app.exec_())

    def Inserir(self):
        nome = self.campoNomeMed.text()
        codEspecMed = self.campoCodEspecMed.text()
        if len(nome)!= 0:
            if len(codEspecMed) != 0:
                try:
                    codEspecMed = int(codEspecMed)
                    operacao = CRUD_Clinica.InserirMedico(nome,codEspecMed)
                    self.popUp(operacao)
                except:
                    self.popUp("Código deve conter apenas números!",1)
            else:
                operacao = CRUD_Clinica.InserirMedico(nome)
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

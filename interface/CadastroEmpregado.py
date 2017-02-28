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

class Ui_DialogEmp(object):
    def setupUi(self, DialogEmp):
        DialogEmp.setObjectName(_fromUtf8("DialogEmp"))
        DialogEmp.resize(320, 196)
        DialogEmp.setStyleSheet(_fromUtf8("background:rgb(90, 181, 134)"))
        self.labelEmp = QtGui.QLabel(DialogEmp)
        self.labelEmp.setGeometry(QtCore.QRect(40, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelEmp.setFont(font)
        self.labelEmp.setObjectName(_fromUtf8("labelEmp"))
        self.formLayoutWidget = QtGui.QWidget(DialogEmp)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 60, 301, 71))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayoutEspec = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayoutEspec.setObjectName(_fromUtf8("formLayoutEspec"))
        self.labelCodCliEmp = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodCliEmp.setObjectName(_fromUtf8("labelCodCliEmp"))
        self.formLayoutEspec.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelCodCliEmp)
        self.campoCodCliEmp = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodCliEmp.setObjectName(_fromUtf8("campoCodCliEmp"))
        self.formLayoutEspec.setWidget(0, QtGui.QFormLayout.FieldRole, self.campoCodCliEmp)
        self.labelCodMedEmp = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodMedEmp.setObjectName(_fromUtf8("labelCodMedEmp"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelCodMedEmp)
        self.campoCodMedEmp = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodMedEmp.setObjectName(_fromUtf8("campoCodMedEmp"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.FieldRole, self.campoCodMedEmp)
        self.btnCancelar = QtGui.QPushButton(DialogEmp)
        self.btnCancelar.setGeometry(QtCore.QRect(230, 150, 75, 23))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.btnCadastrar = QtGui.QPushButton(DialogEmp)
        self.btnCadastrar.setGeometry(QtCore.QRect(140, 150, 75, 23))
        self.btnCadastrar.setObjectName(_fromUtf8("btnCadastrar"))

        self.retranslateUi(DialogEmp)
        QtCore.QMetaObject.connectSlotsByName(DialogEmp)

        self.btnRun()

    def retranslateUi(self, DialogEmp):
        DialogEmp.setWindowTitle(_translate("DialogEmp", "Cadastro de Empregado", None))
        self.labelEmp.setText(_translate("DialogEmp", "Cadastro de Empregados", None))
        self.labelCodCliEmp.setText(_translate("DialogEmp", "Código Clínica", None))
        self.labelCodMedEmp.setText(_translate("DialogEmp", "Código Médico", None))
        self.btnCancelar.setText(_translate("DialogEmp", "Cancelar", None))
        self.btnCadastrar.setText(_translate("DialogEmp", "Cadastrar", None))

    def run(self):
        DialogEmp = QtGui.QDialog()
        ui = Ui_DialogEmp()
        ui.setupUi(DialogEmp)
        DialogEmp.show()
        sys.exit(app.exec_())

    def Close(self):
        DialogEmp = QtGui.QDialog()
        ui = Ui_DialogEmp()
        ui.setupUi(DialogEmp)
        DialogEmp.close()
        sys.exit(app.exec_())

    def Inserir(self):
        codCliEmp = self.campoCodCliEmp.text()
        codMedEmp = self.campoCodMedEmp.text()

        if len(codCliEmp) !=0 and len(codMedEmp) != 0:
            try:
                codCliEmp = int(codCliEmp)
                codMedEmp = int(codMedEmp)
                operacao = CRUD_Clinica.InserirClinicaMedico(codCliEmp,codMedEmp)
                self.popUp(operacao)
            except:
                self.popUp("Código deve conter apenas números!",1)
        else:
            self.popUp("Campo(s) Vazio(s)!",1)

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

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
    def setupUi(self, DialogMed,codMed):
        DialogMed.setObjectName(_fromUtf8("DialogMed"))
        DialogMed.resize(320, 193)
        DialogMed.setStyleSheet(_fromUtf8("background:rgb(90, 181, 134)"))
        self.formLayoutWidget = QtGui.QWidget(DialogMed)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 300, 91))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayoutMed = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayoutMed.setObjectName(_fromUtf8("formLayoutMed"))

        self.labelCodMed = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodMed.setObjectName(_fromUtf8("labelCodMed"))
        self.formLayoutMed.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelCodMed)
        self.campoCodMed = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodMed.setObjectName(_fromUtf8("campoCodMed"))
        self.formLayoutMed.setWidget(1, QtGui.QFormLayout.FieldRole, self.campoCodMed)
        self.labelNomeMed = QtGui.QLabel(self.formLayoutWidget)
        self.labelNomeMed.setObjectName(_fromUtf8("labelNomeMed"))
        self.formLayoutMed.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelNomeMed)
        self.campoNomeMed = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoNomeMed.setObjectName(_fromUtf8("campoNomeMed"))
        self.formLayoutMed.setWidget(2, QtGui.QFormLayout.FieldRole, self.campoNomeMed)
        self.labelCodEspecMed = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodEspecMed.setObjectName(_fromUtf8("labelCodEspecMed"))
        self.formLayoutMed.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelCodEspecMed)
        self.campoCodEspecMed = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodEspecMed.setObjectName(_fromUtf8("campoCodEspecMed"))
        self.formLayoutMed.setWidget(3, QtGui.QFormLayout.FieldRole, self.campoCodEspecMed)

        self.labelMed = QtGui.QLabel(DialogMed)
        self.labelMed.setGeometry(QtCore.QRect(100, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelMed.setFont(font)
        self.labelMed.setObjectName(_fromUtf8("labelMed"))
        self.btnExcluir = QtGui.QPushButton(DialogMed)
        self.btnExcluir.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.btnExcluir.setObjectName(_fromUtf8("btnExcluir"))
        self.btnCancelar = QtGui.QPushButton(DialogMed)
        self.btnCancelar.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.retranslateUi(DialogMed)
        QtCore.QMetaObject.connectSlotsByName(DialogMed)
        self.setCamposMedico(codMed)
        self.btnRun()

    def retranslateUi(self, DialogMed):
        DialogMed.setWindowTitle(_translate("DialogMed", "Excluir Médico", None))

        self.labelCodMed.setText(_translate("DialogMed", "Código", None))
        self.labelNomeMed.setText(_translate("DialogMed", "Nome", None))
        self.labelCodEspecMed.setText(_translate("DialogMed", "Código Especialidade", None))
        self.labelMed.setText(_translate("DialogMed", "Excluir Médico", None))
        self.btnExcluir.setText(_translate("DialogMed", "Confirmar", None))
        self.btnCancelar.setText(_translate("DialogMed", "Cancelar", None))


    def run(self,codMed):
        DialogMed = QtGui.QDialog()
        ui = Ui_DialogMed()
        ui.setupUi(DialogMed,codMed)
        DialogMed.show()
        sys.exit(app.exec_())

    def Close(self):
        DialogMed = QtGui.QDialog()
        ui = Ui_DialogMed()
        ui.setupUi(DialogMed,0)
        DialogMed.close()
        sys.exit(app.exec_())

    def setCamposMedico(self,codMed):
        medico, boolean, menssagem = CRUD_Clinica.BuscarMedicoCod(codMed)
        nome, codEspeci = medico[1][0], str(medico[2][0])
        self.campoCodMed.setText(codMed)
        self.campoCodMed.setReadOnly(True)
        self.campoNomeMed.setText(nome)
        self.campoNomeMed.setReadOnly(True)
        self.campoCodEspecMed.setText(codEspeci)
        self.campoCodEspecMed.setReadOnly(True)

    def Excluir(self):
        cod = self.campoCodMed.text()
        if len(cod)!= 0:
            cod = int(cod)
            operacao = CRUD_Clinica.ApagarMedico(cod)
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

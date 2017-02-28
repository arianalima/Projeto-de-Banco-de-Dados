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
    def setupUi(self, DialogMedi,codMed):

        DialogMedi.setObjectName(_fromUtf8("DialogMed"))
        DialogMedi.resize(320, 193)
        DialogMedi.setStyleSheet(_fromUtf8("background:rgb(90, 181, 134)"))
        self.formLayoutWidget = QtGui.QWidget(DialogMedi)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 301, 91))
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
        self.labelMed = QtGui.QLabel(DialogMedi)
        self.labelMed.setGeometry(QtCore.QRect(50, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelMed.setFont(font)
        self.labelMed.setObjectName(_fromUtf8("labelMed"))
        self.btnEditar = QtGui.QPushButton(DialogMedi)
        self.btnEditar.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))
        self.btnCancelar = QtGui.QPushButton(DialogMedi)
        self.btnCancelar.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.retranslateUi(DialogMedi)
        QtCore.QMetaObject.connectSlotsByName(DialogMedi)
        self.setCamposMedico(codMed)
        self.btnRun()

    def retranslateUi(self, DialogMed):
        DialogMed.setWindowTitle(_translate("DialogMed", "Editar Médico", None))

        self.labelCodMed.setText(_translate("DialogMed", "Código", None))
        self.labelNomeMed.setText(_translate("DialogMed", "Nome", None))
        self.labelCodEspecMed.setText(_translate("DialogMed", "Código Especialidade", None))
        self.labelMed.setText(_translate("DialogMed", "Editar Médico", None))
        self.btnEditar.setText(_translate("DialogMed", "Editar", None))
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

    def setCamposMedico(self,cod):
        medico,boolean,menssagem = CRUD_Clinica.BuscarMedicoCod(cod)
        nome,codEspeci = medico[1][0],str(medico[2][0])
        self.campoCodMed.setText(cod)
        self.campoCodMed.setReadOnly(True)
        self.campoNomeMed.setText(nome)
        self.campoCodEspecMed.setText(codEspeci)


    def Editar(self):
        codMed = self.campoCodMed.text()
        nome = self.campoNomeMed.text()
        codEspecMed = self.campoCodEspecMed.text()
        if len(nome)!= 0:
            codMed = int(codMed)
            if len(codEspecMed) != 0:
                try:
                    codEspecMed = int(codEspecMed)
                    operacao = CRUD_Clinica.AlterarMedico(codMed,nome,codEspecMed)
                    self.popUp(operacao)
                except:
                    self.popUp("Os códigos devem conter apenas números!",1)
            else:
                operacao = CRUD_Clinica.AlterarMedico(codMed,nome)
                self.popUp(operacao)

        else:
            self.popUp("Insira um nome!",1)

    def btnRun(self):
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

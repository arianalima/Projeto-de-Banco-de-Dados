#coding: utf-8
from PyQt4 import QtCore, QtGui
import time
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

class Ui_DialogAgenCons(object):
    def setupUi(self, DialogAgenCons,codCli,codMed,data,hora):
        DialogAgenCons.setObjectName(_fromUtf8("DialogAgenCons"))
        DialogAgenCons.resize(317, 188)
        DialogAgenCons.setStyleSheet(_fromUtf8("background:rgb(90, 181, 134)"))
        self.labelCons = QtGui.QLabel(DialogAgenCons)
        self.labelCons.setGeometry(QtCore.QRect(80, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelCons.setFont(font)
        self.labelCons.setObjectName(_fromUtf8("labelCons"))
        self.formLayoutWidget = QtGui.QWidget(DialogAgenCons)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 301, 100))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayoutEspec = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayoutEspec.setObjectName(_fromUtf8("formLayoutEspec"))
        self.labelCodCliCons = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodCliCons.setObjectName(_fromUtf8("labelCodCliCons"))
        self.formLayoutEspec.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelCodCliCons)
        self.campoCodCliCons = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodCliCons.setObjectName(_fromUtf8("campoCodCliCons"))
        self.formLayoutEspec.setWidget(0, QtGui.QFormLayout.FieldRole, self.campoCodCliCons)
        self.labelCodMedCons = QtGui.QLabel(self.formLayoutWidget)
        self.labelCodMedCons.setObjectName(_fromUtf8("labelCodMedCons"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelCodMedCons)
        self.campoCodMedCons = QtGui.QLineEdit(self.formLayoutWidget)
        self.campoCodMedCons.setObjectName(_fromUtf8("campoCodMedCons"))
        self.formLayoutEspec.setWidget(1, QtGui.QFormLayout.FieldRole, self.campoCodMedCons)
        self.labelDataCons = QtGui.QLabel(self.formLayoutWidget)
        self.labelDataCons.setObjectName(_fromUtf8("labelDataCons"))
        self.formLayoutEspec.setWidget(2, QtGui.QFormLayout.LabelRole, self.labelDataCons)
        self.labelHoraCons = QtGui.QLabel(self.formLayoutWidget)
        self.labelHoraCons.setObjectName(_fromUtf8("labelHoraCons"))
        self.formLayoutEspec.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelHoraCons)
        self.campoDataCons = QtGui.QDateEdit(self.formLayoutWidget)
        self.campoDataCons.setObjectName(_fromUtf8("campoDataCons"))
        self.formLayoutEspec.setWidget(2, QtGui.QFormLayout.FieldRole, self.campoDataCons)
        self.campoHoraCons = QtGui.QTimeEdit(self.formLayoutWidget)
        self.campoHoraCons.setObjectName(_fromUtf8("campoHoraCons"))
        self.formLayoutEspec.setWidget(3, QtGui.QFormLayout.FieldRole, self.campoHoraCons)
        self.btnCancelar = QtGui.QPushButton(DialogAgenCons)
        self.btnCancelar.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.btnEditar = QtGui.QPushButton(DialogAgenCons)
        self.btnEditar.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.btnEditar.setObjectName(_fromUtf8("btnEditar"))

        self.data = data
        self.hora = hora

        self.retranslateUi(DialogAgenCons)
        QtCore.QMetaObject.connectSlotsByName(DialogAgenCons)
        self.setCamposConsulta(codCli,codMed,data,hora)
        self.btnRun()

    def retranslateUi(self, DialogAgenCons):
        DialogAgenCons.setWindowTitle(_translate("DialogAgenCons", "Editar Consulta", None))
        self.labelCons.setText(_translate("DialogAgenCons", "Editar Consulta", None))
        self.labelCodCliCons.setText(_translate("DialogAgenCons", "Código Clínica", None))
        self.labelCodMedCons.setText(_translate("DialogAgenCons", "Código Médico", None))
        self.labelDataCons.setText(_translate("DialogAgenCons", "Data", None))
        self.labelHoraCons.setText(_translate("DialogAgenCons", "Hora", None))
        self.btnCancelar.setText(_translate("DialogAgenCons", "Cancelar", None))
        self.btnEditar.setText(_translate("DialogAgenCons", "Editar", None))


    def run(self,codCli,codMed,data,hora):
        DialogAgenCons = QtGui.QDialog()
        ui = Ui_DialogAgenCons()
        ui.setupUi(DialogAgenCons,codCli,codMed,data,hora)
        DialogAgenCons.show()
        sys.exit(app.exec_())

    def Close(self):
        DialogAgenCons = QtGui.QDialog()
        ui = Ui_DialogAgenCons()
        ui.setupUi(DialogAgenCons,0,0,0,0)
        DialogAgenCons.close()
        sys.exit(app.exec_())

    def setCamposConsulta(self,codCli,codMed,data,hora):
        boolean = CRUD_Clinica.BuscarConsulta(codCli,codMed,data,hora)
        data = data.split("/")
        hora = hora.split(":")
        qdata = QtCore.QDate(int(data[2]),int(data[1]),int(data[0]))

        h,m = int(hora[0]),int(hora[1])
        qhora = QtCore.QTime(h,m)
        if boolean == True:
            self.campoCodCliCons.setText(codCli)
            self.campoCodCliCons.setReadOnly(True)
            self.campoCodMedCons.setText(codMed)
            self.campoCodMedCons.setReadOnly(True)
            self.campoDataCons.setDate(qdata)
            self.campoHoraCons.setTime(qhora)

    def Editar(self):
        codCliCons = self.campoCodCliCons.text()
        codMedCons = self.campoCodMedCons.text()
        dataCons = self.campoDataCons.text()
        horaCons = self.campoHoraCons.text()

        horaAnt = self.hora
        dataAnt = self.data
        dataAtual = time.strftime('%d/%m/%Y')
        newDataCons = time.strptime(dataCons, "%d/%m/%Y")
        newDataAtual = time.strptime(dataAtual, "%d/%m/%Y")

        if len(codCliCons) and len(codMedCons) != 0:
            codCliCons = int(codCliCons)
            codMedCons = int(codMedCons)
            if newDataCons > newDataAtual and horaCons!="00:00":

                operacao = CRUD_Clinica.AlterarConsulta(codCliCons,codMedCons,dataAnt,dataCons,horaAnt,horaCons)
                self.popUp(operacao)
            else:
                self.popUp("Data/Hora inválida(s)",1)
        else:
            self.popUp("Campo(s) Vazio(s)!",1)

    def btnRun(self):
        self.btnCancelar.clicked.connect(self.Close)
        self.btnEditar.clicked.connect(self.Editar)

    def popUp(self,msg,tipo=None):
        mensagem = QtGui.QMessageBox()
        mensagem.setWindowTitle("Aviso")
        mensagem.setText(msg)
        mensagem.setStandardButtons(mensagem.Ok)
        if tipo is None:
            mensagem.buttonClicked.connect(self.Close)
        mensagem.exec_()

#coding: utf-8
from PyQt4 import QtCore, QtGui
import CRUD_Clinica
import sys


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

class Ui_tabWidget(object):
    def setupUi(self, tabWidget):
        tabWidget.setObjectName(_fromUtf8("tabWidget"))
        tabWidget.resize(596, 380)
        tabWidget.setStyleSheet(_fromUtf8("background:rgb(90, 181, 134)"))

       #-------------------#medico#----------------------------------------#

        self.tabMedicos = QtGui.QWidget()
        self.tabMedicos.setObjectName(_fromUtf8("tabMedicos"))
        self.campoBuscaMed = QtGui.QLineEdit(self.tabMedicos)
        self.campoBuscaMed.setGeometry(QtCore.QRect(20, 10, 201, 20))
        self.campoBuscaMed.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.campoBuscaMed.setText(_fromUtf8("Busca"))
        self.campoBuscaMed.setFrame(True)
        self.campoBuscaMed.setEchoMode(QtGui.QLineEdit.Normal)
        self.campoBuscaMed.setCursorPosition(5)
        self.campoBuscaMed.setReadOnly(False)
        self.campoBuscaMed.setObjectName(_fromUtf8("campoBuscaMed"))
        self.tipoBuscaMed = QtGui.QComboBox(self.tabMedicos)
        self.tipoBuscaMed.setGeometry(QtCore.QRect(240, 10, 131, 22))
        self.tipoBuscaMed.setObjectName(_fromUtf8("tipoBuscaMed"))
        self.tipoBuscaMed.addItem(_fromUtf8(""))
        self.tipoBuscaMed.addItem(_fromUtf8(""))
        self.tipoBuscaMed.addItem(_fromUtf8(""))
        self.btnBuscaMed = QtGui.QPushButton(self.tabMedicos)
        self.btnBuscaMed.setGeometry(QtCore.QRect(390, 10, 41, 23))
        self.btnBuscaMed.setObjectName(_fromUtf8("btnBuscaMed"))
        self.btnCadastrarMed = QtGui.QPushButton(self.tabMedicos)
        self.btnCadastrarMed.setGeometry(QtCore.QRect(450, 130, 75, 23))
        self.btnCadastrarMed.setObjectName(_fromUtf8("btnCadastrarMed"))
        self.btnEditarMed = QtGui.QPushButton(self.tabMedicos)
        self.btnEditarMed.setGeometry(QtCore.QRect(450, 70, 75, 23))
        self.btnEditarMed.setObjectName(_fromUtf8("btnEditarMed"))
        self.btnAtualizarMed = QtGui.QPushButton(self.tabMedicos)
        self.btnAtualizarMed.setGeometry(QtCore.QRect(450, 200, 75, 23))
        self.btnAtualizarMed.setObjectName(_fromUtf8("btnAtualizarMed"))

        self.tableMedicos = QtGui.QTableWidget(self.tabMedicos)
        self.tableMedicos.setGeometry(QtCore.QRect(20, 40, 421, 281))
        self.tableMedicos.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableMedicos.setObjectName(_fromUtf8("tableMedicos"))
        self.tableMedicos.setColumnCount(3)
        self.tableMedicos.setRowCount(CRUD_Clinica.QuantidadeMedicos())
        item = QtGui.QTableWidgetItem()
        self.tableMedicos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableMedicos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableMedicos.setHorizontalHeaderItem(2, item)

        medicos = CRUD_Clinica.ListarMedicos()
        if medicos != None:
            for n in range(3):
                for m in range(len(medicos[n])):
                    item = QtGui.QTableWidgetItem(medicos[n][m])
                    self.tableMedicos.setItem(m,n,item)

        self.btnExcluirMed = QtGui.QPushButton(self.tabMedicos)
        self.btnExcluirMed.setGeometry(QtCore.QRect(450, 100, 75, 23))
        self.btnExcluirMed.setObjectName(_fromUtf8("btnExcluirMed"))
        tabWidget.addTab(self.tabMedicos, _fromUtf8(""))

        # -------------------#especialidade#----------------------------------------#

        self.tabEspecialidades = QtGui.QWidget()
        self.tabEspecialidades.setObjectName(_fromUtf8("tabEspecialidades"))
        self.tipoBuscaEspec = QtGui.QComboBox(self.tabEspecialidades)
        self.tipoBuscaEspec.setGeometry(QtCore.QRect(240, 10, 131, 22))
        self.tipoBuscaEspec.setObjectName(_fromUtf8("tipoBuscaEspec"))
        self.tipoBuscaEspec.addItem(_fromUtf8(""))
        self.tipoBuscaEspec.addItem(_fromUtf8(""))
        self.tipoBuscaEspec.addItem(_fromUtf8(""))
        self.btnExcluirEspec = QtGui.QPushButton(self.tabEspecialidades)
        self.btnExcluirEspec.setGeometry(QtCore.QRect(450, 100, 75, 23))
        self.btnExcluirEspec.setObjectName(_fromUtf8("btnExcluirEspec"))
        self.btnEditarEspec = QtGui.QPushButton(self.tabEspecialidades)
        self.btnEditarEspec.setGeometry(QtCore.QRect(450, 70, 75, 23))
        self.btnEditarEspec.setObjectName(_fromUtf8("btnEditarEspec"))
        self.btnAtualizarEspec = QtGui.QPushButton(self.tabEspecialidades)
        self.btnAtualizarEspec.setGeometry(QtCore.QRect(450, 200, 75, 23))
        self.btnAtualizarEspec.setObjectName(_fromUtf8("btnAtualizarEspec"))

        self.tableEspecialidades = QtGui.QTableWidget(self.tabEspecialidades)
        self.tableEspecialidades.setGeometry(QtCore.QRect(20, 40, 421, 281))
        self.tableEspecialidades.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableEspecialidades.setObjectName(_fromUtf8("tableEspecialidades"))
        self.tableEspecialidades.setColumnCount(3)
        self.tableEspecialidades.setRowCount(CRUD_Clinica.QuantidadeEspecialidades())
        item = QtGui.QTableWidgetItem()
        self.tableEspecialidades.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableEspecialidades.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableEspecialidades.setHorizontalHeaderItem(2, item)

        especialidades = CRUD_Clinica.ListarEspecialidades()
        if especialidades!=None:
            for n in range(3):
                for m in range(len(especialidades[n])):
                    item = QtGui.QTableWidgetItem(especialidades[n][m])
                    self.tableEspecialidades.setItem(m,n,item)

        self.btnCadastrarEspec = QtGui.QPushButton(self.tabEspecialidades)
        self.btnCadastrarEspec.setGeometry(QtCore.QRect(450, 130, 75, 23))
        self.btnCadastrarEspec.setObjectName(_fromUtf8("btnCadastrarEspec"))
        self.btnBuscaEspec = QtGui.QPushButton(self.tabEspecialidades)
        self.btnBuscaEspec.setGeometry(QtCore.QRect(390, 10, 41, 23))
        self.btnBuscaEspec.setObjectName(_fromUtf8("btnBuscaEspec"))
        self.campoBuscaEspec = QtGui.QLineEdit(self.tabEspecialidades)
        self.campoBuscaEspec.setGeometry(QtCore.QRect(20, 10, 201, 20))
        self.campoBuscaEspec.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.campoBuscaEspec.setText(_fromUtf8("Busca"))
        self.campoBuscaEspec.setFrame(True)
        self.campoBuscaEspec.setEchoMode(QtGui.QLineEdit.Normal)
        self.campoBuscaEspec.setCursorPosition(5)
        self.campoBuscaEspec.setReadOnly(False)
        self.campoBuscaEspec.setObjectName(_fromUtf8("campoBuscaEspec"))
        tabWidget.addTab(self.tabEspecialidades, _fromUtf8(""))

        # -------------------#clinica#----------------------------------------#

        self.tabClinicas = QtGui.QWidget()
        self.tabClinicas.setObjectName(_fromUtf8("tabClinicas"))
        self.tipoBuscaCli = QtGui.QComboBox(self.tabClinicas)
        self.tipoBuscaCli.setGeometry(QtCore.QRect(240, 10, 131, 22))
        self.tipoBuscaCli.setObjectName(_fromUtf8("tipoBuscaCli"))
        self.tipoBuscaCli.addItem(_fromUtf8(""))
        self.tipoBuscaCli.addItem(_fromUtf8(""))
        self.tipoBuscaCli.addItem(_fromUtf8(""))
        self.btnExcluirCli = QtGui.QPushButton(self.tabClinicas)
        self.btnExcluirCli.setGeometry(QtCore.QRect(450, 100, 75, 23))
        self.btnExcluirCli.setObjectName(_fromUtf8("btnExcluirCli"))
        self.btnEditarCli = QtGui.QPushButton(self.tabClinicas)
        self.btnEditarCli.setGeometry(QtCore.QRect(450, 70, 75, 23))
        self.btnEditarCli.setObjectName(_fromUtf8("btnEditarCli"))
        self.btnAtualizarCli = QtGui.QPushButton(self.tabClinicas)
        self.btnAtualizarCli.setGeometry(QtCore.QRect(450, 200, 75, 23))
        self.btnAtualizarCli.setObjectName(_fromUtf8("btnAtualizarCli"))

        self.tableClinicas = QtGui.QTableWidget(self.tabClinicas)
        self.tableClinicas.setGeometry(QtCore.QRect(20, 40, 421, 281))
        self.tableClinicas.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableClinicas.setObjectName(_fromUtf8("tableClinicas"))
        self.tableClinicas.setColumnCount(3)
        self.tableClinicas.setRowCount(CRUD_Clinica.QuantidadeClinicas())
        item = QtGui.QTableWidgetItem()
        self.tableClinicas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableClinicas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableClinicas.setHorizontalHeaderItem(2, item)

        clinicas = CRUD_Clinica.ListarClinicas()
        if clinicas!= None:
            for n in range(3):
                for m in range(len(clinicas[n])):
                    item = QtGui.QTableWidgetItem(clinicas[n][m])
                    self.tableClinicas.setItem(m,n,item)

        self.btnCadastrarCli = QtGui.QPushButton(self.tabClinicas)
        self.btnCadastrarCli.setGeometry(QtCore.QRect(450, 130, 75, 23))
        self.btnCadastrarCli.setObjectName(_fromUtf8("btnCadastrarCli"))
        self.btnBuscaCli = QtGui.QPushButton(self.tabClinicas)
        self.btnBuscaCli.setGeometry(QtCore.QRect(390, 10, 41, 23))
        self.btnBuscaCli.setObjectName(_fromUtf8("btnBuscaCli"))
        self.campoBuscaCli = QtGui.QLineEdit(self.tabClinicas)
        self.campoBuscaCli.setGeometry(QtCore.QRect(20, 10, 201, 20))
        self.campoBuscaCli.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.campoBuscaCli.setText(_fromUtf8("Busca"))
        self.campoBuscaCli.setFrame(True)
        self.campoBuscaCli.setEchoMode(QtGui.QLineEdit.Normal)
        self.campoBuscaCli.setCursorPosition(5)
        self.campoBuscaCli.setReadOnly(False)
        self.campoBuscaCli.setObjectName(_fromUtf8("campoBuscaCli"))
        tabWidget.addTab(self.tabClinicas, _fromUtf8(""))

        # -------------------#consulta#----------------------------------------#

        self.tabConsultas = QtGui.QWidget()
        self.tabConsultas.setObjectName(_fromUtf8("tabConsultas"))
        self.tipoBuscaCons = QtGui.QComboBox(self.tabConsultas)
        self.tipoBuscaCons.setGeometry(QtCore.QRect(240, 10, 131, 22))
        self.tipoBuscaCons.setObjectName(_fromUtf8("tipoBuscaCons"))
        self.tipoBuscaCons.addItem(_fromUtf8(""))
        self.tipoBuscaCons.addItem(_fromUtf8(""))
        self.tipoBuscaCons.addItem(_fromUtf8(""))
        self.tipoBuscaCons.addItem(_fromUtf8(""))
        self.btnExcluirCons = QtGui.QPushButton(self.tabConsultas)
        self.btnExcluirCons.setGeometry(QtCore.QRect(450, 100, 75, 23))
        self.btnExcluirCons.setObjectName(_fromUtf8("btnExcluirCons"))
        self.btnEditarCons = QtGui.QPushButton(self.tabConsultas)
        self.btnEditarCons.setGeometry(QtCore.QRect(450, 70, 75, 23))
        self.btnEditarCons.setObjectName(_fromUtf8("btnEditarCons"))
        self.btnAtualizarCons = QtGui.QPushButton(self.tabConsultas)
        self.btnAtualizarCons.setGeometry(QtCore.QRect(450, 200, 75, 23))
        self.btnAtualizarCons.setObjectName(_fromUtf8("btnAtualizarCons"))

        self.tableConsultas = QtGui.QTableWidget(self.tabConsultas)
        self.tableConsultas.setGeometry(QtCore.QRect(20, 40, 421, 281))
        self.tableConsultas.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableConsultas.setObjectName(_fromUtf8("tableConsultas"))
        self.tableConsultas.setColumnCount(4)
        self.tableConsultas.setRowCount(CRUD_Clinica.QuantidadeConsultas())
        item = QtGui.QTableWidgetItem()
        self.tableConsultas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableConsultas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableConsultas.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableConsultas.setHorizontalHeaderItem(3, item)

        consultas = CRUD_Clinica.ListarConsultas()
        if consultas!=None:
            for n in range(4):
                for m in range(len(consultas[n])):
                    item = QtGui.QTableWidgetItem(consultas[n][m])
                    self.tableConsultas.setItem(m,n,item)

        self.btnCadastrarCons = QtGui.QPushButton(self.tabConsultas)
        self.btnCadastrarCons.setGeometry(QtCore.QRect(450, 130, 75, 23))
        self.btnCadastrarCons.setObjectName(_fromUtf8("btnCadastrarCons"))
        self.btnBuscaCons = QtGui.QPushButton(self.tabConsultas)
        self.btnBuscaCons.setGeometry(QtCore.QRect(390, 10, 41, 23))
        self.btnBuscaCons.setObjectName(_fromUtf8("btnBuscaCons"))
        self.campoBuscaCons = QtGui.QLineEdit(self.tabConsultas)
        self.campoBuscaCons.setGeometry(QtCore.QRect(20, 10, 201, 20))
        self.campoBuscaCons.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.campoBuscaCons.setText(_fromUtf8("Busca"))
        self.campoBuscaCons.setFrame(True)
        self.campoBuscaCons.setEchoMode(QtGui.QLineEdit.Normal)
        self.campoBuscaCons.setCursorPosition(5)
        self.campoBuscaCons.setReadOnly(False)
        self.campoBuscaCons.setObjectName(_fromUtf8("campoBuscaCons"))
        tabWidget.addTab(self.tabConsultas, _fromUtf8(""))

        # -------------------#empregado/clinicamedicos#----------------------------------------#

        self.tabEmpregados = QtGui.QWidget()
        self.tabEmpregados.setObjectName(_fromUtf8("tabEmpregados"))
        self.tipoBuscaEmp = QtGui.QComboBox(self.tabEmpregados)
        self.tipoBuscaEmp.setGeometry(QtCore.QRect(240, 10, 131, 22))
        self.tipoBuscaEmp.setObjectName(_fromUtf8("tipoBuscaEmp"))
        self.tipoBuscaEmp.addItem(_fromUtf8(""))
        self.tipoBuscaEmp.addItem(_fromUtf8(""))
        self.btnExcluirEmp = QtGui.QPushButton(self.tabEmpregados)
        self.btnExcluirEmp.setGeometry(QtCore.QRect(450, 100, 75, 23))
        self.btnExcluirEmp.setObjectName(_fromUtf8("btnExcluirEmp"))
        self.btnAtualizarEmp = QtGui.QPushButton(self.tabEmpregados)
        self.btnAtualizarEmp.setGeometry(QtCore.QRect(450, 200, 75, 23))
        self.btnAtualizarEmp.setObjectName(_fromUtf8("btnAtualizarEmp"))

        self.tableEmpregados = QtGui.QTableWidget(self.tabEmpregados)
        self.tableEmpregados.setGeometry(QtCore.QRect(20, 40, 421, 281))
        self.tableEmpregados.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableEmpregados.setObjectName(_fromUtf8("tableEmpregados"))
        self.tableEmpregados.setColumnCount(2)
        self.tableEmpregados.setRowCount(CRUD_Clinica.QuantidadeClinicaMedicos())
        item = QtGui.QTableWidgetItem()
        self.tableEmpregados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableEmpregados.setHorizontalHeaderItem(1, item)

        clinicaMedicos = CRUD_Clinica.ListarClinicaMedicos()
        if clinicaMedicos != None:
            for n in range(2):
                for m in range(len(clinicaMedicos[n])):
                    item = QtGui.QTableWidgetItem(clinicaMedicos[n][m])
                    self.tableEmpregados.setItem(m, n, item)

        self.btnCadastrarEmp = QtGui.QPushButton(self.tabEmpregados)
        self.btnCadastrarEmp.setGeometry(QtCore.QRect(450, 130, 75, 23))
        self.btnCadastrarEmp.setObjectName(_fromUtf8("btnCadastrarEmp"))
        self.btnBuscaEmp = QtGui.QPushButton(self.tabEmpregados)
        self.btnBuscaEmp.setGeometry(QtCore.QRect(390, 10, 41, 23))
        self.btnBuscaEmp.setObjectName(_fromUtf8("btnBuscaEmp"))
        self.campoBuscaEmp = QtGui.QLineEdit(self.tabEmpregados)
        self.campoBuscaEmp.setGeometry(QtCore.QRect(20, 10, 201, 20))
        self.campoBuscaEmp.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.campoBuscaEmp.setText(_fromUtf8("Busca"))
        self.campoBuscaEmp.setFrame(True)
        self.campoBuscaEmp.setEchoMode(QtGui.QLineEdit.Normal)
        self.campoBuscaEmp.setCursorPosition(5)
        self.campoBuscaEmp.setReadOnly(False)
        self.campoBuscaEmp.setObjectName(_fromUtf8("campoBuscaEmp"))
        tabWidget.addTab(self.tabEmpregados, _fromUtf8(""))

        self.retranslateUi(tabWidget)
        tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(tabWidget)
        self.runBtn()

    def retranslateUi(self, tabWidget):
        tabWidget.setWindowTitle(_translate("tabWidget", "Clínica Médica", None))
        self.tipoBuscaMed.setItemText(0, _translate("tabWidget", "Nome", None))
        self.tipoBuscaMed.setItemText(1, _translate("tabWidget", "Código", None))
        self.tipoBuscaMed.setItemText(2, _translate("tabWidget", "Código Especialidade", None))
        self.btnBuscaMed.setText(_translate("tabWidget", "Ir", None))
        self.btnCadastrarMed.setText(_translate("tabWidget", "Novo", None))
        self.btnEditarMed.setText(_translate("tabWidget", "Editar", None))
        self.btnAtualizarMed.setText(_translate("tabWidget","Atualizar",None))
        item = self.tableMedicos.horizontalHeaderItem(0)
        item.setText(_translate("tabWidget", "Código", None))
        item = self.tableMedicos.horizontalHeaderItem(1)
        item.setText(_translate("tabWidget", "Nome", None))
        item = self.tableMedicos.horizontalHeaderItem(2)
        item.setText(_translate("tabWidget", "Cód. Especialidade", None))
        self.btnExcluirMed.setText(_translate("tabWidget", "Excluir", None))
        tabWidget.setTabText(tabWidget.indexOf(self.tabMedicos), _translate("tabWidget", "Médicos", None))

        self.tipoBuscaEspec.setItemText(0, _translate("tabWidget", "Nome", None))
        self.tipoBuscaEspec.setItemText(1, _translate("tabWidget", "Código Especialidade", None))
        self.tipoBuscaEspec.setItemText(2, _translate("tabWidget", "Código Especialidade Genérica", None))
        self.btnExcluirEspec.setText(_translate("tabWidget", "Excluir", None))
        self.btnEditarEspec.setText(_translate("tabWidget", "Editar", None))
        self.btnAtualizarEspec.setText(_translate("tabWidget","Atualizar",None))
        item = self.tableEspecialidades.horizontalHeaderItem(0)
        item.setText(_translate("tabWidget", "Código", None))
        item = self.tableEspecialidades.horizontalHeaderItem(1)
        item.setText(_translate("tabWidget", "Nome", None))
        item = self.tableEspecialidades.horizontalHeaderItem(2)
        item.setText(_translate("tabWidget", "Cód Espec Genérica", None))
        self.btnCadastrarEspec.setText(_translate("tabWidget", "Novo", None))
        self.btnBuscaEspec.setText(_translate("tabWidget", "Ir", None))
        tabWidget.setTabText(tabWidget.indexOf(self.tabEspecialidades), _translate("tabWidget", "Especialidades", None))

        self.tipoBuscaCli.setItemText(0, _translate("tabWidget", "Nome", None))
        self.tipoBuscaCli.setItemText(1, _translate("tabWidget", "Código", None))
        self.tipoBuscaCli.setItemText(2, _translate("tabWidget", "Local", None))
        self.btnExcluirCli.setText(_translate("tabWidget", "Excluir", None))
        self.btnEditarCli.setText(_translate("tabWidget", "Editar", None))
        self.btnAtualizarCli.setText(_translate("tabWidget","Atualizar",None))
        item = self.tableClinicas.horizontalHeaderItem(0)
        item.setText(_translate("tabWidget", "Código", None))
        item = self.tableClinicas.horizontalHeaderItem(1)
        item.setText(_translate("tabWidget", "Nome", None))
        item = self.tableClinicas.horizontalHeaderItem(2)
        item.setText(_translate("tabWidget", "Local", None))
        self.btnCadastrarCli.setText(_translate("tabWidget", "Novo", None))
        self.btnBuscaCli.setText(_translate("tabWidget", "Ir", None))
        tabWidget.setTabText(tabWidget.indexOf(self.tabClinicas), _translate("tabWidget", "Clínicas", None))

        self.tipoBuscaCons.setItemText(0, _translate("tabWidget", "Data", None))
        self.tipoBuscaCons.setItemText(1, _translate("tabWidget", "Código Clínica", None))
        self.tipoBuscaCons.setItemText(2, _translate("tabWidget", "Código Médico", None))
        self.tipoBuscaCons.setItemText(3, _translate("tabWidget", "Hora", None))
        self.btnExcluirCons.setText(_translate("tabWidget", "Excluir", None))
        self.btnEditarCons.setText(_translate("tabWidget", "Editar", None))
        self.btnAtualizarCons.setText(_translate("tabWidget", "Atualizar", None))
        item = self.tableConsultas.horizontalHeaderItem(0)
        item.setText(_translate("tabWidget", "Cód Clínica", None))
        item = self.tableConsultas.horizontalHeaderItem(1)
        item.setText(_translate("tabWidget", "Cód Médico", None))
        item = self.tableConsultas.horizontalHeaderItem(2)
        item.setText(_translate("tabWidget", "Data", None))
        item = self.tableConsultas.horizontalHeaderItem(3)
        item.setText(_translate("tabWidget", "Hora", None))
        self.btnCadastrarCons.setText(_translate("tabWidget", "Novo", None))
        self.btnBuscaCons.setText(_translate("tabWidget", "Ir", None))
        tabWidget.setTabText(tabWidget.indexOf(self.tabConsultas), _translate("tabWidget", "Consultas", None))

        self.tipoBuscaEmp.setItemText(0, _translate("tabWidget", "Código Clínica", None))
        self.tipoBuscaEmp.setItemText(1, _translate("tabWidget", "Código Médico", None))
        self.btnExcluirEmp.setText(_translate("tabWidget", "Excluir", None))
        item = self.tableEmpregados.horizontalHeaderItem(0)
        item.setText(_translate("tabWidget", "Cód Clínica", None))
        item = self.tableEmpregados.horizontalHeaderItem(1)
        item.setText(_translate("tabWidget", "Cód Médico", None))
        self.btnCadastrarEmp.setText(_translate("tabWidget", "Novo", None))
        self.btnBuscaEmp.setText(_translate("tabWidget", "Ir", None))
        self.btnAtualizarEmp.setText(_translate("tabWidget", "Atualizar", None))
        tabWidget.setTabText(tabWidget.indexOf(self.tabEmpregados), _translate("tabWidget", "Empregados", None))

    def Run(self):
        tabWidget = QtGui.QTabWidget()
        ui = Ui_tabWidget()
        ui.setupUi(tabWidget)
        tabWidget.show()
        sys.exit(app.exec_())

    def runBtn(self):
        self.btnCadastrarMed.clicked.connect(self.runMedico)
        self.btnCadastrarCli.clicked.connect(self.runClinica)
        self.btnCadastrarCons.clicked.connect(self.runConsulta)
        self.btnCadastrarEmp.clicked.connect(self.runEmpregado)
        self.btnCadastrarEspec.clicked.connect(self.runEspecialidade)

        self.btnAtualizarMed.clicked.connect(self.atualizarMedicos)
        self.btnAtualizarEspec.clicked.connect(self.atualizarEspecialidades)
        self.btnAtualizarCli.clicked.connect(self.atualizarClinicas)
        self.btnAtualizarCons.clicked.connect(self.atualizarConsultas)
        self.btnAtualizarEmp.clicked.connect(self.atualizarEmpregados)

        self.btnBuscaMed.clicked.connect(self.buscarMedicos)
        self.btnBuscaCli.clicked.connect(self.buscarClinicas)
        self.btnBuscaCons.clicked.connect(self.buscarConsultas)
        self.btnBuscaEmp.clicked.connect(self.buscarEmpregados)
        self.btnBuscaEspec.clicked.connect(self.buscarEspecialidades)

        self.btnExcluirMed.clicked.connect(self.getRowMedDel)
        self.btnExcluirCli.clicked.connect(self.getRowCliDel)
        self.btnExcluirCons.clicked.connect(self.getRowConsDel)
        self.btnExcluirEmp.clicked.connect(self.getRowEmpDel)
        self.btnExcluirEspec.clicked.connect(self.getRowEspecDel)

        self.btnEditarMed.clicked.connect(self.getRowMedEdit)
        self.btnEditarCli.clicked.connect(self.getRowCliEdit)
        self.btnEditarCons.clicked.connect(self.getRowConsEdit)
        self.btnEditarEspec.clicked.connect(self.getRowEspecEdit)


# -------------------------getRowsObject-----------------------------------------#
    def getRowMedEdit(self):
        linha = self.tableMedicos.currentRow()
        codMed = self.tableMedicos.item(linha,0)
        if codMed != None:
            codMed = codMed.text()
            self.runEditarMedico(codMed)
        else:
            self.popUp("Selecione algum médico para editar!")

    def getRowMedDel(self):
        linha = self.tableMedicos.currentRow()
        codMed = self.tableMedicos.item(linha,0)
        if codMed != None:
            codMed = codMed.text()
            self.runExcluirMedico(codMed)
        else:
            self.popUp("Selecione algum médico para excluir!")

    def getRowEspecEdit(self):
        linha = self.tableEspecialidades.currentRow()
        codEspec = self.tableEspecialidades.item(linha,0)
        if codEspec != None:
            codEspec = codEspec.text()
            self.runEditarEspecialidade(codEspec)
        else:
            self.popUp("Selecione alguma especialidade para editar!")

    def getRowEspecDel(self):
        linha = self.tableEspecialidades.currentRow()
        codEspec = self.tableEspecialidades.item(linha,0)
        if codEspec != None:
            codEspec = codEspec.text()
            self.runExcluirEspecialidade(codEspec)
        else:
            self.popUp("Selecione alguma especialidade para excluir!")

    def getRowCliEdit(self):
        linha = self.tableClinicas.currentRow()
        codCli = self.tableClinicas.item(linha,0)
        if codCli != None:
            codCli = codCli.text()
            self.runEditarClinica(codCli)
        else:
            self.popUp("Selecione alguma clínica para editar!")

    def getRowCliDel(self):
        linha = self.tableClinicas.currentRow()
        codCli = self.tableClinicas.item(linha,0)
        if codCli != None:
            codCli = codCli.text()
            self.runExcluirClinica(codCli)
        else:
            self.popUp("Selecione alguma clínica para excluir!")

    def getRowConsEdit(self):
        linha = self.tableConsultas.currentRow()
        codCli = self.tableConsultas.item(linha,0)
        codMed = self.tableConsultas.item(linha,1)
        data = self.tableConsultas.item(linha,2)
        hora = self.tableConsultas.item(linha,3)
        if codCli!= None and codMed!=None:
            codCli = codCli.text()
            codMed = codMed.text()
            data = data.text()
            hora = hora.text()
            self.runEditarConsulta(codCli,codMed,data,hora)
        else:
            self.popUp("Selecione alguma consulta para editar!")

    def getRowConsDel(self):
        linha = self.tableConsultas.currentRow()
        codCli = self.tableConsultas.item(linha,0)
        codMed = self.tableConsultas.item(linha,1)
        data = self.tableConsultas.item(linha,2)
        hora = self.tableConsultas.item(linha,3)
        if codCli!= None and codMed != None:
            codCli = codCli.text()
            codMed = codMed.text()
            data = data.text()
            hora = hora.text()
            self.runExcluirConsulta(codCli,codMed,data,hora)
        else:
            self.popUp("Selecione alguma consulta para excluir!")

    def getRowEmpDel(self):
        linha = self.tableEmpregados.currentRow()
        codCli = self.tableEmpregados.item(linha,0)
        codMed = self.tableEmpregados.item(linha,1)
        if codCli!=None and codMed!=None:
            codCli = codCli.text()
            codMed = codMed.text()
            self.runExcluirEmpregado(codCli,codMed)
        else:
            self.popUp("Selecione algum empregado para excluir!")

#-------------------------runDialogsCadastro-----------------------------------------#
    def runMedico(self):
        import CadastroMedico
        medico = CadastroMedico.Ui_DialogMed()
        medico.run()


    def runClinica(self):
        import CadastroClinica
        clinica = CadastroClinica.Ui_DialogCli()
        clinica.Run()

    def runConsulta(self):
        import CadastroConsulta
        consulta = CadastroConsulta.Ui_DialogAgenCons()
        consulta.run()

    def runEmpregado(self):
        import CadastroEmpregado
        empregado = CadastroEmpregado.Ui_DialogEmp()
        empregado.run()

    def runEspecialidade(self):
        import CadastroEspecialidade
        especialidade = CadastroEspecialidade.Ui_DialogEspec()
        especialidade.Run()

# -------------------------runDialogsExcluir-----------------------------------------#

    def runExcluirMedico(self,codMed):
        import ExcluirMedico
        medico = ExcluirMedico.Ui_DialogMed()
        medico.run(codMed)

    def runExcluirClinica(self,codCli):
        import ExcluirClinica
        clinica = ExcluirClinica.Ui_DialogCli()
        clinica.run(codCli)

    def runExcluirEspecialidade(self,codEspec):
        import ExcluirEspecialidade
        especialidade = ExcluirEspecialidade.Ui_DialogEspec()
        especialidade.run(codEspec)

    def runExcluirConsulta(self,codCli,codMed,data,hora):
        import ExcluirConsulta
        consulta = ExcluirConsulta.Ui_DialogAgenCons()
        consulta.run(codCli,codMed,data,hora)

    def runExcluirEmpregado(self,codCli,codMed):
        import ExcluirEmpregado
        empregado = ExcluirEmpregado.Ui_DialogEmp()
        empregado.run(codCli,codMed)

# -------------------------runDialogsEditar-----------------------------------------#
    def runEditarMedico(self,codMed):
        import EditarMedico
        medico = EditarMedico.Ui_DialogMed()
        medico.run(codMed)

    def runEditarEspecialidade(self,codEspec):
        import EditarEspecialidade
        especialidade = EditarEspecialidade.Ui_DialogEspec()
        especialidade.run(codEspec)

    def runEditarClinica(self,codCli):
        import EditarClinica
        clinica = EditarClinica.Ui_DialogCli()
        clinica.run(codCli)

    def runEditarConsulta(self,codCli,codMed,data,hora):
        EditarConsulta
        consulta = EditarConsulta.Ui_DialogAgenCons()
        consulta.run(codCli,codMed,data,hora)
#------------------------------atualizar------------------------------------------#

    def atualizarMedicos(self):
        novaQuantidadeMedicos = CRUD_Clinica.QuantidadeMedicos()
        self.tableMedicos.setRowCount(novaQuantidadeMedicos)

        medicos = CRUD_Clinica.ListarMedicos()
        if medicos != None:
            for n in range(3):
                for m in range(len(medicos[n])):
                    item = QtGui.QTableWidgetItem(medicos[n][m])
                    self.tableMedicos.setItem(m,n,item)
        else:
            self.popUp("Não há médicos cadastrados!")

    def atualizarEspecialidades(self):
        novaQuantidadeEspecialidades = CRUD_Clinica.QuantidadeEspecialidades()
        self.tableEspecialidades.setRowCount(novaQuantidadeEspecialidades)

        especialidades = CRUD_Clinica.ListarEspecialidades()
        if especialidades != None:
            for n in range(3):
                for m in range(len(especialidades[n])):
                    item = QtGui.QTableWidgetItem(especialidades[n][m])
                    self.tableEspecialidades.setItem(m, n, item)
        else:
            self.popUp("Não há especialidades cadastradas!")

    def atualizarClinicas(self):
        novaQuantidadeClinicas = CRUD_Clinica.QuantidadeClinicas()
        self.tableClinicas.setRowCount(novaQuantidadeClinicas)

        clinicas = CRUD_Clinica.ListarClinicas()
        if clinicas != None:
            for n in range(3):
                for m in range(len(clinicas[n])):
                    item = QtGui.QTableWidgetItem(clinicas[n][m])
                    self.tableClinicas.setItem(m,n,item)
        else:
            self.popUp("Não há clínicas cadastradas!")

    def atualizarConsultas(self):
        novaQuantidadeConsultas = CRUD_Clinica.QuantidadeConsultas()
        self.tableConsultas.setRowCount(novaQuantidadeConsultas)

        consultas = CRUD_Clinica.ListarConsultas()
        if consultas != None:
            for n in range(4):
                for m in range(len(consultas[n])):
                    item = QtGui.QTableWidgetItem(consultas[n][m])
                    self.tableConsultas.setItem(m,n,item)
        else:
            self.popUp("Não há consultas cadastradas!")

    def atualizarEmpregados(self):
        novaQuantidadeEmpregados = CRUD_Clinica.QuantidadeClinicaMedicos()
        self.tableEmpregados.setRowCount(novaQuantidadeEmpregados)

        empregados = CRUD_Clinica.ListarClinicaMedicos()
        if empregados != None:
            for n in range(2):
                for m in range(len(empregados[n])):
                    item = QtGui.QTableWidgetItem(empregados[n][m])
                    self.tableEmpregados.setItem(m,n,item)
        else:
            self.popUp("Não há empregados cadastrados!")

#-----------------------------buscar--------------------------------------------#
            # NAO ALTERAR A ORDEM DAS VARIAVEIS  #

    def buscarMedicos(self):
        palavra = self.campoBuscaMed.text()
        tipoBusca = self.tipoBuscaMed.currentIndex()
        if len(palavra)!=0:
            if tipoBusca == 0:
                resultado,boolean,menssagem = CRUD_Clinica.BuscarNomeMedico(palavra)
            elif tipoBusca == 1:
                resultado,boolean,menssagem = CRUD_Clinica.BuscarMedicoCod(palavra)
        if tipoBusca == 2:
            resultado,boolean,menssagem = CRUD_Clinica.BuscarEspecialidadeMedico(palavra)

        if menssagem!=None:
            self.popUp(menssagem)

        self.tableMedicos.clearContents()

        for n in range(3):
            for m in range(len(resultado[n])):
                item = QtGui.QTableWidgetItem(resultado[n][m])
                self.tableMedicos.setItem(m,n,item)

    def buscarEspecialidades(self):
        palavra = self.campoBuscaEspec.text()
        tipoBusca = self.tipoBuscaEspec.currentIndex()
        if len(palavra)!=0:
            if tipoBusca == 0:
                resultado, boolean, menssagem = CRUD_Clinica.BuscarNomeEspecialidade(palavra)
            elif tipoBusca == 1:
                resultado, boolean, menssagem = CRUD_Clinica.BuscarCodEspecialidade(palavra)
        if tipoBusca == 2:
            resultado, boolean, menssagem = CRUD_Clinica.BuscarCodEspecialidadeGenerica(palavra)

        if menssagem != None:
            self.popUp(menssagem)

        self.tableEspecialidades.clearContents()

        for n in range(3):
            for m in range(len(resultado[n])):
                item = QtGui.QTableWidgetItem(resultado[n][m])
                self.tableEspecialidades.setItem(m,n,item)

    def buscarClinicas(self):
        palavra = self.campoBuscaCli.text()
        tipoBusca = self.tipoBuscaCli.currentIndex()
        if len(palavra) != 0:
            if tipoBusca == 0:
                resultado, boolean, menssagem = CRUD_Clinica.BuscarNomeClinica(palavra)
            elif tipoBusca == 1:
                resultado, boolean, menssagem = CRUD_Clinica.BuscarClinicaCod(palavra)
            elif tipoBusca == 2:
                resultado, boolean, menssagem = CRUD_Clinica.BuscarLocalClinica(palavra)

        if menssagem != None:
            self.popUp(menssagem)

        self.tableClinicas.clearContents()

        for n in range(3):
            for m in range(len(resultado[n])):
                item = QtGui.QTableWidgetItem(resultado[n][m])
                self.tableClinicas.setItem(m,n,item)

    def buscarConsultas(self):
        palavra = self.campoBuscaCons.text()
        tipoBusca = self.tipoBuscaCons.currentIndex()
        if len(palavra) != 0:
            if tipoBusca == 0:
                resultado, boolean, menssagem = CRUD_Clinica.BuscarConsultaData(palavra)
            elif tipoBusca == 1:
                resultado, boolean, menssagem = CRUD_Clinica.BuscarConsultaCodClinica(palavra)
            elif tipoBusca == 2:
                resultado, boolean, menssagem = CRUD_Clinica.BuscarConsultaCodMedico(palavra)
            elif tipoBusca == 3:
                resultado, boolean, menssagem = CRUD_Clinica.BuscarConsultaHora(palavra)

        if menssagem != None:
            self.popUp(menssagem)

        self.tableConsultas.clearContents()

        for n in range(4):
            for m in range(len(resultado[n])):
                item = QtGui.QTableWidgetItem(resultado[n][m])
                self.tableConsultas.setItem(m,n,item)

    def buscarEmpregados(self):
        palavra = self.campoBuscaEmp.text()
        tipoBusca = self.tipoBuscaEmp.currentIndex()
        if len(palavra) != 0:
            if tipoBusca == 0:
                resultado, boolean, menssagem = CRUD_Clinica.BuscarCodMed(palavra)
            elif tipoBusca == 1:
                resultado, boolean, menssagem = CRUD_Clinica.BuscarCodCli(palavra)

        if menssagem != None:
            self.popUp(menssagem)

        self.tableEmpregados.clearContents()

        for n in range(2):
            for m in range(len(resultado[n])):
                item = QtGui.QTableWidgetItem(resultado[n][m])
                self.tableEmpregados.setItem(m,n,item)


#-------------------------PopUp------------------------------------------------#
    def popUp(self, msg):
        mensagem = QtGui.QMessageBox()
        mensagem.setWindowTitle("Aviso")
        mensagem.setText(msg)
        mensagem.setStandardButtons(mensagem.Ok)
        mensagem.exec_()
#-------------------------------------------------------------------------#

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    tabWidget = QtGui.QTabWidget()
    ui = Ui_tabWidget()
    ui.setupUi(tabWidget)
    tabWidget.show()
    sys.exit(app.exec_())

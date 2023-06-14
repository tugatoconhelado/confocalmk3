# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'record_cpsQsUsPT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.9
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

from pyqtgraph import PlotWidget


class Ui_timetrace(object):
    def setupUi(self, timetrace):
        if not timetrace.objectName():
            timetrace.setObjectName(u"timetrace")
        timetrace.resize(712, 531)
        self.verticalLayout_6 = QVBoxLayout(timetrace)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.control_cps_layout = QHBoxLayout()
        self.control_cps_layout.setObjectName(u"control_cps_layout")
        self.run_cps_button = QPushButton(timetrace)
        self.run_cps_button.setObjectName(u"run_cps_button")

        self.control_cps_layout.addWidget(self.run_cps_button)

        self.stop_button = QPushButton(timetrace)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"color: rgb(255, 0, 0);")

        self.control_cps_layout.addWidget(self.stop_button)

        self.cps_value_layout = QHBoxLayout()
        self.cps_value_layout.setObjectName(u"cps_value_layout")
        self.cps_text_label = QLabel(timetrace)
        self.cps_text_label.setObjectName(u"cps_text_label")
        self.cps_text_label.setFrameShape(QFrame.NoFrame)
        self.cps_text_label.setFrameShadow(QFrame.Plain)

        self.cps_value_layout.addWidget(self.cps_text_label)

        self.cps_label = QLabel(timetrace)
        self.cps_label.setObjectName(u"cps_label")

        self.cps_value_layout.addWidget(self.cps_label)

        self.cps_units_label = QLabel(timetrace)
        self.cps_units_label.setObjectName(u"cps_units_label")

        self.cps_value_layout.addWidget(self.cps_units_label)


        self.control_cps_layout.addLayout(self.cps_value_layout)


        self.verticalLayout_6.addLayout(self.control_cps_layout)

        self.acquisition_cps_layout = QHBoxLayout()
        self.acquisition_cps_layout.setObjectName(u"acquisition_cps_layout")
        self.refresh_time_label = QLabel(timetrace)
        self.refresh_time_label.setObjectName(u"refresh_time_label")

        self.acquisition_cps_layout.addWidget(self.refresh_time_label)

        self.refresh_time_edit = QLineEdit(timetrace)
        self.refresh_time_edit.setObjectName(u"refresh_time_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_time_edit.sizePolicy().hasHeightForWidth())
        self.refresh_time_edit.setSizePolicy(sizePolicy)

        self.acquisition_cps_layout.addWidget(self.refresh_time_edit)

        self.samp_freq_label = QLabel(timetrace)
        self.samp_freq_label.setObjectName(u"samp_freq_label")

        self.acquisition_cps_layout.addWidget(self.samp_freq_label)

        self.samp_freq_edit = QLineEdit(timetrace)
        self.samp_freq_edit.setObjectName(u"samp_freq_edit")
        sizePolicy.setHeightForWidth(self.samp_freq_edit.sizePolicy().hasHeightForWidth())
        self.samp_freq_edit.setSizePolicy(sizePolicy)

        self.acquisition_cps_layout.addWidget(self.samp_freq_edit)

        self.samp_avg_label = QLabel(timetrace)
        self.samp_avg_label.setObjectName(u"samp_avg_label")

        self.acquisition_cps_layout.addWidget(self.samp_avg_label)

        self.samples_avg_edit = QLineEdit(timetrace)
        self.samples_avg_edit.setObjectName(u"samples_avg_edit")
        sizePolicy.setHeightForWidth(self.samples_avg_edit.sizePolicy().hasHeightForWidth())
        self.samples_avg_edit.setSizePolicy(sizePolicy)

        self.acquisition_cps_layout.addWidget(self.samples_avg_edit)


        self.verticalLayout_6.addLayout(self.acquisition_cps_layout)

        self.stats_layout = QHBoxLayout()
        self.stats_layout.setObjectName(u"stats_layout")
        self.stats_checkbox_layout = QVBoxLayout()
        self.stats_checkbox_layout.setObjectName(u"stats_checkbox_layout")
        self.std_cps_checkbox = QCheckBox(timetrace)
        self.std_cps_checkbox.setObjectName(u"std_cps_checkbox")

        self.stats_checkbox_layout.addWidget(self.std_cps_checkbox)

        self.mean_cps_checkbox = QCheckBox(timetrace)
        self.mean_cps_checkbox.setObjectName(u"mean_cps_checkbox")

        self.stats_checkbox_layout.addWidget(self.mean_cps_checkbox)


        self.stats_layout.addLayout(self.stats_checkbox_layout)

        self.stats_value_layout = QVBoxLayout()
        self.stats_value_layout.setObjectName(u"stats_value_layout")
        self.std_cps_label = QLabel(timetrace)
        self.std_cps_label.setObjectName(u"std_cps_label")

        self.stats_value_layout.addWidget(self.std_cps_label)

        self.mean_cps_label = QLabel(timetrace)
        self.mean_cps_label.setObjectName(u"mean_cps_label")

        self.stats_value_layout.addWidget(self.mean_cps_label)


        self.stats_layout.addLayout(self.stats_value_layout)

        self.save_load_layout = QVBoxLayout()
        self.save_load_layout.setObjectName(u"save_load_layout")
        self.save_button = QPushButton(timetrace)
        self.save_button.setObjectName(u"save_button")

        self.save_load_layout.addWidget(self.save_button)

        self.load_layout = QHBoxLayout()
        self.load_layout.setObjectName(u"load_layout")
        self.load_button = QPushButton(timetrace)
        self.load_button.setObjectName(u"load_button")

        self.load_layout.addWidget(self.load_button)

        self.previous_button = QPushButton(timetrace)
        self.previous_button.setObjectName(u"previous_button")

        self.load_layout.addWidget(self.previous_button)

        self.next_button = QPushButton(timetrace)
        self.next_button.setObjectName(u"next_button")

        self.load_layout.addWidget(self.next_button)


        self.save_load_layout.addLayout(self.load_layout)


        self.stats_layout.addLayout(self.save_load_layout)


        self.verticalLayout_6.addLayout(self.stats_layout)

        self.cps_plot = PlotWidget(timetrace)
        self.cps_plot.setObjectName(u"cps_plot")

        self.verticalLayout_6.addWidget(self.cps_plot)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(3, 5)

        self.retranslateUi(timetrace)

        QMetaObject.connectSlotsByName(timetrace)
    # setupUi

    def retranslateUi(self, timetrace):
        timetrace.setWindowTitle(QCoreApplication.translate("timetrace", u"Record CPS", None))
        self.run_cps_button.setText(QCoreApplication.translate("timetrace", u"Run CPS", None))
        self.stop_button.setText(QCoreApplication.translate("timetrace", u"Stop", None))
        self.cps_text_label.setText(QCoreApplication.translate("timetrace", u"CPS", None))
        self.cps_label.setText(QCoreApplication.translate("timetrace", u"TextLabel", None))
        self.cps_units_label.setText(QCoreApplication.translate("timetrace", u"cts/sec", None))
        self.refresh_time_label.setText(QCoreApplication.translate("timetrace", u"Refresh time (sec)", None))
        self.samp_freq_label.setText(QCoreApplication.translate("timetrace", u"Samp Freq", None))
        self.samp_avg_label.setText(QCoreApplication.translate("timetrace", u"Window Time (sec)", None))
        self.std_cps_checkbox.setText(QCoreApplication.translate("timetrace", u"Standard Deviation", None))
        self.mean_cps_checkbox.setText(QCoreApplication.translate("timetrace", u"Mean", None))
        self.std_cps_label.setText(QCoreApplication.translate("timetrace", u"0.001", None))
        self.mean_cps_label.setText(QCoreApplication.translate("timetrace", u"10", None))
        self.save_button.setText(QCoreApplication.translate("timetrace", u"Save", None))
        self.load_button.setText(QCoreApplication.translate("timetrace", u"Load", None))
        self.previous_button.setText(QCoreApplication.translate("timetrace", u"Previous", None))
        self.next_button.setText(QCoreApplication.translate("timetrace", u"Next", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'record_cpsIbOpIJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_record_cps(object):
    def setupUi(self, record_cps):
        if not record_cps.objectName():
            record_cps.setObjectName(u"record_cps")
        record_cps.resize(799, 597)
        self.verticalLayout_6 = QVBoxLayout(record_cps)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.control_cps_layout = QHBoxLayout()
        self.control_cps_layout.setObjectName(u"control_cps_layout")
        self.run_cps_button = QPushButton(record_cps)
        self.run_cps_button.setObjectName(u"run_cps_button")

        self.control_cps_layout.addWidget(self.run_cps_button)

        self.stop_button = QPushButton(record_cps)
        self.stop_button.setObjectName(u"stop_button")

        self.control_cps_layout.addWidget(self.stop_button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cps_text_label = QLabel(record_cps)
        self.cps_text_label.setObjectName(u"cps_text_label")
        self.cps_text_label.setFrameShape(QFrame.NoFrame)
        self.cps_text_label.setFrameShadow(QFrame.Plain)

        self.horizontalLayout.addWidget(self.cps_text_label)

        self.cps_label = QLabel(record_cps)
        self.cps_label.setObjectName(u"cps_label")

        self.horizontalLayout.addWidget(self.cps_label)


        self.control_cps_layout.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.control_cps_layout)

        self.acquisition_cps_layout = QHBoxLayout()
        self.acquisition_cps_layout.setObjectName(u"acquisition_cps_layout")
        self.refresh_time_label = QLabel(record_cps)
        self.refresh_time_label.setObjectName(u"refresh_time_label")

        self.acquisition_cps_layout.addWidget(self.refresh_time_label)

        self.refresh_time_edit = QLineEdit(record_cps)
        self.refresh_time_edit.setObjectName(u"refresh_time_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refresh_time_edit.sizePolicy().hasHeightForWidth())
        self.refresh_time_edit.setSizePolicy(sizePolicy)

        self.acquisition_cps_layout.addWidget(self.refresh_time_edit)

        self.samp_freq_label = QLabel(record_cps)
        self.samp_freq_label.setObjectName(u"samp_freq_label")

        self.acquisition_cps_layout.addWidget(self.samp_freq_label)

        self.samp_freq_edit = QLineEdit(record_cps)
        self.samp_freq_edit.setObjectName(u"samp_freq_edit")
        sizePolicy.setHeightForWidth(self.samp_freq_edit.sizePolicy().hasHeightForWidth())
        self.samp_freq_edit.setSizePolicy(sizePolicy)

        self.acquisition_cps_layout.addWidget(self.samp_freq_edit)

        self.samp_avg_label = QLabel(record_cps)
        self.samp_avg_label.setObjectName(u"samp_avg_label")

        self.acquisition_cps_layout.addWidget(self.samp_avg_label)

        self.samples_avg_edit = QLineEdit(record_cps)
        self.samples_avg_edit.setObjectName(u"samples_avg_edit")
        sizePolicy.setHeightForWidth(self.samples_avg_edit.sizePolicy().hasHeightForWidth())
        self.samples_avg_edit.setSizePolicy(sizePolicy)

        self.acquisition_cps_layout.addWidget(self.samples_avg_edit)


        self.verticalLayout_6.addLayout(self.acquisition_cps_layout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stats_checkbox_layout = QVBoxLayout()
        self.stats_checkbox_layout.setObjectName(u"stats_checkbox_layout")
        self.std_cps_checkbox = QCheckBox(record_cps)
        self.std_cps_checkbox.setObjectName(u"std_cps_checkbox")

        self.stats_checkbox_layout.addWidget(self.std_cps_checkbox)

        self.mean_cps_checkbox = QCheckBox(record_cps)
        self.mean_cps_checkbox.setObjectName(u"mean_cps_checkbox")

        self.stats_checkbox_layout.addWidget(self.mean_cps_checkbox)


        self.horizontalLayout_3.addLayout(self.stats_checkbox_layout)

        self.stats_value_layout = QVBoxLayout()
        self.stats_value_layout.setObjectName(u"stats_value_layout")
        self.std_cps_label = QLabel(record_cps)
        self.std_cps_label.setObjectName(u"std_cps_label")

        self.stats_value_layout.addWidget(self.std_cps_label)

        self.mean_cps_label = QLabel(record_cps)
        self.mean_cps_label.setObjectName(u"mean_cps_label")

        self.stats_value_layout.addWidget(self.mean_cps_label)


        self.horizontalLayout_3.addLayout(self.stats_value_layout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.cps_plot = PlotWidget(record_cps)
        self.cps_plot.setObjectName(u"cps_plot")

        self.verticalLayout_6.addWidget(self.cps_plot)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(3, 5)

        self.retranslateUi(record_cps)

        QMetaObject.connectSlotsByName(record_cps)
    # setupUi

    def retranslateUi(self, record_cps):
        record_cps.setWindowTitle(QCoreApplication.translate("record_cps", u"Record CPS", None))
        self.run_cps_button.setText(QCoreApplication.translate("record_cps", u"Run CPS", None))
        self.stop_button.setText(QCoreApplication.translate("record_cps", u"Stop", None))
        self.cps_text_label.setText(QCoreApplication.translate("record_cps", u"CPS", None))
        self.cps_label.setText(QCoreApplication.translate("record_cps", u"TextLabel", None))
        self.refresh_time_label.setText(QCoreApplication.translate("record_cps", u"Refresh time (sec)", None))
        self.samp_freq_label.setText(QCoreApplication.translate("record_cps", u"Samp Freq", None))
        self.samp_avg_label.setText(QCoreApplication.translate("record_cps", u"Samples Avg", None))
        self.std_cps_checkbox.setText(QCoreApplication.translate("record_cps", u"Standard Deviation", None))
        self.mean_cps_checkbox.setText(QCoreApplication.translate("record_cps", u"Mean", None))
        self.std_cps_label.setText(QCoreApplication.translate("record_cps", u"0.001", None))
        self.mean_cps_label.setText(QCoreApplication.translate("record_cps", u"10", None))
    # retranslateUi


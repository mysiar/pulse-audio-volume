import os
import pulsectl
from UIMainWindowForm import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QComboBox
from PyQt5.QtCore import Qt
import app_info


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__pulse = None
        self.__sinks = list()
        self.__activeSink = None

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__setup()

    def __setup(self):
        self.setWindowTitle(app_info.TITLE)
        self.setMinimumWidth(self.width())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMaximumHeight(self.height())
        self.__ui.sinks.currentIndexChanged.connect(self.__set_active_sink)

        self.__ui.volumeStep.setEditable(True)
        le = self.__ui.volumeStep.lineEdit()
        le.setAlignment(Qt.AlignCenter)
        self.__ui.volumeStep.addItems(['10%', '20%', '30%'])
        le.setReadOnly(True)
        self.__ui.volumeStep.setEditable(False)
        self.__ui.volumeUp.clicked.connect(self.__volume_up)
        self.__ui.volumeDown.clicked.connect(self.__volume_down)

        self.__ui.sinks.setInsertPolicy(QComboBox.InsertAlphabetically)
        with pulsectl.Pulse('pulse-audio-volume') as pulse:
            for sink in pulse.sink_list():
                self.__sinks.append(sink)
                self.__ui.sinks.addItem(sink.description)

        self.__pulse = pulse

    def __find_sink_by_description(self, description):
        for sink in self.__sinks:
            if sink.description == description:
                return sink

    def __set_active_sink(self):
        item = str(self.__ui.sinks.currentText())
        self.__activeSink = self.__find_sink_by_description(item)

    def __volume_up(self):
        # self.__pulse.volume_change_all_chans(self.__activeSink, float(self.__ui.volumeStep.currentText()))
        # pactl set-sink-volume 'alsa_output.pci-0000_00_1f.3.analog-stereo' +10%
        # due to Assertion 'c' failed at pulse/introspect.c:1421, function pa_context_set_sink_volume_by_index()
        command = "pactl set-sink-volume '" + self.__activeSink.name + "' " + "+" + self.__ui.volumeStep.currentText()
        os.system(command)

    def __volume_down(self):
        # self.__pulse.volume_change_all_chans(self.__activeSink, -1 * float(self.__ui.volumeStep.currentText()))
        command = "pactl set-sink-volume '" + self.__activeSink.name + "' " + "-" + self.__ui.volumeStep.currentText()
        os.system(command)

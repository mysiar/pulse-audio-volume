import os
import pulsectl

from Sink import Sink
from UIMainWindowForm import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QComboBox
import app_info


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__sinks = list()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.__setup()

    def __setup(self):
        self.setWindowTitle(app_info.TITLE)
        self.setMinimumWidth(self.width())
        self.setMaximumWidth(self.width())
        self.setMinimumHeight(self.height())
        self.setMaximumHeight(self.height())
        self.__ui.volumeStep.addItems(['10%', '20%', '30%'])

        self.__ui.sinks.setInsertPolicy(QComboBox.InsertAlphabetically)
        with pulsectl.Pulse('pulse-audio-volume') as pulse:
            for _sink in pulse.sink_list():
                sink = Sink()
                sink.name = _sink.name
                sink.description = _sink.description
                sink.volume = _sink.volume.values[0]
                sink.pulse = pulse
                sink.muted = False
                self.__sinks.append(sink)
                self.__ui.sinks.addItem(sink.description)

        self.__ui.sinks.currentIndexChanged.connect(self.__set_active_sink)
        self.__ui.volumeMute.clicked.connect(self.__volume_mute_toggle)
        self.__ui.volumeUp.clicked.connect(self.__volume_up)
        self.__ui.volumeDown.clicked.connect(self.__volume_down)

    def __find_sink_by_description(self, description):
        for sink in self.__sinks:
            if sink.description == description:
                return sink

    def __set_active_sink(self):
        sink = self.__get_current_sink()
        if sink.muted:
            self.__ui.volumeMute.setText('Muted')
        else:
            self.__ui.volumeMute.setText('Mute')

    def __volume_up(self):
        # self.__pulse.volume_change_all_chans(self.__activeSink, float(self.__ui.volumeStep.currentText()))
        # pactl set-sink-volume 'alsa_output.pci-0000_00_1f.3.analog-stereo' +10%
        # due to Assertion 'c' failed at pulse/introspect.c:1421, function
        # pa_context_set_sink_volume_by_index()
        sink = self.__get_current_sink()
        command = "pactl set-sink-volume '" + sink.name + \
            "' " + "+" + self.__ui.volumeStep.currentText()
        os.system(command)

    def __volume_down(self):
        # self.__pulse.volume_change_all_chans(self.__activeSink, -1 * float(self.__ui.volumeStep.currentText()))
        sink = self.__get_current_sink()
        command = "pactl set-sink-volume '" + sink.name + \
            "' " + "-" + self.__ui.volumeStep.currentText()
        os.system(command)

    def __get_volume(self):
        return self.__activeSink.volume

    def __volume_mute_toggle(self):
        sink = self.__get_current_sink()
        if sink.muted:
            self.__unmute()
        else:
            self.__mute()

    def __mute(self):
        sink = self.__get_current_sink()
        # pactl set-sink-mute 'alsa_output.pci-0000_00_1f.3.analog-stereo' true
        command = "pactl set-sink-mute '" + sink.name + "' true"
        os.system(command)
        self.__ui.volumeMute.setText('Unmute')
        sink.muted = True

    def __unmute(self):
        sink = self.__get_current_sink()
        # pactl set-sink-mute 'alsa_output.pci-0000_00_1f.3.analog-stereo' true
        command = "pactl set-sink-mute '" + sink.name + "' false"
        os.system(command)
        self.__ui.volumeMute.setText('Mute')
        sink.muted = False

    def __get_current_sink(self):
        return self.__get_sink_by_description(
            str(self.__ui.sinks.currentText()))

    def __get_sink_by_description(self, description):
        for sink in self.__sinks:
            if description == sink.description:
                return sink

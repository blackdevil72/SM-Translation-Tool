# -*- coding: utf-8 -*-
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import \
    QApplication, QPushButton, QLabel, QListWidget, QListWidgetItem, QFileDialog
from PySide2.QtCore import QFile, QThread, Signal
import sys
import time
from configparser import RawConfigParser
import codecs
from loguru import logger
import os
from platform import platform


from ressources import qt_resource_data, qt_resource_name, qt_resource_struct
from model import Plugin, Session

logger.info(os.name)
logger.info(platform())


class Worker(QThread):
    start_state = Signal()
    end_state = Signal()
    updateData = Signal()

    def __init__(self):
        QThread.__init__(self)

    def run(self):
        self.start_state.emit()
        time.sleep(2)
        self.updateData.emit()
        self.end_state.emit()


class Main:
    page = 0

    def __init__(self):
        # init config
        self.config = RawConfigParser()
        self.config.read_file(codecs.open('config.ini', encoding='utf8'))

        logger.info('Configuration loaded')
        # init database
        self.session = Session()

        # init Qt windows
        self.app = QApplication(sys.argv)
        self.file = QFile("main_window.ui")
        self.file.open(QFile.ReadOnly)
        self.loader = QUiLoader()

        self.window = self.loader.load(self.file)

        self.update_mpc_plugin_list()

        self.window.findChild(QLabel, 'mpc_title_frame_title').setText(self.config['options']['project_name'])
        self.window.setWindowTitle(self.config['options']['project_name'])
        self.window.findChild(QPushButton, 'mpc_btn_import').clicked.connect(self.import_plugin)

        self.window.show()

        # todo: Delete this part before first release
        self.garbage_test_code()
        sys.exit(self.app.exec_())

    def update_mpc_plugin_list(self):
        list_ = self.window.findChild(QListWidget, 'mpc_plugins_list')
        list_.clear()
        for plugin in self.session.query(Plugin.name, Plugin.id):
            list_.addItem(QListWidgetItem(plugin.name))

    def import_plugin(self):
        path = QFileDialog.getExistingDirectory(dir=self.config['history']['last_open_folder'])
        if path:
            logger.debug(f'Selected path: {path}')
            name = path.split('/')[-1]
            p = Plugin(name=name, path=path)
            self.session.add(p)
            self.session.commit()
            self.update_mpc_plugin_list()


    def garbage_test_code(self):
        # p = Plugin(name='Hide & Seek', path="C:\\Users\\Tamer\\PycharmProjects\\SM-Translation-Tool\\Test")
        # self.session.add(p)
        # self.session.commit()
        pass


if __name__ == '__main__':
    Main()

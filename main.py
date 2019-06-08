# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QFileDialog, QMessageBox, QWidget
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QThread, Signal
import sys
import time
from configparser import RawConfigParser
import codecs
from loguru import logger
import os
from platform import platform

from model import Plugin, Session, Plugin_language, Language
from language_widget import Ui_Form as Language_Widget
from main_window import Ui_MainWindow


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
    current_plugin = None

    def __init__(self):
        # init config
        self.config = RawConfigParser()
        self.config.read_file(codecs.open('config.ini', encoding='utf8'))

        logger.info('Configuration loaded')
        # init database
        self.session = Session()

        # init Qt windows
        self.app = QApplication(sys.argv)

        self.window = QMainWindow()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)

        self.update_mpc_plugin_list()

        self.ui.mpc_title_frame_title.setText(self.config['options']['project_name'])
        self.window.setWindowTitle(self.config['options']['project_name'])
        self.ui.mpc_btn_import.clicked.connect(self.import_plugin)
        self.ui.mpc_plugins_list.itemClicked.connect(self.load_plugin_by_item)

        self.ui.ps_btn_back.clicked.connect(self.go_to_main_screen)
        self.ui.ps_delete_plugin_btn.clicked.connect(self.delete_plugin)

        self.go_to_main_screen()
        self.window.show()

        # todo: Delete this part before first release
        self.garbage_test_code()
        sys.exit(self.app.exec_())

    def update_mpc_plugin_list(self):
        list_ = self.ui.mpc_plugins_list
        list_.clear()
        for plugin in self.session.query(Plugin.name, Plugin.id):
            string = plugin.name
            if len(string) > int(self.config['options']['plugin_list_max_len']):
                string = string[:int(self.config['options']['plugin_list_max_len'])] + ' ...'
            item = QListWidgetItem(string)
            item.setStatusTip(str(plugin.id))
            list_.addItem(item)

    def import_plugin(self):
        path = QFileDialog.getOpenFileName(dir=self.config['history']['last_open_folder'], filter='*.txt')[0]
        logger.debug(f'Selected path: {path}')
        if path:
            name = path.split('/')[-1]
            p = Plugin(name=name, path=path)
            self.session.add(p)
            self.session.commit()
            self.update_mpc_plugin_list()
            self.import_plugin_files(p)

    def load_plugin_by_item(self, item):
        layout = self.ui.ps_plugin_language_frame.layout()
        for i in reversed(range(layout.count())):
            widget = layout.takeAt(i)
            if hasattr(widget, 'widget') and widget.widget() is not None:
                if hasattr(widget.widget(), 'deleteLater'):
                    widget.widget().deleteLater()
            layout.removeItem(widget)

        logger.debug(item)
        logger.debug(item.text())
        logger.debug(item.statusTip())

        self.current_plugin = item.statusTip()
        self.ui.ps_plugin_name.setText(item.text())
        pls = self.session.query(Plugin_language).filter(Plugin_language.plugin_id == self.current_plugin).all()
        languages = self.session.query(Language).all()
        lw = Language_Widget()

        for pl in pls:
            w = QWidget()
            lw.setupUi(w)
            lw.label.setText(languages[pl.language_id-1].short)
            lw.progressBar.setValue(pl.progression)
            lw.flag.setPixmap(QPixmap(f":/flag/ressources/flag_famfamfam/{languages[pl.language_id-1].icon}.png"))
            layout.addWidget(w)

        self.ui.stackedWidget.setCurrentIndex(1)

    def go_to_main_screen(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def delete_plugin(self):
        plugin = self.session.query(Plugin).filter(Plugin.id == self.current_plugin).first()
        answer = QMessageBox.question(None, f"Deleting plugin {plugin.name}", "Are you sure ?")
        if answer == QMessageBox.StandardButton.Yes:
            self.session.query(Plugin).filter(Plugin.id == self.current_plugin).delete()
            self.update_mpc_plugin_list()
            self.go_to_main_screen()
            self.session.commit()

    def import_plugin_files(self, plugin):
        backslash = '\\'
        path = backslash.join(plugin.path.split('/')[:-1])
        logger.debug(plugin.name)
        logger.debug(path)
        for root, dirs, files in os.walk(path):
            if root != path:
                for file in files:
                    language = root.split(backslash)[-1]
                    if file == plugin.name:
                        logger.debug(f"{language}\t{file}")
                        l_id = self.session.query(Language.id).filter(Language.short == language).first().id
                        pl = Plugin_language(plugin_id=plugin.id, language_id=l_id, progression=0)
                        self.session.add(pl)
        self.session.commit()

    def garbage_test_code(self):
        pass


if __name__ == '__main__':
    Main()

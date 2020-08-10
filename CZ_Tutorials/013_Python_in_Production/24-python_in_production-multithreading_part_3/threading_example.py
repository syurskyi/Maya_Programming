import datetime
import json
import sys
import time
from PySide2 import QtCore, QtGui, QtWidgets


class AssetListWorker(QtCore.QObject):

    refresh_started = QtCore.Signal()
    refresh_ended = QtCore.Signal()

    progress_sent = QtCore.Signal(int)


    def __init__(self):
        super(AssetListWorker, self).__init__()
        self.running = False

    def run(self):
        if not self.running:
            self.running = True

            self.refresh_started.emit()

            self.progress_sent.emit(0)
            for i in range(100):
                time.sleep(0.05)
                self.progress_sent.emit(i)

                QtCore.QCoreApplication.processEvents()
                if not self.running:
                    break

            self.running = False
            self.refresh_ended.emit()

    def cancel(self):
        if self.running:
            self.running = False

    def shutdown(self):
        self.running = False

        current_thread = QtCore.QThread.currentThread()
        if current_thread:
            current_thread.exit(0)


class AssetViewer(QtWidgets.QWidget):

    ROOT_PATH = "D:/Development/Patreon/Sandbox"

    ASSET_DIR_PATH = "{0}/Assets".format(ROOT_PATH)
    JSON_FILE_NAME = "assets.json"

    IMAGE_WIDTH = 400
    IMAGE_HEIGHT = IMAGE_WIDTH / 1.77778

    shutdown_asset_list_worker = QtCore.Signal()


    def __init__(self):
        super(AssetViewer, self).__init__(parent=None)

        self.setWindowTitle("Asset Viewer")
        self.setMinimumSize(400, 300)

        self.json_file_path = "{0}/{1}".format(self.ASSET_DIR_PATH, self.JSON_FILE_NAME)

        self.create_widgets()
        self.create_layout()
        self.create_connections()
        self.create_threads()

        self.set_edit_enabled(False)

        self.load_assets_from_json()

        self.refresh_asset_list_in_progress = False

    def create_widgets(self):
        self.refresh_asset_list_button = QtWidgets.QPushButton(QtGui.QIcon("{0}/refresh.png".format(AssetViewer.ROOT_PATH)), "")
        self.cancel_refresh_asset_list_button = QtWidgets.QPushButton(QtGui.QIcon("{0}/error.png".format(AssetViewer.ROOT_PATH)), "")
        self.cancel_refresh_asset_list_button.setVisible(False)

        self.refresh_progress_bar = QtWidgets.QProgressBar()
        palette = self.refresh_progress_bar.palette()
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
        self.refresh_progress_bar.setPalette(palette)
        self.refresh_progress_bar.setVisible(False)

        self.asset_list_label = QtWidgets.QLabel("Asset Code:")
        self.asset_list_cmb = QtWidgets.QComboBox()

        self.preview_image_label = QtWidgets.QLabel()
        self.preview_image_label.setFixedHeight(self.IMAGE_HEIGHT)

        self.name_le = QtWidgets.QLineEdit()
        self.description_plaintext = QtWidgets.QPlainTextEdit()
        self.description_plaintext.setFixedHeight(100)
        self.creator_le = QtWidgets.QLineEdit()
        self.created_date_le = QtWidgets.QLineEdit()
        self.modified_date_le = QtWidgets.QLineEdit()

        self.edit_button = QtWidgets.QPushButton("Edit")
        self.save_button = QtWidgets.QPushButton("Save")
        self.cancel_button = QtWidgets.QPushButton("Cancel")

    def create_layout(self):
        asset_list_layout = QtWidgets.QHBoxLayout()
        asset_list_layout.addWidget(self.refresh_asset_list_button)
        asset_list_layout.addWidget(self.refresh_progress_bar)
        asset_list_layout.addWidget(self.cancel_refresh_asset_list_button)
        asset_list_layout.addStretch()
        asset_list_layout.addWidget(self.asset_list_label)
        asset_list_layout.addWidget(self.asset_list_cmb)

        details_layout = QtWidgets.QFormLayout()
        details_layout.addRow("Name:", self.name_le)
        details_layout.addRow("Description:", self.description_plaintext)
        
        details_layout.addRow("Creator:", self.creator_le)
        details_layout.addRow("Created:", self.created_date_le)
        details_layout.addRow("Modified:", self.modified_date_le)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.edit_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.addLayout(asset_list_layout)
        main_layout.addWidget(self.preview_image_label)
        main_layout.addLayout(details_layout)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.asset_list_cmb.currentTextChanged.connect(self.refresh_asset_details)

        self.edit_button.clicked.connect(self.edit_asset_details)
        self.save_button.clicked.connect(self.save_asset_details)
        self.cancel_button.clicked.connect(self.cancel_edit)

    def create_threads(self):
        self.asset_list_thread = QtCore.QThread(self)
        self.asset_list_worker = AssetListWorker()

        self.refresh_asset_list_button.clicked.connect(self.asset_list_worker.run)
        self.cancel_refresh_asset_list_button.clicked.connect(self.asset_list_worker.cancel)

        self.shutdown_asset_list_worker.connect(self.asset_list_worker.shutdown)

        self.asset_list_worker.refresh_started.connect(self.on_asset_list_refresh_started)
        self.asset_list_worker.refresh_ended.connect(self.on_asset_list_refresh_ended)
        self.asset_list_worker.progress_sent.connect(self.on_asset_list_progress_received)

        self.asset_list_worker.moveToThread(self.asset_list_thread)
        self.asset_list_thread.start()

    def set_edit_enabled(self, enabled):
        read_only = not enabled

        self.name_le.setReadOnly(read_only)
        self.description_plaintext.setReadOnly(read_only)
        if read_only:
            self.creator_le.setReadOnly(read_only)
            self.created_date_le.setReadOnly(read_only)
            self.modified_date_le.setReadOnly(read_only)

        self.edit_button.setVisible(read_only)
        self.save_button.setHidden(read_only)
        self.cancel_button.setHidden(read_only)

    def set_preview_image(self, file_name):
        image_path = "{0}/{1}".format(self.ASSET_DIR_PATH, file_name)

        file_info = QtCore.QFileInfo(image_path)
        if file_info.exists():
            image = QtGui.QImage(image_path)
            image = image.scaled(self.preview_image_label.width(), self.preview_image_label.height(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            pixmap = QtGui.QPixmap()
            pixmap.convertFromImage(image)

        else:
            pixmap = QtGui.QPixmap(self.preview_image_label.size())
            pixmap.fill(QtCore.Qt.transparent)

        self.preview_image_label.setPixmap(pixmap)
    
    def load_assets_from_json(self):
        with open(self.json_file_path, "r") as file_for_read:
            self.assets = json.load(file_for_read)

        for asset_code in self.assets.keys():
            self.asset_list_cmb.addItem(asset_code)

    def save_assets_to_json(self):
        with open(self.json_file_path, "w") as file_for_write:
            json.dump(self.assets, file_for_write, indent=4)

    def on_asset_list_refresh_started(self):
        self.set_refresh_in_progress_widgets_visible(True)

    def on_asset_list_refresh_ended(self):
        self.set_refresh_in_progress_widgets_visible(False)

    def on_asset_list_progress_received(self, progress_value):
        self.refresh_progress_bar.setValue(progress_value)

    def set_refresh_in_progress_widgets_visible(self, visible):
        self.refresh_asset_list_button.setVisible(not visible)
        self.refresh_progress_bar.setVisible(visible)
        self.cancel_refresh_asset_list_button.setVisible(visible)
        self.repaint()

    def refresh_asset_details(self):
        asset_code = self.asset_list_cmb.currentText()

        current_asset = self.assets[asset_code]

        self.name_le.setText(current_asset["name"])
        self.description_plaintext.setPlainText(current_asset["description"])
        self.creator_le.setText(current_asset["creator"])
        self.created_date_le.setText(current_asset["created"])
        self.modified_date_le.setText(current_asset["modified"])

        self.set_preview_image(current_asset["image_path"])

    def edit_asset_details(self):
        self.set_edit_enabled(True)

    def save_asset_details(self):
        self.set_edit_enabled(False)

        modified = datetime.datetime.now()
        self.modified_date_le.setText(modified.strftime("%Y/%m/%d %H:%M:%S"))

        asset_code = self.asset_list_cmb.currentText()

        current_asset = self.assets[asset_code]
        current_asset["name"] = self.name_le.text()
        current_asset["description"] = self.description_plaintext.toPlainText()
        current_asset["modified"] = self.modified_date_le.text()

        self.save_assets_to_json()

    def cancel_edit(self):
        self.set_edit_enabled(False)

        self.refresh_asset_details()  

    def closeEvent(self, event):
        #self.asset_list_thread.exit()

        self.shutdown_asset_list_worker.emit()

        self.asset_list_thread.wait(500)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    app.setStyle(QtWidgets.QStyleFactory.create("fusion"))

    dark_palette = QtGui.QPalette()
    dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(45, 45, 45))
    dark_palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(208, 208, 208))
    dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
    dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(208, 208, 208))
    dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(208, 208, 208))
    dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(208, 208, 208))
    dark_palette.setColor(QtGui.QPalette.Text, QtGui.QColor(208, 208, 208))
    dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(45, 45, 48))
    dark_palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(208, 208, 208))
    dark_palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QtGui.QPalette.Highlight, QtCore.Qt.black)
    app.setPalette(dark_palette)

    window = AssetViewer()
    window.show()

    app.exec_()
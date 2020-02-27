import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

import Config


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Open file'
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setMinimumSize(self.width, self.height)
        self.openFileNamesDialog()

        self.show()

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Open file", "",
                                                "Text Files (*.txt)", options=options)
        if files:
            self.addText(files)

    def addText(self, files: []):
        for i in files:
            if i not in Config.words:
                Config.words.append(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

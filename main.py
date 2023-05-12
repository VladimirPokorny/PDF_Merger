from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QFileDialog, QListWidget, QAbstractItemView, QCheckBox, QLineEdit
from PyPDF2 import PdfFileReader, PdfFileMerger
import natsort
import sys
import os
from os.path import expanduser


def clean_file_name(filename):
    filename = os.path.basename(filename)
    return filename


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.window_width, self.window_height = 800, 400
        self.setMinimumSize(self.window_width, self.window_height)

        self.files = None
        self.files_with_path = None
        self.out_dir = os.path.expanduser('~') + '/PDF_Merger-Output'

        layout = QGridLayout()
        self.setLayout(layout)

        self.add_button = QPushButton('Import Files')
        self.add_button.clicked.connect(self.add)

        self.remove_button = QPushButton('Delete Selected')
        self.remove_button.clicked.connect(self.remove)

        self.clear_button = QPushButton('Clear List')
        self.clear_button.clicked.connect(self.clear)

        self.list_widget = QListWidget()
        self.list_widget.setDragDropMode(QAbstractItemView.InternalMove)
        self.list_widget.setAcceptDrops(True)

        self.merge_button = QPushButton('Merge PDFs')
        self.merge_button.clicked.connect(self.mergePDFs)

        self.output_dir_text = QLineEdit()
        self.output_dir_text.setEnabled(False)
        self.output_dir_text.setText('{}'.format(self.out_dir))

        self.output_dir_button = QPushButton('Output Directory')
        self.output_dir_button.clicked.connect(self.output_directory)

        self.sort_check_box = QCheckBox('Sort Alphabetically')

        layout.addWidget(self.list_widget, 1, 0, 3, 4)

        layout.addWidget(self.add_button, 0, 0)
        layout.addWidget(self.remove_button, 0, 1)
        layout.addWidget(self.clear_button, 0, 2)

        layout.addWidget(self.sort_check_box, 4, 3)
        layout.addWidget(self.merge_button, 5, 3)

        layout.addWidget(self.output_dir_text, 5, 0, 1, 2)
        layout.addWidget(self.output_dir_button, 5, 2)

    def add(self):
        file_filter = 'PDF Files (*.pdf);; All Files (*.*)'
        response = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Select a PDF file',
            directory=os.getcwd(),
            # directory=os.path.expanduser('~'),
            filter=file_filter,
            initialFilter='PDF Files (*.pdf)'
        )
        files, extension = response

        self.files_with_path = files


        for i in range(len(files)):
            cleaned_filename = clean_file_name(files[i])
            self.list_widget.addItem(cleaned_filename)

    def remove(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            current_item = self.list_widget.takeItem(current_row)
            self.files_with_path.pop(current_row)
            del current_item

    def clear(self):
        self.list_widget.clear()
        self.files_with_path = []

    def mergePDFs(self):
        pdfs = []
        # for i in range(self.list_widget.count()):
        # pdfs.append(self.list_widget.item(i).text())

        pdfs = self.files_with_path

        if self.sort_check_box.isChecked():
            pdfs = self.files
            pdfs = natsort.natsorted(pdfs, reverse=False)

        merger = PdfFileMerger()

        for pdf in pdfs:  # iterate over the list of files
            merger.append(PdfFileReader(pdf), 'rb')

        merger.write(self.out_dir + '/' + 'Merged.pdf')
        merger.close()

        self.clear()

    def output_directory(self):
        self.out_dir = QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        self.output_dir_text.setText('{}'.format(self.out_dir))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 15px;
        }
    ''')

    myApp = MyApp()

    # dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    # myApp.setStyleSheet(dark_stylesheet)

    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

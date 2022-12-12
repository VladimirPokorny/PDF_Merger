from PyQt5.QtWidgets import QDialog

class SettingDialog:
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Settings')

        self.default_output_directory = None



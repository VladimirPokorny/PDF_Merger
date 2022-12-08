import os


def clean_file_name(filename):
    clean_filename = []
    for i in range(len(filename)):
        clean_filename.append(os.path.basename(filename[i]))
    return clean_filename


# for i in range(len(files)):
# cleaned_filename = clean_file_name(files[i])
# self.list_widget.addItem(cleaned_filename)


files = ['C:\\pystem\\data\\performance_tests\\reports\\2022-12-07_08-37-29_ScanningMonitoring_.dat', 'C:\\pystem\\data\\performance_tests\\reports\\2022-12-07_08-46-24_ScanningMonitoring_.dat']

print(clean_file_name(files))
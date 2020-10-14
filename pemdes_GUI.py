import sys
from PyQt5.QtWidgets import *

def window ():
    #_inisialisasi pyqt5
    app = QApplication(sys.argv)
    window = QWidget()

    #_menyiapkan label,menempelkan ke window
    #_settext dan posisi
    lbl = QLabel(window)
    lbl.setText('Input Biodata')
    lbl.setStyleSheet ("Font : Bold; color: #ADFF2F; Background-color: #F0FFF0; Font-size: 28pt")

    Awal = QLineEdit()
    Awal1= QLineEdit()
    Awal2= QLineEdit()

    layout = QFormLayout()
    layout.addRow (lbl)
    layout.addRow ('Nama', Awal)
    layout.addRow ('Alamat', Awal1)
    layout.addWidget (Awal2)

    #_menampilkan CheckBox
    coba = QCheckBox ('Makan')
    coba1= QCheckBox ('Tidur')
    coba2= QCheckBox ('Main')
    layout.addRow('Hobby',coba)
    layout.addWidget(coba1)
    layout.addWidget(coba2)

    #_menampilkan Button
    button = QRadioButton ('Pelajar')
    button1= QRadioButton ('Pegawai')
    button2= QRadioButton ('Wiraswasta')
    layout.addRow('Status',button)
    layout.addWidget(button1)
    layout.addWidget(button2)
    #_menentukan ukuran window, + title dan menampilkan
    window.setLayout(layout)
    window.setGeometry(400,100,700,500)
    window.setWindowTitle('PyQt5')
    window.show()
    sys.exit(app.exec_())


	
if __name__ == '__main__':
   window()

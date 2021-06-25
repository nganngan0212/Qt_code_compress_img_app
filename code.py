import sys
from PyQt5 import QtCore 
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Image procesing")

        self.setGeometry(0, 0, 1280, 720) 
  
        self.setStyleSheet("background-color: #4682B4;") 

        self.original = QLabel(self)
        self.original.setText('Original')
        self.original.setAlignment(QtCore.Qt.AlignCenter)
        self.original.setFont(QFont('Proxima Nova', 15))
        self.original.setGeometry(100, 60, 256, 30) 
        self.original.setStyleSheet("color: #000000;")

        self.input_image = QLabel(self) 
        self.input_image.setGeometry(100, 115, 256, 256) 
        self.input_image.setAlignment(QtCore.Qt.AlignCenter)
        self.input_image.setStyleSheet("background-color:  #D2B29B; ")

        self.reconstruction = QLabel(self)
        self.reconstruction.setText('Reconstruction')
        self.reconstruction.setAlignment(QtCore.Qt.AlignCenter)
        self.reconstruction.setFont(QFont('Proxima Nova', 15))
        self.reconstruction.setGeometry(414, 60, 256, 30) 
        self.reconstruction.setStyleSheet("color: #000000;")

        self.output_image = QLabel(self)
        self.output_image.setGeometry(414, 115, 256, 256) 
        self.output_image.setAlignment(QtCore.Qt.AlignCenter)
        self.output_image.setStyleSheet("background-color:  #D2B29B;")

        
        self.file = QPushButton('File', self)
        self.file.setFont(QFont('Proxima Nova', 10))
        self.file.setStyleSheet("background-color: #C4C4C4;color: #000000; border-radius: 20px")
        self.file.resize(120,60)
        self.file.move(100, 400)   
        self.file.clicked.connect(self.browsefiles)

        self.compress = QPushButton('Compress', self)
        self.compress.setFont(QFont('Proxima Nova', 10))
        self.compress.setStyleSheet("background-color: #C4C4C4;color: #000000; border-radius: 20px")
        self.compress.resize(120,60)
        self.compress.move(250, 400)  
        self.compress.clicked.connect(self.compress_image)

        self.decompress = QPushButton('Decompress', self)
        self.decompress.setFont(QFont('Proxima Nova', 10))
        self.decompress.setStyleSheet("background-color: #C4C4C4;color: #000000; border-radius: 20px")
        self.decompress.resize(120,60)
        self.decompress.move(400, 400) 
        self.decompress.clicked.connect(self.decompress_image)

        self.properties = QPushButton('Properties', self)
        self.properties.setFont(QFont('Proxima Nova', 10))
        self.properties.setStyleSheet("background-color: #C4C4C4;color: #000000; border-radius: 20px")
        self.properties.resize(120,60)
        self.properties.move(550, 400) 
        self.properties.clicked.connect(self.properties_image)

        self.label = QLabel(self) 
        self.label.setGeometry(780, 0, 500, 720) 
        self.label.setStyleSheet("background-color:  #C4C4C4; border-radius: 20px ")     

        self.prop = QLabel(self)
        self.prop.setText('PROPERTIES')
        self.prop.setAlignment(QtCore.Qt.AlignCenter)
        self.prop.setFont(QFont('Proxima Nova', 20))
        self.prop.setGeometry(870, 20, 330, 60) 
        self.prop.setStyleSheet("color: #000000; background-color: #C4C4C4;")   

        self.original_volume = QLabel(self)
        self.original_volume.setText('Original volume :')
        self.original_volume.setAlignment(QtCore.Qt.AlignRight)
        self.original_volume.setFont(QFont('Proxima Nova', 10))
        self.original_volume.setGeometry(780, 110, 180, 40) 
        self.original_volume.setStyleSheet("color: #000000; background-color: #C4C4C4;")

        self.box1 = QLabel(self)
        self.box1.setAlignment(QtCore.Qt.AlignCenter)
        self.box1.setFont(QFont('Proxima Nova', 10))
        self.box1.setGeometry(985, 100, 250, 40) 
        self.box1.setStyleSheet("color: #000000; background-color: #FFFFFF; border-radius: 10px;")

        self.compress_volumn = QLabel(self)
        self.compress_volumn.setText('Compress volume :')
        self.compress_volumn.setAlignment(QtCore.Qt.AlignRight)
        self.compress_volumn.setFont(QFont('Proxima Nova', 10))
        self.compress_volumn.setGeometry(780, 160, 180, 40) 
        self.compress_volumn.setStyleSheet("color: #000000; background-color: #C4C4C4;")

        self.box2 = QLabel(self)
        self.box2.setAlignment(QtCore.Qt.AlignCenter)
        self.box2.setFont(QFont('Proxima Nova', 10))
        self.box2.setGeometry(985, 150, 250, 40) 
        self.box2.setStyleSheet("color: #000000; background-color: #FFFFFF; border-radius: 10px;")

        self.compress_ratio = QLabel(self)
        self.compress_ratio.setText('Original volume :')
        self.compress_ratio.setAlignment(QtCore.Qt.AlignRight)
        self.compress_ratio.setFont(QFont('Proxima Nova', 10))
        self.compress_ratio.setGeometry(780, 210, 180, 40) 
        self.compress_ratio.setStyleSheet("color: #000000; background-color: #C4C4C4;")

        self.box3 = QLabel(self)
        self.box3.setAlignment(QtCore.Qt.AlignCenter)
        self.box3.setFont(QFont('Proxima Nova', 10))
        self.box3.setGeometry(985, 200, 250, 40) 
        self.box3.setStyleSheet("color: #000000; background-color: #FFFFFF; border-radius: 10px;")

        self.time = QLabel(self)
        self.time.setText('Original volume :')
        self.time.setAlignment(QtCore.Qt.AlignRight)
        self.time.setFont(QFont('Proxima Nova', 10))
        self.time.setGeometry(780, 260, 180, 40) 
        self.time.setStyleSheet("color: #000000; background-color: #C4C4C4;")

        self.box4 = QLabel(self)
        self.box4.setAlignment(QtCore.Qt.AlignCenter)
        self.box4.setFont(QFont('Proxima Nova', 10))
        self.box4.setGeometry(985, 250, 250, 40) 
        self.box4.setStyleSheet("color: #000000; background-color: #FFFFFF; border-radius: 10px;")

        self.mse = QLabel(self)
        self.mse.setText('Original volume :')
        self.mse.setAlignment(QtCore.Qt.AlignRight)
        self.mse.setFont(QFont('Proxima Nova', 10))
        self.mse.setGeometry(780, 310, 180, 40) 
        self.mse.setStyleSheet("color: #000000; background-color: #C4C4C4;")

        self.box5 = QLabel(self)
        self.box5.setAlignment(QtCore.Qt.AlignCenter)
        self.box5.setFont(QFont('Proxima Nova', 10))
        self.box5.setGeometry(985, 300, 250, 40) 
        self.box5.setStyleSheet("color: #000000; background-color: #FFFFFF; border-radius: 10px;")

        self.psnr = QLabel(self)
        self.psnr.setText('Original volume :')
        self.psnr.setAlignment(QtCore.Qt.AlignRight)
        self.psnr.setFont(QFont('Proxima Nova', 10))
        self.psnr.setGeometry(780, 360, 180, 40) 
        self.psnr.setStyleSheet("color: #000000; background-color: #C4C4C4;")

        self.box6 = QLabel(self)
        self.box6.setAlignment(QtCore.Qt.AlignCenter)
        self.box6.setFont(QFont('Proxima Nova', 10))
        self.box6.setGeometry(985, 350, 250, 40) 
        self.box6.setStyleSheet("color: #000000; background-color: #FFFFFF; border-radius: 10px;")

        self.label2 = QLabel(self) 
        self.label2.setGeometry(100, 480, 580, 160) 
        self.label2.setStyleSheet("background-color:  #C4C4C4; border-radius: 20px ")        

        self.gaussian_persent = QLabel(self)
        self.gaussian_persent.setText('Gaussian Persent')
        self.gaussian_persent.setAlignment(QtCore.Qt.AlignCenter)
        self.gaussian_persent.setFont(QFont('Proxima Nova', 10))
        self.gaussian_persent.setGeometry(130, 515, 160, 40) 
        self.gaussian_persent.setStyleSheet("color: #000000; background-color: #C4C4C4;")

        self.gau_box = QLineEdit(self)
        self.gau_box.setAlignment(QtCore.Qt.AlignCenter)
        self.gau_box.setFont(QFont('Proxima Nova', 10))
        self.gau_box.move(130, 570) 
        self.gau_box.resize(160, 50)
        self.gau_box.setStyleSheet("color: #000000; background-color: #FFFFFF; border-radius: 10px;")

        self.quantization_ratio = QLabel(self)
        self.quantization_ratio.setText('Quantization Ratio')
        self.quantization_ratio.setAlignment(QtCore.Qt.AlignCenter)
        self.quantization_ratio.setFont(QFont('Proxima Nova', 10))
        self.quantization_ratio.setGeometry(310, 515, 160, 40) 
        self.quantization_ratio.setStyleSheet("color: #000000; background-color: #C4C4C4;")

        self.quan_box = QLineEdit(self)
        self.quan_box.setAlignment(QtCore.Qt.AlignCenter)
        self.quan_box.setFont(QFont('Proxima Nova', 10))
        self.quan_box.setGeometry(310, 575, 160, 50) 
        self.quan_box.setStyleSheet("color: #000000; background-color: #FFFFFF; border-radius: 10px;")

        self.arithmetic = QLabel(self)
        self.arithmetic.setText('Arithmetic Block Size')
        self.arithmetic.setAlignment(QtCore.Qt.AlignCenter)
        self.arithmetic.setFont(QFont('Proxima Nova', 10))
        self.arithmetic.setGeometry(490, 515, 160, 40) 
        self.arithmetic.setStyleSheet("color: #000000; background-color: #C4C4C4;")

        self.arth_box = QLineEdit(self)
        self.arth_box.setAlignment(QtCore.Qt.AlignCenter)
        self.arth_box.setFont(QFont('Proxima Nova', 10))
        self.arth_box.setGeometry(490, 575, 160, 50) 
        self.arth_box.setStyleSheet("color: #000000; background-color: #FFFFFF; border-radius: 10px;")

        self.button = QPushButton("OK", self)
        self.button.setGeometry(365, 650, 70, 40) 
        self.button.setStyleSheet("color: #000000; background-color: #FFFFFF; border-radius: 10px;")
        self.button.clicked.connect(self.save_result)

    def browsefiles(self):
        # print("clicked file")
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'This PC', 'Images (*.png *.jpg)')
        file_name = fname[0]
        # print(file_name)
        pixmap = QPixmap(file_name)
        self.input_image.setPixmap(pixmap.scaled(256, 256, Qt.KeepAspectRatio))

    def compress_image(self):
        # put your code here
        print("Clicked compress image")

    def decompress_image(self):
        # put your code here
        print("Clicked decompress image")

    def properties_image(self):
        # put your code here
        print("clicked properties")
        self.box1.setText("Hello, how are you?")

    def save_result(self):
        # Ham lay ket qua cua ba o nhap vao
        num_gaussian = self.gau_box.text()
        num_quantization = self.quan_box.text()
        num_arithmetic = self.arth_box.text()
        print(num_arithmetic)
        print(num_gaussian)
        print(num_quantization)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
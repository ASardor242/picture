# создай тут фоторедактор Easy Editor!
import os

from PIL import Image
from PIL.ImageFilter import SHARPEN
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QHBoxLayout, QVBoxLayout, QListWidget, QFileDialog)
app = QApplication([])
main_win = QWidget()
main_win.resize(700, 500)
main_win.setWindowTitle("Easy Editor")
btn_dir = QPushButton('Папка')
list_images = QListWidget()
label_image = QLabel('Картинка')

btn_left = QPushButton('Лево')
btn_right = QPushButton('Право')

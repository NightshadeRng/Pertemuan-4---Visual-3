# Cara 1 ============================================
from PyQt5 import QtGui, QtCore, QtWidgets

app = QtWidgets.QApplication([])  # Membuat aplikasi
window = QtWidgets.QPushButton("MyButton")  # Membuat tombol dengan teks "MyButton"
window.show()  # Menampilkan tombol
app.exec_()  # Menjalankan event loop aplikasi


# Cara 2 ============================================
from PyQt5.QtWidgets import *  # Mengimpor semua dari QtWidgets
from PyQt5.QtCore import *  # Mengimpor semua dari QtCore
from PyQt5.QtGui import *  # Mengimpor semua dari QtGui

app = QApplication([])  # Membuat aplikasi
window = QPushButton("MyButton")  # Membuat tombol dengan teks "MyButton"
window.show()  # Menampilkan tombol
app.exec_()  # Menjalankan event loop aplikasi


# Cara 3 ============================================
from PyQt5 import QtWidgets as qtw  # Mengimpor QtWidgets dan memberikannya alias 'qtw'

app = qtw.QApplication([])  # Membuat aplikasi
window = qtw.QPushButton("MyButton")  # Membuat tombol dengan teks "MyButton"
window.show()  # Menampilkan tombol
app.exec_()  # Menjalankan event loop aplikasi


# Cara 4 (Recommended, lebih hemat memori) ==========
from PyQt5.QtWidgets import QApplication, QPushButton  # Hanya mengimpor QApplication dan QPushButton

app = QApplication([])  # Membuat aplikasi
window = QPushButton("MyButton")  # Membuat tombol dengan teks "MyButton"
window.show()  # Menampilkan tombol
app.exec_()  # Menjalankan event loop aplikasi

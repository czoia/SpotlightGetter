__author__ = 'czoia'

import sys
import os

from PyQt4 import QtCore, QtGui
from gui import UiMyForm
from getpass import getuser
from PIL import Image
from shutil import copyfile

class ImageItem(QtGui.QListWidgetItem):
    def __init__(self, name, width, height):
        super(ImageItem, self).__init__()
        self.setText(name)
        self.w = width
        self.h = height

    def get_width(self):
        return self.w

    def get_height(self):
        return self.h


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = UiMyForm()
        self.ui.setupUi(self)
        self.image_path = "C:\\Users\\"+getuser()+"\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\Assets"
        self.image_dict = dict({'Smartphone': list(),
                                'Landscape' : list()})
        self.temp_img = ''

        for i in os.listdir(self.image_path):
            try:
                image = Image.open(self.image_path+"\\"+i)
                if 'jfif_density' in list(image.info) or 'adobe_transform' in list(image.info):
                    itm = ImageItem(i, image.size[0], image.size[1])
                    if image.size[0] >= image.size[1]:  # width > height
                        self.image_dict['Landscape'].append(itm)
                    else:
                        self.image_dict['Smartphone'].append(itm)
                    # update listView widget
                    self.ui.imageList.addItem(itm)
                    print "Image info",i,image.size, list( image.info)
            except IOError:
                print "Not an Image " + i

    def file_save(self):
        fd = QtGui.QFileDialog(self)
        filename = fd.getSaveFileName(self, "Save file", filter="Image (*.jpg)")
        copyfile(self.temp_img, filename)

    def change_image_preview(self, row):
        if row is not None and row >= 0:
            item = self.ui.imageList.item(row)
            if not os.path.isfile(self.image_path+"\\_copy"+item.text()+".jpg"):
                copyfile(self.image_path+"\\"+item.text(), self.image_path+"\\_copy"+item.text())
                os.rename(self.image_path+"\\_copy"+item.text(), self.image_path+"\\_copy"+item.text()+".jpg")
            image_profile = QtGui.QImage(self.image_path+"\\_copy"+item.text()+".jpg")
            if item.get_width() > item.get_height():
                                                    # width, height, aspectRatioMode
                image_profile = image_profile.scaled(800, 500, QtCore.Qt.KeepAspectRatio)
                self.ui.image_preview_portrait.hide()
                self.ui.image_preview_landscape.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.image_preview_landscape.show()
            else:
                                                    # width, height, aspectRatioMode
                image_profile = image_profile.scaled(261, 431, QtCore.Qt.KeepAspectRatio)
                self.ui.image_preview_landscape.hide()
                self.ui.image_preview_portrait.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.image_preview_portrait.show()
            self.temp_img = self.image_path+"\\_copy"+item.text()+".jpg"

    def switch_samples(self, sel_item):
        for x in range(0, self.ui.imageList.count()):
            self.ui.imageList.takeItem(0)  # takeItem works like a FIFO
        if sel_item not in self.image_dict.keys():
            for key in self.image_dict.keys():
                for x in self.image_dict[key]:
                    self.ui.imageList.addItem(x)
        else:
            for x in self.image_dict[str(sel_item)]:
                self.ui.imageList.addItem(x)

    def closeEvent(self, event):
        self.delete_temp_file()
        event.accept()

    def delete_temp_file(self):
        from fnmatch import fnmatch
        for f in os.listdir(self.image_path):
            if fnmatch(f, "_copy*"):
                os.remove(self.image_path+"\\"+f)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    my_app = MyForm()
    my_app.show()

    sys.exit(app.exec_())

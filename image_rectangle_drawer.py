from PyQt6.QtWidgets import QGraphicsItem, QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QScrollArea, QPushButton, QHBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, QMenu
from PyQt6.QtGui import QPixmap, QScreen, QMouseEvent, QPen, QBrush, QColor, QAction
from PyQt6.QtCore import Qt, QPointF, QPoint, QRectF
import os
import sys
from PyQt6.QtWidgets import QGraphicsItem, QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QScrollArea, QPushButton, QHBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, QMenu
from PyQt6.QtGui import QPixmap, QScreen, QMouseEvent, QPen, QBrush, QColor, QAction
from PyQt6.QtCore import Qt, QPointF, QPoint, QRectF
import os
import sys


current_image_file = None  # Global variable to store the current image file name
image_data = {}
scale_factor = 1.0
from PyQt6.QtWidgets import QGraphicsItem, QApplication, QWidget, QLabel, QVBoxLayout, QComboBox, QScrollArea, QPushButton, QHBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem, QMenu
from PyQt6.QtGui import QPixmap, QScreen, QMouseEvent, QPen, QBrush, QColor, QAction
from PyQt6.QtCore import Qt, QPointF, QPoint, QRectF
import os
import sys

current_image_file = None  # Global variable to store the current image file name
image_data = {}

class RectangleDrawer(QGraphicsView):
    def __init__(self, scene, parent=None):
        super(RectangleDrawer, self).__init__(scene, parent)
        self.start = QPointF()
        self.end = QPointF()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.start = self.mapToScene(event.position().toPoint())

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() & Qt.MouseButton.LeftButton:
            self.end = self.mapToScene(event.position().toPoint())
            self.update()

    def mouseReleaseEvent(self, event: QMouseEvent):
        global current_image_file
        if event.button() == Qt.MouseButton.LeftButton:
            self.end = self.mapToScene(event.position().toPoint())
            rect = ContextMenuRectangle(QRectF(QPointF(self.start), QPointF(self.end)))


            rect.setPen(QPen(Qt.GlobalColor.red))
            self.scene().addItem(rect)


            # Save the QGraphicsEllipseItem for the start and end positions
            start_item = QGraphicsEllipseItem(self.start.x(), self.start.y(), 5, 5)
            start_item.setBrush(QBrush(QColor("green")))
            self.scene().addItem(start_item)

            end_item = QGraphicsEllipseItem(self.end.x(), self.end.y(), 5, 5)
            end_item.setBrush(QBrush(QColor("red")))
            self.scene().addItem(end_item)

            # Save both the QPointF and QGraphicsEllipseItem
            rect.start_point = self.start
            rect.start_item = start_item
            rect.end_point = self.end
            rect.end_item = end_item


            start_point = QGraphicsEllipseItem(self.start.x(), self.start.y(), 5, 5)
            start_point.setBrush(QBrush(QColor("green")))
            self.scene().addItem(start_point)

            end_point = QGraphicsEllipseItem(self.end.x(), self.end.y(), 5, 5)
            end_point.setBrush(QBrush(QColor("red")))
            self.scene().addItem(end_point)

            rect.start_point = self.start  # Store as QPointF
            rect.end_point = self.end  # Store as QPointF

            self.update()
            if current_image_file in image_data:
                image_data[current_image_file].append((self.start, self.end))
            else:
                image_data[current_image_file] = [(self.start, self.end)]

            save_rectangle_data()

class ContextMenuRectangle(QGraphicsRectItem):
    def __init__(self, rect, parent=None):
        super(ContextMenuRectangle, self).__init__(rect, parent)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable, True)
        self.start_point = None
        self.end_point = None
        self.start_item = None  # Added initialization
        self.end_item = None  # Added initialization

    def contextMenuEvent(self, event):
        menu = QMenu()
        remove_action = QAction("Remove")
        remove_action.triggered.connect(self.remove)
        menu.addAction(remove_action)
        menu.exec(event.screenPos())

    def remove(self):
        global image_data, current_image_file

        # Remove the QGraphicsEllipseItem instead of the QPointF
        if self.start_item is not None:
            self.scene().removeItem(self.start_item)
        if self.end_item is not None:
            self.scene().removeItem(self.end_item)
        self.scene().removeItem(self)

        # Update image_data dictionary
        if current_image_file in image_data:
            rect_points = (self.start_point, self.end_point)  # Create a tuple with start and end points
            if rect_points in image_data[current_image_file]:  # If this tuple is in the list for current image file
                image_data[current_image_file].remove(rect_points)  # remove it

        save_rectangle_data()


app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
controls_layout = QHBoxLayout()

scene = QGraphicsScene()
view = RectangleDrawer(scene)

scroll_area = QScrollArea()
scroll_area.setWidgetResizable(True)
scroll_area.setWidget(view)

cwd = os.getcwd()
image_files = [file for file in os.listdir(cwd) if file.endswith('.jpg')]

image_selector = QComboBox()
image_selector.addItems(image_files)

zoom_in_button = QPushButton("+")
zoom_out_button = QPushButton("-")

scale_factor = 0.15
image_data = {}

def save_rectangle_data():
    global current_image_file, image_data
    if current_image_file is not None:
        with open(f"{current_image_file}.txt", "w") as file:
            for start, end in image_data.get(current_image_file, []):
                start_x, start_y = start.x(), start.y()
                end_x, end_y = end.x(), end.y()
                file.write(f"{start_x},{start_y},{end_x},{end_y}\n")

def load_image(image_file):
    global scale_factor, image_data, current_image_file
    image_path = os.path.join(cwd, image_file)
    pixmap = QPixmap(image_path)

    new_size = pixmap.size() * scale_factor
    pixmap = pixmap.scaled(new_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

    scene.clear()
    scene.addPixmap(pixmap)

    if image_file in image_data:
        for start, end in image_data[image_file]:
            rect = ContextMenuRectangle(QRectF(start, end))

            # Save the QGraphicsEllipseItem for the start and end positions
            start_item = QGraphicsEllipseItem(start.x(), start.y(), 5, 5)
            start_item.setBrush(QBrush(QColor("green")))
            scene.addItem(start_item)

            end_item = QGraphicsEllipseItem(end.x(), end.y(), 5, 5)
            end_item.setBrush(QBrush(QColor("red")))
            scene.addItem(end_item)

            rect.start_item = start_item  # Store the item
            rect.end_item = end_item  # Store the item

            scene.addItem(rect)

    current_image_file = image_file

if image_files:
    current_image_file = image_files[0]
image_selector.currentTextChanged.connect(load_image)

def zoom_in():
    global scale_factor
    scale_factor += 0.05
    load_image(current_image_file)

def zoom_out():
    global scale_factor
    scale_factor -= 0.05 if scale_factor > 0.1 else 0
    load_image(current_image_file)

zoom_in_button.clicked.connect(zoom_in)
zoom_out_button.clicked.connect(zoom_out)

controls_layout.addWidget(image_selector)
controls_layout.addWidget(zoom_in_button)
controls_layout.addWidget(zoom_out_button)
layout.addLayout(controls_layout)
layout.addWidget(scroll_area)
window.resize(600, 820)
window.setLayout(layout)

load_image(current_image_file)

window.show()
sys.exit(app.exec())

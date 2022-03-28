"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""
# -------------------------------------------------------------------------
"""InteractiveTutorials\\editor\\scripts\\InteractiveTutorials_dialog.py
Generated from O3DE PythonToolGem Template"""

from PySide2 import QtCore
from PySide2.QtCore import QMargins, Qt
from PySide2.QtGui import QColor, QPainter, QPen
from PySide2.QtWidgets import QDialog, QDialogButtonBox, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget

import editor_python_test_tools.pyside_utils as pyside_utils

from demo_tutorial import DemoTutorial


class HighlightWidget(QWidget):
    def __init__(self, parent=None):
        super(HighlightWidget, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowTransparentForInput | Qt.WindowDoesNotAcceptFocus)
        self.setAttribute(Qt.WA_TranslucentBackground);
        self.setAttribute(Qt.WA_NoSystemBackground);
        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.border_width = 5

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(QColor(131, 238, 255))
        pen.setWidth(self.border_width)
        painter.setPen(pen)
        painter.drawRect(event.rect())

    def update_widget(self, item):
        if item:
            self.show()

            # Position our highlight widget on top of the specified item, but with an offset
            # so that the rectangle border that we draw doesn't overlap the actual item itself
            item_size = item.size()
            new_size = item_size.grownBy(QMargins(self.border_width / 2, self.border_width / 2, 0, 0))
            self.resize(new_size)
            self.window().move(item.mapToGlobal(QtCore.QPoint(-self.border_width / 2, -self.border_width / 2)))
            self.raise_()
        else:
            self.hide()

class InteractiveTutorialsDialog(QDialog):
    def __init__(self, parent=None):
        super(InteractiveTutorialsDialog, self).__init__(parent)

        self.main_layout = QVBoxLayout(self)

        self.highlight_widget = HighlightWidget()
        self.highlight_widget.hide()

        self.title_label = QLabel(self)
        self.main_layout.addWidget(self.title_label)

        self.content_area = QTextEdit(self)
        self.content_area.setReadOnly(True)
        self.main_layout.addWidget(self.content_area, 1)

        self.button_box = QDialogButtonBox(self)
        self.next_button = QPushButton("Next", self)
        self.next_button.setDefault(True)
        self.next_button.clicked.connect(self.on_next_button_clicked)
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.on_back_button_clicked)
        self.button_box.addButton(self.next_button, QDialogButtonBox.ActionRole)
        self.button_box.addButton(self.back_button, QDialogButtonBox.ResetRole)
        self.main_layout.addWidget(self.button_box)

        self.setLayout(self.main_layout)

        # TODO: Have real system for loading tutorials
        self.load_tutorial()

    def load_tutorial(self):
        self.current_tutorial = DemoTutorial()

        # Update the title based on the loaded tutorial
        self.setWindowTitle("InteractiveTutorials - " + self.current_tutorial.get_title())

        self.current_step = self.current_tutorial.get_first_step()
        self.update_step_view()

    def update_step_view(self):
        if not self.current_step:
            return

        self.title_label.setText(self.current_step.get_title())
        self.content_area.setText(self.current_step.get_content())

        # If a highlight pattern was set for this step, then find that widget/item
        # and highlight it
        highlight_pattern = self.current_step.get_highlight_pattern()
        if highlight_pattern:
            item = pyside_utils.find_child_by_pattern(None, highlight_pattern)
            self.highlight_widget.update_widget(item)
            if not item:
                print(f"Couldn't find widget or item matching pattern: { highlight_pattern }")
        else:
            self.highlight_widget.update_widget(None)

    def on_next_button_clicked(self):
        if self.current_step and self.current_step.next_step:
            self.current_step = self.current_step.next_step
            self.update_step_view()

    def on_back_button_clicked(self):
        if self.current_step and self.current_step.prev_step:
            self.current_step = self.current_step.prev_step
            self.update_step_view()


if __name__ == "__main__":
    # Create a new instance of the tool if launched from the Python Scripts window,
    # which allows for quick iteration without having to close/re-launch the Editor
    test_dialog = InteractiveTutorialsDialog()
    test_dialog.show()
    test_dialog.adjustSize()

"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""
# -------------------------------------------------------------------------
"""InteractiveTutorials\\editor\\scripts\\InteractiveTutorials_dialog.py
Generated from O3DE PythonToolGem Template"""

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QDialogButtonBox, QLabel, QPushButton, QTextEdit, QVBoxLayout

from demo_tutorial import DemoTutorial


class InteractiveTutorialsDialog(QDialog):
    def __init__(self, parent=None):
        super(InteractiveTutorialsDialog, self).__init__(parent)

        self.main_layout = QVBoxLayout(self)

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

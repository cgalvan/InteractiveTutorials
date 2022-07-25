"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""
# -------------------------------------------------------------------------
"""InteractiveTutorials\\editor\\scripts\\InteractiveTutorials_dialog.py
Generated from O3DE PythonToolGem Template"""

from PySide2 import QtCore
from PySide2.QtCore import QMargins, QStringListModel, Qt
from PySide2.QtGui import QColor, QPainter, QPen
from PySide2.QtWidgets import (QDialog, QDialogButtonBox, QLabel, QListView,
    QMessageBox, QPushButton, QStackedWidget, QTextEdit, QVBoxLayout, QWidget
)

# This import will fail when the AP launches, will only work once the Editor is running
try:
    import editor_python_test_tools.pyside_utils as pyside_utils
except:
    pass

from demo_tutorial import DemoTutorial, IntroTutorial
from tutorial import Tutorial
from rigid_body_tutorial import RigidBodyTutorial
from finding_ui_objects import FindingUIObjectsTutorial

class HighlightWidget(QWidget):
    def __init__(self, parent=None):
        super(HighlightWidget, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowTransparentForInput | Qt.WindowDoesNotAcceptFocus | Qt.WindowStaysOnTopHint)
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

        # Stacked widget so we can switch between the intro screen that lets you
        # choose a tutorial, and the actual tutorial in progress view
        self.stacked_widget = QStackedWidget(self)

        # Intro screen that shows list for picking a tutorial
        self.intro_widget = QWidget(self)
        self.intro_layout = QVBoxLayout()

        self.choose_tutorial_label = QLabel("Choose a tutorial", self)
        self.intro_layout.addWidget(self.choose_tutorial_label, 0, Qt.AlignCenter)

        self.tutorial_list = QListView(self)

        # TODO: Have real system for loading tutorials
        self.tutorials = [
            {
                "name": "Intro to the Editor",
                "tutorial": IntroTutorial
            },
            {
                "name": "Demo Tutorial",
                "tutorial": DemoTutorial
            },
            {
                "name": "Create an Entity",
                "tutorial": lambda: Tutorial.create_from_json_file("create_entity_tutorial.json")
            },
            {
                "name": "PhysX Rigid Bodies",
                "tutorial": RigidBodyTutorial
            },
            {
                "name": "Highlighting UI Objects",
                "tutorial": FindingUIObjectsTutorial
            }
        ]
        tutorial_names = [tutorial['name'] for tutorial in self.tutorials]
        self.tutorial_list_model = QStringListModel(self)
        self.tutorial_list_model.setStringList(tutorial_names)
        self.tutorial_list.setModel(self.tutorial_list_model)
        self.tutorial_list.setAlternatingRowColors(True)
        self.intro_layout.addWidget(self.tutorial_list, 0, Qt.AlignCenter)

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.on_start_button_clicked)
        self.intro_layout.addWidget(self.start_button, 0, Qt.AlignCenter)

        self.intro_widget.setLayout(self.intro_layout)
        self.stacked_widget.addWidget(self.intro_widget)

        # Tutorial in progress view
        self.tutorial_widget = QWidget(self)
        self.tutorial_layout = QVBoxLayout()

        self.highlight_widget = HighlightWidget()
        self.highlight_widget.hide()

        self.title_label = QLabel(self)
        # TODO: Use the Text::addHeadlineStyle method when more of AzQtComponents are exposed to python
        self.title_label.setProperty("class", "Headline")
        self.tutorial_layout.addWidget(self.title_label)

        self.content_area = QLabel(self)
        self.content_area.setWordWrap(True)
        self.tutorial_layout.addWidget(self.content_area, 1)

        self.step_label = QLabel(self)
        self.tutorial_layout.addWidget(self.step_label)

        self.button_box = QDialogButtonBox(self)
        self.next_button = QPushButton("Next", self)
        self.next_button.setDefault(True)
        self.next_button.clicked.connect(self.load_next_step)
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.load_previous_step)
        self.button_box.addButton(self.next_button, QDialogButtonBox.ActionRole)
        self.button_box.addButton(self.back_button, QDialogButtonBox.ResetRole)
        self.tutorial_layout.addWidget(self.button_box)

        self.tutorial_widget.setLayout(self.tutorial_layout)
        self.stacked_widget.addWidget(self.tutorial_widget)

        self.stacked_layout = QVBoxLayout()
        self.stacked_layout.addWidget(self.stacked_widget)
        self.setLayout(self.stacked_layout)

    def load_tutorial(self, index):
        # Switch to the tutorial view
        self.stacked_widget.setCurrentIndex(1)

        tutorial_factory = self.tutorials[index]["tutorial"]
        self.current_tutorial = tutorial_factory()
        
        self.current_tutorial_num_steps = len(self.current_tutorial.get_steps())

        # Invoke the tutorial start method
        self.current_tutorial.on_tutorial_start()

        # Update the title based on the loaded tutorial
        self.setWindowTitle("InteractiveTutorials - " + self.current_tutorial.get_title())

        # Reset initial state and load first step
        self.current_step_index = 0 
        self.current_step = None
        first_step = self.current_tutorial.get_first_step()
        self.load_step(first_step)
        
    def end_tutorial(self):
        if not self.current_step:
            return

        # Call the on_step_end for the final step
        self.current_step.on_step_end()

        # Call the on_tutorial_end for the tutorial
        self.current_tutorial.on_tutorial_end()

        # Clear our state and switch back to the intro view
        # Save our tutorial title so we can show it in the completion message
        title = self.current_tutorial.get_title()
        self.highlight_widget.update_widget(None)
        self.current_tutorial = None
        self.stacked_widget.setCurrentIndex(0)

        # Give user a nice congratulations message for completing the tutorial
        QMessageBox.information(self, "Tutorial completed",
            f"Congratulations! Great job completing the { title } tutorial :)")

    def update_step_view(self):
        if not self.current_step:
            return

        self.title_label.setText(self.current_step.get_title())
        self.content_area.setText(self.current_step.get_content())
        self.step_label.setText(f"Step {self.current_step_index} of {self.current_tutorial_num_steps}")
        # If there are no steps remaining in the tutorial, then
        # update the Next button text to "End"
        next_button_text = "Next"
        if not self.current_step.next_step:
            next_button_text = "End"
        self.next_button.setText(next_button_text)

        # If a highlight pattern was set for this step, then find that widget/item
        # and highlight it
        highlight_item = None
        highlight_pattern = self.current_step.get_highlight_pattern()
        if not highlight_pattern:
            self.highlight_widget.update_widget(None)
            return

        highlight_parent = self.current_step.get_highlight_parent()
        if not highlight_parent:
            highlight_item = pyside_utils.find_child_by_pattern(None, highlight_pattern)
        else:
            if isinstance(highlight_parent, str):
                highlight_parent = pyside_utils.find_child_by_pattern(None, highlight_parent)
            highlight_item = pyside_utils.find_child_by_hierarchy(highlight_parent, highlight_pattern, 
                    child_index=self.current_step.get_highlight_index())

        if not highlight_item:
            self.highlight_widget.update_widget(None)
            print(f"Couldn't find widget or item matching pattern: { highlight_pattern }")
            return

        self.highlight_widget.update_widget(highlight_item)

    def load_step(self, step):
        # If there was a step already loaded, call its ending method
        if self.current_step:
            self.current_step.on_step_end()

        self.current_step = step
        self.current_step_index += 1 

        # Invoke the method for the beginning of this step
        self.current_step.on_step_start()

        self.update_step_view()

    def load_next_step(self):
        if self.current_step:
            next_step = self.current_step.next_step
            if next_step:
                self.load_step(next_step)
            else:
                # If there are no next steps left,
                # then we have finished the tutorial!
                self.end_tutorial()

    def load_previous_step(self):
        if self.current_step:
            self.current_step_index -= 1
            prev_step = self.current_step.prev_step
            if prev_step:
                self.current_step_index -= 1
                self.load_step(prev_step)


    def on_start_button_clicked(self):
        tutorial_index = self.tutorial_list.currentIndex().row()

        self.load_tutorial(tutorial_index)


if __name__ == "__main__":
    # Create a new instance of the tool if launched from the Python Scripts window,
    # which allows for quick iteration without having to close/re-launch the Editor
    test_dialog = InteractiveTutorialsDialog()
    test_dialog.show()
    test_dialog.adjustSize()

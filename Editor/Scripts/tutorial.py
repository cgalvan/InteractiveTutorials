"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

import json
import os

# Class that describes a step in the tutorial
class TutorialStep:
    def __init__(self, title, content, highlight_pattern=None):
        self.title = title
        self.content = content

        # The highlight pattern is a widget/item that will be highlighted
        # for this particular step (can be None)
        # This pattern will be passed to `editor_python_test_tools.pyside_utils`
        # to find the widget/item. See its documentation for supported patterns
        self.highlight_pattern = highlight_pattern

        self.prev_step = None
        self.next_step = None

    # Method that will be called when the step starts
    # A step class can override this method if they need
    # to setup any special handling/listeners
    def on_step_start(self):
        # Automated testing scripts go here
        pass

    # Method that will be called after a step has ended
    # A step class can override this method if they need
    # to perform any cleanup or other tasks
    def on_step_end(self):
        pass

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_highlight_pattern(self):
        return self.highlight_pattern

# Top-level entry point for describing a tutorial which is made up of a series of steps
class Tutorial:
    def __init__(self):
        self.steps = []
        self.title = ""

    @classmethod
    def create_from_json_file(cls, file_path):
        # If the specified file path isn't an absolute path,
        # try to resolve it locally
        if not os.path.isabs(file_path):
            local_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(local_dir, file_path)

        # Read the json data in from the json file
        f = open(file_path)
        data = json.load(f)

        # Create the new tutorial
        new_tutorial = cls()
        new_tutorial.title = data["title"]

        # Add the tutorial steps
        steps = data["steps"]
        for step in steps:
            title = step["title"]
            content = step["content"]
            highlight_pattern = step.get("highlight_pattern", None)
            new_step = TutorialStep(title, content, highlight_pattern)
            new_tutorial.add_step(new_step)

        return new_tutorial

    # Method that will be called when the tutorial starts
    # A tutorial class can override this method if they need
    # to setup any special handling/listeners
    def on_tutorial_start(self):
        pass

    # Method that will be called after a tutorial has ended
    # A tutorial class can override this method if they need
    # to perform any cleanup or other tasks
    def on_tutorial_end(self):
        pass

    def get_title(self):
        return self.title

    def add_step(self, step):
        # Set the step references for the current last step on the list
        if self.steps:
            last_step = self.steps[-1]
            last_step.next_step = step
            step.prev_step = last_step

        self.steps.append(step)

    def get_first_step(self):
        if self.steps:
            return self.steps[0]

        return None

    def get_steps(self):
        return self.steps

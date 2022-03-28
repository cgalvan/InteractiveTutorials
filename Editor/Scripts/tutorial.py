"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""


# Class that describes a step in the tutorial
class TutorialStep:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.prev_step = None
        self.next_step = None

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

# Top-level entry point for describing a tutorial which is made up of a series of steps
class Tutorial:
    def __init__(self):
        self.steps = []
        self.title = ""

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

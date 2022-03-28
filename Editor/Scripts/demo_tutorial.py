"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

from PySide2.QtWidgets import QMenuBar

from tutorial import Tutorial, TutorialStep


class DemoTutorial(Tutorial):
    def __init__(self):
        super(DemoTutorial, self).__init__()

        self.title = "Demo Tutorial"

        self.add_step(TutorialStep("First things first", "Welcome! This first step shouldn't highlight any widget."))
        self.add_step(TutorialStep("Select an Entity", "Next, select any Entity in the Entity Outliner", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Add a component", "Use the Add Component button to add a component to the Entity", "m_addComponentButton"))
        self.add_step(TutorialStep("Cool menu bar", "This step is just to showcase highlighting an item without a direct name but by using a type pattern instead", {"type": QMenuBar}))

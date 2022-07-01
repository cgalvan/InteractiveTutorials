"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

import sys
import azlmbr

from PySide2 import QtWidgets
import editor_python_test_tools.pyside_utils as pyside_utils

from tutorial import Tutorial, TutorialStep

class FindingUIObjectsTutorial(Tutorial):
    def __init__(self):
        super(FindingUIObjectsTutorial, self).__init__()

        self.title = "Highlighting UI Objects"

        self.add_step(TutorialStep("Highlighting UI Objects", 
                """<html><p style="font-size:13px">Greetings!<br><br>This tutorial demonstrates methods to find UI 
                objects to highlight in tutorial steps. You can use the <b>Object Tree</b> tool to find named UI 
                objects or a named parent of a UI object. Then, use one of methods in this tutorial to specify the 
                widget to highlight in a <strong><code style="font-size:14px;color:#E44C9A">TutorialStep</code></strong>
                .<br><br>The available methods are:<ul><li><b>Highlight by name</b> - Specify the name of the 
                UI object to highlight.</li><li><b>Highlight by parent</b> - Specify a named parent and a pattern for 
                the UI object. The UI object is the first child of the parent that matches the specified pattern.</li>
                <li><b>Highlight from hierarchy with index</b> - Specify an index to select a specific child UI object 
                when the parent has multiple children that have the same pattern.</li></ul></p></html>"""))
        self.add_step(TutorialStep("Highlight by name", """<html><p style="font-size:13px">This step highlights the 
                <b>Entity Outliner</b>, finding it by its name, <strong><code style="font-size:14px;color:#E44C9A">
                "EntityOutlinerWidgetUI"</code></strong>.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Highlight from parent", """<html><p style="font-size:13px">This step highlights 
                the <b>Console Variables</b> tool button in the lower-left corner of the Editor. The Console Variables 
                tool button has a name, but is found through its parent in this example. It is the first QToolButton 
                child of a QWidget named <strong><code style="font-size:14px;color:#E44C9A">container2</code></strong>.
                </p></html>""", QtWidgets.QToolButton, "container2"))
        self.add_step(TutorialStep("Highlight from hierarchy with index", """<html><p style="font-size:13px">This step 
                highlights the <b>Play</b> tool button in the upper-right corner of the Editor. The Play tool button is 
                unnamed, and it is the third QToolButton child of a QToolBar named 
                <strong><code style="font-size:14px;color:#E44C9A">PlayConsole</code></strong>. Supplying 
                <strong><code style="font-size:14px;color:#E44C9A">2</code></strong> for the index value selects the 
                third child QToolButton.</p></html>""", QtWidgets.QToolButton, "PlayConsole", 2))

    def on_tutorial_start(self):
        print("Starting Widget By Hierarchy tutorial.")

    def on_tutorial_end(self):
        print("Widget By Hierarchy tutorial complete!")
"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the 
LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

from PySide2 import QtWidgets

# This import will fail when AP launches, only works once the Editor is running
try:
    import pyside_utils
except:
    pass

from tutorial import Tutorial, TutorialStep

class FindingUIObjectsTutorial(Tutorial):
    def __init__(self):
        super(FindingUIObjectsTutorial, self).__init__()

        self.title = "Highlighting UI Objects"
        #self.is_automated = False

        self.add_step(TutorialStep("Highlighting UI Objects", 
                """<html><p style="font-size:13px">Greetings!<br><br>This 
                tutorial demonstrates methods to find UI objects to highlight in
                 tutorial steps. You can use the <b>Object Tree</b> tool to find
                 named UI objects or a named parent of a UI object. Then, use 
                one of methods in this tutorial to specify the widget to 
                highlight in a <strong>
                <code style="font-size:14px;color:#E44C9A">TutorialStep</code>
                </strong>.<br><br>The available methods are:<ul><li><b>Highlight
                 by name</b> - Specify the name of the UI object to highlight.
                </li><li><b>Highlight by parent</b> - Specify a named parent and
                 a pattern for the UI object. The UI object is the first child 
                of the parent that matches the specified pattern.</li><li><b>
                Highlight from hierarchy with index</b> - Specify an index to 
                select a specific child UI object when the parent has multiple 
                unnamed children of the same type.</li></ul></p></html>"""))
        self.add_step(TutorialStep("Highlight by name", """<html><p style=
                "font-size:13px">This step highlights the <b>Entity Outliner</b>
                , finding it by its name, <strong>
                <code style="font-size:14px;color:#E44C9A">
                "EntityOutlinerWidgetUI"</code></strong>.</p></html>""", 
                "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Highlight by pattern", """<html>
                <p style="font-size:13px">This step highlights the <b>Console 
                Variables</b> tool button in the lower-left corner of the Editor
                . The Console Variables tool button has a name, but is found 
                through a dictionary that contains text (the widget name) and 
                its type, <strong><code style="font-size:14px;color:#E44C9A">
                {"text": "button", "type": QtWidgets.QToolButton}</code>
                </strong>. </p></html>""", {"text": "button", "type": 
                QtWidgets.QToolButton}))
        self.add_step(TutorialStep("Highlight by pattern", """<html>
                <p style="font-size:13px">This step highlights the <b>Play</b> 
                tool button in the upper-right corner of the Editor. The Play 
                tool button is unnamed, but it has a text attribute for a 
                tooltip. You can use a dictionary to find this UI element by 
                providing the widget type and the tooltip text, <strong>
                <code style="font-size:14px;color:#E44C9A">{"type": 
                QtWidgets.QToolButton, "text": "Play Game"}</code></strong>.
                </p></html>""", {"type": QtWidgets.QToolButton, 
                "text": "Play Game"}))
        self.add_step(TutorialStep("Highlight from named parent", """<html>
                <p style="font-size:13px">This step highlights the <b>Transform 
                Toolbar</b> in the upper-left corner of the viewport. The 
                Transform Toolbar widget is unnamed and has no tooltip text. You
                 can find it by its type through its named parent. It's the 
                first child of type <strong>
                <code style="font-size:14px;color:#E44C9A">QtWidgets.QToolBar
                </code></strong> of a widget named <strong>
                <code style="font-size:14px;color:#E44C9A">"ViewportUiOverlay"
                </code></strong>.</p></html>""", QtWidgets.QToolBar, 
                "ViewportUiOverlay"))
        self.add_step(TutorialStep("Highlight with index", """<html>
                <p style="font-size:13px">In the upper-right corner of the 
                viewport is the <b>Transform Space Toolbar</b>. It is an unnamed
                 widget of type <strong>
                <code style="font-size:14px;color:#E44C9A">
                QtWidgets.QToolBar</code></strong>. It's also the second child 
                of the <strong><code style="font-size:14px;color:#E44C9A">
                "ViewportUiOverlay"</code></strong> widget that was referenced 
                in the previous step. To highlight the Transform Space Toolbar, 
                use the same method as the previous step, but provide an 
                optional index value of <strong>
                <code style="font-size:14px;color:#E44C9A">1</code></strong> to 
                select the second child.</p></html>""", QtWidgets.QToolBar, 
                "ViewportUiOverlay", 1))
        item_parent = pyside_utils.find_child_by_pattern(None, 
                        "ViewportUiOverlay")
        item = pyside_utils.find_child_by_hierarchy(item_parent, 
                        QtWidgets.QToolBar, child_index=1)
        self.add_step(TutorialStep("Highlight with index - advanced", """<html>
                <p style="font-size:13px">What if you want to highlight a UI 
                element, but its nearest named parent is a couple of levels and 
                indices away?<br><br>The Transform Space Toolbar has three 
                buttons: <b>W</b>orld, <b>P</b>arent, and <b>L</b>ocal space. 
                Suppose you want to highlight the Local space button. It's the 
                fourth <strong><code style="font-size:14px;color:#E44C9A">
                QtWidgets.QToolButton</code></strong> in the second <strong>
                <code style="font-size:14px;color:#E44C9A">QtWidgets.QToolBar
                </code></strong> beneath a parent named <strong>
                <code style="font-size:14px;color:#E44C9A">ViewportUiOverlay
                </code></strong>.<br><br>You can get the local space button by 
                finding it's direct unnamed parent prior to defining the step, 
                and supplying the direct parent and an index to the tutorial 
                step. See this step in this tutorial's Python script for an 
                example.</p></html>""", QtWidgets.QToolButton, item, 3))
        

    def on_tutorial_start(self):
        print("Starting Widget By Hierarchy tutorial.")

    def on_tutorial_end(self):
        print("Widget By Hierarchy tutorial complete!")
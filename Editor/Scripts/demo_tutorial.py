"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

from PySide2.QtWidgets import QMenuBar

from tutorial import Tutorial, TutorialStep


# Example of a custom step that overrides the start/end hooks
class SelectEntityStep(TutorialStep):
    def __init__(self):
        super(SelectEntityStep, self).__init__("Select an Entity",
            "Next, select any Entity in the Entity Outliner", "EntityOutlinerWidgetUI")

    def on_step_start(self):
        print("Starting the select Entity step")

    def on_step_end(self):
        print("Ended the select Entity step")

# Interactive tutorial version of this Editor tour:
#   https://www.o3de.org/docs/welcome-guide/tours/editor-tour/
class IntroTutorial(Tutorial):
    def __init__(self):
        super(IntroTutorial, self).__init__()

        self.title = "Intro to the Editor"

        self.add_step(TutorialStep("Introduction", """<html><p style="font-size:13px">The default layout of O3DE Editor contains the most commonly used tools in a configuration similar to other content creation applications. The core workflow of O3DE is to create and place entities in a level, so the default layout contains a menu bar, toolbars, panes, and tool tabs focused on entity creation and placement.
<br/><br/>
You can customize the layout through drag and drop, and save to a custom layout through the <b>Layouts</b> option in the <b>View</b> menu of the main menu bar. Drag the separator bars between panes to resize the panes. Drag the title bar of a pane to tear off the pane. The pane can be dropped anywhere in the layout or dropped outside of O3DE Editor as its own window. To restore the default layout, in the main menu bar choose <b>View > Layouts > Default Layout</b>.</p></html>
"""))

        self.add_step(TutorialStep("Menu Bar", """<html><p style="font-size:13px">Near the top of O3DE Editor are the <b>Menu Bar</b> and the <b>Tool Bar</b>.
<br/><br/>
The Menu Bar contains several familiar menus:
<ul>
  <li><b>File</b> - File menu items include actions for opening and saving levels, managing editor and project settings, and creating and opening projects.</li>
  <li><b>Edit</b> - Edit menu items include actions for working with selections such as duplicate, delete, hide and show selection, and working with selection transforms.</li>
  <li><b>Game</b> - Game menu items include actions for running the project, enabling in editor simulation, enabling and refreshing audio, and debugging.</li>
  <li><b>Tools</b> - Tools menu items provide access to all of O3DE’s tools and editors.</li>
  <li><b>View</b> - View menu items include actions to configure both the Perspective viewport and O3DE Editor layout.</li>
  <li><b>AWS</b> - AWS menu items include tools and links to documentation for working with AWS in your O3DE projects.</li>
  <li><b>Help</b> - Help menu items provide links to O3DE community and documentation resources.</li>
</ul>
</p></html>""", {"type": QMenuBar}))

        self.add_step(TutorialStep("Toolbar", """<html><p style="font-size:13px">
The <b>Tool Bar</b> provides easy access to various editor tools and features. On the left are buttons to open various O3DE tools and editors, on the right are controls to run your project or activate simulation in editor. The Tool Bar is docked at the top of the editor by default, but you can also dock it vertically on the edges of the editor. To customize the toolbar, right-click anywhere on the toolbar and select <b>Customize</b> from the context menu. You can choose which toolbars to include, and add commands to the toolbar.
</p></html>""", "EditMode"))

        self.add_step(TutorialStep("Entity Outliner", """<html><p style="font-size:13px">
On the left side of O3DE Editor, <b>Entity Outliner</b> displays a list of entities and prefabs in the current level. Right-click in Entity Outliner to open the context menu to create entities and instantiate prefabs. When an entity or prefab is selected in Entity Outliner, the context menu also has options to duplicate or delete entities, find selected entities and prefabs, organize the list, and open the properties for the selected entity or prefab.
</p></html>""", "EntityOutlinerWidgetUI"))

        self.add_step(TutorialStep("Asset Browser", """<html><p style="font-size:13px">
Below Entity Outliner is <b>Asset Browser</b>, which you can use to browse your project’s on-disk assets. Assets such as meshes, animations, and textures are created in third-party applications. Assets such as materials, scripts, and prefabs are created in O3DE Editor, or in editor tools such as <b>Script Canvas</b>. The assets that you create are stored in your project directory. You can also browse default assets that are included with O3DE, as well as assets that are included with Gems that have been added to your project.
<br/><br/>
The left pane of the Asset Browser displays a directory structure that you can browse for available assets. When an asset is selected, the preview pane on the right displays a thumbnail preview and information about the asset, if available.
<br/><br/>
With an asset selected in Asset Browser, the right-click context menu has options to open <b>Scene Settings</b> where you can set <b>Asset Processor</b> options for the asset, as well as open the asset in an associated application such as a modeling program, or open the file location in the system file browser.
</p></html>""", "AzAssetBrowserWindowClass"))

        self.add_step(TutorialStep("Entity Inspector", """<html><p style="font-size:13px">
On the right side of O3DE Editor, <b>Entity Inspector</b> displays the components of the currently selected entity. At the top of Entity Inspector is a field for the entity <b>Name</b> and an <b>Add Component</b> button. The Add Component button opens a list of available components, sorted by type, that can be added to the entity. Each component has its own set of properties that are displayed in Entity Inspector. All entities contain a <b>Transform</b> component that sets the position, rotation, and scale of the entity in the level.
</p></html>""", "InspectorMainWindow"))

        self.add_step(TutorialStep("Console", """<html><p style="font-size:13px">
At the bottom of the default O3DE Editor layout is the <b>Editor Console</b>, which shows command and process output from O3DE Editor and your project. When you load a level, for example, the console displays messages about assets and configuration files as they load, and might display warnings and errors if issues are encountered.
<br/><br/>
You can enter console commands such as setting console variables in the entry field at the bottom of the console. Choose the <b>{x}</b> button in the lower left of Editor Console to open the <b>Console Variables Editor</b>, which provides a simple interface for setting console variables.
</p></html>""", "Console"))

        self.add_step(TutorialStep("Viewport", """<html><p style="font-size:13px">
In the center of the default O3DE Editor layout is the <b>Viewport</b>. This 3D viewport is a real-time view of your level. In the viewport, you create and place entities, and view and play your project.
<br/><br/>
Right-click in the top bar of the viewport to open the viewport menu. From the menu, you can toggle visibility for various helpers. You can also select a target aspect ratio, view through various cameras placed in the level, and create a new camera from the current view.
<br/><br/>
On the right side of the top bar, are several icons to select cameras, set camera movement speed, set information display, enable view icons, set aspect ratio, and set grid snapping options.
<br/><br/>
Right-click in the viewport to open the context menu to create entities and instantiate prefabs. Much of the context menu functionality is shared with the context menu functionality of Entity Outliner.
<br/><br/>
In the upper left and upper right corners of the viewport are icon trays for manipulating entities. On the left, you can use the icons to select a transform operation. From top to bottom the icons represent  translate,  rotate, and  scale operations. On the right, you can use the icons to select a space for the transform operation. From top to bottom the icons represent  world,  parent, and  local spaces.
</p></html>""",  "renderOverlay"))

        self.add_step(TutorialStep("Navigating the O3DE Perspective viewport", """<html><p style="font-size:13px">
O3DE has familiar viewport interaction models based on first-person PC games and popular modeling applications, with a few minor tweaks and additions. Movement is handled by keyboard input, and view is handled by pointer device input.
<ul>
  <li><b>W</b> - Move forward.</li>
  <li><b>S</b> - Move backward.</li>
  <li><b>A</b> - Move left.</li>
  <li><b>D</b> - Move right.</li>
  <li><b>Q</b> - Move down.</li>
  <li><b>E</b> - Move up.</li>
  <li><b>Z</b> - Focus on selected.</li>
  <li><b>Right mouse + drag</b> - Rotate view, known as mouselook in most games.</li>
  <li><b>Mouse wheel scroll</b> - Zoom view.</li>
  <li><b>Middle mouse + drag</b> - Pan view.</li>
  <li><b>Left mouse</b> - Select entity.</li>
  <li><b>Left mouse + drag</b> - Area select entities.</li>
</ul>
The camera controls above are game-centric. If you prefer to use camera controls closer to those you would find in a DCC application such as Maya, use these hotkeys.
<ul>
  <li><b>Alt + left mouse + drag</b> - Orbit view.</li>
  <li><b>Alt + right mouse + drag</b> - Dolly view.</li>
  <li><b>Alt + right mouse + drag</b> - Track view.</li>
</ul>
</p></html>""", "renderOverlay"))

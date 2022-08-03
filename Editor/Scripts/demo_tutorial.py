"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE
at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

from PySide2.QtWidgets import QMenuBar

from tutorial import Tutorial, TutorialStep


# Example of a custom step that overrides the start/end hooks
class SelectEntityStep(TutorialStep):
    def __init__(self):
        super(SelectEntityStep, self).__init__("Select an entity", """<html>
                <p style="font-size:13px">Next, select any entity in  <b>Entity 
                Outliner</b>.</p></html>""", "EntityOutlinerWidgetUI")

    def on_step_start(self):
        print("Starting the select Entity step")

    def on_step_end(self):
        print("Ended the select Entity step")

class DemoTutorial(Tutorial):
    def __init__(self):
        super(DemoTutorial, self).__init__()

        self.title = "Demo Tutorial"

        self.add_step(TutorialStep("First things first", """<html>
                <p style="font-size:13px">Welcome! This first step shouldn't 
                highlight any widget.</p></html>"""))
        self.add_step(SelectEntityStep())
        self.add_step(TutorialStep("Add a component", """<html>
                <p style="font-size:13px">Use the Add Component button to add a 
                component to the entity.</p></html>""", "m_addComponentButton"))
        self.add_step(TutorialStep("Cool menu bar", """<html>
                <p style="font-size:13px">This step demonstrates highlighting an
                 item without a direct name but by using a type pattern instead.
                </p></html>""", {"type": QMenuBar}))

    def on_tutorial_start(self):
        print("Where we're going, we don't need roads")

    def on_tutorial_end(self):
        print("Follow the yellow brick road")

# Interactive tutorial version of this Editor tour:
#   https://www.o3de.org/docs/welcome-guide/tours/editor-tour/
class IntroTutorial(Tutorial):
    def __init__(self):
        super(IntroTutorial, self).__init__()

        self.title = "Intro To O3DE Editor"

        self.add_step(TutorialStep("O3DE Editor tour", """<html>
                <p style="font-size:13px">The default layout of <b>O3DE 
                Editor</b> contains the most commonly used tools in a 
                configuration similar to other content creation applications. 
                The core workflow of O3DE is to create and place entities and 
                prefabs in a level, so the default layout contains a menu bar, 
                tool bars, panes, and tool tabs focused on entity creation and 
                placement.<br><br>
                You can customize the layout through drag and drop, and save to 
                a custom layout through the <b>Layouts</b> option in the 
                <b>View</b> menu of the <b>Menu bar</b>. To restore the default 
                layout, in the Menu Bar choose <b>View > Layouts > 
                Default Layout</b>.</p></html>"""))

        self.add_step(TutorialStep("Menu Bar", """<html>
                <p style="font-size:13px">At the top of O3DE Editor is the 
                <b>Menu Bar</b>. The Menu Bar contains several familiar menus:
                <ul>
                <li><b>File</b> - File menu items include actions for opening 
                and saving levels, managing editor and project settings, and 
                creating and opening projects.</li>
                <li><b>Edit</b> - Edit menu items include actions for working 
                with selections such as duplicate, delete, hide and show 
                selection, and working with selection transforms.</li>
                <li><b>Game</b> - Game menu items include actions for running 
                the project, enabling in editor simulation, enabling and 
                refreshing audio, and debugging.</li>
                <li><b>Tools</b> - Tools menu items provide access to all of 
                O3DE’s tools and editors.</li>
                <li><b>View</b> - View menu items include actions to configure 
                both the viewport and O3DE Editor layout.</li>
                <li><b>AWS</b> - AWS menu items include tools and links to 
                documentation for working with AWS in your O3DE projects.</li>
                <li><b>Help</b> - Help menu items provide links to O3DE 
                community and documentation resources.</li>
                </ul>
                </p><</html>""", {"type": QMenuBar}))

        self.add_step(TutorialStep("Tool Bar", """<html>
                <p style="font-size:13px">The <b>Tool Bar</b> provides easy 
                access to O3DE's tools and features. On the left are buttons to 
                open various O3DE tools and editors. On the right are controls 
                to run your project or activate simulation in editor.<br><br>The
                 Tool Bar is docked at the top of the editor by default, but you
                 can also dock it vertically on the edges of the editor. 
                Right-click anywhere on the tool bar and select <b>Customize</b>
                 from the context menu to modify its contents. You can also 
                choose which tool bars to include, and add commands as well.
                </p></html>""", "EditMode"))

        self.add_step(TutorialStep("Entity Outliner", """<html>
                <p style="font-size:13px">On the left side of O3DE Editor, 
                <b>Entity Outliner</b> displays a list of entities and prefabs 
                in the current level.<br><br>Right-click in Entity Outliner to 
                open the context menu to create entities and instantiate 
                prefabs. When an entity or prefab is selected in Entity 
                Outliner, the context menu also has options to duplicate or 
                delete entities, find selected entities and prefabs, organize 
                the list, and open the properties for the selected entity or 
                prefab.</p></html>""", "EntityOutlinerWidgetUI"))

        self.add_step(TutorialStep("Asset Browser", """<html>
                <p style="font-size:13px">In <b>Asset Browser</b>, you can 
                browse your project’s on-disk assets. Meshes, 
                animations, and textures are created in third-party 
                applications. Materials, scripts, and prefabs 
                are created in O3DE's tools and editors. Asset Browser displays 
                assets that have been found in <i>scan directories</i> that are 
                monitored for new asset files and file changes.<br/><br/>
                The left pane of the Asset Browser displays a directory 
                structure that you can browse for available assets. When an 
                asset is selected, the preview pane on the right displays a 
                thumbnail preview and information about the asset, if available.
                <br/><br/>With an asset selected in Asset Browser, the 
                right-click context menu has options to open <b>Scene 
                Settings</b> where you can set processing options for the asset,
                 as well as open the asset in an associated application such as 
                a modeling program, or open the file location in the system 
                file browser.</p></html>""", "AzAssetBrowserWindowClass"))

        self.add_step(TutorialStep("Entity Inspector", """<html>
                <p style="font-size:13px">On the right side of O3DE Editor, 
                <b>Entity Inspector</b> displays the components of the currently
                 selected entity. At the top of Entity Inspector is a field for 
                the entity Name and an <b>Add Component</b> button.<br><br>The 
                Add Component button opens a list of components, sorted by
                 type, that can be added to the entity. Each component has its 
                own set of properties that are displayed in Entity Inspector. 
                All entities contain a <b>Transform</b> component that sets the 
                position, rotation, and scale of the entity in the level.</p>
                </html>""", "InspectorMainWindow"))

        self.add_step(TutorialStep("Console", """<html>
                <p style="font-size:13px">At the bottom of O3DE Editor is the 
                <b>Editor Console</b>, which shows command and process output 
                from O3DE Editor and your project.<br><br>When you load a level,
                 for example, the console displays messages about assets and 
                configuration files as they load, and might display warnings and
                 errors if issues are encountered.<br/><br/>You can enter 
                console commands in the entry field at the bottom of the 
                console. Choose the <b>{x}</b> button in the lower left of 
                Editor Console to open the <b>Console Variables Editor</b>, 
                which provides a simple interface for setting console variables.
                </p></html>""", "Console"))

        self.add_step(TutorialStep("Viewport", """<html>
                <p style="font-size:13px">The central viewport is a real-time 
                view of your level. In the viewport, you create and place 
                entities, and view and play your project.<br/><br/>Use the tool 
                bar above the viewport and the right-click context menu to 
                access tools to toggle visibility for various helpers, bounds, 
                and guides. You can also select an aspect ratio, view through 
                various cameras placed in the level, create new cameras from 
                the current view, set camera speed, and enable grid snapping. 
                Right-click in the viewport to open the context menu 
                to create entities and prefabs.<br/><br/>In the upper left and 
                upper right corners of the viewport are icon trays for 
                manipulating entities. On the left, you can use the icons to 
                select a transform operation. From top to bottom the icons 
                represent translate,  rotate, and  scale operations. On the 
                right, you can use the icons to select a space for the 
                transform operation. From top to bottom the icons represent 
                world,  parent, and local spaces.</p></html>""", 
                "renderOverlay"))

        self.add_step(TutorialStep("Navigate the viewport", """<html>
                <p style="font-size:13px">O3DE has familiar viewport interaction
                 models based on first-person PC games and 3D modeling 
                applications, with a few minor tweaks and additions. Movement is
                 handled by keyboard input, and view is handled by pointer 
                device input.
                <ul>
                <li><b>W</b> - forward</li>
                <li><b>S</b> - backward</li>
                <li><b>A</b> - left</li>
                <li><b>D</b> - right</li>
                <li><b>Q</b> - down</li>
                <li><b>E</b> - up</li>
                <li><b>Z</b> - focus on selected</li>
                <li><b>Right mouse + drag</b> - rotate view, known as 
                <i>mouselook</i> in most games</li>
                <li><b>Mouse wheel scroll</b> - zoom view</li>
                <li><b>Middle mouse + drag</b> - pan view</li>
                <li><b>Left mouse</b> - select entity</li>
                <li><b>Left mouse + drag</b> - area select entities</li>
                </ul>
                The camera controls above are game-centric. If you prefer to 
                use camera controls closer to those you would find in a 3D 
                modeling application, use the following hotkeys:
                <ul>
                <li><b>Alt + left mouse + drag</b> - orbit view</li>
                <li><b>Alt + right mouse + drag</b> - dolly view</li>
                <li><b>Alt + middle mouse + drag</b> - track view</li>
                </ul>
                </p></html>""", "renderOverlay"))

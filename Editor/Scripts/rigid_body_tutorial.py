"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

from time import sleep

#import os
#import sys
#import azlmbr
#import azlmbr.bus as bus
#import azlmbr.editor as editor
#import azlmbr.legacy.general as general
#import azlmbr.entity as entity
#import azlmbr.math as math
#import azlmbr.prefab as prefab
#from azlmbr.entity import EntityId
#from editor_python_test_tools.utils import TestHelper as helper
#import azlmbr.asset as asset
#from PySide2.QtWidgets import QMenuBar
#from PySide2.QtWidgets import QDialog
from PySide2 import QtWidgets
from tutorial import Tutorial, TutorialStep

#class Tests():
#    enter_game_mode            = ("Entered game mode",                       "Failed to enter game mode")
#    exit_game_mode             = ("Exited game mode",                        "Couldn't exit game mode")
# fmt: on

#class RigidBody:
#    gravity_enabled = False
#    linear_velocity = 10
#    angular_velocity = 10
#    mass = 0.0

class RigidBodyTutorial(Tutorial):
    def __init__(self):
        super(RigidBodyTutorial, self).__init__()

        self.title = "PhysX Rigid Bodies"
        self.has_automation = True

        self.add_step(TutorialStep("Dynamic Simulation with PhysX Rigid Bodies", 
                """<html><p style="font-size:13px">Greetings!<br><br><i>Rigid bodies</i> are dynamic solid objects that 
                simulate reactions to collisions and other physical forces.<br><br>In this tutorial, you'll edit an 
                existing prefab to create a dynamic simulation with forces and collisions. You'll add a 
                <b>PhysX Collider</b> component and a <b>PhysX Rigid Body</b> component, create collider for the ground 
                plane, and simulate the results.</p></html>"""))
        self.add_step(StepOne("Preparing the scene", """<html><p style="font-size:13px">The default level includes 
                a bunch of starter entities. See what's included in the <b>Atom Default Environment</b>.<br><br>In 
                <b>Entity Outliner</b>, click the arrow next to the <b>Atom Default Environment</b> entity to expand it.
                <br><br>The list of child entities are all the entities in the level. Each entity has a collection of 
                components that provide some functionality. The <b>Sun</b> entity, for example, has a <b>Directional 
                Light</b> component the simulates a very bright distant light with parallel rays. It also has a 
                <b>Transform</b> component that places it in the level in relation to its parent, the <b>Atom Default 
                Environment</b> entity.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(StepTwo("Delete the Shader Ball entity", """<html><p style="font-size:13px">Tidy up the scene 
                a bit.<br><br>In <b>Entity Outliner</b>, click the <b>Shader Ball</b> entity to select it and press 
                <b>Del</b> to remove it from the level.</p></html>""", 
                "EntityOutlinerWidgetUI"))
        self.add_step(StepThree("Find a prefab in Asset Browser", """<html><p style="font-size:13px">A <i>prefab</i> 
                is a reusable asset that has been saved to disk and that can be added to a level as an instance or 
                spawned at runtime. Find a prefab to use the basis of the rigid body.<br><br>In 
                <b>Asset Browser</b>, use the <b>Search...</b> filter to find the 
                <strong><code style="font-size:14px;color:#E44C9A">20-sided-dice.prefab</code></strong>.
                </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(StepFour("Instantiate a prefab", """<html><p style="font-size:13px">To use the prefab in the 
                level you need to create an instance, or <i>instantiate</i> the prefab in the level.<br><br>Drag the 
                <strong><code style="font-size:14px;color:#E44C9A">20-sided-dice.prefab</code></strong> into the 
                viewport to instantiate it in the level.</p></html>""", "renderOverlay"))
        self.add_step(StepFive("Position the prefab", """<html><p style="font-size:13px"> Use the <b>Move</b> tool 
                to position the dice prefab instance in the camera's view.<ul><li>In the viewport, ensure the prefab 
                instance is selected by clicking it.</li><li>Use the translate handles to drag the prefab instance so 
                that it is in the yellow wireframe that represents the camera's view frustum.</li><li>Drag the prefab 
                instance up so that it is a few units above the ground plane.</li></p>
                </p></html>""", "renderOverlay"))
        self.add_step(StepSix("Open the prefab instance in Focus Mode", """<html><p style="font-size:13px">You'll 
                need to add a couple components to the prefab. The prefab in the level is an instance so it has to be 
                opened for editing in <b>Focus Mode</b><br><br>In <b>Entity Outliner</b> double-click the dice prefab 
                instance to open it for editing.<br><br>Note that the prefab instance is highlighted in a light blue 
                frame. In Focus Mode, any modifications you make happen in the context of the prefab instance that is 
                open for editing.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(StepSeven("Edit the dice entity", """<html><p style="font-size:13px">With the dice prefab 
                instance open for editing, you can see that it contains an entity (denoted by a white box icon). You'll 
                add some PhysX components to this entity.<br><br>In <b>Entity Outliner</b> click the <b>20-sided-dice</b> 
                entity to select it.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(StepEight("Inspect the dice entity", """<html><p style="font-size:13px"><b>Entity 
                Inspector</b> displays the dice entity's three components.<ul><li><b>Transform</b> - Places and orients 
                the entity in the local space of the prefab instance.</li><li><b>Mesh</b> - Supplies a render mesh for 
                the entity.</li><li><b>Material</b> - Applies shaders and textures to the render mesh.</il></ul>In the 
                next steps, you'll add and configure components in Entity Inspector.</p></html>""", 
                "InspectorMainWindow"))
        self.add_step(StepNine("Add a PhysX Collider", """<html><p style="font-size:13px">A collider is a simplified
                 mesh that defines a solid surface that can register collisions and overlaps with other colliders. To 
                add a collider to the entity, you'll add a <b>PhysX Collider</b> component.<br><br>In 
                <b>Entity Inspector</b>, click the <b>Add Component</b> button and select the PhysX Collider component 
                from the list to add a collider to the entity.<br><br>In the viewport, notice that there's now a 
                transparent mesh on the entity. This is the collider mesh. The dice source asset was configured to 
                generate a <i>convex</i> PhysX collision mesh when processed. A convex mesh is a simplified mesh that 
                can approximate a complex surface and be used in a dynamic physics simulation.<br><br>The PhysX Collider
                 component was automatically configured with the convex collider when you added it to the entity. In the 
                collider component, notice that the <b>Shape</b> property is set to 
                <strong><code style="font-size:14px;color:#E44C9A">PhysicsAsset</code></strong> and that the 
                <b>PhysX Mesh</b> property is set to <strong><code style="font-size:14px;color:#E44C9A"> 
                20-sided-dice</code></strong>, which is the convex mesh that was generated when the dice asset was 
                processed.</p></html>""", "m_addComponentButton"))
        self.add_step(StepTen("Add a PhysX Rigid Body", """<html><p style="font-size:13px">A rigid body is a 
                dynamic hard surface that responds to collisions and forces. Currently, the entity can be 
                collided with, but it won't respond when a simulation runs. You need to add a <b>PhysX Rigid Body</b> 
                component.<br><br>In <b>Entity Inspector</b> click the <b>Add Component</b> button and select the 
                PhysX Rigid Body component from the list.<br><br>The entity can now be simulated, but 
                there's a couple more things you need to do before you test it.</p></html>""", 
                "m_addComponentButton"))
        self.add_step(StepEleven("Add an initial linear velocity", """<html><p style="font-size:13px">The <b>PhysX 
                Rigid Body</b> component has a lot of properties. The most important one, <b>Gravity enabled</b>, is 
                turned on by default. When simulated, the entity will fall due to gravity. Add a small upward 
                initial velocity to the rigid body so you see an interesting result when you run the simulation.<br><br>
                In the PhysX Rigid Body component, set the <b>Initial linear velocity</b> property's <b>Z</b> value to 
                <strong><code style="font-size:14px;color:#E44C9A">10</code></strong>.</p></html>""", 
                "InspectorMainWindow"))
        self.add_step(StepTwelve("Add an initial angular velocity", """<html><p style="font-size:13px">You can also 
                spin the dice entity. Add a small initial angular velocity to the rigid body as well.<br><br>In 
                the <b>PhysX Rigid Body</b> component, set the <b>Initial angular velocity</b> property's <b>Y</b> 
                value to <strong><code style="font-size:14px;color:#E44C9A">15</code></strong>.<br><br>With these two 
                properties set, the entity will pop straight up and spin when the entity is activated.</p></html>""", 
                "InspectorMainWindow"))
        self.add_step(StepThirteen("Exit Focus Mode", """<html><p style="font-size:13px">You're done editing the prefab 
                instance, so you can exit Focus Mode.<br><br>In <b>Entity Outliner</b> double click the dice prefab 
                instance to close it.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(StepFourteen("Save the prefab", """<html><p style="font-size:13px">In <b>Entity Outliner</b>, 
                note the <b>*</b> asterisk next to the dice prefab file name on the left. This tells us the prefab 
                instance has been edited and there are unsaved changes. Save the prefab.<br><br>In Entity 
                Outliner, right-click the dice prefab instance and choose <b>Save Prefab to file</b>.<br><br>Saving the 
                prefab overwrites the prefab file on disk. Any new instances of the prefab will contain the <b>PhysX 
                Collider</b> and <b>PhysX Rigid Body</b> components you added in the previous steps.</p></html>""", 
                "EntityOutlinerWidgetUI"))
        self.add_step(StepFifteen("Add a ground plane collider", """<html><p style="font-size:13px">You need to add a 
                collider to the ground plane so that the dice prefab instance has a surface to collide against in the 
                simulation.<br><br>In <b>Entity Outliner</b>, right-click and select <b>Create Entity</b> from the 
                context menu.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(StepSixteen("Add a PhysX Shape Collider", """<html><p style="font-size:13px">With the 
                new entity selected, you'll add a <b>PhysX Shape Collider</b> component to create a collision surface for 
                the ground plane.<br><br>In <b>Entity Inspector</b> click the <b>Add Component</b> button and select the
                PhysX Shape Collider component from the list.</p></html>""", 
                "m_addComponentButton"))
        self.add_step(StepSeventeen("Add a Shape for the ground collider", """<html><p style="font-size:13px">In the 
                <b>PhysX Shape Collider</b> component, there is a warning about a missing component service. The shape 
                collider requires a shape component to define the collider.<br><br>Click the <b>Add Required 
                Component</b> button and select <b>Quad Shape</b> from the shape component list.</p></html>""", 
                "InspectorMainWindow"))
        self.add_step(StepEighteen("Set the ground collider size", """<html><p style="font-size:13px">The <b>Quad 
                Shape</b> component is a flat plane with a default size of one meter by one meter. You need to make it 
                much larger to ensure the dice prefab instance collides with it.<br><br>In the Quad Shape component, set
                 both the <b>Width</b> and <b>Height</b> properties to 
                 <strong><code style="font-size:14px;color:#E44C9A">512</code></strong> so that the collision plane 
                matches the size of the ground plane.</p></html>""", "InspectorMainWindow"))
        self.add_step(StepNineteen("Position the ground collider", """<html><p style="font-size:13px">The ground 
                collider you just created is not aligned with the ground mesh. Move the collider so that 
                it aligns better with the ground plane.<br><br>With the ground collider entity selected, in the 
                viewport, use the <b>Z</b> handle of the move tool to move the ground collider just enough for 
                the quad shape to disappear below the ground plane.</p></html>""", 
                "renderOverlay"))
        self.add_step(StepTwenty("Run the simulation", """<html><p style="font-size:13px">You can now run the 
                simulation and view the results. Press the <b>Play</b> button in the upper-right corner of 
                <b>O3DE Editor</b> to enter game mode. The dice prefab instance flies in the air an spins, 
                then falls and collide with the ground plane. Press <b>Esc</b> to exit.
                </p></html>""", {"type": QtWidgets.QToolButton, "text": "Play Game"}))

    def on_tutorial_start(self):
        print("Starting PhysX Rigid Body tutorial.")

    def on_tutorial_end(self):
        print("PhysX Rigid Body tutorial complete!")

class StepOne(TutorialStep):

        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 1")
                sleep(2)

class StepTwo(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 2")
                sleep(2)

class StepThree(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 3")
                sleep(2)

class StepFour(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 4")
                sleep(2)

class StepFive(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 5")
                sleep(2)

class StepSix(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 6")
                sleep(2)

class StepSeven(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 7")
                sleep(2)

class StepEight(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 8")
                sleep(2)

class StepNine(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 9")
                sleep(2)

class StepTen(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 10")
                sleep(2)

class StepEleven(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 11")
                sleep(2)

class StepTwelve(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 12")
                sleep(2)

class StepThirteen(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 13")
                sleep(2)

class StepFourteen(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 14")
                sleep(2)

class StepFifteen(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 15")
                sleep(2)

class StepSixteen(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 16")
                sleep(2)

class StepSeventeen(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 17")
                sleep(2)

class StepEighteen(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 18")
                sleep(2)

class StepNineteen(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step and set appropriate sleep()
                print("Automating step 19")
                sleep(2)

class StepTwenty(TutorialStep):
                
        def automate(self):
                # Add script logic to perform step
                print("Automating step 20")
                sleep(2)

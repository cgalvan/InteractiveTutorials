"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

import sys
import azlmbr

from PySide2.QtWidgets import QMenuBar

from tutorial import Tutorial, TutorialStep

class RigidBodyTutorial(Tutorial):
    def __init__(self):
        super(RigidBodyTutorial, self).__init__()

        self.title = "PhysX Rigid Bodies"

        self.add_step(TutorialStep("Dynamic Simulation with PhysX Rigid Bodies", 
                """<html><p style="font-size:13px">Greetings! <i>Rigid bodies</i> are dynamic solid objects that 
                simulate reactions to collisions and other physical forces. In this tutorial, we'll edit an existing 
                prefab, add a <b>PhysX Collider</b> component and a <b>PhysX Rigid Body</b> component, create collider 
                for the ground plane, and test the results.<br><br>Click next to continue.</p></html>"""))
        self.add_step(TutorialStep("Preparing the scene", """<html><p style="font-size:13px">The default level includes 
                a bunch of starter entities. Let's tidy up a bit.<br><br>In <b>Entity Outliner</b>, click the arrow next
                 to the <b>Atom Default Environment</b> entity to expand it.<br><br>The list of child entites are all 
                the entities in the curent level.<br><br><br>Step 1 of 20</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Delete the Shader Ball entity", """<html><p style="font-size:13px">In 
                <b>Entity Outliner</b>, click the <b>Shader Ball</b> entity to select it and press <b>DEL</b> to remove 
                it from the level.<br><br><br>Step 2 of 20</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Find a prefab in Asset Browser", """<html><p style="font-size:13px">A <i>prefab</i> 
                is a reusable asset that has been saved to disk, and can be instantiated in a level or spawned at 
                runtime. Let's instantiate a prefab to use the basis of the rigid body.<br><br>In <b>Asset Browser</b>, 
                use the <b>Search...</b> filter to find the 
                <strong><code style="font-size:14px;color:#E44C9A">20-sided-dice.prefab</code></strong>.
                <br><br><br>Step 3 of 20</p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Instantiate a prefab", """<html><p style="font-size:13px">A prefab is a file on 
                disk. To use the prefab in our level we need to create an instance, or <i>instantiate</i> the prefab.
                <br><br>Drag the 
                <strong><code style="font-size:14px;color:#E44C9A">20-sided-dice.prefab</code></strong> into the 
                viewport to instatiate it in our level.<br><br><br>Step 4 of 20</p></html>""", "renderOverlay"))
        self.add_step(TutorialStep("Position the prefab", """<html><p style="font-size:13px"> Use the <b>Move</b> tool 
                to position the dice prefab in the camera's view frustum.<ul><li>In the viewport, ensure the prefab is 
                selected by clicking it.</li><li>Use the translate handles to drag the prefab so that it is in the 
                yellow wireframe that represents the camera's view frustum.</li><li>Drag the prefab up so that it is a 
                few units above the ground plane.</li></p><p><br>Step 5 of 20</p></html>""", "renderOverlay"))
        self.add_step(TutorialStep("Open the prefab in Focus Mode", """<html><p style="font-size:13px">We'll need to 
                add a couple components to the prefab. The prefab in the level is an instance so it has to be opened for
                 editing in <b>Focus Mode</b><br><br>In <b>Entity Outliner</b> double-click the dice prefab to open it 
                for editing.<br><br>Note that the prefab is highlighted in a light blue frame and that the viewport also
                 has a light blue frame titled <b>Focus Mode</b>. In Focus Mode, any modifications we make, happen in 
                the context of the prefab that is open for editing.<br><br><br>Step 6 of 20</p></html>""", 
                "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Edit the dice entity", """<html><p style="font-size:13px">With the dice prefab open 
                for editing, we can see it contains an enity (denoted by a white box icon). We'll add some PhysX 
                components to this entity.<br><br>In <b>Enity Outliner</b> click the <b>20-sided-dice</b> entity to 
                select it.<br><br><br>Step 7 of 20</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Inspect the dice entity", """<html><p style="font-size:13px"><b>Entity 
                Inspector</b> displays the dice entity's three components.<ul><li><b>Transform</b> - Places and orients 
                the entity in the level.</li><li><b>Mesh</b> - Supplies a render mesh for the 
                entity.</li><li><b>Material</b> - Applies shaders and textures to the mesh.</il></ul>In the next steps 
                we'll add and configure components in Entity Inspector.<br><br><br>Step 8 of 20</p></html>""", 
                "InspectorMainWindow"))
        self.add_step(TutorialStep("Add a PhysX Collider", """<html><p style="font-size:13px">A collider is a simplified
                 mesh that defines a solid surface that can register collisions and overlaps with other colliders. To 
                add a collider entity, we'll add a <b>PhysX Collider</b> component.<br><br>In <b>Entity Inspector</b> 
                click the <b>Add Component</b> button and select the <b>PhysX Collider</b> component from the list to 
                add a collider to the entity.<br><br>In the viewport, notice that there's now a transparent mesh on the
                 entity. This is the colider mesh. The dice source asset was configured to generate a <i>convex</i> 
                PhysX collision mesh when processed. A convex mesh is a simplified mesh that can approximate a complex 
                surface and be used in a dynamic physics simulation.<br><br>The PhysX Collider component was 
                automatically configured with the convex collider when we added it to the entity. In the collider 
                component, notice that the <b>Shape</b> property is set to 
                <strong><code style="font-size:14px;color:#E44C9A">PhysicsAsset</code></strong> and that the 
                 <b>PhysX Mesh</b> property is set to <strong><code style="font-size:14px;color:#E44C9A">
                 20-sided-dice</code></strong>, the generated convex mesh.<br><br><br>Step 9 of 20</p></html>""", 
                "m_addComponentButton"))
        self.add_step(TutorialStep("Add a PhysX Rigid Body", """<html><p style="font-size:13px">A rigid body is a 
                dynamic hard surface that simulates reactions to collisions and forces. Currently, the enity can be 
                collided with, but it won't respond to collisions or forces. We need to add a <b>PhysX Rigid Body</b> 
                component.<br><br>In <b>Entity Inspector</b> click the <b>Add Component</b> button and select the 
                PhysX Rigid Body component from the list.<br><br>The entity is can now be simultated, but there's 
                a couple more things we need to do before we test it.<br><br><br>Step 10 of 20</p></html>""", 
                "m_addComponentButton"))
        self.add_step(TutorialStep("Add an initial linear velocity", """<html><p style="font-size:13px">The <b>PhysX 
                Rigid Body</b> component has a lot of properties. The most important one, <b>Gravity enabled</b>, is 
                turned on by default. When simulated the enity will fall due to gravity. Let's add a small upward 
                initial velocity to the rigid body so we see an interesting result when we test the simulation.<br><br>
                In the PhysX Rigid Body component, set the <b>Initial linear velocity</b> property's <b>Z</b> value to 
                <strong><code style="font-size:14px;color:#E44C9A">10</code></strong>.<br><br><br>Step 11 of 
                20</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Add an initial angular velocity", """<html><p style="font-size:13px">We can also 
                spin the dice entity. Let's add a small inital angular velocity to the rigid body as well.<br><br>In the
                 <b>PhysX Rigid Body</b> component, set the <b>Initial angular 
                velocity</b> property's <b>Y</b> value to 
                <strong><code style="font-size:14px;color:#E44C9A">15</code></strong>.<br><br>With these two properties 
                set, the entity will pop straight up and spin when the entity is activated.<br><br><br>Step 12 of 
                20</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Exit Focus Mode", """<html><p style="font-size:13px">We're done editing the prefab, 
                so let's exit Focus Mode.<br><br>In <b>Entity Outliner</b> double click the dice prefab to close 
                it.<br><br><br>Step 13 of 20</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Save the prefab", """<html><p style="font-size:13px">In <b>Entity Outliner</b>, 
                note the <b>*</b> asterisk next to the dice prefab file name on the left. This tells us the prefab 
                instance has been edited and there are unsaved changes. Let's save the prefab.<br><br>In Entity 
                Outliner, right-click the dice prefab and choose <b>Save Prefab to file</b>.<br><br>Saving the prefab 
                overwrites the prefab file on disk. Any new instances of the prefab will contain the <b>PhysX 
                Collider</b> and <b>PhysX Rigid Body</b> components added in the previous setps.<br><br><br>Step 14 of 
                20</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Add a ground plane collider", """<html><p style="font-size:13px">We need to add a 
                collider to the ground plane so that the dice prefab instance has a surface to collide against in the 
                simulation.<br><br>In <b>Entity Outliner</b>, right-click and select <b>Create Entity</b> from the 
                context menu.<br><br><br>Step 15 of 20</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Add a PhysX Shape Collider", """<html><p style="font-size:13px">With the 
                new enity selected, we'll add a <b>PhysX Shape Collider</b> componnet to create a collision surface for 
                the ground plane.<br><br>In <b>Entity Inspector</b> click the <b>Add Component</b> button and select 
                PhysX Shape Collider component from the list.<br><br><br>Step 16 of 20</p></html>""", 
                "m_addComponentButton"))
        self.add_step(TutorialStep("Add a Shape for the ground collider", """<html><p style="font-size:13px">In the 
                <b>PhysX Shape Collider</b> component, there is a warning about a missing component service. The shape 
                collider requires a shape component to define the collider. Let's add a <b>Quad Shape</b> 
                component.<br><br>Click the <b>Add Required Component</b> button and select <b>Quad Shape</b> from the 
                shape component list.<br><br><br>Step 17 of 20</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Set the ground collider size", """<html><p style="font-size:13px">The <b>Quad 
                Shape</b> component is a flat plane with a default size of one meter by one meter. We need to make it 
                much larger to ensure the dice prefab instance collides with it.<br><br>In the Quad Shape component, set
                 both the <b>Width</b> and <b>Height</b> properties to 
                 <strong><code style="font-size:14px;color:#E44C9A">512</code></strong> so the collision plane matches 
                 the size of the gorund plane.<br><br><br>Step 18 of 20</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Position the ground collider", """<html><p style="font-size:13px">The ground 
                collider we just created is not aligned with the ground mesh. Let's move the collider so that 
                it aligns better with the ground plane.<br><br>With the ground collider entity selected, in the 
                viewpoort, use the <b>Z</b> handle of the move tool to move the ground collider just enough for 
                the quad shape to disappear below the ground plane.<br><br><br>Step 19 of 20</p></html>""", 
                "renderOverlay"))
        self.add_step(TutorialStep("Test the simulation", """<html><p style="font-size:13px">We can now run the 
                simualtion and view the results. Press <b>CTRL+G</b> to enter game mode and see the dice prefab fly in 
                the air an spin, then fall an collide with the ground plane. Press <b>ESC</b> to exit.<br><br><br>Step 
                20 of 20</p></html>"""))

    def on_tutorial_start(self):
        print("Starting PhysX Rigid Body tutorial.")

    def on_tutorial_end(self):
        print("PhysX Rigid Body tutorial complete!")
"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""
import os
import sys
import azlmbr
import azlmbr.bus as bus
import azlmbr.editor as editor
import azlmbr.legacy.general as general
import azlmbr.entity as entity
import azlmbr.math as math
import azlmbr.prefab as prefab
from azlmbr.entity import EntityId
from editor_python_test_tools.utils import TestHelper as helper
import azlmbr.asset as asset
from PySide2.QtWidgets import QMenuBar
from PySide2.QtWidgets import QDialog
from tutorial import Tutorial, TutorialStep

class Tests():
    enter_game_mode            = ("Entered game mode",                       "Failed to enter game mode")
    exit_game_mode             = ("Exited game mode",                        "Couldn't exit game mode")
# fmt: on

class RigidBodyTutorial(Tutorial):
    def __init__(self):
        super(RigidBodyTutorial, self).__init__()

        self.title = "PhysX Rigid Bodies"
        self.current_step_index = 0
        self.last_clicked_step_index = 0

        self.add_step(TutorialStep("Dynamic Simulation with PhysX Rigid Bodies", 
                """<html><p style="font-size:13px">Greetings!<br><br><i>Rigid bodies</i> are dynamic solid objects that 
                simulate reactions to collisions and other physical forces.<br><br>In this tutorial, we'll edit an 
                existing prefab to create a dynamic simulation with forces and collisions. We'll add a 
                <b>PhysX Collider</b> component and a <b>PhysX Rigid Body</b> component, create collider for the ground 
                plane, and simulate the results.<br><br>Click next to continue.</p></html>"""))
        self.add_step(TutorialStep("Preparing the scene", """<html><p style="font-size:13px">The default level includes 
                a bunch of starter entities. Let's see what we have.<br><br>In <b>Entity Outliner</b>, click the arrow 
                next to the <b>Atom Default Environment</b> entity to expand it.<br><br>The list of child entites are 
                all the entities in the level. Each entity has a collection of components that provide some 
                functionality. The <b>Sun</b> entity, for example, has a <b>Directional Light</b> component the 
                simulates a very bright distant light with parallel rays. It also has a <b>Transform</b> component that 
                places it in the level in relation to it's parent, the <b>Atom Default Environment</b> entity.
                </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Delete the Shader Ball entity", """<html><p style="font-size:13px">Let's tidy up a 
                bit.<br><br>In <b>Entity Outliner</b>, click the <b>Shader Ball</b> entity to select it and press 
                <b>DEL</b> to remove it from the level.</p></html>""", 
                "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Find a prefab in Asset Browser", """<html><p style="font-size:13px">A <i>prefab</i> 
                is a reusable asset that has been saved to disk and that can be added to a level as an instance or 
                spawned at runtime. Let's find a prefab to use the basis of the rigid body.<br><br>In 
                <b>Asset Browser</b>, use the <b>Search...</b> filter to find the 
                <strong><code style="font-size:14px;color:#E44C9A">20-sided-dice.prefab</code></strong>.
                </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Instantiate a prefab", """<html><p style="font-size:13px">To use the prefab in our 
                level we need to create an instance, or <i>instantiate</i> the prefab in the level.<br><br>Drag the 
                <strong><code style="font-size:14px;color:#E44C9A">20-sided-dice.prefab</code></strong> into the 
                viewport to instatiate it in the level.</p></html>""", "renderOverlay"))
        self.add_step(TutorialStep("Position the prefab", """<html><p style="font-size:13px"> Use the <b>Move</b> tool 
                to position the dice prefab instance in the camera's view.<ul><li>In the viewport, ensure the prefab 
                instance is selected by clicking it.</li><li>Use the translate handles to drag the prefab instance so 
                that it is in the yellow wireframe that represents the camera's view frustum.</li><li>Drag the prefab 
                instance up so that it is a few units above the ground plane.</li></p>
                </p></html>""", "renderOverlay"))
        self.add_step(TutorialStep("Open the prefab instance in Focus Mode", """<html><p style="font-size:13px">We'll 
                need to add a couple components to the prefab. The prefab in the level is an instance so it has to be 
                opened for editing in <b>Focus Mode</b><br><br>In <b>Entity Outliner</b> double-click the dice prefab 
                instance to open it for editing.<br><br>Note that the prefab instance is highlighted in a light blue 
                frame and that the viewport also has a light blue frame titled <b>Focus Mode</b>. In Focus Mode, any 
                modifications we make happen in the context of the prefab instance that is open for editing.<br><br><br>
                </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Edit the dice entity", """<html><p style="font-size:13px">With the dice prefab 
                instance open for editing, we can see it contains an enity (denoted by a white box icon). We'll add some
                 PhysX components to this entity.<br><br>In <b>Enity Outliner</b> click the <b>20-sided-dice</b> entity 
                to select it.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Inspect the dice entity", """<html><p style="font-size:13px"><b>Entity 
                Inspector</b> displays the dice entity's three components.<ul><li><b>Transform</b> - Places and orients 
                the entity in the local space of the prefab instance.</li><li><b>Mesh</b> - Supplies a render mesh for 
                the entity.</li><li><b>Material</b> - Applies shaders and textures to the render mesh.</il></ul>In the 
                next steps, we'll add and configure components in Entity Inspector.</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Add a PhysX Collider", """<html><p style="font-size:13px">A collider is a simplified
                 mesh that defines a solid surface that can register collisions and overlaps with other colliders. To 
                add a collider to the entity, we'll add a <b>PhysX Collider</b> component.<br><br>In 
                <b>Entity Inspector</b>, click the <b>Add Component</b> button and select the PhysX Collider component 
                from the list to add a collider to the entity.<br><br>In the viewport, notice that there's now a 
                transparent mesh on the entity. This is the colider mesh. The dice source asset was configured to 
                generate a <i>convex</i> PhysX collision mesh when processed. A convex mesh is a simplified mesh that 
                can approximate a complex surface and be used in a dynamic physics simulation.<br><br>The PhysX Collider
                 component was automatically configured with the convex collider when we added it to the entity. In the 
                collider component, notice that the <b>Shape</b> property is set to 
                <strong><code style="font-size:14px;color:#E44C9A">PhysicsAsset</code></strong> and that the 
                <b>PhysX Mesh</b> property is set to <strong><code style="font-size:14px;color:#E44C9A"> 
                20-sided-dice</code></strong>, the generated convex mesh.</p></html>""", 
                "m_addComponentButton"))
        self.add_step(TutorialStep("Add a PhysX Rigid Body", """<html><p style="font-size:13px">A rigid body is a 
                dynamic hard surface that responds to collisions and forces. Currently, the enity can be 
                collided with, but it won't respond when a simulation runs. We need to add a <b>PhysX Rigid Body</b> 
                component.<br><br>In <b>Entity Inspector</b> click the <b>Add Component</b> button and select the 
                PhysX Rigid Body component from the list.<br><br>The entity can now be simulated, but 
                there's a couple more things we need to do before we test it.</p></html>""", 
                "m_addComponentButton"))
        self.add_step(TutorialStep("Add an initial linear velocity", """<html><p style="font-size:13px">The <b>PhysX 
                Rigid Body</b> component has a lot of properties. The most important one, <b>Gravity enabled</b>, is 
                turned on by default. When simulated, the enity will fall due to gravity. Let's add a small upward 
                initial velocity to the rigid body so we see an interesting result when we run the simulation.<br><br>
                In the PhysX Rigid Body component, set the <b>Initial linear velocity</b> property's <b>Z</b> value to 
                <strong><code style="font-size:14px;color:#E44C9A">10</code></strong>.</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Add an initial angular velocity", """<html><p style="font-size:13px">We can also 
                spin the dice entity. Let's add a small inital angular velocity to the rigid body as well.<br><br>In the
                 <b>PhysX Rigid Body</b> component, set the <b>Initial angular 
                velocity</b> property's <b>Y</b> value to 
                <strong><code style="font-size:14px;color:#E44C9A">15</code></strong>.<br><br>With these two properties 
                set, the entity will pop straight up and spin when the entity is activated.</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Exit Focus Mode", """<html><p style="font-size:13px">We're done editing the prefab 
                instance, so let's exit Focus Mode.<br><br>In <b>Entity Outliner</b> double click the dice prefab 
                instance to close it.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Save the prefab", """<html><p style="font-size:13px">In <b>Entity Outliner</b>, 
                note the <b>*</b> asterisk next to the dice prefab file name on the left. This tells us the prefab 
                instance has been edited and there are unsaved changes. Let's save the prefab.<br><br>In Entity 
                Outliner, right-click the dice prefab instance and choose <b>Save Prefab to file</b>.<br><br>Saving the 
                prefab overwrites the prefab file on disk. Any new instances of the prefab will contain the <b>PhysX 
                Collider</b> and <b>PhysX Rigid Body</b> components we added in the previous setps.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Add a ground plane collider", """<html><p style="font-size:13px">We need to add a 
                collider to the ground plane so that the dice prefab instance has a surface to collide against in the 
                simulation.<br><br>In <b>Entity Outliner</b>, right-click and select <b>Create Entity</b> from the 
                context menu.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Add a PhysX Shape Collider", """<html><p style="font-size:13px">With the 
                new enity selected, we'll add a <b>PhysX Shape Collider</b> componnet to create a collision surface for 
                the ground plane.<br><br>In <b>Entity Inspector</b> click the <b>Add Component</b> button and select the
                PhysX Shape Collider component from the list.</p></html>""", 
                "m_addComponentButton"))
        self.add_step(TutorialStep("Add a Shape for the ground collider", """<html><p style="font-size:13px">In the 
                <b>PhysX Shape Collider</b> component, there is a warning about a missing component service. The shape 
                collider requires a shape component to define the collider. Let's add a shape  
                component.<br><br>Click the <b>Add Required Component</b> button and select <b>Quad Shape</b> from the 
                shape component list.</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Set the ground collider size", """<html><p style="font-size:13px">The <b>Quad 
                Shape</b> component is a flat plane with a default size of one meter by one meter. We need to make it 
                much larger to ensure the dice prefab instance collides with it.<br><br>In the Quad Shape component, set
                 both the <b>Width</b> and <b>Height</b> properties to 
                 <strong><code style="font-size:14px;color:#E44C9A">512</code></strong> so that the collision plane 
                matches the size of the gorund plane.</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Position the ground collider", """<html><p style="font-size:13px">The ground 
                collider we just created is not aligned with the ground mesh. Let's move the collider so that 
                it aligns better with the ground plane.<br><br>With the ground collider entity selected, in the 
                viewpoort, use the <b>Z</b> handle of the move tool to move the ground collider just enough for 
                the quad shape to disappear below the ground plane.</p></html>""", 
                "renderOverlay"))
        self.add_step(TutorialStep("Run the simulation", """<html><p style="font-size:13px">We can now run the 
                simualtion and view the results. Press <b>CTRL+G</b> to enter game mode and see the dice prefab instance
                 fly in the air an spin, then fall and collide with the ground plane. Press <b>ESC</b> to exit.
                </p></html>"""))

    def on_tutorial_start(self):
        print("Starting PhysX Rigid Body tutorial.")
        
    def simulate(self):
        if self.current_step_index < 3 :
                return
        
        Working_Steps = [3, 5, 10, 16, 21]
        Step5_SubSteps = [1, 2, 3]
        
        #3 : delete shader ball
        #5 : prepare the dice entity
        #10 : add component features
        #16 : create ground collider entity
        #21 : enter focus mode

        current_working_step = 0
        last_working_step = 0

        #print("current step" + str(self.current_step_index))
        #print("last step" + str(self.last_clicked_step_index))

        for x in range(0, 3):
                if self.current_step_index >= Working_Steps[x] and self.current_step_index < Working_Steps[x + 1]:
                        current_working_step = Working_Steps[x]
                if self.last_clicked_step_index >= Working_Steps[x] and self.last_clicked_step_index < Working_Steps[x + 1]:
                        last_working_step = Working_Steps[x]

        print("current working step" + str(current_working_step))
        print("last working step" + str(last_working_step))

        # From this point on we know that something should be simulated
        if last_working_step == 0: #current_working_step has to be at least 3 to get to this point
                editor.EditorComponentAPIBus(bus.Broadcast, 'SetVisibleEnforcement', True)
                searchFilter = entity.SearchFilter()
                searchFilter.names = ['Shader Ball']
                searchResult = entity.SearchBus(bus.Broadcast, 'SearchEntities', searchFilter)
                shaderBallId = searchResult[0]
                editor.ToolsApplicationRequestBus(bus.Broadcast, 'DeleteEntityAndAllDescendants', shaderBallId)
        if current_working_step >= 5 and last_working_step < 5:
                #if current_working_step >= 5 and current_working_step <= 8:
                        # Instantiate and position the prefab
                        transform = math.Transform_CreateIdentity()
                        position = math.Vector3(0.0, 0.0, 5.0)
                        transform.invoke('SetPosition', position)
                        test_prefab_path = os.path.relpath("20-sided-dice/20-sided-dice.prefab")
                        dice_prefab = prefab.PrefabPublicRequestBus(bus.Broadcast, 'InstantiatePrefab', test_prefab_path, entity.EntityId(), position)
                        search_filter2 = entity.SearchFilter()
                        search_filter2.names = ["20-sided-dice"]
                        prefab_lc_root = entity.SearchBus(bus.Broadcast, 'SearchEntities', search_filter2)[0]  
                        azlmbr.prefab.PrefabFocusPublicRequestBus(bus.Broadcast, "FocusOnOwningPrefab", prefab_lc_root)
                        
                        #Create new Dice Entity parented to Prefab
                        newEntity5 = editor.ToolsApplicationRequestBus(bus.Broadcast, 'CreateNewEntity', EntityId())
                        editor.EditorEntityAPIBus(bus.Event, 'SetName', newEntity5, "20-sided-dice-2")   
                        #Add Mesh, Material, and Position Components to the Entity             
                        meshComponentTypeId = editor.EditorComponentAPIBus(bus.Broadcast, 'FindComponentTypeIdsByEntityType', ["Position"], entity.EntityType().Game)[0]
                        materialComponentTypeId = editor.EditorComponentAPIBus(bus.Broadcast, 'FindComponentTypeIdsByEntityType', ["Material"], entity.EntityType().Game)[0]
                        positionComponentTypeId = editor.EditorComponentAPIBus(bus.Broadcast, 'FindComponentTypeIdsByEntityType', ["Mesh"], entity.EntityType().Game)[0]
                        editor.EditorComponentAPIBus(bus.Broadcast, 'AddComponentsOfType', newEntity5, [meshComponentTypeId])
                        editor.EditorComponentAPIBus(bus.Broadcast, 'AddComponentsOfType', newEntity5, [materialComponentTypeId])
                        editor.EditorComponentAPIBus(bus.Broadcast, 'AddComponentsOfType', newEntity5, [positionComponentTypeId])
                
                        #Add PhysX Collider Component and Rigid Body Component
                        colliderComponentTypeId = editor.EditorComponentAPIBus(bus.Broadcast, 'FindComponentTypeIdsByEntityType', ["PhysX Collider"], entity.EntityType().Game)[0]
                        editor.EditorComponentAPIBus(bus.Broadcast, 'AddComponentsOfType', newEntity5, [colliderComponentTypeId])
                        rigidBodyComponentTypeId = editor.EditorComponentAPIBus(bus.Broadcast, 'FindComponentTypeIdsByEntityType', ["PhysX Rigid Body"], entity.EntityType().Game)[0]
                        editor.EditorComponentAPIBus(bus.Broadcast, 'AddComponentsOfType', newEntity5, [rigidBodyComponentTypeId])            

        #Edit Linear Velocity 
        if current_working_step >= 10 and last_working_step < 10:                        
                rigid_body_id = general.find_game_entity(newEntity5)
                azlmbr.physics.RigidBodyRequestBus(azlmbr.bus.Event, "SetGravityEnabled", newEntity5, True)
                azlmbr.physics.RigidBodyRequestBus(azlmbr.bus.Event, "SetLinearDamping", rigidBodyComponentTypeId, 0.06)
                azlmbr.physics.RigidBodyRequestBus(bus.Event, "SetLinearVelocity", rigid_body_id, 1.0)
                azlmbr.physics.RigidBodyRequestBus(bus.Event, "SetLinearVelocity", rigidBodyComponentTypeId, 3.0)
                        
                #Edit Linear Velocity 
                #Edit Angular Velocity 
                test_prefab_path = os.path.relpath("20-sided-dice/20-sided-dice.prefab")

                rigid_body_id = general.find_game_entity(newEntity5)
                azlmbr.physics.RigidBodyRequestBus(azlmbr.bus.Event, "SetGravityEnabled", newEntity5, True)
                azlmbr.physics.RigidBodyRequestBus(azlmbr.bus.Event, "SetLinearDamping", rigidBodyComponentTypeId, 0.06)
                azlmbr.physics.RigidBodyRequestBus(bus.Event, "SetLinearVelocity", rigid_body_id, 1.0)
                azlmbr.physics.RigidBodyRequestBus(bus.Event, "SetLinearVelocity", rigidBodyComponentTypeId, 3.0)
        if current_working_step == 16 or (current_working_step > 16 and last_working_step < 16):
                search_filter3 = entity.SearchFilter()
                search_filter3.names = ["Sun"]
                prefab_lc_root3 = entity.SearchBus(bus.Broadcast, 'SearchEntities', search_filter3)[0]
                azlmbr.prefab.PrefabFocusPublicRequestBus(bus.Broadcast, "FocusOnOwningPrefab", prefab_lc_root3)

                transform = math.Transform_CreateIdentity()
                position = math.Vector3(0.0, 0.0, 5.0)
                transform.invoke('SetPosition', position)
                collider_entity = editor.ToolsApplicationRequestBus(bus.Broadcast, 'CreateNewEntity', EntityId())
                shapeComponentTypeId = editor.EditorComponentAPIBus(bus.Broadcast, 'FindComponentTypeIdsByEntityType', ["PhysX Shape Collider"], entity.EntityType().Game)[0]
                editor.EditorComponentAPIBus(bus.Broadcast, 'AddComponentsOfType', collider_entity, [shapeComponentTypeId])
        if current_working_step == 21:
                helper.enter_game_mode(Tests.enter_game_mode)

    def set_last_clicked_step(self, x):
        self.last_clicked_step_index = x 

    def set_current_step(self, x):
        self.current_step_index = x

    def on_tutorial_end(self):
        print("PhysX Rigid Body tutorial complete!")

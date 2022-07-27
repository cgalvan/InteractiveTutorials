"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

import sys
import azlmbr

from PySide2.QtWidgets import QMenuBar

from tutorial import Tutorial, TutorialStep

class WindForcesTutorial(Tutorial):
    def __init__(self):
        super(WindForcesTutorial, self).__init__()

        self.title = "PhysX Wind Forces"

        self.add_step(TutorialStep("Create Wind Forces", 
                """<html><p style="font-size:13px">Greetings!<br><br>A <i>wind provider</i> is an entity that 
                defines a global or localized wind force that can affect certain components such as <b>Cloth</b> components. 
                <br><br>In this tutorial, we'll set up a local wind provider, add a cloth object to the scene, and configure the cloth object to simulate a sheet gently blowing in the breeze. 
                Let's begin by creating a new entity for a wind provider. Right click in <b>Entity Outliner</b> and choose <b>Create Entity</b> from the context menu. Name the new entity Wind Provider.
                <br><br>For this tutorial, make sure that you have the <b>Nvidia Cloth Gem</b> and <b>PhysX Gem</b> enabled in your project.</p></html>"""))
        self.add_step(TutorialStep("Add a Tag component",  """<html><p style="font-size:13px">
                Create an entity for the wind provider by right-clicking in <b>Entity Outliner</b> and selecting <b>Create Entity</b>.<br><br>
		We need to add a tag to the entity to identify it as a wind provider and specify the type of wind force. We can do this with a Tag component.
                In Entity Inspector, choose Add Component and select Tag from the components list to add a Tag component to the entity. </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Create a local wind force tag",  """<html><p style="font-size:13px">A wind provider can create a global wind force for the entire level, or a local wind force that is contained within a volume. Let's create a local wind force.
                In the Tag component, click the + button to add a new tag element. Enter wind in the new element field to create a local wind force.<br><br> </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Add a tag component for the entity",  """<html><p style="font-size:13px"> Edit the tag value to <b>global_wind</b>.
                <br><br> There are two types of wind: global and local, used to specify which entities provide wind forces. <br><br>
                If you choose to use the Local wind tag property, the wind force affects only certain entities.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Add a PhysX collider component",  """<html><p style="font-size:13px"> Wind providers must have a PhysX collider. For local wind forces, the collider specifies the volume that contains the wind force. 
                Objects are affected by the local wind force only when they are inside the wind provider's PhysX collider.
                In Entity Inspector, choose Add Component and add a PhysX Collider component to the entity. <br><br> </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Set the collider shape", """<html><p style="font-size:13px">We'll use a simple box for the volume of our local wind force.
                In Entity Inspector, in the PhysX Collider component, set the Shape property to Box.
                The wind force can only affect entities that are within this box collider shape. </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Resize the wind provider", """<html><p style="font-size:13px">The box is quite small. Let's enlarge it so that it affects a larger area and so that we can easily position the cloth entity inside it.
                In Entity Inspector in the PhysX Collider component, set the X, Y, and Z components of the Dimensions property to 5.0.</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Position the Entity", """<html><p style="font-size:13px"> Use the Move tool to position the wind provider entity in the level. 
                Ensure that the bottom of the PhysX collider box is roughly on the ground plane, and that the collider is in the camera's view frustum.</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Add a PhysX Force Region component", """<html><p style="font-size:13px"> 
                Ensure Entity Inspector is highlighted in this step. <br><br>Our wind provider entity has a Tag that identifies it as a local wind provider and a box collider that defines a volume for the wind force. We need to add a PhysX Force Region that defines the wind force.
                In Entity Inspector, choose Add Component, and select PhysX Force Region from the component list. </p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Configure the wind force component direction", """<html><p style="font-size:13px"> 
                We need to specify a direction for the wind force. <br><br>In <b>Entity Inspector</b>, in the <b>PhysX Force Region</b> 
                component, click the <b>+</b> button to add a force. <br><br>Set the <b>X</b> value of the <b>Direction</b> property to -1.0. Set the <b>Y</b> 
                value of the <b>Direction</b> property to -8.0. Set the <b>Z</b> value of the <b>Direction</b> property to 0.0. <br><br> 
                These value create a slightly off axis horizontal wind direction. Notice that the collider box has blue cones that display the direction of the wind force. </p></html>""", "InspectorMainWindow"))        
        self.add_step(TutorialStep("Configure the wind force magnitude", """<html><p style="font-size:13px"> 
                We can specify the strength of the wind force with the magnitude property.
                <br><br>In Entity Inspector, in the PhysX Force Region component, set Magnitude property to 8.0. </p></html>""", "InspectorMainWindow"))                
        self.add_step(TutorialStep("Add a Cloth Prefab", """<html><p style="font-size:13px">We'll test the wind provider by adding
                a NVIDIA Cloth Mesh. <br><br> In <b>Asset Browser</b>, locate <i>cloth_locked_edge.prefab</i> within
                <i>Gems/NvCloth/Assets/prefabs/Cloth</i>, and drag the prefab into the viewport. </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Position the Prefab", """<html><p style="font-size:13px">
                Ensure the viewport is highlighted. <br><br>Because we created a local wind force, the cloth prefab can only be affected when it is inside the wind provider's collider.
                <br><br>Use the Move tool to position the cloth prefab inside the collider box shape.
                </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Hide the Wind Provider Entity", """<html><p style="font-size:13px">Once the prefab's in position, you can hide the wind provider entity. In <b>Entity Outliner</b>, in the column to the 
                right of the wind provider entity, toggle the <b>Show/Hide Entity</b> setting. <br><br>
                </p></html>""", "EntityOutlinerWidgetUI"))        
        self.add_step(TutorialStep("Configure the Cloth Prefab", """<html><p style="font-size:13px">The cloth prefab 
                has its own local wind property enabled, which overrides the wind provider we created. Let's disable it.
                <br><br>In <b>Entity Outliner</b> double-click the <b>cloth_locked_edge</b> prefab to edit it in Focus Mode. 
                Select the <b>cloth_locked_edge</b> entity contained in the prefab. Then, in <b>Entity Inspector</b>, in the <b>Cloth</b> component, 
                expand the <b>Wind</b> property group and disable the <b>Enable local wind velocity</b> property.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Tune the Cloth Simulation", """<html><p style="font-size:13px">
                We need to enable the simulation to tune it. In <b>Entity Inspector<b/>, in the <b>Cloth component</b>, enable <b>Simulate in editor</b>
                to view the simulation. With the simulation running, we can adjust the various cloth properties to create a desired result. 
                Here are some suggested settings: <br><br>
                <b>Wind</b> <br>
                        <ul><li><b>Air drag coefficient </b>0.1</li><li><br>
                        <b>Air lift coefficient</b> 0,4</li></ul>
                <br><br><b>Fabric stiffness</b><br><ul><li>
                        <b>Horizontal </b>0.25</li>
                        <li><b>Vertical </b>0.25</li>
                        <li><b>Bending </b>0.25</li>
                        <li><b>Shearing </b>0.25</li></ul><br><br>
                The settings in this tutorial create a gentle breeze.<br><br> 
                Take some time to experiment with various properties of the <b>Cloth</b> component, as well as the wind direction and magnitude in the <b>PhysX Force Region</b> component to test their affect on the result of the simulation. </p></html>""", "EntityOutlinerWidgetUI"))


    def on_tutorial_start(self):
        print("Starting Wind Forces tutorial.")

    def on_tutorial_end(self):
        print("Wind Forces tutorial complete!")

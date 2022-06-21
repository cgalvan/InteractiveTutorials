"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

from tutorial import Tutorial, TutorialStep

class WindForcesTutorial(Tutorial):
    def __init__(self):
        super(WindForcesTutorial, self).__init__()

        self.title = "Create Wind Forces"

        self.add_step(TutorialStep("Create Wind Forces", """<html><p style="font-size:13px">Greetings!<br><br>We can use a <b>PhysX Force Region</b> component to
                create both global and local wind forces. Wind forces affect entities with components that are affected by wind,
                such as cloth. Wind forces don't affect <b>PhysX Rigid Body</b> components.
                For this tutorial, make sure that you have the <b>Nvidia Cloth Gem</b> enabled in your project.
                <br><br>Click next to continue.</p></html>"""))
        self.add_step(TutorialStep("Create a wind provider entity", """<html><p style="font-size:13px"><li>First, create an entity 
                for the wind provider. <li>Next, add a <b>Tag</b> component for the entity. The Tag will specify whether the 
                wind is a global or a local force. Edit the tag value to specify the wind type by choosing <b>PhysX Configuration</b>
                from the <b>Tools</b> menu and toggling the <b>Wind Configuration</b>. <br><br>
                <b>Wind Configuration</b> includes the <b>Global wind tag</b> and the <b>Local wind tag</b>. </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Update the Shape", """<html><p style="font-size:13px">Set the PhysX Collider component's Shape
                property to <i>Box</i>. </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Scale the Entity", """<html><p style="font-size:13px">Adjust the <b>Box Dimensions>
                to your specifications. If you're creating a localized wind force, make the dimenesions large enough that they can 
                contain the entity that receives the wind force.</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Position the Entity", """<html><p style="font-size:13px"> Use the <b>Move</b> tool 
                to position the entity in the level. For instance, you might consider positioning the entity so that 
                the bottom of the box is level with the ground. </p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Add a PhysX Region component to the entity", """<html><p style="font-size:13px"> 
                Select the <b>Add</b> button located next to <b>Forces</b>. Then, in the <b>Direction</b> property
                of your new force, set the <b>Y</b> component to <i>-1.0</i>, and the <b>Z</b> component to <i>0.0</i>, to create
                a direction for the wind. The PhysX collider box displays cones indicating the direction of the wind force. <br>
                Set the <b>Magnitude</b> to <i>10.0</i>. </p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Add a Cloth Prefab", """<html><p style="font-size:13px">We'll test the wind provider by adding
                a NVIDIA Cloth Mesh. In <b>Asset Browser</b>, navigate to <i>Gems\NvCloth\Assets\prefabs\Cloth</i>, then locate
                <i>cloth_locked_edge.prefab</i>, and drag that asset into the viewport. </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Position the Prefab", """<html><p style="font-size:13px">Use the Move tool to place the cloth prefab. 
                Once the prefab's in position, you can hide the wind provider entity. In <b>Entity Outliner</b>, in the column to the 
                right of the wind provider entity, toggle the <b>Show/Hide Entity</b> setting. <br><br>Note: if you're using the 
                <b>Local wind tag</b>, you must place the cloth asset inside the PhysX Collider volume of the wind provider entity. 
                </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Edit the Prefab", """<html><p style="font-size:13px">The cloth prefab has a local wind property 
                enabled which generates a local wind force that overrides our wind provider entity. We will deactiate the local
                wind force of the prefab so that we can view the results of the wind provider we created. <br><br>
                In Entity Outliner, double-click the <b>cloth_locked_edge</b> prefab to edit it in Focus Mode, and select the <b>cloth_locked_edge</b>
                entity. Then, in the Cloth component of the Entity Inspector, expand the <b>Wind</b> propoerty group and deselect
                <b>Enable local wind velocity</b>. </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Run the simulation", """<html><p style="font-size:13px">We can now run the 
                simualtion and view the results. With the <b>cloth_locked_edge</b> prefab open for editing in Focus mode, select the 
                <b> Simulate in editor</b> option located at the top of the Cloth component. As the simulation begins, the cloth object might flip and 
                stretch wildly, but it will quickly settle into a breezy wind simulation. The simulation plays while in editor mode, so you can 
                adjust various properties within the Cloth component and view the results in real time. <br>Consider adjusting the: <li>
                Air drag coefficient <li>Air lift coefficient<li>Air density<br></p></html>""","InspectorMainWindow"))
    def on_tutorial_start(self):
        print("Starting Wind Forces tutorial.")

    def on_tutorial_end(self):
        print("Wind Forces tutorial complete!")


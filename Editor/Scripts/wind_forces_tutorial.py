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
                <br><br>For this tutorial, make sure that you have the <b>Nvidia Cloth Gem</b> enabled in your project.
                <br><br>Click next to continue.</p></html>"""))
        self.add_step(TutorialStep("Create a wind provider entity", """<html><p style="font-size:13px">First, create an entity 
                for the wind provider. You can also use an existing entity. </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Create a Tab",  """<html><p style="font-size:13px">
		Next, right-click the entity and select the option to <b>Open Pinned Inspector</b>. </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Add a tag component for the entity",  """<html><p style="font-size:13px"> Within the Entity Inspector,
                select <b>Add Component</b> and add a <b>Tag</b> element to the entity. <br><br> </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Add a tag component for the entity",  """<html><p style="font-size:13px"> Edit the tag value to <b>global_wind</b>.
                <br><br> There are two types of wind: global and local, used to specify which entities provide wind forces. <br><br>
                If you choose to use the Local wind tag property, the wind force affects only certain entities.</p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Add a PhysX collider component for the entity",  """<html><p style="font-size:13px"> Still within the Entity Inspector,
                select <b>Add Component</b> and add a <b>PhysX Collider</b> component to the entity. <br><br> </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Update the Shape", """<html><p style="font-size:13px">Now, within the PhysX Collider component, set the <b>Shape</b>
                property to <b>Box</b>. </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Scale the Entity", """<html><p style="font-size:13px">Adjust the <b>Box Dimensions</b>
                to your taste. <br><br>If you're creating a local wind force, make the dimeneions large enough that they can 
                contain the entity that receives the wind force.</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Position the Entity", """<html><p style="font-size:13px"> Use the <b>Move</b> tool 
                to position the entity in the level. For instance, you might consider positioning the entity so that 
                the bottom of the box is level with the ground. </p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Add a PhysX Region component to the entity", """<html><p style="font-size:13px"> 
                Within the Entity Inspector, add a <b>PhysX Force Region</b> component. Select the <b>Add</b> button located next to <b>Forces</b>. Then, in the <b>Direction</b> property
                of your new force, set the <b>Y</b> component to <i>-1.0</i>, and the <b>Z</b> component to <i>0.0</i>, to create
                a direction for the wind. The PhysX collider box displays cones indicating the direction of the wind force. <br>
                Set the <b>Magnitude</b> to <i>10.0</i>. </p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Edit the PhysX Region component direction", """<html><p style="font-size:13px"> 
                Within the <b>PhysX Force Region</b> component, select the <b>Add</b> button located next to <b>Forces</b>. <br><br> In the <b>Direction</b> property
                of your new force, set the <b>Y</b> component to <i>-1.0</i>, and the <b>Z</b> component to <i>0.0</i>, to create
                a direction for the wind. <br><br> The PhysX collider box displays cones indicating the direction of the wind force. </p></html>""", "InspectorMainWindow"))        
        self.add_step(TutorialStep("Edit the PhysX Region component magnitude", """<html><p style="font-size:13px"> 
                Within the <b>PhysX Force Region</b> component, set the <b>Magnitude</b> to <i>10.0</i>. </p></html>""", "InspectorMainWindow"))                
        self.add_step(TutorialStep("Add a Cloth Prefab", """<html><p style="font-size:13px">We'll test the wind provider by adding
                a NVIDIA Cloth Mesh. <br><br> In <b>Asset Browser</b>, locate <i>cloth_locked_edge.prefab</i> within
                <i>Gems/NvCloth/Assets/prefabs/Cloth</i>, and drag the prefab into the viewport. </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Position the Prefab", """<html><p style="font-size:13px">Use the Move tool to place the cloth prefab. 
                </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Hide the Wind Provider Entity", """<html><p style="font-size:13px">Once the prefab's in position, you can hide the wind provider entity. In <b>Entity Outliner</b>, in the column to the 
                right of the wind provider entity, toggle the <b>Show/Hide Entity</b> setting. <br><br>Note: if you're using the 
                <b>Local wind tag</b>, you must place the cloth asset inside the PhysX Collider volume of the wind provider entity. 
                </p></html>""", "EntityOutlinerWidgetUI"))        
        self.add_step(TutorialStep("Select the Cloth Prefab", """<html><p style="font-size:13px">The cloth prefab has a local wind property 
                enabled which generates a local wind force that overrides our wind provider entity. We will deactivate the local
                wind force of the prefab so that we can view the results of the wind provider we created. <br><br>
                In Entity Outliner, double-click the <b>cloth_locked_edge</b> prefab to edit it in Focus Mode, and select the <b>cloth_locked_edge</b>
                entity. Then, in the Cloth component of the Entity Inspector, expand the <b>Wind</b> propoerty group and deselect
                <b>Enable local wind velocity</b>. </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Edit the Prefab", """<html><p style="font-size:13px">Then, in the Cloth component of the Entity Inspector, 
                expand the <b>Wind</b> property group and deselect
                <b>Enable local wind velocity</b>. </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Run the simulation", """<html><p style="font-size:13px">We can now run the 
                simualtion and view the results. <br><br>With the <b>cloth_locked_edge</b> prefab open for editing in Focus mode, select the 
                <b> Simulate in editor</b> option located at the top of the Cloth component. </p></html>""","InspectorMainWindow"))
        self.add_step(TutorialStep("Run the simulation", """<html><p style="font-size:13px"> As the simulation begins, the cloth object might flip and 
                stretch wildly, but it will quickly settle into a breezy wind simulation. <br><br>The simulation plays while in editor mode, so you can 
                adjust various properties within the Cloth component and view the results in real time. <br>Consider adjusting the air drag coefficient,
                air lift coefficient, or air density. </p></html>""","InspectorMainWindow"))

    def on_tutorial_start(self):
        print("Starting Wind Forces tutorial.")

    def on_tutorial_end(self):
        print("Wind Forces tutorial complete!")



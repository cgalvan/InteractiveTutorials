"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of 
this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

from PySide2 import QtWidgets

from tutorial import Tutorial, TutorialStep

class WindForcesTutorial(Tutorial):
    def __init__(self):
        super(WindForcesTutorial, self).__init__()

        self.title = "PhysX Wind Forces"

        self.add_step(TutorialStep("PhysX Wind Forces", 
                """<html><p style="font-size:13px">Greetings!<br><br>A <i>wind 
                provider</i> is an entity that defines a global or localized 
                wind force that can affect certain components such as 
                <b>Cloth</b> components. <br><br>In this tutorial, you'll set up
                 a local wind provider, add a cloth object to the scene, and 
                configure the cloth object to simulate a sheet gently blowing in
                 the breeze. <br><br>For this tutorial, make sure that you have 
                 the <b>Nvidia Cloth Gem</b> and <b>PhysX Gem</b> enabled in 
                 your project.</p></html>"""))
        self.add_step(TutorialStep("Create a wind provider entity", """<html>
                <p style="font-size:13px">Begin by creating a new entity for a 
                wind provider.<br><br>Right click in <b>Entity Outliner</b> and 
                choose <b>Create Entity</b> from the context menu. Name the new 
                entity <strong><code style="font-size:14px;color:#E44C9A">Wind 
                Provider</code></strong>.</p></html>""", 
                "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Add a Tag component",  """<html><p style=
                "font-size:13px">The entity needs a tag that identifies it as a 
                wind provider and specifies the type of wind force. You can add 
                the tag with a <b>Tag</b> component.<br><br>In Entity Inspector,
                 choose <b>Add Component</b> and select <b>Tag</b> from the 
                components list to add a Tag component to the entity. 
                </p></html>""", "m_addComponentButton"))                
        self.add_step(TutorialStep("Create a local wind force tag",  """<html>
                <p style="font-size:13px">A wind provider can create a global 
                wind force for the entire level, or a local wind force that is 
                contained within a volume. You'll create a local wind force.
                <br><br>In <b>Entity Inspector</b>, in the <b>Tag</b> component,
                 click the <b>+</b> button to add a new tag element.<br><br>
                Enter <strong><code style="font-size:14px;color:#E44C9A">wind
                </code></strong> in the new element field to create a local 
                wind force.</p></html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Add a PhysX Collider component",  """<html>
                <p style="font-size:13px"> Wind providers must have a PhysX 
                collider. For local wind forces, the collider defines the volume
                 that contains the wind force. Objects are affected by the local
                  wind force only when they are inside of the wind provider's 
                PhysX collider.<br><br>In <b>Entity Inspector</b>, choose <b>Add
                 Component</b> and add a <b>PhysX Collider</b> component to the 
                 entity.</p></html>""", "m_addComponentButton"))
        self.add_step(TutorialStep("Set the collider shape", """<html>
                <p style="font-size:13px">You'll use a simple box for the volume
                 of your local wind force.<br><br>In <b>Entity Inspector</b>, in
                 the <b>PhysX Collider</b> component, set the <b>Shape</b> 
                property to <strong><code style="font-size:14px;color:#E44C9A">
                Box</code></strong>.<br><br>The wind force can only affect 
                entities that are within this box collider shape.</p></html>""",
                 "InspectorMainWindow"))
        self.add_step(TutorialStep("Resize the wind provider", """<html><p 
                style="font-size:13px">The box is quite small. Enlarge it 
                so that it affects a larger area and so that you can easily 
                position the cloth entity inside it.<br><br>In <b>Entity 
                Inspector</b>, in the <b>PhysX Collider</b> component, set the 
                <b>X</b>, <b>Y</b>, and <b>Z</b> components of the 
                <b>Dimensions</b> property to <strong><code 
                style="font-size:14px;color:#E44C9A">5.0</code></strong>.</p>
                </html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Position the wind provider", """<html>
                <p style="font-size:13px">Use the <b>Move</b> tool to position 
                the wind provider entity in the level. Ensure that the bottom of
                 the PhysX collider box is roughly on the ground plane, and that
                 the collider is in the camera's view frustum.</p></html>""", 
                "renderOverlay"))
        self.add_step(TutorialStep("Add a PhysX Force Region component", 
                """<html><p style="font-size:13px">The wind provider entity has
                 a tag that identifies it as a local wind provider and a box 
                collider that defines a volume for the wind force. You need to 
                add a <b>PhysX Force Region</b> component that defines the wind 
                force.<br><br>In <b>Entity Inspector</b>, choose <b>Add 
                Component</b>, and select <b>PhysX Force Region</b> from the 
                component list.</p></html>""", "m_addComponentButton"))
        self.add_step(TutorialStep("Configure the wind force direction", """
                <html><p style="font-size:13px">You need to specify a direction 
                for the wind force.<br><br>In <b>Entity Inspector</b>, in the 
                <b>PhysX Force Region</b> component, click the <b>+</b> button 
                to add a force.<br><br>In the new force, set the following 
                values for the <b>Direction</b> properties:<br><br>
                X: <strong><code style="font-size:14px;
                color:#E44C9A">-1.0</code></strong><br>
                Y: <strong><code style="font-size:14px;
                color:#E44C9A">0.5</code></strong><br>
                Z: <strong><code style="font-size:14px;
                color:#E44C9A">0.0</code></strong><br><br>
                These values create a slightly off axis horizontal wind 
                direction. Notice that the collider box has blue cones that 
                display the direction of the wind force.</p></html>""", 
                {"text": "Forces", "type": QtWidgets.QFrame}))       
        self.add_step(TutorialStep("Configure the wind force magnitude", """
                <html><p style="font-size:13px">You can specify the strength of 
                the wind force with the magnitude property.<br><br>In <b>Entity 
                Inspector</b>, in the <b>PhysX Force Region</b> component, set 
                the <b>Magnitude</b> property to <strong>
                <code style="font-size:14px;color:#E44C9A">8.0</code></strong>.
                </p></html>""", 
                {"text": "Magnitude", "type": QtWidgets.QFrame}))              
        self.add_step(TutorialStep("Add a cloth prefab", """<html><p 
                style="font-size:13px">You'll test the wind provider by adding a
                 NVIDIA Cloth Mesh.<br><br>In <b>Asset Browser</b>, locate the
                <strong><code style="font-size:14px;color:#E44C9A">
                cloth_locked_edge.prefab</code></strong> within <strong><code 
                style="font-size:14px;color:#E44C9A">
                Gems/NvCloth/Assets/prefabs/Cloth</code></strong>, and drag the 
                prefab into the viewport.</p></html>""", 
                "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Position the prefab", """<html><p 
                style="font-size:13px">Because you created a local wind force, 
                the cloth prefab can only be affected when it is inside the wind
                 provider's collider.<br><br>Use the <b>Move</b> tool to 
                position the cloth prefab in the center of the collider box 
                shape.</p></html>""", "renderOverlay"))
        self.add_step(TutorialStep("Hide the Wind Provider entity", """<html><p 
                style="font-size:13px">Once the prefab's in position, you can 
                hide the wind provider entity.<br><br>In <b>Entity Outliner</b>,
                 in the column to the right of the wind provider entity, toggle 
                the <b>Show/Hide Entity</b> setting.
                </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Test the simulation", """<html><p 
                style="font-size:13px">You can test the simulation by entering 
                <b>Game Mode</b>.<br><br>In the upper-right corner of <b>O3DE 
                Editor</b>, click the play button to enter game mode.<br><br>
                The cloth falls and settles into an unnatural shape. In the next
                 steps, you'll adjust some properties to create a more natural 
                looking simulation. Press <b>Esc</b> to return to the editor.
                </p></html>""", {"type": QtWidgets.QToolButton, "text": 
                "Play Game"}))
        self.add_step(TutorialStep("Open the cloth prefab", """<html><p 
                style="font-size:13px">The cloth prefab has its own local wind 
                property enabled, which overrides any wind providers in the 
                level. You need to disable it for the cloth prefab to be 
                affected by the wind provider you created.<br><br>In <b>Entity 
                Outliner</b> double-click the <b>cloth_locked_edge</b> prefab to
                 edit it in <i>Focus Mode</i>. Then, click the 
                <b>cloth_locked_edge</b> entity contained in the prefab to 
                inspect its components.</p></html>""", 
                "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Edit the cloth prefab", """<html><p 
                style="font-size:13px">Disable the local wind force in the <b>
                Cloth</b> component.<br><br>In <b>Entity Inspector</b>, in the 
                <b>Cloth</b> component, expand the <b>Wind</b> property group 
                and disable the <b>Enable local wind velocity</b> property.
                </p></html>""", {"text": "Wind", "type": QtWidgets.QFrame}))
        self.add_step(TutorialStep("Tune the cloth simulation", """<html>
                <p style="font-size:13px">
                You can enable the simulation in the editor to tune it.<br><br>
                In <b>Entity Inspector</b>, in the <b>Cloth</b> component, 
                enable the <b>Simulate in editor</b> toggle to view the 
                simulation. With the simulation running, you can adjust 
                the various cloth properties to create a desired result. Here 
                are some suggested settings to create a gentle breeze:<br><br>
                <b>Wind</b><br>
                Air drag coefficient: <strong><code 
                style="font-size:14px;color:#E44C9A">0.1</code></strong><br>
                Air lift coefficient: <strong><code 
                style="font-size:14px;color:#E44C9A">0.4</code></strong><br>
                <b>Fabric stiffness</b><br>
                Horizontal: <strong><code 
                style="font-size:14px;color:#E44C9A">0.25</code></strong><br>
                Vertical: <strong><code style=
                "font-size:14px;color:#E44C9A">0.25</code></strong><br>
                Bending: <strong><code style="
                font-size:14px;color:#E44C9A">0.25</code></strong><br>
                Shearing: <strong><code style="
                font-size:14px;color:#E44C9A">0.25</code></strong><br>
                <br>
                Take some time to experiment with various properties of the 
                Cloth component, as well as the wind direction and magnitude in 
                the <b>PhysX Force Region</b> component to test their affect on 
                the simulation. </p></html>""", "EntityPropertyEditor"))
                
    def on_tutorial_start(self):
        print("Starting Wind Forces tutorial.")

    def on_tutorial_end(self):
        print("Wind Forces tutorial complete!")

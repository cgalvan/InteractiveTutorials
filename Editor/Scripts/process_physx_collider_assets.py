"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

from tutorial import Tutorial, TutorialStep

class ColliderAssetsTutorial(Tutorial):
    def __init__(self):
        super(ColliderAssetsTutorial, self).__init__()

        self.title = "PhysX Collider Assets"

        self.add_step(TutorialStep("Process PhysX Collider Assets", 
                """<html><p style="font-size:13px">Greetings!<br><br><i>Collider assets</i> are assets
                generated based on input meshes. There are various types of colliders, such as triangle, primitive, and convex. 
                Colliders are categorized based on the shapes they are comprised of: triangle, sphere,
                box, capsule, and/or convex. <br><br>In this tutorial, we'll edit an 
                existing source asset to create a Physx collider asset. <br><br>Click next to continue.</p></html>"""))
        self.add_step(TutorialStep("Select the Asset", """<html><p style="font-size:13px">Locate your source asset in the 
                <b>Asset Browser</b>. You can use your own or use one of the provided <i>.fbx</i> files, such as <i>sphere.fbx</i>. 
                Right click the <i>.fbx</i> source asset and select 'Edit Settings.' 
                </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Add a PhysX Mesh", """<html><p style="font-size:13px"> Select the 
                PhysX tab and select <b>Add another physxmesh</b> to create a PhysX mesh group. <br><br>
                Each PhysX group produces as <i>.pxmesh</i> product asset.
                </p></html>""", 
                "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Add a PhysX Mesh", """<html><p style="font-size:13px"> To select which 
                meshes to include in the PhysX mesh group, use the file select button. <br><br> If you select multiple meshes, 
                you might want to also enable the <b>Merge Meshes</b> and <b>Weld Vertices</b>
                features to optimize the asset's appearance. 
                </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Customize the PhysX Mesh Collider Type", """<html><p style="font-size:13px"> Customize the 
                PhysX mesh collider type by setting the <b>Export As</b> property to the type you choose. You might prefer to 
                selecct the 'Convex' type so that you can create any type of entity (static, kinematic, dynamic), but 
                Triangle and Primitive types each also have their respective advantages and limitations. <br><br>You can visit the 
                Docs online if you want to learn more.<br><br> Then select <b>Update</b> (in the bottom right corner) 
                to update the <i>.assetinfo</i> file and trigger the Asset Processor. </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("View the Entity", """<html><p style="font-size:13px"> .</li><li>Drag the <i>.azmodel</i> 
                product asset into the viewport from the Asset Browser.<br><br> As you do this, O3DE automatically creates
                an entity with a <b>Mesh</b> component referencing the mesh product asset. </li></p>
                </p></html>""", "renderOverlay"))
        self.add_step(TutorialStep("View the Entity with the Collider component", """<html><p style="font-size:13px" Select the entity 
                in the viewport. Then, in <b>Entity Inspector</b>, select <b>Add Component</b> and then <b>PhysX Collider</b>.
                The component we've just added automatically detects the <i>.pxmesh</i> asset. <br><br>
                The <Shape> is set to <i>PhysicsAsset</i> and the <PhysX Mesh> references the <i>.pxmesh</i> product asset. <br><br><br>
                </html>""", "InspectorMainWindow"))
        self.add_step(TutorialStep("Optimize your Entity", """<html><p style="font-size:13px">Our entity is currently static, because 
                we only have a PhysX Collider component. A static entity is solid (it can be collided with) but does not move
                in response to collisions. <li>If you want a static entity, you can enable the <b>Static</b> property within the <b>Transform</b>
                component to maximize your entity's runtime performance. <li>If you want a dynamic entity, add a <b>PhysX Rigid Body</b>
                component. (Make sure that the <b>Static</b> property in the <b>Transform</b> component is disabled.)
                Select the entity in the viewport. Then, in <b> Entity Inspector</b>, select <b>Add Compoonent</b> and then 
                <b>PhysX Rigid Body</b> to enable the effect of gravity on your entity. You can observe the changes by selecting the 
                simulation button. <li>If you want a kinematic entity, add a <b>PhysX Rigid Body Component</b>. Then, within the component,
                enable the <b>Kinematic</b> property. (Make sure that the <b>Static</b> property in the <b>Transform</b> component is disabled.) </p></html>""", "InspectorMainWindow"))
        
    def on_tutorial_start(self):
        print("Starting PhysX Collider Assets tutorial.")

    def on_tutorial_end(self):
        print("PhysX Collider Assets tutorial complete!")

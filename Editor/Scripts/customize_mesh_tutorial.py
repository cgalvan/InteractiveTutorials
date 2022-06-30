
"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

from tutorial import Tutorial, TutorialStep

class CustomizeMeshAssetProcessingTutorial(Tutorial):
    def __init__(self):
        super(CustomizeMeshAssetProcessingTutorial, self).__init__()

        self.title = "Customize Mesh Asset Processing"

        self.add_step(TutorialStep("Customize Mesh Asset Processing", 
                """<html><p style="font-size:13px">Greetings!<br><br><i> Meshes </i> refer to the external appearances
                of objects.<br>In this tutorial, we'll edit the mesh of a sphere by enlarging it. We'll also introduce
                some other ways you can edit the mesh. <br><br>Click next to continue.</p></html>"""))
        self.add_step(TutorialStep("Preparing the scene", """<html><p style="font-size:13px">The <b>Asset Processor </b> runs 
                in the background automatically detecting source assets and scheduling process jobs for them.
                <br><br>In <b>Asset Browser</b>, locate your asset by typing <b>sphere.fbx</b> in the search field.
                </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Preparing the scene", """<html><p style="font-size:13px">Right click the
                <b>.fbx</b> source asset to expand it and select 'Edit Settings' from the context menu to open Scene Settings.
                </p></html>""", "AzAssetBrowserWindowClass"))        
        self.add_step(TutorialStep("Edit the Scene Settings", """<html><p style="font-size:13px">The Scene Settings window 
                presents different tabs depending on the contents of the source asset file. 
                Make sure the <b>Meshes</b> tab is selected.
                </p></html>""", "AzAssetBrowserWindowClass"))            
        self.add_step(TutorialStep("Edit the Scene Settings", """<html><p style="font-size:13px">By default, 
                all the meshes in a source asset are processed as a single group, each of which produces a set of product assets. Let's create additional mesh groups for our sphere source asset by
                choosing <b>Add another mesh.</b><br><br>
                The Name mesh property contains the name of the source asset.
                The Select meshes property reads All meshes selected. 
                You can choose the file select button to select which meshes to include in the mesh group.
                For this tutorial, you can use the default mesh group with all meshes selected.
                </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Change the Coordinate System", """<html><p style="font-size:13px">Let’s add a modifier to customize 
                how the asset is processed. Choose the <b>Add Modifier</b> button to view the mesh modifier list 
                and select <b>Coordinate system change</b>. <br><br>
                The Coordinate system change mesh modifier is used to scale or transform the asset for scenarios 
                where the asset might be too small, too large, or incorrectly oriented in O3DE. 
                By default, the modifier provides a single option to rotate the mesh 180 degrees. 
                </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Change the Coordinate System", """<html><p style="font-size:13px"> Select the <b>Use advanced settings</b> toggle 
                to expose the advanced modifier settings
                </p></html>""", "AzAssetBrowserWindowClass"))        
        self.add_step(TutorialStep("Change the Coordinate System", """<html><p style="font-size:13px"> Now we can
                 customize the scale of the asset. Set the <b>Scale</b> property to <i>5.0</i> to scale the asset to five times its size.
                </p></html>""", "AzAssetBrowserWindowClass"))        
        self.add_step(TutorialStep("Position the prefab", """<html><p style="font-size:13px"> 
                Choose the <b>Update</b> button at the bottom-right of Scene Settings. 
                This creates or updates the .assetinfo sidecar file and triggers Asset Processor to reprocess the asset.
                Drag the .azmodel product asset from Asset Browser into the viewport.
                </p></html>""", "renderOverlay"))        
        self.add_step(TutorialStep("View Changes", """<html><p style="font-size:13px">To use the prefab in our 
                level we need to create an instance, or <i>instantiate</i> the prefab in the level.<br><br>Drag the 
                <strong><code style="font-size:14px;color:#E44C9A">20-sided-dice.prefab</code></strong> into the 
                viewport to instatiate it in the level.</p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Position the prefab", """<html><p style="font-size:13px"> 
                Choose the <b>Update</b> button at the bottom-right of Scene Settings. 
                This creates or updates the .assetinfo sidecar file and triggers Asset Processor to reprocess the asset.
                Drag the .azmodel product asset from Asset Browser into the viewport.
                </p></html>""", "renderOverlay"))

    def on_tutorial_start(self):
        print("Starting Mesh Asset Process tutorial.")

    def on_tutorial_end(self):
        print("Mesh Asset Process tutorial complete!")
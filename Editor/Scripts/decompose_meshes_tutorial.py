"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

from tutorial import Tutorial, TutorialStep

class DecomposeInputMeshes(Tutorial):
    def __init__(self):
        super(DecomposeInputMeshes, self).__init__()

        self.title = "Decompose Input Meshes"

        self.add_step(TutorialStep("Decompose Input Meshes", 
                """<html><p style="font-size:13px">Greetings!<br><br>Exporting a PhysX mesh as a convex or a primitive collider 
                might not produce good results if the mesh’s shape is concave or doesn’t closely fit one of the primitive shapes. 
                Exporting a PhysX mesh as a triangle mesh collider creates a collider that accurately resembles the original mesh, 
                but won’t work with a dynamic entity. For these scenarios, O3DE supports approximate convex decomposition. 
                <br><br>Assets composed of multiple and/or complex meshes, 
                such as some kinematic or dynamic entities, might require similarly complex PhysX collider assets. In these cases,
                you can decompose the input mesh into convex parts. You can automatically generate primitive or convex colliders,
                fit them to each part, and process them as collider <i>.pxmesh</i> product assets. <br><br>
                Mesh decomposition is part of the process of 
                generating and fitting primitive or convex collider assets, and it doesn’t alter the input mesh. 
                .<br><br>Click next to continue.</p></html>"""))
        self.add_step(TutorialStep("Select the Asset", """<html><p style="font-size:13px">Locate your source asset in the 
                <b>Asset Browser</b>. You can use your own or use one of the provided <i>.fbx</i> files, such as <i>sphere.fbx</i>. 
                </p></html>""", "AzAssetBrowserWindowClass"))        
        self.add_step(TutorialStep("Select the Asset", """<html><p style="font-size:13px">Right click the <i>.fbx</i> 
                source asset and select 'Edit Settings.' 
                </p></html>""", "AzAssetBrowserWindowClass"))        
        self.add_step(TutorialStep("Decompose Meshes", """<html><p style="font-size:13px">In Scene Settings, underneath 
                <b>PhysX Mesh Group</b>, select <b>Export As</b>. You can export the mesh as either <i>Primitive</i> or <i>Convex</i>. <br><br>
                <li>For primitive colliders, the input mesh is decomposed into primitive parts. The best fitting primitive shapes 
                are automatically selected and transformed to encompass each part and the primitives are processed as a 
                product asset. <li>For convex colliders, the input mesh is decomposed into convex parts.
                A convex hull is generated for each part and the convex hulls are processed as a collider product asset. 
                In general, collider assets generated with decomposed meshes provide a more accurate representation of 
                the render mesh than a single primitive or convex collider can. 
                </p></html>""", "EntityOutlinerWidgetUI"))
        self.add_step(TutorialStep("Decompose Meshes", """<html><p style="font-size:13px"> Next, enable
                <b>Decompose Meshes</b>. Enabling Decompose Meshes reveals many options that you can use to fine-tune mesh decomposition. 
                <br><br> </p></html>""", "EntityOutlinerWidgetUI"))   
        self.add_step(TutorialStep("Decompose Meshes", """<html><p style="font-size:13px"> Finally, you can add a comment, or multiple, to the file for the 
                PhysX mesh group. You can add a comment about changes made to the source asset file for tracking purposes or notes on export options, 
                for example. Comments don’t affect how files are processed. 
                <br><br> </p></html>""", "EntityOutlinerWidgetUI"))

    def on_tutorial_start(self):
        print("Starting tutorial to decompose input meshes.")

    def on_tutorial_end(self):
        print("'Decompose input meshes' tutorial complete!")
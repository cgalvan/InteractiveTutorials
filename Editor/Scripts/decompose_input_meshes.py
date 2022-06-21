"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

import sys
import azlmbr

from PySide2.QtWidgets import QMenuBar

from tutorial import Tutorial, TutorialStep

class DecomposeInputMeshes(Tutorial):
    def __init__(self):
        super(DecomposeInputMeshes, self).__init__()

        self.title = "Decompose Input Meshes"

        self.add_step(TutorialStep("Decompose Input Meshes", 
                """<html><p style="font-size:13px">Greetings!<br><br>Assets composed of multiple and/or complex meshes, 
                such as some kinematic or dynamic entities, might require similarly complex PhysX collider assets. In these cases,
                you can decompose the input mesh into convex parts. You can automatically generate primitive or convex colliders,
                fit them to each part, and process them as collider <i>.pxmesh</i> product assets. <br><br>
                Mesh decomposition is part of the process of 
                generating and fitting primitive or convex collider assets, and it doesn’t alter the input mesh. 
                .<br><br>Click next to continue.</p></html>"""))
        self.add_step(TutorialStep("Select the Asset", """<html><p style="font-size:13px">Locate your source asset in the 
                <b>Asset Browser</b>. You can use your own or use one of the provided <i>.fbx</i> files, such as <i>sphere.fbx</i>. 
                Right click the <i>.fbx</i> source asset and select 'Edit Settings.' 
                </p></html>""", "AzAssetBrowserWindowClass"))
        self.add_step(TutorialStep("Decompose Meshes", """<html><p style="font-size:13px">In Scene Settings, underneath 
                <b>PhysX Mesh Group</b>, choose to <b>Export As</b> either <i>Primitive</i> or <i>Convex</i>. Then enable
                <b>Decompose Meshes</b>. <br><br>
                <li>For primitive colliders, the input mesh is decomposed into primitive parts. The best fitting primitive shapes 
                are automatically selected and transformed to encompass each part and the primitives are processed as a 
                product asset. <li>For convex colliders, the input mesh is decomposed into convex parts.
                A convex hull is generated for each part and the convex hulls are processed as a collider product asset. 
                In general, collider assets generated with decomposed meshes provide a more accurate representation of 
                the render mesh than a single primitive or convex collider can.  </p></html>""", "EntityOutlinerWidgetUI"))
  
    def on_tutorial_start(self):
        print("Starting tutorial to decompose input meshes.")

    def on_tutorial_end(self):
        print("'Decompose input meshes' tutorial complete!")

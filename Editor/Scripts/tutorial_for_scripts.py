"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""
import os
import azlmbr.bus as bus # type: ignore
import azlmbr.editor as editor   # type: ignore
import azlmbr.entity  # type: ignore
from azlmbr.entity import EntityId  # type: ignore
import azlmbr.paths as paths
from tutorial import Tutorial, TutorialStep  # type: ignore

class TutorialForScripts(Tutorial):
    FILE_PATH = os.path.join(paths.projectroot, "TestAssets", "test_file.scriptevents")

    def __init__(self):
        super(TutorialForScripts, self).__init__()

        self.title = "Entity Creating and Naming"

        self.add_step(TutorialStep("Entity Creating and Naming", 
                """<html><p style="font-size:13px"> My goals for this tutorial are to use scripts
                to create an entity, to name an entity, and to delete an entity.
                Future goals: open a window (tools-> ___), 
                create a script to apply the 'result' of a tutorial to an entity </p></html>"""))
    
    def on_step_start(self):
        print("Starting the select Entity step")
        newEntity = TutorialForScripts.ToolsApplicationRequestBus(bus.Broadcast, 'CreateNewEntity', EntityId())
        editor.AssetEditorWidgetRequestsBus(bus.Broadcast, "SaveAssetAs", FILE_PATH)
        # SCRIPTS I HAVE TRIED 
        # self.generate_variable_test_output(self, "create")
        # get_action_for_menu_path
        # _get_children --> the direct descendants from a given PySide object.

    def on_tutorial_start(self):
        print("Starting Mesh Asset Process tutorial.")

    def on_tutorial_end(self):
        print("Mesh Asset Process tutorial complete!")


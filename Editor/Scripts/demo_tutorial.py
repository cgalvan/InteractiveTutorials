"""
Copyright (c) Contributors to the Open 3D Engine Project.
For complete copyright and license terms please see the LICENSE at the root of this distribution.

SPDX-License-Identifier: Apache-2.0 OR MIT
"""

from tutorial import Tutorial, TutorialStep


class DemoTutorial(Tutorial):
    def __init__(self):
        super(DemoTutorial, self).__init__()

        self.title = "Demo Tutorial"

        self.add_step(TutorialStep("First things first", "Do blah blah blah and click on foo"))
        self.add_step(TutorialStep("Hello World", "Time to do foo bar baz"))
        self.add_step(TutorialStep("Last things last", "Woo you did it!"))

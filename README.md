# Interactive Tutorials
This project provides interactive tutorials for O3DE (Open 3D Engine https://github.com/o3de/o3de). We provide both a tool for running existing tutorials, and a framework for building your very own tutorials as well!

# Download and Install
The Interactive Tutorials tool is provided through a gem that extends the Editor.

## Clone the repository
`git clone https://github.com/cgalvan/InteractiveTutorials.git`

## Register the gem
Once you've cloned the repo, you first need to register your gem with your current project.
`scripts\o3de register -gp <path-to-cloned-repo> -espp <your-project-path>`

## Enable gem for your project
`scripts\o3de enable-gem -gn InteractiveTutorials -pp <your-project-path>

You can find more information on adding/enabling gems with O3DE here: https://www.o3de.org/docs/user-guide/project-config/add-remove-gems/

# Usage
Once the gem has been added to your project and you've rebuilt, the `Interactive Tutorials` tool can be launched from the "Tools" menu in the Editor, or from the toolbar icon. From the tool, you can find all current tutorials and launch them. Upon completion, you can choose another tutorial to experience.

## Custom tutorials
If you would like to create your own tutorial, check out some of the examples in `Editor/Scripts/demo_tutorial.py`

# Example

Here's a screen recording of our PhysX Rigid Bodies Tutorial in action!

![RigidBodyTutorial](https://user-images.githubusercontent.com/7519264/167025468-b3dd1a38-34a3-4529-8a85-901e3a9e7f87.gif)

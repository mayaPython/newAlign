'''
    written by Emily Pollacchi
    file name newAlign
    Copyright (C) 2024 by Emily Pollacchi
    epollacchi@gmail.com
    Based on a script by Delano Athias
    www.delanimo.blogspot.co.uk
    Instructions: first select source object, then select target object.

'''
import maya.cmds as cmds

# Use selected objects
objects = cmds.ls(selection=True)

# Check for selection
if not objects:
    cmds.error("No objects selected.")

# Centre pivot
cmds.xform(objects, cp=True, p=True)

# Delete the history of the objects
cmds.bakePartialHistory(objects, prePostDeformers=True)

# Creates a parent contraint with no offset
prtCns = cmds.parentConstraint()

# Deletes the parent constraint
cmds.delete(prtCns)

# Clear selection
cmds.select(clear=True)


# Freeze transformations and delete the history of the objects
def freezeDelete():
    cmds.makeIdentity(objects, apply=True, t=1, r=1, s=1, n=0)
    cmds.bakePartialHistory(objects, prePostDeformers=True)


freezeDelete()
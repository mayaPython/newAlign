'''
    written by Emily Pollacchi
    file name newAlign
    Copyright (C) 2016 by Emily Pollacchi
    epollacchi@gmail.com
    Based on a script by Delano Athias
    www.delanimo.blogspot.co.uk
    Instructions: first select source object, then select target object.

'''
import maya.cmds as mc

#use selected objects
objects = mc.ls(selection = True)

#centre pivot
mc.xform(objects, cp=True, p=True)

#delete the history of the objects
mc.bakePartialHistory(objects, prePostDeformers = True)

    
# creates a parent contraint with no offset
prtCns = mc.parentConstraint()

#deletes the parent constraint
mc.delete(prtCns)

#clear selection
mc.select(clear=True)

#define a funtion to freeze transformations and delete the history of the objects
def freezeDelete():
    mc.makeIdentity(objects, apply = True, t=1, r=1, s=1, n=0)
    mc.bakePartialHistory(objects, prePostDeformers = True)
    

freezeDelete()

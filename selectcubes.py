# -*- coding: utf-8 -*-
"""
Blender vr viewport select cubes,
@author: Louis Griffiths
"""
#hasnt been tested will probably need debuging
#has multiple errors that need fixing

#imports
import bpy
from random import randint
bpy.ops.mesh.primitive_cube_add()

#Code retrieves camera position.
#campos[0] for x, campos[1] for y and campos[2] for z
campos = bpy.data.objects["Camera"].location

#distfrom cam is cubes distance from camera
distfromcam = 10

#setting x pos for cube one
cube1pos = campos[0]-distfromcam
#setting x pos for cube two
cube2pos = campos[0]+distfromcam

#setting y pos
y = campos[1] 
#setting zpos
z = campos[2]

bpy.ops.mesh.primitive_cube_add(location=(cube1pos,y,z))
bpy.ops.mesh.primitive_cube_add(location=(cube2pos,y,z))

#forever loop to check if cam is near cube                            
#loop = 1
#while loop = 1:
#Gets camera pos
campos = bpy.data.objects["Camera"].location
    x = campos[0]
    if x<cube1pos:
        #activates script if near cube 1
        print('near cube 1')
    if x>cube2pos:
        #activates script if near cube 2
        print('near cube 2')  
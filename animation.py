import bpy
import random
import mathutils

# Выбираем объект Lemon
lemon = bpy.data.objects['lemon']
lemon.rotation_euler = original_rotation_lemon = lemon.rotation_euler[:]
lemon.location = original_location_lemon = lemon.location[:]

orange = bpy.data.objects['orange']
orange.rotation_euler = original_rotation_orange = orange.rotation_euler[:]
orange.location = original_location_orange = orange.location[:]

lime = bpy.data.objects['lime']
lime.rotation_euler = original_rotation_lime = lime.rotation_euler[:]
lime.location = original_location_lime = lime.location[:]

mandarin = bpy.data.objects['mandarin']
mandarin.rotation_euler = original_rotation_mandarin = mandarin.rotation_euler[:]
mandarin.location = original_location_mandarin = mandarin.location[:]

grapefruit = bpy.data.objects['grapefruit']
grapefruit.rotation_euler = original_rotation_grapefruit = grapefruit.rotation_euler[:]
grapefruit.location = original_location_grapefruit = grapefruit.location[:]

# Устанавливаем начальную позицию и вращение для каждой копии
copies = [lemon, orange, lime, mandarin, grapefruit]



# Создаем анимацию движения и вращения объектов
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 500

for i in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end, 20):
    bpy.context.scene.frame_set(i)
    
    for j, copy in enumerate(copies):
        random_location = mathutils.Vector((random.uniform(-0.01, 0.01), random.uniform(-0.01, 0.01), random.uniform(-0.01, 0.01)))
        random_rotation = mathutils.Euler((random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)))
        
        new_location = copy.location + random_location
        
        new_rotation = mathutils.Euler((copy.rotation_euler[0] + random_rotation[0], 
                                        copy.rotation_euler[1] + random_rotation[1], 
                                        copy.rotation_euler[2] + random_rotation[2]))
        
        for other_copy in copies:
            if other_copy != copy:
                distance = (new_location - other_copy.location).length
                if distance < 0.1:
                    separation_vector = (new_location - other_copy.location).normalized() * (0.1 - distance)
                    new_location += separation_vector
        
        copy.location = new_location
        copy.rotation_euler = new_rotation
        
        copy.keyframe_insert("location", index=-1, frame=i, options={'INSERTKEY_NEEDED'})
        copy.keyframe_insert("rotation_euler", index=-1, frame=i, options={'INSERTKEY_NEEDED'})

from ursina import *

app = Ursina(borderless=True)  # Borderless window

# Create a cube in 3D space
cube = Entity(model='cube', color=color.azure, scale=2, position=(0,0,0))

# Add a simple ground plane for reference
ground = Entity(model='plane', scale=10, color=color.green, rotation_x=90, y=-1)

# Add a camera with some initial position so you can see the cube
camera.position = (0, 5, -10)
camera.rotation_x = 30

def update():
    # Move the cube with arrow keys in XZ plane
    if held_keys['left']:
        cube.x -= 5 * time.dt
    if held_keys['right']:
        cube.x += 5 * time.dt
    if held_keys['up']:
        cube.z += 5 * time.dt
    if held_keys['down']:
        cube.z -= 5 * time.dt
    
    # Rotate the cube for some visual effect
    cube.rotation_y += 100 * time.dt

app.run()

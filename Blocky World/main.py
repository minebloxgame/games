from ursina import *

app = Ursina()

# Sky with solid blue color
sky = Entity(
    parent=scene,
    model='sphere',
    scale=500,
    double_sided=True,
    color=color.rgb(135, 206, 235)  # Sky blue
)

# Grass ground with solid green color
ground = Entity(
    model='plane',
    scale=(100, 1, 100),
    color=color.lime,
    collider='box'
)

# Player (first person controller)
player = FirstPersonController()
player.gravity = 0.5
player.cursor.visible = True
player.speed = 5

# Light
DirectionalLight(y=2, z=3, shadows=True)

app.run()

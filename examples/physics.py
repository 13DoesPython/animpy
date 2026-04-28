import os
import time
from animpy.animpy import PhysicsScene, EffectText, Text, Shapes


def run_physics_scene_demo(duration_seconds: float = 10.0) -> None:
    try:
        columns, lines = os.get_terminal_size()
    except OSError:
        columns, lines = 80, 24

    scene = PhysicsScene()

    ball = EffectText("O", columns // 2, 1, r=255, g=100, b=100, z_index=1)
    ball.velocity_x = 1.0
    ball.velocity_y = 0.0

    floor_y = lines - 3
    floor = Text(Shapes.rectangle(columns, 1, "-"), 0, floor_y, r=100, g=100, b=255)
    scene.add(floor, ball)

    title = Text("Physics Scene Demo - Press Ctrl+C to exit", 2, 0, r=255, g=255, b=0)
    scene.add(title)

    start_time = time.perf_counter()

    try:
        while time.perf_counter() - start_time < duration_seconds:
            delta_time = scene.dt

            scene.apply_gravity(ball)
            scene.apply_friction(ball, friction=0.02)
            scene.bounce(ball, bounce_factor=0.7)

            if ball.x <= 0:
                ball.x = 0
                ball.velocity_x = abs(ball.velocity_x)
            elif ball.x >= columns - 1:
                ball.x = columns - 1
                ball.velocity_x = -abs(ball.velocity_x)

            if ball.y >= floor_y - 1:
                ball.y = floor_y - 1

            ball.x += ball.velocity_x * delta_time * 20

            scene.clear()
            scene.render()
            time.sleep(1 / 30)
    except KeyboardInterrupt:
        pass
    finally:
        print("\nDemo ended.")


if __name__ == "__main__":
    run_physics_scene_demo()

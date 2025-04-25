from manim import *

class DotTrajectoryWithSound(Scene):
    def construct(self):
                # Configure dot
        self.camera.background_color = BLUE_C
        sun = ImageMobject("images/smile-sun-cartoon-character-png.png")

        sun.set_width(2)
        self.add(sun)

        # 2) Position markers (invisible)
        positions = {
            "center": ORIGIN,
            "up-left": UP * 2.2 + LEFT * 3.5,
            "down-left": DOWN * 2.5 + LEFT * 3.5,
            "down": DOWN * 3,
            "left": LEFT * 3,
            "right": RIGHT * 3,
        }
        markers = {}
        for name, pos in positions.items():
            m = Dot(color=BLACK, radius=0.4).move_to(pos)
            m.set_opacity(0)
            self.add(m)
            markers[name] = m

        # 3) Grow + jump sound
        self.add_sound("sounds/cartoon-jump-6462.mp3", gain=4)
        self.play(GrowFromCenter(sun), run_time=1)

        # 4) Background sound for the movement
        self.add_sound("sounds/cartoon-189231_aJ9EIhA6-[AudioTrimmer.com]-2.mp3", time_offset=0.8)

        # 5) Movement sequence
        move_time = 3
        self.play(sun.animate.move_to(positions["down"]),  run_time=move_time, rate_func=smooth)
        self.play(sun.animate.move_to(positions["up-left"]),    run_time=move_time, rate_func=smooth)
        self.play(sun.animate.move_to(positions["center"]),run_time=move_time, rate_func=smooth)

        # 6) Fade out everything
        self.play(FadeOut(sun), *[FadeOut(m) for m in markers.values()])
        self.wait(1)
        
        self.camera.background_color = WHITE
        # Pop-up animations at different positions
        positions = [
            UP + RIGHT * 3,
            UP + LEFT * 3,
            DOWN * 2 + LEFT * 2,
            DOWN * 2 + RIGHT * 2,
            RIGHT * 3,
            LEFT * 3
        ]
        fruit_files = [
                    "images/cute-and-smile-cartoon-fruit-colorful-character-banana-free-png.png",
                    "images/cute-and-smile-cartoon-fruit-colorful-character-dragon-fruit-free-png.png",
                    "images/cute-and-smile-cartoon-fruit-colorful-character-red-apple-free-png.png",
                    "images/cute-and-smile-cartoon-fruit-colorful-character-pear-free-png.png",
                    "images/cute-and-smile-cartoon-fruit-colorful-character-pineapple-free-png.png",
                    "images/cute-and-smile-cartoon-fruit-colorful-character-watermelon-free-png.png",
                ]
        background_colors = [
            LIGHT_PINK,  # lavanda
            YELLOW_C,  # giallo chiaro
            GREEN_C,  # verde
            RED_C,  # rosso smorzato
            PINK,  # magenta
            "#FFA500",  # arancione
        ]

        for color, pos, file_path in zip(background_colors, positions, fruit_files):
            self.camera.background_color = color
            fruit = ImageMobject(file_path).set_height(2.2)
            fruit.move_to(pos)
            self.add(fruit)
            # jump sound + grow together
            self.add_sound("sounds/cartoon-jump-6462.mp3",gain=4,time_offset=0.2)
            self.play(GrowFromCenter(fruit), run_time=3)
            self.wait(0.1)

            self.wait(0.1)
            # shrink away
            self.play(ShrinkToCenter(fruit), run_time=0.3)
            self.remove(fruit)
            self.wait(0.2)

        self.wait(1)


        # Configure dot
        self.camera.background_color = BLUE_C
        sun = ImageMobject("images/smile-sun-cartoon-character-png.png")

        sun.set_width(2)
        self.add(sun)

        # 2) Position markers (invisible)
        positions = {
            "center": ORIGIN,
            "up-left": UP * 2.2 + LEFT * 3.5,
            "down-left": DOWN * 2.5 + LEFT * 3.5,
            "down": DOWN * 3,
            "left": LEFT * 3,
            "right": RIGHT * 3,
        }
        markers = {}
        for name, pos in positions.items():
            m = Dot(color=BLACK, radius=0.4).move_to(pos)
            m.set_opacity(0)
            self.add(m)
            markers[name] = m

        # 3) Grow + jump sound
        self.add_sound("sounds/cartoon-jump-6462.mp3", gain=4)
        self.play(GrowFromCenter(sun), run_time=1)

        # 4) Background sound for the movement
        self.add_sound("sounds/cartoon-189231_aJ9EIhA6-[AudioTrimmer.com]-2.mp3", time_offset=0.8)

        # 5) Movement sequence
        move_time = 3
        self.play(sun.animate.move_to(positions["down"]),  run_time=move_time, rate_func=smooth)
        self.play(sun.animate.move_to(positions["right"]), run_time=move_time, rate_func=smooth)
        self.play(sun.animate.move_to(positions["center"]),run_time=move_time, rate_func=smooth)

        # 6) Fade out everything
        self.play(FadeOut(sun), *[FadeOut(m) for m in markers.values()])
        self.wait(1)
        credits = Text("Vecteezy.com",font_size=72,weight="BOLD",font="sans-serif", color=WHITE,slant="NORMAL").to_edge(ORIGIN)
        self.play(FadeIn(credits))
        self.wait(1)
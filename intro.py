from manim import *

COURSE_NAME = "Mathematics for Actuarial Studies and Finance 1A"
COURSE_CODE = "MATH1151"
YEAR = "2025"
AUTHOR = "Thomas Petkovic"

custom_color = "#9fa2e5"
custom_light = "#bdc0eb"
custom_dark = "#272a6d"
custom_pink = "#ffc3c3"

class FadeScreenFromBlackToWhite(Scene):
    def construct(self):

        title = Text(COURSE_NAME, font_size=35, color = custom_color)
        self.play(Write(title), run_time = 2.5)

        self.wait(1)

        course_code = Text(COURSE_CODE, font_size = 35, color = custom_color)

        self.play(
            Transform(title, course_code, run_time = 1)
        )

        self.wait(0.5)

        author = Text(AUTHOR + ' ' + YEAR, font_size=30, color=custom_color)
        author.to_corner(DOWN + RIGHT) 
        self.play(
            Transform(title, author, run_time=1)
        )
        self.wait(0.4)
        self.play(FadeOut(title))

        self.wait(2)
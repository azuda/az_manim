from manim import *
from random import *

class Shuffle(Scene):
  def construct(self):
    n = 6

    circles = [
      Circle(color=WHITE, fill_opacity=1).scale(0.5)
      for _ in range(n)
    ]

    spacing = 2
    for i, circle in enumerate(circles):
      circle.shift(RIGHT * (i - (len(circles) - 1) / 2) * spacing)
    self.play(Write(circle) for circle in circles)

    select = randint(0, n-1)
    for _ in range(2):
      self.play(circles[select].animate.set_color(RED), run_time=0.5)
      self.play(circles[select].animate.set_color(WHITE), run_time=0.5)

    swaps = 16
    for i in range(swaps):
      a, b = 0, 0
      while a == b:
        a, b = randint(0, n-1), randint(0, n-1)
      self.play(Swap(circles[a], circles[b]), run_time=0.5, path_arc=120*DEGREES)

    for _ in range(2):
      self.play(circles[select].animate.set_color(RED), run_time=0.5)
      self.play(circles[select].animate.set_color(WHITE), run_time=0.5)

    self.wait(1)



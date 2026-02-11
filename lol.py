from manim import *
import random



class Search(Scene):
  def construct(self):
    square = Square(color="#ff55ff", fill_opacity=0.5).shift(LEFT * 2)
    circle = Circle(color="#55ffff", fill_opacity=0.5).shift(RIGHT * 2)

    self.play(
      Write(square),
      Write(circle),
      run_time=1
    )

    for _ in range(2):
      self.play(
        square.animate.become(circle),
        circle.animate.become(square),
        run_time=0.5
      )

    self.play(
      Swap(square, circle),
      path_arc=30*DEGREES,
      run_time=1
    )
    
    self.play(
      square.animate.shift(RIGHT * 1),
      circle.animate.shift(LEFT * 1),
      run_time=0.25
    )

    self.play(
      Rotate(square, angle=12*PI, rate_func=exponential_decay),
      run_time=3
    )

    self.play(
      circle.animate.become(Triangle(color="#55ff55", fill_opacity=0.5).shift(LEFT * 2)),
      run_time=1
    )


    self.wait(1)



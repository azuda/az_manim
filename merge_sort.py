from manim import *

class Sort(Scene):
  def create_textbox(self, string):
    result = VGroup()
    textbox = Square(
      fill_opacity=0,
      stroke_color="#ffffff"
    )
    text = Text(string, color="#ffffff").move_to(textbox.get_center())
    result.add(textbox, text)
    return result

  def construct(self):
    # scene setup
    boxes = VGroup()
    for i, node in enumerate(unsorted):
      box = self.create_textbox(str(node))
      box.shift(RIGHT * i * 0.8)
      box.scale(0.4)
      boxes.add(box)
    boxes.move_to(ORIGIN)
    self.add(boxes)
    self.play(Write(boxes), run_time=1)

    # sort algo + anim
    print("ooo")

    # done
    self.wait(1)



unsorted = [111, 23, 1, 15, 9, 3, 27, 19, 5, 11, 7, 21, 13, 29, 17, 25, 99]

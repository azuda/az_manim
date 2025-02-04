from manim import *



class Search(MovingCameraScene):
  def construct(self):
    spacing = 2
    textboxes = VGroup()

    for i, node in enumerate(input_list):
      textbox = self.create_textbox(str(node))
      textbox.shift(RIGHT * i * spacing)
      textboxes.add(textbox)
      self.add(textbox)

    pointer = Triangle(color="#ff0000", fill_opacity=1).scale(0.2)
    pointer.rotate(PI)
    pointer.next_to(textboxes[0], UP)
    self.add(pointer)

    for i, textbox in enumerate(textboxes):
      self.play(
        self.camera.frame.animate.move_to(textbox),
        pointer.animate.next_to(textbox, UP),
        run_time=0.3
      )
      if input_list[i] == target:
        textbox.set_fill("#66ff66", opacity=0.5)  # highlight target node
        break

    self.wait(1)



  def create_textbox(self, string):
      result = VGroup()
      box = Square(
          fill_opacity=0,
          stroke_color="#ffffff"
      )
      text = Text(string, color="#ffffff").move_to(box.get_center())
      result.add(box, text) # add text and box to vgroup
      return result



input_list = [23, 1, 15, 9, 3, 27, 19, 5, 11, 7, 21, 13, 29, 17, 25]
target = 17

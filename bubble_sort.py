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

    # create cursors at start of input list
    left = Square(color=BLUE, fill_opacity=0.5).scale(0.4)
    right = Square(color=PINK, fill_opacity=0.5).scale(0.4)
    left.move_to(boxes[0])
    right.move_to(boxes[1])
    self.play(Write(left), Write(right), run_time=1)

    # algo
    def bubble_sort(input_list, n=None, initial_anim_speed=0.5):
      if n is None:
        n = len(input_list)

      # base case
      if n <= 1:
        return input_list

      # recursive case
      for j in range(n-1):
        # scale animation speed
        anim_speed = initial_anim_speed * (n / len(input_list))

        # animate cursor movement
        self.play(
          left.animate.move_to(boxes[j]),
          right.animate.move_to(boxes[j+1]),
          run_time=anim_speed
        )

        if input_list[j] > input_list[j+1]:
          input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

          # animate swapping list elements
          self.play(
            Swap(boxes[j], boxes[j+1], run_time=anim_speed, path_arc=120*DEGREES),
            Swap(left, right, run_time=anim_speed, path_arc=120*DEGREES)
          )
          boxes[j], boxes[j+1] = boxes[j+1], boxes[j]

      return bubble_sort(input_list, n-1, initial_anim_speed*0.9)

    # call sort algo
    bubble_sort(unsorted)

    # remove cursors from scene
    self.play(FadeOut(left), FadeOut(right))
    self.remove(left, right)

    # done
    self.wait(1)

# my change

unsorted = [111, 23, 1, 15, 9, 3, 27, 19, 5, 11, 7, 21, 13, 29, 17, 25, 99]

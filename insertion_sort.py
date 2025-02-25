from manim import *
import random


class Sort(Scene):
  def construct(self):
    # draw list
    boxes_i = VGroup()
    boxes = VGroup()
    for i, val in enumerate(unsorted):
      # set up indices
      index = Square(
        fill_opacity=0,
        stroke_opacity=0
      )
      index.shift(RIGHT * i * 0.8)
      index.scale(0.4)
      boxes_i.add(index)
      # set up textboxes
      textbox = VGroup()
      square = Square(
        fill_opacity=0,
        stroke_color="#ffffff"
      )
      text = Text(str(val), color="#ffffff").move_to(textbox.get_center())
      textbox.add(square, text)
      textbox.shift(RIGHT * i * 0.8)
      textbox.scale(0.4)
      boxes.add(textbox)
    boxes_i.move_to(ORIGIN)
    boxes.move_to(ORIGIN)
    self.add(boxes_i, boxes)
    self.play(Write(boxes_i), Write(boxes), run_time=1)

    # draw cursors
    cursor = Triangle(color="#55ffff", fill_opacity=0.5).scale(0.2)
    cursor.next_to(boxes_i[1], DOWN)
    ins = Triangle(color="#ff5555", fill_opacity=0.5).scale(0.2)
    ins.rotate(180*DEGREES)
    ins.next_to(boxes_i[1], UP)
    self.play(Write(cursor), Write(ins), run_time=1)

    # sort algo
    def insertion_sort(arr):
      n = len(arr)
      if n <= 1:
        return arr

      speed = 0.5
      for i in range(1, n):
        cur = arr[i]
        x = Text(str(arr[i]), color="#ffffff").scale(0.4)
        self.play(
          cursor.animate.next_to(boxes_i[i], DOWN),
          ins.animate.next_to(boxes_i[i], UP),
          run_time=0.5
        )

        j = i - 1
        while j >= 0 and arr[j] > cur:
          arr[j+1] = arr[j]
          y = Text(str(arr[j]), color="#ffffff").scale(0.4)
          y.move_to(boxes[j+1].get_center())
          self.play(
            ins.animate.next_to(boxes_i[j+1], UP),
            Write(boxes[j+1][1].become(y)),
            run_time=0.25
          )
          j -= 1
        arr[j+1] = cur
        self.play(
          ins.animate.next_to(boxes_i[j+1], UP),
          run_time=0.25
        )
        x.move_to(boxes[j+1].get_center())
        self.play(Write(boxes[j+1][1].become(x), run_time=0.25))

      return arr

    # call sort algo
    insertion_sort(unsorted)

    self.wait(1)



unsorted = [random.randint(1, 99) for _ in range(random.randint(10, 18))]

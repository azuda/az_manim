from manim import *


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

    # draw cursor
    cursor = Triangle(color="#55ffff", fill_opacity=0.5).scale(0.2)
    cursor.next_to(boxes[1], DOWN)
    self.play(Write(cursor), run_time=1)

    # sort algo
    def insertion_sort(arr):
      n = len(arr)
      if n <= 1:
        return arr

      for i in range(1, n):
        cur = arr[i]
        self.play(cursor.animate.next_to(boxes[i], DOWN))

        j = i - 1
        while j >= 0 and arr[j] > cur:
          arr[j+1] = arr[j]
          self.play(Write(
            boxes[j+1][1].become(boxes[j][1]),
            run_time=0.25
          ))
          j -= 1
        arr[j+1] = cur
        self.play(Write(
          boxes[j+1][1].become(boxes[i][1]),
          run_time=0.25
        ))

      return arr

    # call sort algo
    insertion_sort(unsorted)

    self.wait(1)



unsorted = [111, 23, 1, 15, 9, 3, 27, 19, 5, 11, 7, 21, 13, 29, 17, 25, 99]

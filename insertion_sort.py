from manim import *


class Sort(Scene):
  def construct(self):
    # draw list
    boxes = VGroup()
    for i, val in enumerate(unsorted):
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
    boxes.move_to(ORIGIN)
    self.add(boxes)
    self.play(Write(boxes), run_time=1)

    # draw cursor
    cursor = Square(color="#55ffff", fill_opacity=0.5).scale(0.4)
    cursor.move_to(boxes[1])
    self.play(Write(cursor), run_time=1)

    # sort algo
    def insertion_sort(arr):
      n = len(arr)
      if n <= 1:
        return arr

      for i in range(1, n):
        cur = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cur:
          arr[j+1] = arr[j]
          j -= 1
        arr[j+1] = cur

      return arr

    # call sort algo
    insertion_sort(unsorted)

    self.wait(1)



unsorted = [111, 23, 1, 15, 9, 3, 27, 19, 5, 11, 7, 21, 13, 29, 17, 25, 99]

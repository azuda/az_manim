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
    def merge_sort(arr):
      if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # left_boxes = boxes[:mid]
        # right_boxes = boxes[mid:]
        # self.play(
        #   left_boxes.animate.shift(LEFT * 0.1),
        #   right_boxes.animate.shift(RIGHT * 0.1),
        #   run_time=0.5
        # )

        merge_sort(left)
        merge_sort(right)

        x = y = z = 0
        while x < len(left) and y < len(right):
          if left[x] < right[y]: # left is lower
            arr[z] = left[x]
            x += 1
          else: # right is lower
            arr[z] = right[y]
            y += 1
          z += 1

        # cleanup left remainder
        while x < len(left):
          arr[z] = left[x]
          x += 1
          z += 1

        # cleanup right remainder
        while y < len(right):
          arr[z] = right[y]
          y += 1
          z += 1

      return arr

    # call merge sort algo
    merge_sort(unsorted)

    # done
    self.wait(1)



unsorted = [111, 23, 1, 15, 9, 3, 27, 19, 5, 11, 7, 21, 13, 29, 17, 25, 99]

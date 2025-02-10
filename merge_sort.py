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
    self.play(Write(boxes), run_time=1)
    sorted_boxes = VGroup()
    sorted_boxes.add(Square(color=GREEN, fill_opacity=0.2).scale(0.4))
    sorted_boxes.next_to(boxes, DOWN * 4)
    self.add(sorted_boxes)

    # sort algo + anim
    def merge_sort(arr, i_boxes=boxes):
      if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left_boxes = i_boxes[:mid]
        right_boxes = i_boxes[mid:]
        self.play(
          left_boxes.animate.shift(LEFT * 0.1),
          right_boxes.animate.shift(RIGHT * 0.1),
          run_time=0.5
        )

        merge_sort(left, left_boxes)
        merge_sort(right, right_boxes)

        x = y = z = 0
        self.add(sorted_boxes)
        while x < len(left) and y < len(right):
          if left[x] < right[y]: # left is lower
            arr[z] = left[x]
            sorted_boxes.add(left_boxes[x])
            x += 1
          else: # right is lower
            arr[z] = right[y]
            sorted_boxes.add(right_boxes[y])
            y += 1
          z += 1 # increment to next spot in sorted list

        # cleanup left remainder
        while x < len(left):
          arr[z] = left[x]
          sorted_boxes.add(left_boxes[x])
          x += 1
          z += 1

        # cleanup right remainder
        while y < len(right):
          arr[z] = right[y]
          sorted_boxes.add(right_boxes[y])
          y += 1
          z += 1

      return arr

    # call merge sort algo
    merge_sort(unsorted)

    for a, split_box in enumerate(sorted_boxes):
      split_box.move_to(sorted_boxes.get_center())
      split_box.shift(RIGHT * a * 2)
    sorted_boxes.move_to(ORIGIN)

    # done
    self.wait(1)



unsorted = [111, 23, 1, 15, 9, 3, 27, 19, 5, 11, 7, 21, 13, 29, 17, 25, 99]

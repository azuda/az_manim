from manim import *
import random


class Sort(Scene):
  def construct(self):
    boxes_i = VGroup()
    boxes = VGroup()
    nums = VGroup()
    for i, val in enumerate(unsorted):
      # index boxes
      box_i = Square(
        fill_opacity=0,
        stroke_opacity=0
      )
      box_i.shift(RIGHT * i * 0.8)
      box_i.scale(0.4)
      boxes_i.add(box_i)
      # actual boxes
      box = Square(
        fill_opacity=0,
        stroke_color="#ffffff"
      )
      box.shift(RIGHT * i * 0.8)
      box.scale(0.4)
      boxes.add(box)
      # text
      text = Text(str(val), color="#ffffff")
      text.move_to(box.get_center())
      text.scale(0.4)
      nums.add(text)
    boxes_i.move_to(ORIGIN)
    boxes.move_to(ORIGIN)
    nums.move_to(ORIGIN)
    self.add(boxes_i, boxes, nums)
    self.play(Write(boxes_i), Write(boxes), Write(nums), run_time=1)

    cursor = Square(color="#ff5555", fill_opacity=0.5).scale(0.4)
    cursor.move_to(boxes[-1].get_center())
    self.play(Write(cursor), run_time=1)

    def partition(arr, lo, hi):
      pivot = arr[hi]
      i = lo - 1
      for j in range(lo, hi):
        if arr[j] < pivot:
          i += 1
          swap(arr, i, j)
      swap(arr, i+1, hi)
      self.play(
        cursor.animate.move_to(boxes[i+1].get_center()),
        run_time=0.5
      )
      return i+1

    def swap(arr, i, j):
      arr[i], arr[j] = arr[j], arr[i]
      self.play(
        Swap(boxes[i], boxes[j], run_time=0.5, path_arc=120*DEGREES),
        Swap(nums[i], nums[j], run_time=0.5, path_arc=120*DEGREES)
      )

    def quicksort(arr, lo=0, hi=None):
      n = len(arr)
      if hi is None:
        hi = n - 1
      
      if lo < hi:
        pi = partition(arr, lo, hi)
        # self.play(cursor.animate.move_to(boxes[pi].get_center()), run_time=0.5)
        quicksort(arr, lo, pi-1)
        quicksort(arr, pi+1, hi)

      return arr

    quicksort(unsorted)

    # check logic by displaying sorted arr
    res = VGroup()
    for ele in quicksort(unsorted):
      text = Text(str(ele), color="#ffffff")
      res.add(text)
    res.scale(0.4)
    res.arrange(RIGHT)
    res.next_to(boxes, DOWN)
    self.play(Write(res), run_time=2)

    self.wait(1)



unsorted = [random.randint(1, 99) for _ in range(random.randint(10, 18))]

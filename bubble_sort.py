from manim import *

class Sort(Scene):
  def construct(self):
    # scene setup

    # algo
    def bubble_sort(input_list, n=None):
      if n is None:
        n = len(input_list)

      # base case
      if n <= 1:
        return input_list

      # recursive case
      for i in range(n-1):
        if input_list[i] > input_list[i+1]:
          input_list[i], input_list[i+1] = input_list[i+1], input_list[i]

      return bubble_sort(input_list, n-1)


    bubble_sort(unsorted)
    self.wait(1)






unsorted = [111, 23, 1, 15, 9, 3, 27, 19, 5, 11, 7, 21, 13, 29, 17, 25]

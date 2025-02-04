from manim import *

class Sort(Scene):
  def construct(self):

    # scene

    self.wait(1)



def slow_sort(input_list):
  for i in range(len(input_list)-1):
    cur = input_list[i]
    nex = input_list[i+1]
    if cur > nex:
      input_list[i], input_list[i+1] = nex, cur
  
  return input_list

from manim import *



class Search(Scene):
  def construct(self):
    textboxes = VGroup()
    for i, node in enumerate(input_list):
      textbox = self.create_textbox(str(node))
      textbox.shift(RIGHT * i * 0.8)
      textbox.scale(0.4)
      textboxes.add(textbox)
    textboxes.move_to(ORIGIN)
    self.add(textboxes)
    self.play(FadeIn(textboxes), run_time=0.5)

    left = Triangle(color=BLUE, fill_opacity=1).scale(0.2)
    right = Triangle(color=BLUE, fill_opacity=1).scale(0.2)
    current = Triangle(color=RED, fill_opacity=1).scale(0.2)

    def binary_search(inputs, target, low=0, high=None):
      if high is None:
        high = len(inputs) - 1
      if low > high: # target doesnt exist
        return -1
      mid = (high+low) // 2
      self.play(
        left.animate.next_to(textboxes[low], DOWN),
        right.animate.next_to(textboxes[high], DOWN),
        run_time=1
      )
      self.play(current.animate.next_to(textboxes[mid], DOWN), run_time=1)
      self.add(left, right, current)

      if inputs[mid] == target: # target found
        t = textboxes[mid]
        t.set_fill("#66ff66", opacity=0.5)
        self.play(FadeOut(left), FadeOut(right), FadeOut(current), run_time=1)
        self.remove(left, right, current)
        ans = Triangle(color=GREEN, fill_opacity=1).scale(0.2)
        ans.next_to(textboxes[mid], DOWN)
        self.add(ans)
        self.blink(ans)
        return mid
      elif inputs[mid] > target: # search bottom half
        return binary_search(inputs, target, low, mid - 1)
      else: # search top half
        return binary_search(inputs, target, mid + 1, high)

    binary_search(input_list, target)
    self.wait(1)

  def create_textbox(self, string):
    result = VGroup()
    box = Square(
      fill_opacity=0,
      stroke_color="#ffffff"
    )
    text = Text(string, color="#ffffff").move_to(box.get_center())
    result.add(box, text)
    return result

  def blink(self, mob, times=3, speed=0.2):
    for _ in range(times):
      self.play(mob.animate.set_opacity(0), run_time=speed)
      self.play(mob.animate.set_opacity(1), run_time=speed)



inp = [23, 1, 15, 9, 3, 27, 19, 5, 11, 7, 21, 13, 29, 17, 25, 99]
input_list = sorted(inp)
target = 5

# binary_search(input_list, target)


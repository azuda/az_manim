from manim import *


class Search(Scene):
  def construct(self):
    # draw each node of graph as a labelled circle
    # draw a line between each node
    tree = VGroup()

    for i, val in enumerate(graph):
      node = VGroup()
      circle = Circle(
        radius=0.4,
        fill_opacity=0,
        stroke_color=BLUE
      )
      text = Text(val, color="#ffffff").move_to(circle.get_center())
      node.add(circle, text)
      node.shift(RIGHT * i * 1)
      tree.add(node)

    tree.move_to(ORIGIN)
    self.add(tree)
    self.play(Write(tree), run_time=1)

    # arrange nodes in a tree graph structure
    # for 
    lines = VGroup()
    for i, val in enumerate(graph):
      for child in graph[val]:
        line = Line(
          start=tree[i][0].get_center(),
          end=tree[ord(child) - 65][0].get_center(),
          color="#ffffff"
        )
        lines.add(line)
    
    self.play(Write(lines), run_time=1)





    self.wait(1)




graph = {
  "A": ["B", "C"],
  "B": ["A", "D", "E"],
  "C": ["A", "F"],
  "D": ["B"],
  "E": ["B", "F"],
  "F": ["C", "E"]
}

def dfs(graph, start, target):
  visited = []
  stack = [start]

  while stack:
    node = stack.pop()
    if node not in visited:
      visited.append(node)
      if node == target:
        return visited
      stack.extend(graph[node])
  return visited

print(dfs(graph, "A", "F"))

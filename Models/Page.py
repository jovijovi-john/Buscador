class Page:

  def __init__(self, title, id_param, content):
    self.score = 0
    self.title = title
    self.id = id_param
    self.content = content

  def addScore(self, score):
    self.score += score

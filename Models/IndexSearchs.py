from Models.Search import Search

class IndexSearchs:

  def __init__(self):
    self.history = {}

  def addNewSearch(self, search: Search):
    try:
      self.history[search.key] = search.results
    except:
      print("Erro ao adicionar busca ao histórico")
      pass
  
  def getSearch(self, search: Search):
    try:
      search = self.history[search.key]
      return search
    except:
      print("A key de busca nao existe no histórico")
      return None
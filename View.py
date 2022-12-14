from Controllers.SearchController import SearchController
import os

class View:
  
    def __init__(self, searchControll: SearchController, pagesDict):
      self.searchController = searchControll
      self.pages = pagesDict
      self.loop()
    
    def loop(self):
      r = "s"

      while r != "nao":
        os.system("clear || cls")
        query = str(input("Digite o que quer buscar: ")).strip()

        results = self.searchController.searchWords(query)

        for i in range(5):
          titlePage = self.pages[results[i]["id_page"]].title
          print(f"[{results[i]['id_page']}] - {titlePage}    \033[1;32m{results[i]['score']}\033[m")

        r = input("Deseja continuar? [ S / N ]: ")
        r = r.lower()
      
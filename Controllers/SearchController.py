from Models.IndexSearchs import IndexSearchs
from Models.Page import Page
from Models.Search import Search

class SearchController:

  def __init__(self, pages):
    self.indexSearchs = IndexSearchs()
    self.pages = pages

  def searchWords(self, words: str):
    
    try: 
      result = self.indexSearchs.history[words]
      return result

    except KeyError:
      wordsSplited = words.split() # separa todos os termos
      limit = 8
      results = []

      for page in self.pages: # percorrendo as paginas
        page.score = 0
        score = 0
        
        try: # Atribuindo uma pontuação maior caso o texto procurado esteja exatamente no titulo da pagina
         
          page.title.lower().index(words)
          sizeTitle = len(page.title.split())
          sizeWordsUser = len(words.split())
          score += (200 + int(sizeWordsUser / sizeTitle) * 10000)
         
        except ValueError:
          pass

        try: # Atribuindo uma pontuação maior caso o texto procurado esteja exatamente no texto da pagina
          page.content.lower().index(words)

          sizeContent = len(page.content.split())
          sizeWordsUser = len(words.split())
          score += (120 + int(sizeWordsUser / sizeContent) * 5000)

        except ValueError:
          pass
        
        for word in wordsSplited:

          if len(word) > 3:
            
            word = self.cutWord(word, limit)

            # Verificando no titulo

            title = page.title.split()
            countTitle = self.countWord(word, title, limit) + 1
            score = score + (countTitle * 50)

            # Verificando no text da page
            content = page.content.split()
            countContent = self.countWord(word, content, limit) + 1

            score = score + (countContent * 10)

            if countTitle > 1:
              score * 10
              
            page.score = score

        resultPage = {"id_page" : page.id, "score": page.score}
        results.append(resultPage)

      results.sort(key=lambda x: x["score"], reverse=True)
      search = Search(words, results)
      self.indexSearchs.addNewSearch(search)
      
      return results
 
  def cutWord(self, word, limit):
    if len(word) > limit:
      return word[:limit]
    return word

  def countWord(self, word, content, limit):
    count = 0
    for wordContent in content:
      
      try:
        # se a palavra é exatamente igual a do usuario
        if self.cutWord(wordContent.lower(), limit) == word:
          count += 2
        # Se a palavra do usuario estiver dentro da palavra do text
        elif wordContent.index(word) != None:
          count += 1
      except:
        pass
    return count
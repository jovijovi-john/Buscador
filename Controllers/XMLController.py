import xml.etree.ElementTree as ET
from Models.Page import Page
from Controllers.SearchController import SearchController
from View import View

from time import sleep
import os

class XMLController:

  def __init__(self):

    tree = ET.parse("data.xml") 
    root = tree.getroot()
    pagesDict = {}

    for page in root.findall('page'):
    
      title = page.find("title").text.lower()
      text = page.find("text").text.lower()
      id_page = int(page.find("id").text.lower())

      pageObj = Page(id_param=id_page, title=title, content=text)
      pagesDict[pageObj.id] = pageObj
  
    searchControl = SearchController(list(pagesDict.values()))
    view = View(searchControl, pagesDict=pagesDict)


 
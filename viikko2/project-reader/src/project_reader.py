from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print("Alkuperäisen tiedoston sisältö: ")
        print(content)
        print("dererialisoitu data:")
        print(data)
        
        project = Project(
             name=data["name"], 
             description=data["description"],
             members=data["members"],
             tasks=data["tasks"]
       )

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return project	

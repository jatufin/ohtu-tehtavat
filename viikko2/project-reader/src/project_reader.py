from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)

        tomli_dict = tomli.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        name = tomli_dict['tool']['poetry']['name']
        description = tomli_dict['tool']['poetry']['description']
        dependencies = tomli_dict['tool']['poetry']['dependencies'].keys()
        dev_dependencies = tomli_dict['tool']['poetry']['dev-dependencies'].keys()
        
        # return Project("Test name", "Test description", [], [])
        return Project(name,
                       description,
                       dependencies,
                       dev_dependencies)

#!/usr/bin/env python

import os
import sys
import ConfigParser

class utils():
	def __init__(self):
		pass

class loadConfProject():
    def __init__(self, pathFile):
        self.pathFile = pathFile
        self.Config = ConfigParser.ConfigParser()
        self.Config.read(self.pathFile)

    def getSections(self):
        return self.Config.sections()

    def getPathProject(self, project):
        return self.Config.get(project, 'path')

    def getLogProject(self, project):
        return self.Config.get(project, 'log')


def main():
    a = loadConfProject('wpchange.conf')
    print a.getSections()
    for i in a.getSections():
        print a.getPathProject(i)
        print a.getLogProject(i)

if __name__ == "__main__":
	main()

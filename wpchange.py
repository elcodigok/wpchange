#!/usr/bin/env python

import os
import sys
import ConfigParser

class wordpressStructure(self):
    def __init__(self):
        self.wpcontent = "wp-content"
        self.wpuploads = "wp-content" + "/" + "uploads"
        self.wpadmin = "wp-admin"
        self.wpincludes = "wp-includes"
        self.wpversion = self.wpincludes + "/" + "version.php"

    def getFileVersion(self):
        return self.wpversion


class workDirectory():
    def __init__(self, path):
        self.path = path

    def exists(self):
        return os.path.exists(self.path)


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
        print workDirectory(a.getPathProject(i)).exists()
        print a.getLogProject(i)

if __name__ == "__main__":
	main()

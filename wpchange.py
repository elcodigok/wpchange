#!/usr/bin/env python

import os
import re
import sys
import ConfigParser
import urllib2
import zipfile

class extractValue():
    def __init__(self, path_file):
        self.path_file = path_file

    def getVersionWordPress(self):
        f = open(self.path_file, 'r')
        content = f.readlines()
        f.close()
        find = "wp_version = '(\d\.\d\.?\d?)'"
        for i in content:
            result = re.search(find, i)
            if result != None:
                return result.group(1)


class wordpressStructure():
    def __init__(self, path_project):
        self.path_project = path_project
        self.wpcontent = self.path_project + "/" + "wp-content"
        self.wpuploads = self.path_project + "/" + "wp-content" + "/" + "uploads"
        self.wpadmin = self.path_project + "/" + "wp-admin"
        self.wpincludes = self.path_project + "/" + "wp-includes"
        self.wpversion = self.wpincludes + "/" + "version.php"
        self.robots = self.path_project + "/" + "robots.txt"
        self.readme = self.path_project + "/" + "readme.html"

    def getFileVersion(self):
        return self.wpversion

    def getFileRobots(self):
        return workDirectory(self.robots).fileExists()

    def getFileReadme(self):
        return workDirectory(self.readme).fileExists()


class workDirectory():
    def __init__(self, path):
        self.path = path

    def exists(self):
        return os.path.exists(self.path)

    def fileExists(self):
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

    def getCheckProject(self, project):
        return self.Config.get(project, 'check')


def main():
    a = loadConfProject('wpchange.conf')
    print a.getSections()
    for i in a.getSections():
        print a.getPathProject(i)
        if workDirectory(a.getPathProject(i)).exists():
            print "WordPress version " + extractValue(
                wordpressStructure(a.getPathProject(i)).getFileVersion()
                ).getVersionWordPress()
        print a.getLogProject(i)

        if wordpressStructure(a.getPathProject(i)).getFileRobots():
            print "The project has the robots.txt file."
        else:
            print "The project does not have the robots.txt file."

        if wordpressStructure(a.getPathProject(i)).getFileReadme():
            print "The project has the readme.html file."
        else:
            print "The project does not have the readme.html file."

        if a.getCheckProject(i) == 'True':
            print "Run Integrity check."
        elif a.getCheckProject(i) == 'False':
            print "No run integrity check."
        else:
            print "Option not valid."



if __name__ == "__main__":
	main()

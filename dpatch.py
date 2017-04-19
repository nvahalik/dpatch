#!/usr/local/bin/python

import json
import re
import urllib2
import subprocess

class Issue:
    def __init__(self, number):
        self.number = number
        self.data = {}
	
    def loadResource(self):
        if (len(self.data) != 0):
            return self.data	
        response = urllib2.urlopen('https://www.drupal.org/api-d7/node/' + self.number + '.json')
        data = response.read()
        self.data = json.loads(data)
        return self.data

    def getNextComment(self):
        data = self.loadResource()
        return len(data['comments']) + 1
    
    def getPatchName(self):
        return str(self.number) + '-' + str(self.getNextComment()) + '-' + self.getPatchMachineTitle() + '.patch';
    
    def getPatchMachineTitle(self):
        data = self.loadResource()
        title = data['title'].lower();
        # Remove special chars.
        title = re.sub(r'[^ a-z]', '-', title)
        # Grab the first 5 words.
        return '_'.join(title.split(' ')[:5])
        
    def getVersion(self):
        data = self.loadResource()
        if (data['field_issue_version'][-4:] == "-dev"):
            return data['field_issue_version'][:-4]
        return data['field_issue_version']

def getGitTicket():
    output = ''
    branch_output = subprocess.Popen(['git', 'branch'], stdout=subprocess.PIPE)
    while True:
        line = branch_output.stdout.readline()
        if line[0] == '*':
            value = re.findall('\* (\d+)', line)
            return value[0]
            break

if __name__ == '__main__':
    import sys
    if (len(sys.argv) == 1):
          ticket = getGitTicket()
    # print ticket
    project = Issue(ticket)
    parent_branch = project.getVersion()
    patch_filename = project.getPatchName()
    interdiff_filename = str(ticket) + '-' + str(project.getNextComment()) + '-interdiff.txt'
    subprocess.call('git diff ' + parent_branch + ' > ' + patch_filename, shell = True);
    subprocess.call('git diff > ' + interdiff_filename, shell = True);
    subprocess.call('/usr/bin/open .', shell = True);
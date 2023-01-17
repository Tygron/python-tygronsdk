import sys, os, subprocess

import random, time
from typing import List

class Processes:

    @staticmethod
    def run_subprocess( cmd:List[str], pidfile:str = None, stdin:str = '/dev/null', stdout:str = '/dev/null', stderr:str = '/dev/null', shell=False ):
        #TODO: stdin can either be /dev/null (string), or -1 (subprocess.PIPE), or sys.stdin etc (handle)
        
        stdin = stdin if not isinstance(stdin, str) else open(stdin, 'r')
        stdout = stdout if not isinstance(stdout, str) else open(stdout, 'a+')
        stderr = stderr if not isinstance(stderr, str) else open(stderr, 'a+')
        
        p = subprocess.Popen(cmd, stdout=stdout, stderr=stderr, stdin=stdin, shell=shell )
        return p
        
        #DEVNULL = open( os.devnull, 'wb' )
        #p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True )
        #p = subprocess.Popen( cmd, stdin=stdin, stdout=stdout, stderr=stderr, shell=True )
        #p = subprocess.Popen( cmd, stdin=stdin, stdout=stdout, stderr=stderr, shell=True )
        #p = subprocess.Popen(cmd, stdout=DEVNULL, stderr=DEVNULL, stdin=DEVNULL, shell=False )
        #p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=False )
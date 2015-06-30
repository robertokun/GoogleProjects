#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys, re, os, sh, commands, shutil

"""Copy Special exercise
"""

def get_special_paths(dir):
    paths = []
    filenames = os.listdir(dir)
    for filename in filenames:
        if re.search('(__)\w+(__)', filename):
            print os.path.abspath(dir) + '/' + filename
            paths.append(os.path.abspath(dir) + '/' + filename)
    return paths
# Write functions and modify main() to call them
def copy_to(paths, dir):
    for path in paths:
        cmd = shutil.copy(path, dir)
        (status, output) = commands.getstatusoutput(cmd)
        if status:
            sys.exit(1)
    return paths

def zip_to(paths, zippath):
    for path in paths:
        cmd = shutil._make_zipfile()
        (status, output) = commands.getstatusoutput(cmd)
        if status:
            sys.exit(1)
    return paths

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

      # todir and tozip are either set from command line
      # or left as the empty string.
      # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    captured_paths = get_special_paths(args[0])
    copy_to(captured_paths, todir)

  # Call your functions

if __name__ == "__main__":
    main()

# get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
# copy_to(paths, dir) given a list of paths, copies those files into the given directory
# zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile
''' TODO: if todir in cmd then invoke todir via copy_to(paths, dir):
          if tozip in cmd then invoke tozip(paths, zippath):
          '''
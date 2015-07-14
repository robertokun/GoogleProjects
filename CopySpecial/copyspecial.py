#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys, re, os, commands, shutil

"""Copy Special exercise
"""

def get_special_paths(dir_name):
    result = []
    paths = os.listdir(dir_name)
    for file_name in paths:
        match = re.search('(__)\w+(__)', file_name)
        if match:
            result.append(os.path.abspath(os.path.join(dir_name, file_name)))
        print result
    return result

def copy_to(paths, to_dir):
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    for path in paths:
        file_name = os.path.basename(path)
        shutil.copy(path, os.path.join(to_dir, file_name))

def zip_to(paths, zipfile):
    cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
    print "Command I'm going to do:" + cmd
    go_forward = raw_input('Do you want to continue? (Y/n) ')
    if go_forward == "Y":
        (status, output) = commands.getstatusoutput(cmd)
        if status:
            sys.stderr.write(output)
            sys.exit(1)

def main():
    print 'hello'
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]
        print tozip

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    paths = []
    for dir_name in args:
        paths.extend(get_special_paths(dir_name))
    if todir:
        copy_to(paths, todir)
    elif tozip:
        zip_to(paths, tozip)
    else:
        print '\n'.join(paths)

if __name__ == "__main__":
    main()

''' TODO: if todir in cmd then invoke todir via copy_to(paths, dir):
          if tozip in cmd then invoke tozip(paths, zippath):
          '''
'''

Copy Special Python Exercise

The Copy Special exercise goes with the file-system and external commands material
in the Python Utilities section. This exercise is in the "copyspecial" directory
within google-python-exercises (download google-python-exercises.zip if you have not
already, see Set Up for details). Add your code in copyspecial.py.

The copyspecial.py program takes one or more directories as its arguments. We'll say
that a "special" file is one where the name contains the pattern __w__ somewhere,
where the w is one or more word chars. The provided main() includes code to parse
the command line arguments, but the rest is up to you. Write functions to implement
the features below and modify main() to call your functions.

Suggested functions for your solution(details below):

get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
copy_to(paths, dir) given a list of paths, copies those files into the given directory
zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile
Part A (manipulating file paths)

Gather a list of the absolute paths of the special files in all the directories. In
the simplest case, just print that list (here the "." after the command is a single
argument indicating the current directory). Print one absolute path per line.

$ ./copyspecial.py .
/Users/nparlante/pycourse/day2/xyz__hello__.txt
/Users/nparlante/pycourse/day2/zz__something__.jpg
We'll assume that names are not repeated across the directories (optional: check that
assumption and error out if it's violated).

Part B (file copying)

If the "--todir dir" option is present at the start of the command line, do not print
anything and instead copy the files to the given directory, creating it if necessary.
Use the python module "shutil" for file copying.

$ ./copyspecial.py --todir /tmp/fooby .
$ ls /tmp/fooby
xyz__hello__.txt        zz__something__.jpg
Part C (calling an external program)

If the "--tozip zipfile" option is present at the start of the command line, run this
command: "zip -j zipfile <list all the files>". This will create a zipfile containing
the files. Just for fun/reassurance, also print the command line you are going to do
first (as shown in lecture). (Windows note: windows does not come with a program to
produce standard .zip archives by default, but you can get download the free and open
zip program from www.info-zip.org.)

$ ./copyspecial.py --tozip tmp.zip .
Command I'm going to do:zip -j tmp.zip /Users/nparlante/pycourse/day2/xyz__hello__.txt
/Users/nparlante/pycourse/day2/zz__something__.jpg


If the child process exits with an error code, exit with an error code and print the
command's output. Test this by trying to write a zip file to a directory that does not exist.

$ ./copyspecial.py --tozip /no/way.zip .
Command I'm going to do:zip -j /no/way.zip /Users/nparlante/pycourse/day2/xyz__hello__.txt
/Users/nparlante/pycourse/day2/zz__something__.jpg


zip I/O error: No such file or directory

zip error: Could not create output file (/no/way.zip)'''

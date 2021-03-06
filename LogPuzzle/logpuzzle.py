#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import commands, re, os, shutil, urllib
import sys

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
# re.search(), vs re.match(), vs re.findall()
# .groups (0-3) = 0 = ?, 1 = ?, 2 = ?, 3 = ?
pattern = r'(GET )(\S.*puzzle.*\.jpg)'
# filename = 'animal_code.google.com'
prefix_pattern = r'(_)(\S+\.\w+)'
# prefix = 'http://code.google.com'

def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    if not os.path.isfile(filename):
        return []
    with open(filename, 'rU') as log_file:
        prefix = 'http://' + re.search(prefix_pattern, filename).group(2)
        image_list = []
        logfile_lines = log_file.readlines()
        for line in logfile_lines:
            match_obj = re.search(pattern, line)
            if match_obj:
                if (prefix + match_obj.group(2)) not in image_list:
                    image_list.append(prefix + match_obj.group(2))
        sorted_image_list = sorted(image_list, key=lambda url: url[-8:-4])
        return sorted_image_list


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order,
    downloads each image into the given directory.
    Gives the images local filenames img0, img1, and so on.

    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    counter = 0
    for url in img_urls:
        urllib.urlretrieve(url, dest_dir + '/img' + str(counter) + '.jpg')
        counter += 1
    with open(dest_dir + '/index.html', 'w') as log_puzzle_file:
        for i in range(len(img_urls)):
            log_puzzle_file.write('<img src="img' + str(i) + '.jpg" />')


def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print '\n'.join(img_urls)

if __name__ == '__main__':
    main()

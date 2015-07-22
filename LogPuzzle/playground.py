
import re, urllib, os
import sys


class Colors:
    HEADER  = '\033[95m'
    INFO    = '\033[94m'
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR   = '\033[91m'
    OTHER   = '\033[96m'
    ENDC    = '\033[0m'

def test(got, expected):
    if got == expected:
        prefix = Colors.SUCCESS + ' OK   ' + Colors.ENDC
    else:
        prefix = Colors.ERROR + ' Fail ' + Colors.ENDC
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))





"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
# re.search(), vs re.match(), vs re.findall()
# .groups (0-3) = 0 = ?, 1 = ?, 2 = ?, 3 = ?
pattern = r'(GET )(\S.*puzzle.*\.jpg)'
# filename = 'animal_code.google.com'
prefix = 'http://code.google.com'

def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    if not os.path.isfile(filename):
        return []
    with open(filename, 'rU') as log_file:
        image_list = []
        logfile_lines = log_file.readlines()
        for line in logfile_lines:
            match_obj = re.search(pattern, line)
            if match_obj:
                if (prefix + match_obj.group(2)) not in image_list:
                    image_list.append(prefix + match_obj.group(2))
                    print "Another one added to the list:", image_list
        sorted_image_list = sorted(image_list)
        return sorted_image_list



test(read_urls('doesnotexist'), [])
test(read_urls('emptyfile'), [])
# test(read_urls('test_code.google.com'), ['10.254.254.28 - - [06/Aug/2007:00:12:20 -0700] "GET /keyser/22300/ HTTP/1.0" 302 528 "-" "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.4) Gecko/20070515 Firefox/2.0.0.4"\n',
# '10.254.254.58 - - [06/Aug/2007:00:10:05 -0700] "GET /edu/languages/google-python-class/images/puzzle/a-baaa.jpg HTTP/1.0" 200 2309 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@google.com,foo123@google.com,foo123@google.com,foo123@google.com)"\n',
# '10.254.254.28 - - [06/Aug/2007:00:11:08 -0700] "GET /favicon.ico HTTP/1.0" 302 3404 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@google.com,foo123@google.com,foo123@google.com,foo123@google.com)"\n',
# '10.254.254.29 - - [06/Aug/2007:00:13:48 -0700] "GET /edu/languages/google-python-class/images/puzzle/a-baag.jpg HTTP/1.0" 302 3404 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@google.com)"\n'
# ])
test(read_urls('test_code.google.com'), ['http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaa.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baag.jpg'])
test(read_urls('test_code.google.com'), ['http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaa.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baac.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baag.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaa.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baac.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baag.jpg'])


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
# # filename = 'animal_code.google.com'
prefix_pattern = r'(_)(\S+\.\w+)'
# prefix = 'http://code.google.com'
#
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
        return
    counter = 0
    for url in img_urls:
        urllib.urlretrieve(url, dest_dir + '/img' + str(counter) + '.jpg')
        counter += 1
    with open(dest_dir + '/index.html', 'w') as log_puzzle_file:
        for i in range(len(img_urls)):
            log_puzzle_file.write('<img src="img' + str(i) + '.jpg" />')

# test(read_urls('doesnotexist'), [])
# test(read_urls('emptyfile_code.google.com'), [])
# test(read_urls('test_code.google.com'), ['10.254.254.28 - - [06/Aug/2007:00:12:20 -0700] "GET /keyser/22300/ HTTP/1.0" 302 528 "-" "Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.1.4) Gecko/20070515 Firefox/2.0.0.4"\n',
# '10.254.254.58 - - [06/Aug/2007:00:10:05 -0700] "GET /edu/languages/google-python-class/images/puzzle/a-baaa.jpg HTTP/1.0" 200 2309 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@google.com,foo123@google.com,foo123@google.com,foo123@google.com)"\n',
# '10.254.254.28 - - [06/Aug/2007:00:11:08 -0700] "GET /favicon.ico HTTP/1.0" 302 3404 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@google.com,foo123@google.com,foo123@google.com,foo123@google.com)"\n',
# '10.254.254.29 - - [06/Aug/2007:00:13:48 -0700] "GET /edu/languages/google-python-class/images/puzzle/a-baag.jpg HTTP/1.0" 302 3404 "-" "googlebot-mscrawl-moma (enterprise; bar-XYZ; foo123@google.com)"\n'
# ])
test(read_urls('test_code.google.com'), ['http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaa.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baag.jpg'])
# test(read_urls('animal_code.google.com'), ['http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaa.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baab.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baac.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baad.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baae.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaf.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baag.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baah.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baai.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaj.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baba.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babb.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babc.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babd.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babe.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babf.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babg.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babh.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babi.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babj.jpg'])
# print '\n' * 2, "Testing start for download_images"
test(read_urls('doesnotexist'), [])
test(read_urls('emptyfile_code.google.com'), [])
# download_images(['http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaa.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baab.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baac.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baad.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baae.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaf.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baag.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baah.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baai.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaj.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-baba.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babb.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babc.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babd.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babe.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babf.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babg.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babh.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babi.jpg', 'http://code.google.com/edu/languages/google-python-class/images/puzzle/a-babj.jpg'], 'test_logpuzzle')
download_images(read_urls('animal_code.google.com'), 'animal_files')
download_images(read_urls('place_code.google.com'), 'place_files')

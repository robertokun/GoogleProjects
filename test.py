__author__ = 'robertokun'

# def foo(num1, num2):
# return num1 + num2
#
#
# class SomeClass(object):
#
# def __init__(self, name):
# self.name = name
#
#     def bar(self):
#         print 'bar' + self.name
#
# # REPL Read Evaluate Print Loop
# # call function foo
# print foo(1, 3)
# # call function bar
# bar_one = SomeClass('Hello')
# bar_one.bar()
# bar_two = SomeClass('World')
# bar_two.bar()
# bar_one.bar()
#
# """
# output will be:
# 4
# foo
# barHello
# barWorld
# barHello
# """
#
# def extract_names(filename):
#     names = []
#
#     f = open(filename, 'rU')
#     text = f.read()
#     year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
#     if not year_match:
#         sys.stderr.write('Couldn\'t find the year!\n')
#         sys.exit(1)
#     year = year_match.group(1)
#     names.append(year)
#
#     tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', text)
#     names_to_rank = {}
#     for rank_tuple in tuples:
#         (rank, boyname, girlname) = rank_tuple
#         if boyname not in names_to_rank:
#             names_to_rank[boyname] = rank
#         if girlname not in names_to_rank:
#             names_to_rank[girlname] = rank
#     sorted_names = sorted(names_to_rank.keys())
#
#     for name in sorted_names:
#         names.append(name + " " + names_to_rank[name])
#     return names
#
#
# def main():
#     args = sys.argv[1:]
#     if not args:
#         print 'usage: [--summaryfile] file [file ...]'
#         sys.exit(1)
#     summary = False
#     if args[0] == '--summaryfile':
#         summary = True
#         del args[0]
#
#     for filename in args:
#         names = extract_names(filename)
#
#         text = '\n'.join(names)
#
#         if summary:
#             outf = open(filename + '.summary', 'w')
#             outf.write(text + '\n')
#             outf.close()
#         else:
#             print text
#
#
# if __name__ == '__main__':
#     main()

# Bisection Searching and exhaustive enumeration
# x = 25
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(1.0, x)
# ans = (high + low)/2.0
# while abs(ans**2 - x) >= epsilon:
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0
# print 'numGuesses =', numGuesses
# print ans, 'is close to square root of', x

# Palindromes
# def isPalindrome(s):
#
#
#     """Assumes s is a str
#     Returns True if s is a palindrome; False otherwise.
#       Punctuation marks, blanks, and capitalization are
#       ignored."""
#     def toChars(s):
#         s = s.lower()
#         letters = ''
#         for c in s :
#             if c in "abcdefghijklmnopqrstuvwxyz":
#                 letters = letters + c
#         return letters
#
#     def isPal(s):
#         print 'isPal called with', s
#         if len(s) <= 1:
#             print '  About to return True from base case'
#             return True
#         else:
#             answer = s[0] == s[-1] and isPal(s[1:-1])
#             print '  About to return', answer, 'for', s
#             return answer
#
#     return isPal(toChars(s))
#
# def testIsPalindrome():
#     print 'Try dogGod'
#     print isPalindrome('dogGod')
#     print 'Try dogGod'
#     print isPalindrome('doGood')

# *Args & kwargs

# def Func(*args):
#
#     for arg in args:
#         print arg
# mylist =[1, 2, 3, 4, 5, 6, 7, 8, 9, "Ham"]
# Func(*mylist)

# CPU issues with for loops:
# max = int(raw_input('Enter a positive integer: '))
# i = 0
# while i < max:
#     i = i + 1
#     print i

# Finding an approximation of a Root!
# def findRoot(x, power, epsilon):
#      """Assumes x and epsilon int or float, power an int,
#           epsilon > 0 & power >= 1
#         Returns float y such that y**power is within epsilon of x.
#              If such a float does not exist, it returns None"""
#      if x < 0 and power%2 == 0:
#          return None
#      low = min(-1.0, x)
#      high = max(1.0, x)
#      ans = (high + low)/2.0
#      while abs(ans**power - x) >= epsilon:
#          if ans**power > x:
#              low = ans
#          else:
#              high = ans
#          ans = (high + low)/2.0
#      return ans
#
# def testFindRoot():
#      epsilon = 0.0001
#      for x in (0.25, -0.25, 2, -2, 8, -8):
#          for power in range(1, 4):
#              print 'Testing x = ' + str(x) + ' and power = ' + str(power)
#              result = findRoot(x, power, epsilon)
#              if result == None:
#                  print '    No root'
#              else:
#                  print '    ', result**power, '~=', x

# s = 'not bad hello I really love not what you have done with your bad hair'
# # s.find('not' and 'bad', 'good')
# print s.index('not')
# print s.count('not')
# print s.index('bad')
# print s.count('bad')
# print not_bad(s)

# def both_ends(s):
#     if len(string) <= 2:
#         print ' '
#     print string[0:2] + string[-2:]
#     return
# print both_ends(string)

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
# a = 'fixxerupper'
# b = 'podrage'
# def mix_up(a, b):
#     first_two_a = a[0:2]
#     first_two_b = b[0:2]
#     print first_two_b + a[3:] + ' ' + first_two_a + b[3:]
#     return
# print mix_up(a, b)

# def not_bad(s):
#     s.find('not' & 'bad', 'good')
#     print s.index('not')
#     print s.count('not')
#     print s.index('bad')
#     print s.count('bad')
#     print not_bad(s)
#     return


# n = 112232211
# G. palindrome
# given an integer n, determine if n is a palindrome
# for ex--> 12321 --> True
# 1555 --> False


# def palindrome(n):

# print "start"
# if int(str(n)[::]) == int(str(n)[::-1]):
#     print True
# print False
# #     return
# # print "heel"
# #
# # print n, "This is N"
# print map(int, str(n))[0:]
# print map(int, str(n))[-1:]
# newlist = map(int, str(n))[0:]
# print newlist[-1:]
# print int(str(n)[::-1])
# print int(str(n)[::])


# nums = [1, 2, 2, 3, 3, 4, 5, 6]
# print len(nums)


# def print_words(filename):
#     word_count = helper(filename)
#     words = sorted(word_count.keys())
#     for word in words:
#         print word, word_count[word]
#
#
# def get_count(word_count_tuple):
#     return word_count_tuple[1]
#
#
# def print_top(filename):
#     word_count = helper(filename)
#     items = sorted(word_count.items(), key=get_count, reverse=True)
#     for item in items[:20]:
#         print item[0], item[1]
#     return
#
#
# # def Find(r':\w+', text):   or r'([a-z]+|[A-Z]+)' or IGNORECASE?  to be used as a flag
# #     match = re.search(pat, text, re.IGNORECASE)
# #     or use re.findall(pat, text)
# #     if match:
# #         print match.group()
# #     else:
# #         print 'Not Found'
# #     return
#
# def helper(filename):
#     word_count = {}
#     input_file = open(filename, 'rU')
#     for line in input_file:
#         words = line.split()
#         for word in words:
#             word = re.sub('[,;\'\-\".?:)!]', '', word.lower())
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1
#     input_file.close()
#     print word_count
#     return word_count
#
#
# def main():
#     if len(sys.argv) != 3:
#         print 'usage: ./wordcount.py {--count | --topcount} file'
#         sys.exit(1)
#
#     option = sys.argv[1]
#     filename = sys.argv[2]
#     if option == '--count':
#         print_words(filename)
#     elif option == '--topcount':
#         print_top(filename)
#     else:
#         print 'unknown option: ' + option
#     sys.exit(1)
#
# if __name__ == '__main__':
#     main()
# import re, sys
#
# word_dict = {}
# word_list = []
# input_file = open('alice.txt', 'rU')
# for line in input_file:
#     words = line.split()
#     for word in words:
#         word = word.lower()
#         word = re.sub('[,;\-\".?:)!]', '', word.lower())
#         word_list.append(word)
#
# input_file.close()
#
# print 'This is Word_Count', word_list
# for x in range(len(word_list) - 1):
#     if word_list[x] not in word_dict:
#         word_dict[word_list[x]] = []
#     word_dict[word_list[x]].append(word_list[x + 1])
#
# print word_list
# print word_dict
# import sys, urllib
# import sys, re, os, sh, commands, shutil

# def Cat(filename):
#     try:
#         f = open(filename)
#         text = f.read()
#         print '-----', filename
#         print text
#     except IOError:
#         print 'IOError: ', filename
#
# input_file.close()
#
# """Copy Special exercise
# """
# def main():
#     args = sys.argv[1:]
#     for arg in  args:
#         Cat(arg)
#
# if __name__ == '__main__':
#     main()

# urllib.urlretrieve('url code here', 'what you want to call the file here')
# def List(dir):
#     filenames = os.listdir(dir)
#     for filename in filenames:
#         path = os.path.join(dir, filename)
#         print path
#         print os.path.abspath(path)

# shutil.copy(source, dest)

# def List(dir):
#     cmd = 'ls -l ' + dir
#     path = os.path.join(dir, 'test.py')
#     print os.path.abspath(path)
#     (status, output) = commands.getstatusoutput(cmd)
#     if status:
#         sys.stderr.write('there was an error:', + output)
#         sys.exit(1)
#     print output
#
# def main():
#     List(sys.argv[1])
#
# # if __name__ == '__main__':
# #     main()
#
# dir = os.path.exists('solutions')
# print dir


import os
import errno
import shutil
import commands
import urllib
# import requests
# import requests_cache
import functools


# path = '..'
# # .     = current directory
# # ..    = up one or parent of current
# # /     = root directory (highest possible directory)
# # ~     = home directory (home directory of current User
# cmd = 'ls -l'
# def make_sure_path_exists(path):
#     we_are_here = os.getcwd()
#     you_are_here = os.path.abspath(path)
#     print 'We are here:', we_are_here
#     print 'You are here:', you_are_here
#     print "This is the listdir: ", os.listdir(path)
#     try:
#         if os.path.exists(path):
#             print 'Path exists', os.path.dirname(path)
#         else:
#             print 'Path does NOT exist, please hit return if you want me to create it for you'
#
#         # os.makedirs(path)
#     except OSError as exception:
#         if exception.errno != errno.EEXIST:
#             raise
#     return path
# make_sure_path_exists(path)
# print commands.getstatusoutput(cmd)
#
# uf = urllib.urlopen('http://www.google.com')
# uf.read()
# print uf
#
# uh = urllib.urlretrieve('http://google.com/intl/en_ALL/images/logo.gif', 'blah.gif')





# def assure_path_exists(path):
#         dir = os.path.dirname(path)
#         if not os.path.exists(dir):
#                 os.makedirs(dir)
#


# def check_for_directory(dir_name, path, recursive=False):
#     if os.path.isdir(path):
#         if dir_name in os.listdir(path):
#             return path
#         if recursive:
#             for directory in os.listdir(path):
#                 new_path = path + '/' + directory
#                 result = check_for_directory(dir_name, new_path, recursive)
#                 if result:
#                     return result
        # os.makedirs(dir_name)
        # print 'Directory %s did not exist, but does now' % dir_name
    # return None


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


# test(check_for_directory('foo', '/foo/tmp'), None)
# test(check_for_directory('GoogleProjects', '/Users/robertokun/robpython/GoogleProjects'), '/Users/robertokun/robpython/GoogleProjects')
# test(check_for_directory('GoogleProjects', '/Users/robertokun', True), '/Users/robertokun/robpython')
# test(check_for_directory('GoogleProjects', '/Users/robertokun', False), None)
# test(check_for_directory('ourtester', '/Users/robertokun/robpython', True), '/Users/robertokun/robpython/ATM/output')


# def factorial(n):
#     if n > 1:
#         return n * factorial(n - 1)
#     return n

# test(factorial(1), 1)
# test(factorial(5), 120)



# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# test(fibonacci(0), 0)
# test(fibonacci(1), 1)
# test(fibonacci(5), 5)
# test(fibonacci(8), 21)
#
# test(fibonacci(50), 21)
# @lru_cache(maxsize=None) # (LRU = Last Recently Used)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
#
# >>> [fib(n) for n in range(16)]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
#
# >>> fib.cache_info()
# CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)









# Plan for coin problem:
# I want to build a dict 'coins' with {25: 1, 10: 2, 5: 0, 1: 2}
# then have a loop to sum the products of keys and respective values.
# when this sum of products matches desired outcome, list out sorted coins and values for values greater than 0
# if value greater than 0, return keys reverse sorted....

# def make_change(n, coins):
#     answer = {}
#     for coin in coins:
#         num_per_coin = n / coin
#         answer[coin] = num_per_coin
#         n = n - (num_per_coin * coin)
#     if n == 0:
#         answer[coin] = num_per_coin
#         num_of_coins = []
#         for unit, number in answer.iteritems():
#             num_of_coins.extend([unit] * number)
#         return num_of_coins
#
# # make_change(37, [25, 10, 5, 1]) -->[25, 10, 1, 1]
# test(make_change(1, [25, 10, 5, 1]), [1])
#
# test(make_change(200, [25, 10, 5, 1]), [25, 25, 25, 25, 25, 25, 25, 25])
#
# test(make_change(37, [25, 10, 5, 1]), [25, 10, 1, 1])
# test(make_change(6, [25, 10, 5, 1]), [5, 1])
# test(make_change(52, [25, 10, 5, 1]), [25, 25, 1, 1])
#
# test(make_change(0, [25, 10, 5, 1]), [])
#
# test(make_change(30, [25, 10, 1]), [10, 10, 10])
#
#
# def making_changes(n, coins):
#     solution = []
#     for coin in coins:
#         solution.extend([coin] * (n / coin))
#         n %= coin
#     if n == 0:
#         return solution
#     return None
#
# test(making_changes(1, [25, 10, 5, 1]), [1])
# test(making_changes(200, [25, 10, 5, 1]), [25, 25, 25, 25, 25, 25, 25, 25])
# test(making_changes(0, [25, 10, 5, 1]), [])
# test(making_changes(100, []), None)
# test(making_changes(37, [25, 5]), None)
# test(making_changes(37, [25, 10, 5, 1]), [25, 10, 1, 1])
# test(making_changes(6, [25, 10, 5, 1]), [5, 1])
# test(making_changes(52, [25, 10, 5, 1]), [25, 25, 1, 1])
# test(making_changes(30, [25, 10, 1]), [10, 10, 10])



# def make_change(coin_value_list, change, min_coins, coins_used):
#     for cents in range(change + 1):
#         print 'Cents =', cents # my assist
#         print 'Range for change + 1 =', change + 1 # my assist
#         coin_count = cents
#         new_coin = 1
#         for j in [c for c in coin_value_list if c <= cents]:
#             print 'This is J:', j # my assist
#             if min_coins[cents-j] + 1 < coin_count:
#                 coin_count = min_coins[cents-j] + 1
#                 new_coin = j
#         min_coins[cents] = coin_count
#         coins_used[cents] = new_coin
#     return min_coins[change]
#
# def print_coins(coins_used, change):
#     coin = change
#     while coin > 0:
#         this_coin = coins_used[coin]
#         print(this_coin)
#         coin = coin - this_coin
#
# def main():
#     amount = 1
#     coin_list = [1, 5, 10, 25]
#     coins_used = [0]*(amount+1)
#     coin_count = [0]*(amount+1)
#
#     print("Making change for", amount, "requires")
#     print(make_change(coin_list, amount, coin_count, coins_used), "coins")
#     print("They are:")
#     print_coins(coins_used, amount)
#     print("The used list is as follows:")
#     print(coins_used)
#
# main()


# TODO: add caching to fib & lookup dynamic programing<--DONE
'''TODO:    DONE-->go over paths on pc<--DONE
            DONE-->go over paths on python<--DONE
            DONE-->fix paths on pycharm/GIT and trash<--DONE
            4. go over regex
            5. website fix admin name and review bottom menu access?
            6. remind David to prepare dicts/list/sets study homework plans
            DONE-->remind David to prepare automated testing plans for study TDD (Test Driven Development) Red Green Refactor<--DONE
            8. ask about raise try command. and command
            DONE-->not clear on "None" issue in tests, discuss<--DONE
            10. coin_value_list is an argument of a function...how must it be used or not?
            11. this solution uses lists in a wonderful way. How can I learn these better?
            '''

# Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.
#
'''# countX("xxhixx")  4
# countX("xhixhix")  3
# countX("hi")  0
'''

# xlist = 'abcxx'
# new_xlist = [i for i in xlist if i == 'x']
# print "The number of x's in the list is: ", len(new_xlist)


'''DONE-->TODO: how do I split everything in ['xxxdsx'] to ['x','x','x',etc.....<--DONE'''

# list5 = list(xlist)
# print list5
#
# def countx(my_list):
#     if len(my_list) == 0:
#         return 0
#     if my_list[0] == 'x':
#         return 1 + countx(my_list[1:])
#     return 0 + countx(my_list[1:])
#
# def foo():
#     return 5 + len('uowegfbub')
#
# print 'This is how many lower case x\'s there are:', countx(xlist)
# print 'This is how many lower case x\'s there are:', countx('jhgfdxxxxtuxx')
#
# test(countx('xxosidufodkjnfs'), 2)
# test(countx(''), 0)
# test(countx('x'), 1)
# test(countx('abc'), 0)
#
# def sum_even(mylist):
#     if len(mylist) == 0:
#         return 0
#     if (mylist[0]) % 2 == 0:
#         return mylist[0] + sum_even(mylist[1:])
#     return sum_even(mylist[1:])
#
# test(sum_even([]), 0)
# test(sum_even([0, 1]), 0)
# test(sum_even([0, 1, 2]), 2)

# F(0) = F(1) = 1
# F(n) = 2F(n-1) * F(n-2)
# F(5) = ?  F(5) = F(4) * F(3)
#           F(4) = F(3) * F(2)
#           F(3) = F(2) * F(1)
#           F(2) = F(1) * F(0) = 1 * 1 = 1



def func_n(n):
    if 0 <= n <= 1:
        return 1
    return 2 * func_n(n-1) * func_n(n-2)

test(func_n(0), 1)
test(func_n(1), 1)
test(func_n(2), 2)
test(func_n(3), 4)
test(func_n(4), 16)
test(func_n(5), 128)

mem = {}
def func_nmem(n):
    if 0 <= n <= 1:
        if n not in mem:
            mem[n] = 1
            print 'n & mem =', n, mem
            return mem[n]
        new_value = (2 * func_nmem(n-1) * func_nmem(n-2))
        mem[n] = new_value
        print 'This is mem:', mem
    return 2 * func_n(n-1) * func_n(n-2)
print 'This is mem:', mem




test(func_nmem(0), 1)
test(func_nmem(1), 1)
test(func_nmem(2), 2)
test(func_nmem(3), 4)
test(func_nmem(4), 16)
test(func_nmem(5), 128)
test(func_nmem(6), 4096)
test(func_nmem(7), 1048576)

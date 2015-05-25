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
import re, sys

word_dict = {}
word_list = []
input_file = open('alice.txt', 'rU')
for line in input_file:
    words = line.split()
    for word in words:
        word = word.lower()
        word = re.sub('[,;\-\".?:)!]', '', word.lower())
        word_list.append(word)

input_file.close()

print 'This is Word_Count', word_list
for x in range(len(word_list) - 1):
    if word_list[x] not in word_dict:
        word_dict[word_list[x]] = []
    word_dict[word_list[x]].append(word_list[x + 1])

print word_list
print word_dict


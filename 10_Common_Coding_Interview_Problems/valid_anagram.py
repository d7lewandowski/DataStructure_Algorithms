'''
input: 
s1 = 'danger'
s2 = 'garden'
output: true
'''

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    freq1 = {}
    freq2 = {}
    

    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    #  print(freq1, freq2)
    return True


assert are_anagrams('danger', 'garden') == True
assert are_anagrams('danger', 'gardec') == False

# second solustion 
from collections import Counter
def are_anagrams(s1, s2):

    if len(s1) != len(s2):
        return False
    
    return Counter(s1) == Counter(s2)

assert are_anagrams('danger', 'garden') == True
assert are_anagrams('danger', 'gardec') == False


"""
Two anagrams have the same 
lexiographically sorted string
"""

def sorted_are_anagrams(s1, s2):

    if len(s1) != len(s2):
        return False
    
    return sorted(s1) == sorted(s2)


assert sorted_are_anagrams('danger', 'garden') == True
assert sorted_are_anagrams('danger', 'gardec') == False



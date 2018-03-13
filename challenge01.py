"""
Translate the following text:
   g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

import string

str1 = "map"
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
step = 2
new_str = []

for letter in str:
    # Check if letter is actually a letter
    if letter in string.ascii_lowercase:
        # Update the index with step
        index = string.ascii_lowercase.index(letter) + step
        # Update the letter
        word = string.ascii_lowercase[index % len(string.ascii_lowercase)]
        # Update the new_str
        new_str.append(word)
    else:
        new_str.append(letter)
    
print("".join(new_str))
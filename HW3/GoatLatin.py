# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:39:21 2019

@author: Liddy Hsieh

# Question 2: 5 points

This question is from leetcode.com

824. Goat Latin

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"


Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Notes:

S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.

You need to write a function called to_goat_latin and call it using the following syntax.

print(to_goat_latin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
print(to_goat_latin("The quick brown fox jumped over the lazy dog")=="heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")

These two print function calls must print True.
"""

class GoatLatin:
    def to_goat_latin(self, s):
        #initialize
        VOWELS = 'aeiou'
        output_list = []
        count = 0
        
        input_list = s.split() #split sentence into a list
        for word in input_list:
            #Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
            count +=1
            #if first letter == a, e, i, o, or u, append "ma" to the end of the word
            if(word[0].lower() in VOWELS):  
                output_list.append(word+'ma' + 'a'*count)
            #else remove the first letter and append it to the end, then add "ma".    
            else:
                output_list.append(word[1:] + word[0] +'ma' + 'a'*count)
             
        output =' '.join(output_list)     
        return output
 

# main       
input1 ='I speak Goat Latin'
input2 ='The quick brown fox jumped over the lazy dog'

o = GoatLatin()
print('Input: '+ input1 + '\nOutput: ' + o.to_goat_latin(input1) + '\n')
print('Input: '+ input2 + '\nOutput: ' + o.to_goat_latin(input2) + '\n')

     
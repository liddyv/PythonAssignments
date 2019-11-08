'''
The standard form of a quadratic expression is ax^2 + bx + c where 
a, b and c are real numbers and a is not equal to zero. The degree of a 
quadratic expression is 2 and a, b and c are called the coefficients. 
For example, in the quadratic expression (3x^2 + 8x − 5), the 
coefficients are 3, 8 and -5 corresponding to the exponent 2, 1 and 0 
respectively. Define and use a Python class that can perform
operations on quadratic expressions such as addition and subtraction. Define 
a Python class called ‘Quadratic’. The Python object 
that will create this class will be as follows
Q1 = Quadratic(3,8,-5)
This corresponds to the expression above.
Define another Python object Q2 as follows
Q2 = Quadratic(2,3,7) which corresponds to the quadratic expression 
2x^2 + 3x + 7

Part I – Addition and subtraction of quadratic expressions
Perform the addition and subtraction operation by using 
operator overloading. Make the following Python calls:
quadsum = Q1+Q2
quaddiff = Q1-Q2
Print the values of quadsum and quaddiff. The output on your screen 
must be similar 
to the one below.
The sum is 5x^2+11x+2
The difference is x^2+5x-12

Part II – Equality operator for quadratic expressions
Two quadratic expressions are equal only if all the corresponding 
coefficients are equal. Define an equality operator that will return 
‘True’ if two quadratic expressions are equal and ‘False’ when they 
are not equal. For example, in this code for Q1 == Q1, the value must be ‘True’
and for Q1 == Q2, the value must be ‘False'.
'''

class Quadratic:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return '%d x^2 + %d x + %d' %(self.a,self.b,self.c)

    def __add__(self,other):
        return Quadratic(self.a + other.a, self.b + other.b, self.c + other.c)

    def __sub__(self,other):
        return Quadratic(self.a - other.a, self.b - other.b, self.c - other.c)

    def __eq__(self,other):
        if(self.a == other.a and self.b == other.b and self.c == other.c):
            print("The two quadratic expressions are equal")
            return True
        else:
            print("The two quadratic expressions are not equal")
            return False

q1 = Quadratic(3, 8, -5)
q2 = Quadratic(2, 3, 7)

print("The sum of the given quadratic expressions is ", q1 + q2)
print("The difference of the given quadratic expressions is ", q1 - q2)
print(q1 == q2)


'''
Leetcode.com

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
'''

def to_goat_latin(text):
    vowels = 'aeiouAEIOU'
    news = ''
    i = 1
    for word in text.split():
        if word[0] in vowels:
            news += word + 'ma' + 'a'*i
        else:
            news += word[1:] + word[0] + 'ma' + 'a'*i
        i += 1
        news += ' '
    return news.strip()

print(to_goat_latin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
print(to_goat_latin("The quick brown fox jumped over the lazy dog")=="heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")





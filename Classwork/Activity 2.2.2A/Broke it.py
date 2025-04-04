# original
This is a long message that I need to decrypt and it needs to be long enough to get enough data to figure out whether this enryption uses substitution or not. The end.

# encrypted message
20393, 800, 11343, 38185, 32479, 11343, 38185, 32479, 23079, 32479, 15804, 19702, 12841, 14767, 32479, 11129, 32033, 38185, 38185, 23079, 14767, 32033, 32479, 24523, 800, 23079, 24523, 32479, 4067, 32479, 12841, 32033, 32033, 37107, 32479, 24523, 19702, 32479, 37107, 32033, 17651, 22210, 7809, 17821, 24523, 32479, 23079, 12841, 37107, 32479, 11343, 24523, 32479, 12841, 32033, 32033, 37107, 38185, 32479, 24523, 19702, 32479, 10667, 32033, 32479, 15804, 19702, 12841, 14767, 32479, 32033, 12841, 19702, 13456, 14767, 800, 32479, 24523, 19702, 32479, 14767, 32033, 24523, 32479, 32033, 12841, 19702, 13456, 14767, 800, 32479, 37107, 23079, 24523, 23079, 32479, 24523, 19702, 32479, 3414, 11343, 14767, 13456, 22210, 32033, 32479, 19702, 13456, 24523, 32479, 1090, 800, 32033, 24523, 800, 32033, 22210, 32479, 24523, 800, 11343, 38185, 32479, 32033, 12841, 22210, 7809, 17821, 24523, 11343, 19702, 12841, 32479, 13456, 38185, 32033, 38185, 32479, 38185, 13456, 10667, 38185, 24523, 11343, 24523, 13456, 24523, 11343, 19702, 12841, 32479, 19702, 22210, 32479, 12841, 19702, 24523, 1184, 32479, 20393, 800, 32033, 32479, 32033, 12841, 37107, 1184

# replacing every number sequence with a random letter (every repeating number has the same letter)
abcdecdefeghijeklddfjlembfmeneilloemheolpqrsmefioecmeillodemhewleghijelihtjbemhejlmelihtjbeofmfemhevcjtqlehtmeublmblqembcdeliqrsmchietdldedtwdmcmtmchiehqeihmxeableliox

# frequency program output
a : 2
b : 8
c : 8
d : 10
e : 32
f : 6
g : 2
h : 13
i : 12
j : 7
k : 1
l : 18
m : 18
n : 1
o : 6
p : 1
q : 5
r : 2
s : 2
w : 2
t : 7
v : 1
u : 1
x : 2

# letter replacement log here:
e> 
a>t
b>h
c>i
d>s
f>a
g>l
h>o
i>n
j>g
k>m
l>e
m>t
n>i
o>d
p>c
q>r
r>y
s>p
x>.
w>b
t>u
v>f
u>w

# decoded message (no keys used, or decrypters)
this is a long message that I need to decrypt and it needs to be long enough to get enough data to figure out whether this enryption uses substitution or not. the end.


"""
EXPLANATION:

Spaces are the most common single character in a message that is long enough.
In that first sentence, for example, had 13 spaces. This was closely followed
by the letter e, at 8 cases. This makes sense, as seperated words is a common
idea in english, and the letter e is the most commonn letter in the english
dictionary. We can decode the subtituted letters by starting with a comparisn
of the most common letters in the english dictionary to the most commonly use
letters in the message. Given that this message is not as extensive as the
english dictionary, I will not get the same frequency results, but it is close
enough. There comes a point in the decoding, when one can easily infer the last
characters. The character swap log shows the order at which I replaced certain
characters using this method, eventually leading to the entire message being decoded.
I used various simple python programs to help aid the process of decoding this 
message, although it is more than possible to decode this type of RSA with just
a pen and paper. I started by encrypting a simple message and deleting all keys
associated with this program, this means I have a lost message that can only be
decoded using special straytegies, as follows. The RSA program outputs a sequence
multidigit numbers in a long list. I can replace each of these items in the list 
with a random letter. If the message contains every letter in the alphabet, one will
need to use a random symbol instead (Due to spaces and possible symbols used in the
message). This can then be compacted into one long string without spaces. This string
can then be in[utted to either a frequency program, or one can manually count how 
many times a character repeats in the message. This makes swapping letters easier
later. One can then use a letter swapper program, or swap letters by hand on paper.
Using the most common repeated character (often spaces) and continuweing down the
most commonly repeated cases, one will eventually be able to decrypt any message.
However, the shorter each message is, the harder it will be to decode. Shorter
messages do make it easier to brute force, on the other hand-
"""
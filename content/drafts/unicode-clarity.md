Title: Unicode Clarity
Date: YYYY-MM-DD HH:MM
Modified: YYYY-MM-DD HH:MM
Tags: reading, life hack, technique, learning, unicode
Slug: unicode-clarity
Summary: How I have Finally Understood Unicode et al




For a good number of years (and like [Joel]() rightly predicted) I have 
struggled with gaining satisfactory understanding of basic Unicode concepts and 
how it works.

First, a disclaimer. At the time of this writing, I have not gained full 
understanding of the more deeply entrenched parts of the Unicode. However, I'd 
like to think I have what would fit as sufficient superficial grasp of the basic 
concepts.

As a programmer, it is expected of you to write your programs with working 
knowledge of how character sets can affect the rendering of text on different 
machines or in different environments.

The most basic of all is ASCII. If you can't understand ASCII, I could bet 
nothing else would make any sense. So let's begin there.

ASCII is pretty dated, and it is somewhat the common precursor of the character sets 
we have today. To use a cliched phrase, let's say, _it is at the bottom of the 
food chain_.

Before going further, I'd like to quickly remind you that, being about the 
tiniest, the corpus of the computer has only two items: 0 and 1. The vast 
majority of abilities possessed by this machine boil down to the many different 
ways of combining those two _states_. So, when I say ASCII, I am essentially 
talking about the X number of ways to arrange those two bit states in 8 places. 
This is what ASCII is, well at least, until you scale up a bit to understand 
what it represents.


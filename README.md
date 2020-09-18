# burger_generator
Author: Jasper Gordon
Title: Burger Generator

Description: Burger Generator uses a markov chain concept to output and display various possible combinations of hamburger toppings. The idea behind it was to try and teach the program what are more common and less common orders to place these toppings, and then have the program generate possible orders based on a probability matrix it was given.

Setting up and executing program: This program has a simple setup. To run the program, make sure your system's version of python is up to date (mine runs Python 3.8.5) and then simply input a desired number of toppings as an arugment on line 138 before calling the program via a terminal command. Exp: python3 burger_builder.py

Project Thinking and Reflection: My aim with this project was to see what types of creative combinations for a burger a computer could come up with. My passion here comes from a love of cooking, and I thought it would be fun to think outside the box see what a program, when given some basic understanding of how humans (or me in this case) commonly order burger toppings, could produce. I think with food there is a commmon sentiment that even the most basic meals or dishes can be revitalized or made exciting given some creativity and new persepctive. Humans will try to eat almost anything if they think it will taste good, so why not try and come up with creative ideas with the help of a computer program? Although the topping options are limited (as I will discuss further below), I do consider this program to be creative because it is visually presenting ideas, some of which I had not considered until fully seeeing on a screen. Exp: Typically people put cheese on top of the burger patty, but what if you put one slice on top and another below? Perhaps create a cheese envelope for the burger. While this may sound a little silly, I think it is creative because not only is this a slightly new combination, but it inspires me to think even further about frying this meat cheese pocket before hand and then putting on the burger, or having no buns but crisping up cheese into crackers to accompany the burger. Not all great ideas, but I do value how the program opens my mind a bit to new ideas.

While this is a simple program, it was still challenging for me in a variety of ways. First off, I have not coded in a few months so there was a lot of refreshing and re-learning of concepts. Secondly, this was my first time using Pillow to help with images in Python, so there was a bit of a learning curve and testing process to make sure I had a solid understanding of the system. As I mentioned above, the toppings choices presented a challenge for me. Origionally, I had 10 topping choices with image assests ready to go, but I quickly realized that hardcoding the matrix table probabilities would take an enormous amount of time. The follow up to this was the question of why hard code any of it? I put typed in probabilities for each combination that I thought were reasonable given my burger experience. Exp: It is more likely that given a bottom bun the next ingredient would be a hamurger patty than a top bun. My origional hope was to perform a webscrape of various resturants to glean some information about ordering, but it became a time issue. I am not proud of the implementation of this system (too many if statements), but I saw it as a good starting point. For one, it got my brain back into thinking practically and in the coding mindset. Additionally, this project has plenty of room to grow, and given more time could vastly exapnd its creative bounds given more toppings and room to paint. I would have also enjoyed having the program display multiple burgers on the screen to give it more of an artistic style, but for now I am happy with it. My next steps will be to challenge myself to let the program do more of the work, and to reintroduce myself to more complex, efficent data structures and systems.

Sources: I spoke with Tenzin Choezin about this project, mainly about updating our computers' python versions and tinkering with Pillow, but also about the general concepts of Markov Chains. I also read the following sites: https://www.datacamp.com/community/tutorials/markov-chains-python-tutorial and https://medium.com/@__amol__/markov-chains-with-python-1109663f3678

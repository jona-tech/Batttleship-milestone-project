# Battleships

Battleships is a game intended for users to have a good and fun time by trying to win and find all five ships before the ten rounds are over. 

The target audience is anybody who enjoys guessing games.
The rules are easy and most people can understand the game, wich makes it suitable for a wide audience throughout most ages.

The live link to the game on Heroku can be found here: https://battleships-jb.herokuapp.com/

![Alt text](https://i.imgur.com/LoOLwIW.png)

## Description

The game is a classic battleship game. Five ships are placed at random places in order to be "hit" by the players guesses. In this version, the player has 10 turns to try to sink the fleet, otherwise the player loose. 

## Features

### Welcome and Info section

The first section displays printed text to welcome the player <br>
![Alt text](https://i.imgur.com/wB9kzxi.png)

Also a short info section to describe the game rules.<br>
![Alt text](https://i.imgur.com/WVjXjcs.png)


### Languages & Modules

* I've been using git throughout the development of this app.
* The game is written entirely in Python and can be played directly in the terminal window.
* The randint statement from random module has been imported to place ships at random places over the board by generating random numbers.
* The python code includes try/exception handling, conditional statements, for and while loops and lists etc.
<br>
![Alt text](https://i.imgur.com/bGLIRMZ.png)

## Testing

* I have been continously testing the game throughout the development by calling functions and testing them myself. 
* The file is designed to fit (pep8) standards and has no errors in the linter<br>
* The application has also been extensively tested on the Heroku platform to ensure consistency throughout platforms.
* The game runs through debug session without any problems.

## Deployment

This project was deployed through Heroku with connection to my Github repository.

A live link kan be found here: https://battleships-jb.herokuapp.com/

Link to the Github repository: https://github.com/jona-tech/Batttleship-milestone-project.git


<ol>
<li>Go to the website https://heroku.com </li>
<li>Log in if you have an account, like me, otherwise sign up</li>
<li>Go to dashboard and select "Create new App"</li>
<li>Create a name for the project and select region</li>
<li>Click create</li>
<li>Go to settings and add config var: Key: PORT, Value: 8000</li>
<li>Add Python and Node.js buildpacks to project.</li>
<li>Go to the Deploy section and choose github as source for deployment</li>
<li>Write the name of your repository</li>
<li>Press search and then click "connect"</li>
<li>Go to manual deploy section and deploy "main" branch</li>
<li>And the game is live!</li>
</ol>

## Credits

* Stackoverflow and youtube has helped me figuring out some problems along the way.
* Code Institute code material is the greatest source of information for this project.
* My cousin Lucas Lundgren, a very experienced developer with Python as one of his main languages, has helped me checking through the material along the way.
* I collected information about the classic game on Youtube to understand the rules and gameplay myself.

## Other

* Fixed Bug: The linter tips showed 7 errors about redifining variables "ships" and "board" from outer scope. 
This was fixed by renaming the global variables
* Game Over didn't show up when the game was over. 
This was fixed by adding a conditional statement that prints game over when the player is out of rounds.


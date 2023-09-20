# Battleships

## How to play.
You try and hit the battleships by calling out the coordinates of one of the squares on the board.
Neither you nor the computer can see the other's board so you must try to guess where they are.
You have 10 shots to sink all of your oppents battleships.

Please follow link below to access the Battleships game -
[Battleships Game](https://battleships62-71e1eab5883b.herokuapp.com/)

## Am I Responsive

As shown below ami.responsive was used -

![am-i-responsive](images/ami.responsive.png)

## Features

A 5x5 grid board will be shown and randomly place ships on it.
The user can not see where the computer has put its ships.
It will also show you how many attempts you have, which takes away one attempt every go you take.

![beginning-of-game](images/begin.png)

It will show that when a ship has been hit, 'X' will appear.

![bullseye](images/hit.png)

When the user misses, 'O' will appear.

![miss](images/miss.png)

Should you pick a space off the board the message 'Where are you off to? Try again' will appear.

![try-again](images/off-board.png)

At the end of the game once, you will be asked if you would like to play a new game.

![new-game](images/rematch.png)

## Validator Testing

PEP8 was used to validate the code.

Four errors were shown from PEP8 -

![validator](images/validator.png)

## Deployment

This project was deployed using CodeInstitutes mock terminal for Heroku.

Steps for deployment included:

1) Clone the repository
2) Create a new Heroku app
3) Set the building packs to python and nodejs in the particular order
4) Link the Heroku app to the repository
5) Deploy


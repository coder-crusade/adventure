# Software requirements

## vision

A playeable text game where a user can navigate around the game space.
This will include the ability to see a map of that space.
Includes inventory manangement, and object interactivy activity, such as 'eating an apple'.
Includes a combat system, so that the player can engage in combat with monsters on the map.

## scope

### in

1. command line interaction
1. combat system, with health points for player and monsters
1. navigation
1. inventory management
1. playable on your local machine, presuming you have the proper version of python installed and poetry

### out

1. not a GUI
1. not mutiplayer
1. not a game on the internet that you connect to

### MVP

- Map : Three rooms inside one hallway with a locked door at the end of the hallway
- Learn how to navigate through the rooms
- A dungeon rat guards the key needed to open the door at the end of the hallway
  - Learn how to defeat the rat and collect the key
  - This interaction will introduce the user to their Health points
- Once the key has been collected, navigate to the door and move onto the next level
- Game ends when the user reaches the exit door

## stretch goals

- add more levels with increased difficulty and complexity, such as procedurally generated maps, and monsters with AI to navigate that map

## Functional requirements

- User can start the game, and play it

## Non-Functional requirements

- every object needs automated testing through pytest

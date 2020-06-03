# Werewolf-Facilitation-Helper

This is a small web app I built to help me facilitate a famous board game, werewolf(狼人杀)。This app enables moderators to create a game with a randomized role distributions. Game players can also use this site to check their roles.

## Webpage URL:
https://werewolf-facilitator.herokuapp.com/

## How to Use - Facilitators:
- Visit the webpage and click on "moderate a game" button
- Enter the numbers of each role you would like in a game and click on "distribute role" button.
- If entered correctly, a random matching between player number and role will appear. Save the Game ID for reference. Players will need this to check their role.

## How to Use - Game Players:
- Visit the webpage and click on "Check Your Roles" button.
- Enter the game ID and player number.
- Click on "Check Your Role" button.

## Future Improvements & Features:
This web app is still pretty much a work-in-progress. Here are a list of items I am thinking of implementing.
- Add user login to improve security of role information.
- Add special werewolf selection for moderators on the werewolf moderation page(*implemented*).
- Implement other games for moderators(e.g. 狼人猜词(A word guessing game, but people have different roles)/谁是卧底(Figure out people who may have a different word that you are describing)).
- Voting for game players.

If you have any suggestions, feel free to put it as an issue. However, I will decide whether to implement it. At the end of the day, I use this app for the purpose of moderating the game.

## Acknowledgement
I would like thank Eric Ma for providing me guidance in terms of implementing a database system for this web application. Much of the system structure is taken from his app for distributing small group members for Bible studies. You can find out more about that web application here: https://github.com/ericmjl/small-group

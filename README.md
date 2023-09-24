# Farkle AI
A project for learning how to apply RL in practice.

**Goal**: Create a `gymnasium` environment for training an AI to play Farkle using Reinforcement Learning.

# Ruleset

We'll be using the farkle ruleset from the game [Kingdom Come: Deliverance](https://kingdom-come-deliverance.fandom.com/wiki/Dice), that is:

- a single 1 is worth 100 points;
- a single 5 is worth 50 points;
- three of a kind is worth 100 points multiplied by the given number, e.g. three 4s are worth 400 points;
- three 1s are worth 1,000 points;
- four or more of a kind is worth double the points of three of a kind, so four 4s are worth 800 points, five 4s are worth 1,600 points etc.
- full straight 1-6 is worth 1500 points.
- partial straight 1-5 is worth 500 points.
- partial straight 2-6 is worth 750 points.

 
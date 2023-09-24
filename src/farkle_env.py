import numpy as np

FULL_STRAIGHT = {1, 2, 3, 4, 5, 6}
PARTIAL_STRAIGHT_LOW = {1, 2, 3, 4, 5}
PARTIAL_STRAIGHT_HIGH = {2, 3, 4, 5, 6}

class FarkleEnv():
    """A class describing the environment of Farkle.

         
    
    """
    def __init__(self):
        """
        Initializes the object with default values for `dice`, `score`, and `done`.

        Parameters:
            self ():
                The instance of the class.

        Returns:
            None
        """
        self.dice = np.zeros((6,), dtype=int)
        self.score = 0
        self.done = False

    def reset(self):
        """
        Reset the state of the game.

        :return: The updated state of the game, including the dice, score, and done status.
        :rtype: Tuple[numpy.ndarray, int, bool]
        """
        """"""
        self.dice = np.zeros((6,), dtype=int)
        self.score = 0;
        self.done = False;

        return self.dice, self.score, self.done

    def roll_dice(self, num_dice):
        """
        Generate a random dice roll.

        Returns:
            ndarray: An array of random dice roll values.
        """
        self.dice = np.random.randint(1, 7, size=(num_dice,))
        return self.dice
    

    def get_score(self, dice: np.array) -> int:
        """
        Calculate the score based on the given dice values.

        Parameters:
            dice (np.array): An array of integers representing the dice values.

        Returns:
            int: The calculated score.
        """
        score = 0
        dice_set = set(dice)
        dice_counts = np.bincount(dice)

        if dice_set == FULL_STRAIGHT:
            score = 1500
        elif dice_set == PARTIAL_STRAIGHT_HIGH:
            score = 750
        elif dice_set == PARTIAL_STRAIGHT_LOW:
            score = 500
        else:
            for i in range(1, 7):
                # Three or more of a kind
                # Four or more gets score doubled for each additional dice
                if dice_counts[i] >= 3:
                    if i == 1:
                        score = 1000 * (2 **(dice_counts[i] - 3))
                    else:
                        score += (100 * i) * (2 **(dice_counts[i] - 3))
                    
                    # Set count to zero so that it won't be double counted below
                    dice_counts[i] = 0
            score += dice_counts[1] * 100 
            score += dice_counts[5] * 50
        return score

    def step(self, action: np.array) -> Tuple[np.array, int, bool, int]:
        reward = 0

        if action == 0:
            # Roll all dice
            self.roll_dice()
            round_score = self.get_score(self.dice)


            # Farkle! (? not sure if this capturing farkle or not)
            if np.count_nonzero(self.dice) == 0:
                self.done = True
                reward = -1000

        else:
            num_dice = np.count_nonzero(action)        
            if num_dice == 0:
                reward -= 100
            else:
                # Filter available dice
                selected_dice = self.dice[action == 1]
                score = self.get_score(selected_dice)

                # Farkle!
                if score == 0:
                    reward -= 100
                else:
                    self.score += score

                    # roll only the selected dice
                    for idx in np.where(action == 1)[0]:
                        self.dice[idx] = np.random.randint(1, 7)

                    if np.count_nonzero(self.dice) == 0:
                        self.done = True
                        reward = -1000
        
        if self.score >= 10000:
            self.done = True
            reward = 1000
    
        return self.dice, self.score, self.done, reward
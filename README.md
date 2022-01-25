# Wordle Game, Solver, Analysis

In attempt to know if all wordle puzzles can be solved in 6 attempts or less, I recreated the game, and build an algorithm to solve user-input words. The choice of initial initial guess plays a role in optimizing the algorithm performance. A performance script returns a summary of the success rate and average number of attempts for each initial guess.

The game was made easier for the user to select the next guess based on a list of valid words return. One may learn to be better at solving wordle, or be lazy and let the solver solve it for you.

## Performance

Out of 2315 common 5-letter words used in wordle, this algorithm achieve highest 99.7% with ARIEL as initial guess. Even when initial guess is not optimalized, it can achieve 99% success rate to solve word under six attempts. Wordle also has another valid list of 10657 less common words, which was also used in this algorithm.

## How to use

Download cloning this repo. 
```
git clone https://github.com/ewinapun/wordle-master.git
```

### Run the Wordle game
```
cd wordle-solver
python3 game.py
```

### Run the Wordle solver
```
cd wordle-solver
python3 solver.py
```

### Run the Wordle analysis
```
cd wordle-solver
python3 performance.py
```

## The search strategy

More details will be added soon. However, I did not attempt to look for a solution. This algorithm is my own design. No machine learning or english language model were used (could have), this algorithm simply just search and letter distribution.

## Extend to n-letter words

Given another list of n-letter words, this algorithm should be capable to solve it as well. Feel free to test it on your own.

## Credits

The word lists were provided from the original wordle website https://www.powerlanguage.co.uk.
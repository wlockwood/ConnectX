# Detecting Wins and Winning Runs
Goal: Develop a method that will determine if someone has won given the current state of the game board.
Optional: Return a list of runs that won


## Win detection - Method 1, iterative
```py
store winning_runs = []
for each cell on board:
	if not occupied, skip
	
	store runs_from_here = []
	read player
	get adjacent cells
	for each adjacent cell owned by matching player:
		store this_run = [starting_cell_index, first_adjacent_cell_index]
		determine transform (UR or D or L, etc.) to get from original to adjacent
		store run_length = 2
		loop:
			apply transform again and check matching player
			if not matched, break
			if matched:
				increment run_length
				append cell index to this_run

	for each run in runs_from_here:
		if len(run) >= rules.win_length:
			append run to winning_runs
```
deduplicate winning runs somehow
return winning_runs. type will be a list of a list of tuples that are cell indices
(Caller can check to see if there are any and choose to display them, if so)

## Win detection - Method 2, recursive
```py
winning_runs = []

for each occupied cell:
	for each adjacent friendly cell:
		run = get_run(adjacent_friendly_cell)
		run.append(starting_cell)
		this_cell_runs.append(run)
		if len(run) >= win_run_length:
			winning_runs.append(run)	

def get_run(current_cell, came_from_cell = (0,0))
	determine directional transform (UR or D or L, etc.)
	next_cell = apply directional transform
	
	# Base case AKA terminating case
	if next_cell is empty or not friendly:
		return [current_cell]
	
	# Recursive case
	if next cell is friendly:
			child_run = get_runs(next_cell, current_cell)  # target_cell is the current cell
			child_run.append(current_cell)
			return child_run
```

## Performance
Method one above runs in O(n^2) time, and method two should run in O(n) but is recursive and thus sensitive to call depth limitations.

## Conclusions
 - Because moving the cell indices around as a group is kind of clunky, I'd implement a Cell class. The Cell class would have methods for seeing who owns it, identifying whether it's occupied at all, and returning its adjacent cells (with an option to only return friendlies).
 - A list of Cells is fine for most purposes, but once you think about how to deduplicate a list of runs, it's obvious a Run class should be involved. 
    - As a bonus, if play were to continue after a win ("You have won. Continue on this board? Y/N") we would need a way of identifying runs so that we could flag them to be ignored. This would be much easier with a Run class, but could be done with a simple list.

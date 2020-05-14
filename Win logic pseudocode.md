 = Win detection - Method 1, iterative = 
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
deduplicate winning runs somehow
return winning_runs. type will be a list of a list of tuples that are cell indices
(Caller can check to see if there are any and choose to display them, if so)

 = Win detection - Method 2, recursive = 

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

def ask_for_int(query: str, required: bool = True, default: int = None,
                accept_min=float("-inf"), accept_max=float("inf")):
    while True:
        try:
            print()
            user_input = input(f"{query} ({accept_min} - {accept_max})?\n")
            user_int = int(user_input)
            # No constraints
            if accept_min == float("-inf") and accept_max == float("inf"):
                return user_int

            if user_int > accept_max or user_int < accept_min:
                print(f"{user_int} is outside allowable range ({accept_min} to {accept_max}). Please try again")
            else:
                return user_int

            # If we get to here, it failed to meet at least one constraint

        except ValueError:
            print(f"Unable to parse '{user_input}' as an integer. Please enter a valid number.")




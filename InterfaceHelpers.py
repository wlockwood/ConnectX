# TODO: Tell user if there is a default
# TODO: Tell user if required
# TODO: Previous two are mutually exclusive?
def ask_for_int(query: str, required: bool = True, default: int = None,
                accept_min=float("-inf"), accept_max=float("inf")):
    if accept_min == accept_max:
        print()
        print(f"{query} ({accept_min} - {accept_max})\n")
        print(f"Due to previous decisions, there are no choices here, defaulting to {accept_min}")
        return accept_min

    while True:
        try:
            print()
            user_input = input(f"{query} ({accept_min} - {accept_max})\n")
            
            if user_input == "" and default is not None:
                return default

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


# TODO: Look into parameter sets. Having required and default is weird.
def ask_for_word(query: str, required: bool = True, allow_spaces=False, default: str = None, max_len=float("inf")):
    while True:
        acceptable_input = True
        print()
        user_input = input(f"{query}?\n")

        if required and default:
            raise Exception("ask_for_word was called with both a default value and required. Please don't.")

        if required and len(user_input) < 1:
            print(f"This is a required value. Please input something.")
            acceptable_input = False

        if allow_spaces and " " in user_input:
            print(f"Spaces are not allowed, but '{user_input}' contains at least one space character.")
            acceptable_input = False

        if len(user_input) > max_len:
            print(f"Your input of '{user_input}' is greater than the max length of {max_len:,}")
            acceptable_input = False

        if acceptable_input:
            return user_input

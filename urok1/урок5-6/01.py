def list_checker(var_1):
    if type(var_1) != list:
        raise TypeError(
            f"Invalid type: {type(var_1)}. Expected a list.")
    else:
        return f"List is OK: {var_1}"
first_var = "hello"
list_checker(first_var)
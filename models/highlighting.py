def failed(string):
    return f"\033[1m\033[31m[FAILED]\033[0m   \033[31m{string}\033[0m"


def successful(string):
    return f"\033[1m\033[32m[SUCCESSFUL]\033[0m   \033[32m{string}\033[0m"


def info(string):
    return f"\033[1m\033[33m[INFO]\033[0m   \033[33m{string}\033[0m"

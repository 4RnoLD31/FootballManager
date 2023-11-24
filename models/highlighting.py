import colorama

colorama.init()


def failed(string):
    return f"{colorama.Fore.RED}{colorama.Style.BRIGHT}[FAILED]   {colorama.Style.NORMAL}{string}{colorama.Style.RESET_ALL}"


def successful(string):
    return f"{colorama.Fore.GREEN}{colorama.Style.BRIGHT}[SUCCESSFUL]   {colorama.Style.NORMAL}{string}{colorama.Style.RESET_ALL}"


def info(string):
    return f"{colorama.Fore.YELLOW}{colorama.Style.BRIGHT}[INFO]   {colorama.Style.NORMAL}{string}{colorama.Style.RESET_ALL}"

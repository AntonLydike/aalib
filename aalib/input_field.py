import readline


def input_field(prompt: str, options: list[str] | None = None, default=""):
    # 1. Setup Autocomplete
    def completer(text, state):
        matches = [opt for opt in options if opt.startswith(text)]
        if state < len(matches):
            return matches[state]
        else:
            return None

    if options is not None:
        readline.set_completer(completer)

    # Enable the 'tab' key for completion
    readline.parse_and_bind("tab: complete")

    # 2. Setup Default Value (The "Hook")
    # This function runs right before the prompt is displayed
    def pre_input_hook():
        readline.insert_text(default)
        readline.redisplay()

    readline.set_pre_input_hook(pre_input_hook)
    val = input(prompt).strip()
    while options is not None and val not in options:
        print(f"Invalid choice: {val}")
        val = input(prompt).strip()

    readline.set_completer(None)
    readline.set_pre_input_hook(None)
    return val

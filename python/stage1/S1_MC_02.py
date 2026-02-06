def run_command(cmd: str):
    match cmd:
        case "start":
            return "STARTING"
        case "stop":
            return "STOPPING"
        case "status":
            return "STATUS_OK"
        case _:
            return "UNKNOWN_COMMAND"


# tests
print(run_command("start"))    # STARTING
print(run_command("stop"))     # STOPPING
print(run_command("status"))   # STATUS_OK
print(run_command("hello"))    # UNKNOWN_COMMAND
print(run_command(""))         # UNKNOWN_COMMAND
print(run_command(None))       # will error (ok to see why)

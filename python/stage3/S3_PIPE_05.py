# S3_PIPE_05 — Log line pipeline

def parse_line(line: str):
    # Example: "INFO: user=42 action=login"
    try:
        level, rest = line.split(":", 1)
        level = level.strip()
        rest = rest.strip()
    except ValueError:
        return None

    data = {"level": level}

    for part in rest.split():
        if "=" in part:
            k, v = part.split("=", 1)
            data[k] = v

    return data


def is_info(entry):
    return entry is not None and entry.get("level") == "INFO"


def get_user_id(entry):
    try:
        return int(entry.get("user"))
    except Exception:
        return None


def extract_info_user_ids(lines):
    result = []
    for line in lines:
        entry = parse_line(line)
        if not is_info(entry):
            continue
        uid = get_user_id(entry)
        if uid is not None:
            result.append(uid)
    return result


# tests
lines = [
    "INFO: user=42 action=login",
    "WARN: user=10 action=timeout",
    "INFO: user=7 action=logout",
    "INFO: user=xx action=login",
    "BROKEN LINE",
]

print(extract_info_user_ids(lines))  # [42, 7]

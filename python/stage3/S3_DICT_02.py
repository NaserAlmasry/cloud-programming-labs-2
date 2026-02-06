# S3_DICT_02 — Merge defaults (shallow)

def merge_defaults(defaults, overrides):
    # Shallow merge: nested dicts are not merged recursively
    return {**defaults, **overrides}


# tests (show shallow behavior)
defaults = {"debug": False, "db": {"host": "localhost", "port": 5432}}
overrides = {"debug": True, "db": {"host": "prod"}}

merged = merge_defaults(defaults, overrides)

print("defaults:", defaults)
print("overrides:", overrides)
print("merged:", merged)

# Note: merged["db"] is replaced entirely by overrides["db"] (shallow merge).

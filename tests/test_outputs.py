with open("environment/output.txt") as f:
    data = f.read().strip()

assert "hello" in data
assert "world" in data
assert "AI" in data
print("Test passed")


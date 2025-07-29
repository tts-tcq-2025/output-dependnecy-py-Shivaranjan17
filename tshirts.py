def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

# -------------------------
# Existing (weak) tests
# -------------------------
assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')

# -------------------------
# Strengthened test — fails!
# -------------------------
def test_size_edge_case():
    result = size(38)
    expected = 'M'
    assert result == expected, f"Expected size(38) to return '{expected}', but got '{result}'"

# Run the test
test_size_edge_case()

print("All is well (maybe!)")

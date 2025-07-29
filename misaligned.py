
import io
import sys

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')  # Potential misalignment
    return len(major_colors) * len(minor_colors)

# -------------------------
# Strengthened test section
# -------------------------
def test_print_color_map_output():
    # Redirect stdout to capture prints
    captured_output = io.StringIO()
    sys.stdout = captured_output

    result = print_color_map()

    # Restore stdout
    sys.stdout = sys.__stdout__

    output_lines = captured_output.getvalue().strip().split('\n')

    # Test 1: Check total line count
    assert result == 25, f"Expected 25 combinations, got {result}"
    assert len(output_lines) == 25, f"Expected 25 lines, got {len(output_lines)}"

    # Test 2: Check formatting of first line
    # It should follow "0 | White | Blue" format (with proper spacing)
    expected_first_line = "0 | White | Blue"
    assert output_lines[0] == expected_first_line, f"Expected: '{expected_first_line}', Got: '{output_lines[0]}'"

    # Test 3: Check alignment (optional) — for example, make sure each line has 3 segments
    for line in output_lines:
        segments = line.split('|')
        assert len(segments) == 3, f"Line format broken: {line.strip()}"

# Run the test
test_print_color_map_output()

print("All is well (maybe!)")

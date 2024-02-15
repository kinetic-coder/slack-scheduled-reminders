def read_single_line(file_path, line_number):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if line_number <= len(lines):
            return lines[line_number - 1].strip()
        else:
            return None
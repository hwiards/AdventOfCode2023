

def load_input_str(filename : str):
    with open(f"inputs/{filename}.txt", 'r') as file:
        # Read the entire content of the file into a string
        file_contents = file.read()
        return file_contents.strip()

def load_input_lines(filename: str):
    input = load_input_str(filename)
    return input.splitlines()
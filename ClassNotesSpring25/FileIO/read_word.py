import random_word_import_then_output as in_word
from pathlib import Path

current_file_path = Path(__file__)
filename = str(current_file_path.parent) + '\\' + 'words.txt'

random_word = in_word.input_word(filename)
print(f"{random_word=}")
import csv


class Unabbreviator():
    def __init__(self, definition_file=None):
        self.abbreviations_dict = {}
        if definition_file:
            set_definitions(definition_file)

    def set_definitions(self, definition_file):
        with open(definition_file) as f:
            reader = csv.reader(f)
            for row in reader:
                abbreviation = row[1]
                full_word = row[0]
                self.abbreviations_dict[abbreviation] = full_word 

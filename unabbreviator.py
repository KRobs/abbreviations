import csv
import re


class Unabbreviator():
    def __init__(self, definition_file=None):
        self.abbreviations_dict = {}
        if definition_file:
            self.set_definitions(definition_file)

    def set_definitions(self, definition_file):
        with open(definition_file) as f:
            reader = csv.reader(f)
            for row in reader:
                abbreviation = row[1].lower()
                full_word = row[0]
                self.abbreviations_dict[abbreviation] = full_word 

    def unabbreviate(self, input_string):
        input_words = re.split('(\W)', input_string)
        output_words = [self.abbreviations_dict.get(word.lower(), word) for word in input_words]
        output_string = ''.join(output_words) 
        return output_string

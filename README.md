# abbreviations
I have written a class `Unabbreviator` which is initialized a csv of (full-length string, abbreviation) pairs. This is probably the most easily accessible way to extend the abbreviation definitions for business users. This class makes accessible a method called `unabbreviate` which inputs a string possibly containing abbreviations and replaces those abbreviations.

The algorithm chosen is rather simple. The string is split on non-word characters into a list of strings. Each entry in that list is looked up in the abbreviation definitions and replaced, if present. The lowercase form of the abbreviations are compared with the entries in the dictionary to account for possible variations in capitalization. The expanded list of strings is then concatenated together to create the output string.
 
### Sample usage
`>>>from unabbreviator import Unabbreviator`
`>>>my_unabbreviator = Unabbreviator('abbreviation_definitions.csv')`
`>>>my_unabbreviator.unabbreviate('Ms State Univ-Student Affairs')`
`'Mississippi State University-Student Affairs'`

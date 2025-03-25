def get_book_text(filepath):
	with open(filepath, encoding="utf-8", errors="replace") as f:
		file_contents = f.read()
	return file_contents
	
def count_words(string):
	string_split = string.split()
	number_of_words = len(string_split)
	print (f"Found {number_of_words} total words")

def count_characters(string):
	count = {}
	for s in string:
		if s.lower() in count:
			count[s.lower()] += 1
		else:
			count[s.lower()] = 1
	return count

def sort_on(dict):
	return dict["count"]

def sort_dict(dictionary):
	sorted_list_of_dictionary = []
	for char in dictionary:
		char_dict = {"character":char, "count": dictionary[char]}
		sorted_list_of_dictionary.append(char_dict)
	sorted_list_of_dictionary.sort(reverse=True, key=sort_on)
	return sorted_list_of_dictionary



import sys
if len(sys.argv) != 2:
	print ("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import get_book_text, count_words, count_characters, sort_dict

def main():
	print (f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	book = get_book_text(sys.argv[1])
	count_words (book)
	print ("--------- Character Count -------")
	dictionary = count_characters(book)
	sorted_chars = sort_dict(dictionary)
	for char_dict in sorted_chars:
		character = char_dict["character"]
		count = char_dict["count"]
		if character.isalpha():
			print (f"{character}: {count}")
	print ("============= END ===============")
main()
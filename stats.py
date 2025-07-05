def get_book_text(path):
        with open(path) as f:
                return f.read()

def main():
        frankenstein = get_book_text(sys.argv[1])
        print(frankenstein)

def number_of_words(text):
        book = get_book_text(text)
        num_words = 0
        words = book.split()
        for word in words:
                num_words += 1
        return num_words

def character_count(text):
	book = get_book_text(text)
	counter = dict()
	words = book.split()
	for word in words:
		lower_case = word.lower()
		characters = list(lower_case)
		for character in characters:
			counter[character] = counter.get(character, 0) + 1 
	return counter

def sort_on(items):
	return items[1]

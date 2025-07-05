import sys 
from stats import number_of_words
from stats import character_count
from stats import sort_on

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	#y = sys.argv[1]
	#print(y)

	x = number_of_words(sys.argv[1])

	frankenstein_characters = character_count(sys.argv[1])

	fr_chr_lst = list(frankenstein_characters.items())
	fr_alph_lst = list()
	for chr, count in fr_chr_lst:
		if chr.isalpha():
			fr_alph_lst.append((chr, count))
		else: continue
	fr_alph_lst.sort(reverse=True, key=sort_on)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {x} total words")
	print("--------- Character Count -------")
	for chr, count in fr_alph_lst:
		print(f"{chr}: {count}")
	print("============= END ===============")

main()
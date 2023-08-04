# import Modul requests
import requests

# define the function to count words
def count_words(text):
    # split the text in words
    words = text.split()
    #count the words
    return len(words)

# define the function to get websitedata
def count_words_in_webpage(url):
	# try to get websitedata
	try:
		# assign the websitedata to a var
		response = requests.get(url)
		# if successfull 
		if response.status_code == 200:
			# assign the text to a var
			text = response.text
			# count the words
			return count_words(text)
		# if not successful
		else:
			# write error if lib not available
			print("Fehler: Die Seite konnte nicht geladen werden.")
			# return the value 0
			return 0
	# more qualified errormassage from lib
	except requests.exceptions.RequestException as e:
			print("Fehler:", e)
			return 0

# dieses programm kann nicht importiert werden
if __name__ == "__main__":
	# prompt to insert URL
    url = input("Gib die URL der Webseite ein: ")
    # count words
    word_count = count_words_in_webpage(url)
    # write the output
    print("Anzahl der Wörter auf der Webseite:", word_count)
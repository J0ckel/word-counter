    #Funktionsdefinition zähle wörter
def count_words(text):
    # teile den text in worte und speichere in variable
    words = text.split()
    #zähle worte und gebe aus
    return len(words)

# Die folgenden Anweisungen werden nur ausgeführt, wenn dieses Skript direkt ausgeführt wird (nicht wenn es importiert wird).
if __name__ == "__main__":
    #den benutzer auffordern einen text einzugeben und diesen in variable speichern
    input_text = input("Gib den Text ein: ")
    #zähle die wörter und speichere in Variable
    word_count = count_words(input_text)
    #gebe die Anzahl der Wörter aus
    print("Anzahl der Wörter:", word_count)
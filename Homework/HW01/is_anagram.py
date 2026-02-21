from count_letters import count_letters

def is_anagram(word1, word2): 
    """Import count_letters, use it to take a dict that counts each words' letters,
    then compare the 2 words to confirm if they are an anagram """
    if count_letters(word1) == count_letters(word2):
        return True
    return False


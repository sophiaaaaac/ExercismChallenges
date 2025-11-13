"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    pass


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    vocab_words_prefix = [prefix + word for word in vocab_words[1:]]
    return prefix + ' :: ' + ' :: '.join(vocab_words_prefix)
    
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    pass


def remove_suffix_ness(word):
    if word[-5:] == 'iness':
        return word[:-5] + "y"
    else :
        return word [:-4] 

    """check for ness and if i exists ...."""
    
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    pass


def adjective_to_verb(sentence, index):
    sentence_nofs = sentence[:-1]
    sentence_string = sentence_nofs.split()
    return sentence_string[index] + "en"




    
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    pass

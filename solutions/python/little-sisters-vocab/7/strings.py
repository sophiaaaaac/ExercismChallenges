"""Functions for creating, transforming, and adding prefixes to strings."""



def add_prefix_un(word: str) -> str:
    return "un" + word



def make_word_groups(vocab_words: str) -> str:
    prefix = vocab_words[0]
    return prefix +  " :: " +  " :: " .join([prefix + word for word in vocab_words[1:]])
    


def remove_suffix_ness(word) -> str:
    if word[-4:] != "ness":
        return word + " this word is trash"
    if word[-5:] == "iness":
        return word[:-5] + "y"
    return word [:-4] 



def adjective_to_verb(sentence, index) -> str:
    punc = [".", "?", "!"]
    if sentence[-1] in punc:
        sentence_nofs = sentence[:-1]
    else:
        sentence_nofs = sentence
    sentence_string = sentence_nofs.split()
    return sentence_string[index] + "en"
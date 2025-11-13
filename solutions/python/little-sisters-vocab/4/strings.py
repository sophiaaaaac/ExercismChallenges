"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    return "un" + word



def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    vocab_words_prefix = [prefix + word for word in vocab_words[1:]]
    return prefix +  " :: " +  " :: " .join(vocab_words_prefix)
    


def remove_suffix_ness(word):
    if word[-5:] == "iness":
        return word[:-5] + "y"
    else :
        return word [:-4] 


def adjective_to_verb(sentence, index):
    sentence_nofs = sentence[:-1]
    sentence_string = sentence_nofs.split()
    return sentence_string[index] + "en"




import re


def read_file():
    """
    Ask user for file name, open file, remove all punctuation,
    normalize all characters
    """
    user_file = input("Enter File Name: ")

    with open(user_file) as file:
        input_file = re.sub(r'[^A-Za-z ]', '', file.read().lower())
        return input_file.split()


def word_frequency(user_file):
    """
    Create a dict of words and their total count,
    excluding ignored words, from users file.
    """

    words_dict = {}

    for word in user_file:
        # if word in ignored_list:
        #     continue
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    return words_dict


def sort_dict(words_dict):
    """Return a sorted dictionary"""
    return sorted(words_dict.items(), key=lambda x: x[1], reverse=True)


def words_histogram(sorted_dict):
    for key, value in sorted_dict[:21]:
        print('{}: {}'.format(key, value))


if __name__ == '__main__':

    ignored_list = ['a','able','about','across','after','all','almost','also',
                    'am','among','an','and','any','are','as','at','be',
                    'because','been','but','by','can','cannot','could','dear',
                    'did','do','does','either','else','ever','every','for',
                    'from','get','got','had','has','have','he','her','hers',
                    'him','his','how','however','i','if','in','into','is',
                    'it','its','just','least','let','like','likely','may',
                    'me','might','most','must','my','neither','no','nor',
                    'not','of','off','often','on','only','or','other','our',
                    'own','rather','said','say','says','she','should','since',
                    'so','some','than','that','the','their','them','then',
                    'there','these','they','this','tis','to','too','twas',
                    'us','wants','was','we','were','what','when','where',
                    'which','while','who','whom','why','will','with','would',
                    'yet','you','your']

    words_histogram(sort_dict(word_frequency(read_file())))

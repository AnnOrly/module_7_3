class WordsFinder:
    file_names = []

    def __init__(self, *files):
        self.files = files

    def get_all_words(self):
        all_words = {}
        import string
        table = str.maketrans("", "", string.punctuation)

        for file_name in self.files:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    new_line = line.translate(table)
                    words.extend(new_line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                results[file_name] = words.index(word) + 1
            else:
                results[file_name] = None
        return results

    def count(self, word):
        word = word.lower()
        counts = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            counts[file_name] = words.count(word)
        return counts


finder2 = WordsFinder('Mother Goose - Monday’s Child.txt',
                      'Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt')

print(finder2.get_all_words())

print(finder2.find('the'))

print(finder2.count('The'))
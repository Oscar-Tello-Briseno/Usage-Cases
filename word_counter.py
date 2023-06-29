from collections import defaultdict


class WordCounter:
    def __init__(self):
        self.word_count = defaultdict(int)

    def count_words(self, text):
        """Count the frequency of each word in the given text."""
        try:
            if not isinstance(text, str):
                raise ValueError("Text must be a string.")

            words = text.split()
            for word in words:
                self.word_count[word.lower()] += 1
        except Exception as e:
            print("An error occurred while counting words:", str(e))

    def get_word_count(self):
        """Retrieve the word count dictionary."""
        return dict(self.word_count)

    def get_most_common_words(self, n):
        """Retrieve the n most common words and their frequencies."""
        try:
            if not isinstance(n, int) or n <= 0:
                raise ValueError("n must be a positive integer.")

            most_common = sorted(self.word_count.items(), key=lambda x: x[1], reverse=True)[:n]
            return most_common
        except Exception as e:
            print("An error occurred while retrieving most common words:", str(e))


# Example usage
text = "This is a sample text. Sample text is used for testing purposes."
counter = WordCounter()
counter.count_words(text)
word_count = counter.get_word_count()
print("Word Count:", word_count)

most_common_words = counter.get_most_common_words(3)
print("Most Common Words:", most_common_words)

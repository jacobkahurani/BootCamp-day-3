import unittest
def words(s):
    w = s.split()
    a = []
    for i in w:
        a.append((i,w.count(i)))
    b = [i for i in set(a)]
    return dict(b)
    
class TestWordCounts(unittest.TestCase):

    """
        Counts the occurrences or characters in a word
    """

    def test_word_occurance1(self):
        self.assertEqual(words('word'),{'word': 1},msg='should count one word')

    def test_word_occurance2(self):
        self.assertEqual(words("one of each"), {'one': 1, 'of': 1, 'each': 1},msg='should count one of each')

    def test_word_occurance3(self):
        self.assertEqual(words("one fish two fish red fish blue fish"),{'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            msg='should count multiple occurrences')

    def test_word_occurance4(self):
        self.assertEqual(words('car : carpet as java : javascript!!&@$%^&'), {'car': 1,":": 2,'carpet': 1,'as': 1,'java': 1,'javascript!!&@$%^&': 1}, msg='should include punctuation')

    def test_word_occurance5(self):
        self.assertEqual(words('testing 1 2 testing'),{'testing': 2, '1': 1, '2': 1},msg='should include numbers')

    def test_word_occurance6(self):
        self.assertEqual(words('go Go GO'),{'go': 1, 'Go': 1, 'GO': 1},msg='should respect case')

    def test_word_occurance7(self):
        self.assertEqual(words('¡Hola! ¿Qué tal? Привет!'),{"¡Hola!": 1, "¿Qué": 1, "tal?": 1, "Привет!": 1},
            msg='should count international characters properly'
        )

    def test_word_occurance8(self):
        self.assertEqual(words('hello\nworld'),{'hello': 1, 'world': 1},msg='should not count multilines')

    def test_word_occurance9(self):
        self.assertEqual(words('hello\tworld'),{'hello': 1, 'world': 1},msg='should not count tabs')

    def test_word_occurance0(self):
        self.assertEqual(words('hello  world'),{'hello': 1, 'world': 1},msg='should count multiple spaces as one')
if __name__ == '__main__':
    unittest.main()
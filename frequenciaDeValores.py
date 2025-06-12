class WordFrequency:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def count_words(self, text):
        words = text.split()
        for word in words:
            index = self.hash_function(word)
            if self.table[index] is None:
                self.table[index] = []
            found = False
            for i, (k, v) in enumerate(self.table[index]):
                if k == word:
                    self.table[index][i] = (k, v + 1)
                    found = True
            if not found:
                self.table[index].append((word, 1))

    def print_table(self):
        for bucket in self.table:
            if bucket:
                for word, freq in bucket:
                    print(f"{word}: {freq}")


text = ("Espante o Stress. A Casa dos Esportes tem a melhor receita para você arejar a cabeça. "
        "Que tal uma pescaria, caçada ou acampamento? – Tudo em caça, pesca e camping você encontra "
        "na Casa dos Esportes de São Domingos. Barracas, fogareiros, anzóis, redes e tarrafas e "
        "demais apetrechos. Fique longe do Stress. Na hora de relaxar, relaxe com os melhores preços "
        "à vista, as melhores condições a prazo e o atendimento da Casa dos Esportes.")
word_freq = WordFrequency(10)
word_freq.count_words(text)
word_freq.print_table()
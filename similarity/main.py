import fingerprint 
from algo import distance

class Similarity:
    """find similarity between given strings"""

    def __init__(self):
        self.strings = []
        self.fingerprints = []
        self.hashes = []
        self.distances = []
        self.ratios = []

    def generate(self):
        self.get_fingerprints()
        self.get_hashes()
        self.get_distances()
        self.get_ratios()
    def add_strings(self, *args):
        for arg in args:
            self.strings.append(arg)

    def get_fingerprints(self):
        """list of fingerprints for each string"""
        fprint = fingerprint.Fingerprint(kgram_len=4, window_len=5, base=10, modulo=1000)
        fp = fprint.generate

        self.fingerprints = [fp(item) for item in self.strings]

    def get_hashes(self):
        """list of hashes for each string"""
        for item in self.fingerprints:
            hash = []
            for each in item:
                hash.append(each[0])
            self.hashes.append(hash)

    def get_distances(self):
        """get levenshtein distance between fingerprints"""
        self.distances = [[-1 for i in range(len(self.strings))] for j in range(len(self.strings))]
        # calculate levenshtein distance 
        for i, first in enumerate(self.hashes):
            for j, second in enumerate(self.hashes):
                self.distances[i][j] = distance(first, second)

    def get_ratios(self):
        """normalised levenshtein"""
        self.ratios = [[-1 for i in range(len(self.strings))] for j in range(len(self.strings))]
        # identical to nothing in commong [0, 1]
        for i, first in enumerate(self.hashes):
            for j, second in enumerate(self.hashes):
                # forms symmetrix matrix
                self.ratios[i][j] = round(distance(first, second) / max(len(first), len(second)), 2)

import random
from Bio.Seq import Seq

class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return self.sequence


class DNASequence(Sequence):
    pass


class ProteinSequence(Sequence):
    pass

class SequenceStorage:

    _instance = None
    #Use Singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SequenceStorage, cls).__new__(cls)
            cls._instance.data = {}
        return cls._instance

    def save(self, name, seq):
        self.data[name] = seq

    def read(self, name):
        return self.data[name]


class DNASequenceGenerator:
    alphabet = ['A', 'C', 'G', 'T']

    def create_sequence(self, n):
        result = ''
        for i in range(n):
            idx = random.randint(0, 3)
            result += DNASequenceGenerator.alphabet[idx]
        return result


class Translator:

    @staticmethod
    def transcribe_dna_to_rna(dna):
        return dna.replace("T", "U")

    @staticmethod
    def reverse_transcribe_rna_to_dna(rna):
        return rna.replace("U", "T")

    @staticmethod
    def translate_rna_to_protein(rna):
        rna_seq = Seq(rna)
        return str(rna_seq.translate())

    @staticmethod
    def translate_dna_to_protein(dna):
        dna_seq = Seq(dna)
        return str(dna_seq.translate())

class SequenceFactory:

    DNA_ALPHABET = ['A', 'C', 'G', 'T']

    PROTEIN_ALPHABET = [
        'A', 'R', 'N', 'D', 'C',
        'Q', 'E', 'G', 'H', 'I',
        'L', 'K', 'M', 'F', 'P',
        'S', 'T', 'W', 'Y', 'V'
    ]

    @staticmethod
    def create_sequence(length, seq_type="DNA"):

        result = ""

        if seq_type.upper() == "DNA":
            alphabet = SequenceFactory.DNA_ALPHABET

        elif seq_type.upper() == "PROTEIN":
            alphabet = SequenceFactory.PROTEIN_ALPHABET

        else:
            raise ValueError("Unknown sequence type")

        for _ in range(length):
            result += random.choice(alphabet)

        if seq_type.upper() == "DNA":
            return DNASequence(result)

        else:
            return ProteinSequence(result)

if __name__ == '__main__':

    dna_sequence = SequenceFactory.create_sequence(50, "DNA")

    print("Random DNA Sequence:")
    print(dna_sequence)

    cd28 = (
        "ATGCTCAGGCTGCTCTTGGCTCTCAACTTATTCCCTTCAATTCAAGTAACAGGAAACAAGATTTTGGTGA"
        "AGCAGTCGCCCATGCTTGTAGCGTACGACAATGCGGTCAACCTTAGCTGGAAACACCTTTGTCCAAGTCC"
        "CCTATTTCCCGGACCTTCTAAGCCCTTTTGGGTGCTGGTGGTGGTTGGTGGAGTCCTGGCTTGCTATAGC"
        "TTGCTAGTAACAGTGGCCTTTATTATTTTCTGGGTGAGGAGTAAGAGGAGCAGGCTCCTGCACAGTGACT"
        "ACATGAACATGACTCCCCGCCGCCCCGGGCCCACCCGCAAGCATTACCAGCCCTATGCCCCACCACGCGA"
        "CTTCGCAGCCTATCGCTCCTGA"
    )

    rna_sequence = Translator.transcribe_dna_to_rna(cd28)

    print("\nRNA Sequence:")
    print(rna_sequence)

    protein_sequence = Translator.translate_rna_to_protein(rna_sequence)

    print("\nProtein Sequence:")
    print(protein_sequence)

    storage = SequenceStorage()

    storage.save("CD28_DNA", cd28)
    storage.save("CD28_RNA", rna_sequence)
    storage.save("CD28_PROTEIN", protein_sequence)
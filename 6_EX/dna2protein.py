from Bio.Seq import Seq


class Sequence:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class DNASequence(Sequence):
    pass


class ProteinSequence(Sequence):
    pass


class SequenceUtility:
    @staticmethod
    def transcribe_dna_to_rna(dna_sequence):
        return dna_sequence.replace("T", "U")

    @staticmethod
    def translate_rna_to_protein(rna_sequence):
        return str(Seq(rna_sequence).translate())


class SequenceStorage:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = {}
        return cls._instance

    def save(self, name, sequence):
        self.data[name] = sequence

    def read(self, name):
        return self.data[name]


class SequenceFactory:
    @staticmethod
    def create_sequence(sequence, sequence_type):
        if sequence_type.upper() == "DNA":
            return DNASequence(sequence)
        if sequence_type.upper() == "PROTEIN":
            return ProteinSequence(sequence)
        raise ValueError("sequence_type must be DNA or PROTEIN")


if __name__ == "__main__":
    cd28_dna = (
        "ATGCTCAGGCTGCTCTTGGCTCTCAACTTATTCCCTTCAATTCAAGTAACAGGAAACAAGATTTTGGTGA"
        "AGCAGTCGCCCATGCTTGTAGCGTACGACAATGCGGTCAACCTTAGCTGGAAACACCTTTGTCCAAGTCC"
        "CCTATTTCCCGGACCTTCTAAGCCCTTTTGGGTGCTGGTGGTGGTTGGTGGAGTCCTGGCTTGCTATAGC"
        "TTGCTAGTAACAGTGGCCTTTATTATTTTCTGGGTGAGGAGTAAGAGGAGCAGGCTCCTGCACAGTGACT"
        "ACATGAACATGACTCCCCGCCGCCCCGGGCCCACCCGCAAGCATTACCAGCCCTATGCCCCACCACGCGA"
        "CTTCGCAGCCTATCGCTCCTGA"
    )

    dna_sequence = SequenceFactory.create_sequence(cd28_dna, "DNA")
    rna_sequence = SequenceUtility.transcribe_dna_to_rna(dna_sequence.value)
    protein_value = SequenceUtility.translate_rna_to_protein(rna_sequence)
    protein_sequence = SequenceFactory.create_sequence(protein_value, "PROTEIN")

    storage = SequenceStorage()
    storage.save("CD28_DNA", dna_sequence)
    storage.save("CD28_RNA", Sequence(rna_sequence))
    storage.save("CD28_PROTEIN", protein_sequence)

    print("Singleton pattern is used for SequenceStorage.")
    print("CD28 DNA:")
    print(storage.read("CD28_DNA"))
    print("\nCD28 RNA:")
    print(storage.read("CD28_RNA"))
    print("\nCD28 protein:")
    print(storage.read("CD28_PROTEIN"))

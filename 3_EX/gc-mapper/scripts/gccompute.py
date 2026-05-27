
from Bio import SeqIO


def compute_gc_content(fasta_file):
    with open(fasta_file, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            seq = record.seq
            gc_content = 100 * (seq.count("G") + seq.count("C")) / len(seq)
            print(f"{record.id}\n{gc_content:.6f}", "%")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python gccompute.py <fasta_file>")
        sys.exit(1)
    
    fasta_file = sys.argv[1]
    compute_gc_content(fasta_file)



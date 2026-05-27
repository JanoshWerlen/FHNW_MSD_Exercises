import sys
import gzip
import hashlib
from collections import Counter

def md5_of_file(filename):
    md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            md5.update(chunk)
    return md5.hexdigest()


def main(filename):
    total_genes = 0
    human_genes = 0
    gene_types = Counter()

    with gzip.open(filename, "rt", encoding="utf-8", errors="ignore") as f:
        header = f.readline().strip().split("\t")

        # get column indices
        tax_id_idx = header.index("#tax_id")
        type_idx = header.index("type_of_gene")

        for line in f:
            parts = line.strip().split("\t")
            if len(parts) <= type_idx:
                continue

            total_genes += 1

            tax_id = parts[tax_id_idx]
            gene_type = parts[type_idx]

            if tax_id == "9606":   # Homo sapiens
                human_genes += 1

            gene_types[gene_type] += 1

    most_common_type = gene_types.most_common(1)[0][0]

    # OUTPUT (exact format requested)
    print("md5 hash: ", md5_of_file(filename))
    print("total genes", total_genes)
    print("human genes", human_genes)
    print("gene types:", ", ".join(sorted(gene_types.keys())))
    print("most common", most_common_type)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gene.py INPUT_FILE")
        sys.exit(1)

    main(sys.argv[1])
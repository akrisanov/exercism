def distance(strand_a: str, strand_b: str) -> int:
    """Calculate Hamming Distance between two DNAs."""

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    difference = [dna for idx, dna in enumerate(strand_b) if dna != strand_a[idx]]

    return len(difference)

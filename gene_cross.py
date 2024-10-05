def binomial_coefficient(n, k):
    """Calculate the binomial coefficient 'n choose k'."""
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    num = 1
    den = 1
    for i in range(1, k + 1):
        num *= (n - (i - 1))
        den *= i
    return num // den

def calculate_genotype_probabilities(parent1, parent2):
    """Calculate genotype probabilities using the binomial theorem."""
    # Assuming both parents are heterozygous (e.g., Aa x Aa)
    allele1 = parent1[0]  # Assume first allele is dominant
    allele2 = parent1[1]  # Assume second allele is recessive
    allele3 = parent2[0]  # Same for the second parent
    allele4 = parent2[1]

    # Count the total number of alleles
    total_alleles = 2  # Each parent contributes 2 alleles

    # Calculate the probabilities using the binomial theorem
    p_dominant = 0.5  # Probability of getting dominant allele from one parent
    p_recessive = 0.5  # Probability of getting recessive allele from one parent

    # Calculate genotype probabilities
    p_AA = binomial_coefficient(total_alleles, 2) * (p_dominant ** 2) * (p_recessive ** 0)
    p_Aa = binomial_coefficient(total_alleles, 1) * (p_dominant ** 1) * (p_recessive ** 1)
    p_aa = binomial_coefficient(total_alleles, 0) * (p_dominant ** 0) * (p_recessive ** 2)

    return {
        'AA': p_AA,
        'Aa': p_Aa,
        'aa': p_aa
    }

def calculate_ratios(genotype_probabilities):
    """Calculate the ratios of genotypes."""
    total = sum(genotype_probabilities.values())
    genotype_ratios = {genotype: prob / total for genotype, prob in genotype_probabilities.items()}
    return genotype_ratios

def phenotypic_ratio(genotype_ratios):
    """Calculate phenotypic ratios from genotype ratios."""
    dominant_ratio = genotype_ratios.get('AA', 0) + genotype_ratios.get('Aa', 0)
    recessive_ratio = genotype_ratios.get('aa', 0)
    
    return {
        'Dominant': dominant_ratio,
        'Recessive': recessive_ratio
    }

def main(parent1, parent2):
    """Main function to calculate genotype and phenotype ratios."""
    genotype_probabilities = calculate_genotype_probabilities(parent1, parent2)
    genotype_ratios = calculate_ratios(genotype_probabilities)
    phenotype_ratios = phenotypic_ratio(genotype_ratios)
    
    print("Genotype Probabilities:", genotype_probabilities)
    print("Genotype Ratios:", genotype_ratios)
    print("Phenotype Ratios:", phenotype_ratios)

# Example usage
if __name__ == "__main__":
    parent1 = 'Aa'
    parent2 = 'Aa'
    main(parent1,parent2)
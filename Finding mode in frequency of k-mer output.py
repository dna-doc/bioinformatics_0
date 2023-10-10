# Finding mode in frequency of k-mer output
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        # add each key to words whose corresponding frequency value is equal to m
        if key == m :
            words += words.append[key]
       
    return words
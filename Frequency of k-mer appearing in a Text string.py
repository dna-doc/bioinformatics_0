#Frequency of k-mer appearing in a Text string.
# Insert your completed FrequencyMap() function here.
Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 3 

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    # add another for loop here to range over each k-mer Pattern of text and increase freq[Pattern] by 1 each time
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] += 1
    return freq
    print (freq)




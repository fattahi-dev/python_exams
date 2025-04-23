def read_file(filename):
    data = []
    with open(filename, "r") as my_file:
        data = my_file.read().split()
    return data


def find_sequences(N, data):
    word_sequence = []
    for i, word1 in enumerate(data):
        for j, word2 in enumerate(data):
            if i != j and len(word1) == len(word2):
                word_sequence.append(word1,word2)
    return word_sequence
        

def main():
    #word_sequence = read file
    #find the words with same length 
    #print the words with same length
    words = read_file("text.txt")
    #print(words)
    same_length_sequence = find_sequences(2, words)
    print(same_length_sequence)
if __name__ =="__main__":
    main()

import numpy as np

elements=[]
match_score = 1
mismatch_score = -1
gap_penalty = -1


sequence_1 = "TGCTGC"
sequence_2 = "GGCCGG"

sequence_2rvs = sequence_2[::-1]


seq1_list=list(sequence_1)
seq2_list=list(sequence_2rvs)


len_1 = len(sequence_1)
len_2 = len(sequence_2rvs)

array = np.zeros(shape=(len_1 + 1, len_2 + 1))


def p(i, j):
    if sequence_1[i] == sequence_2rvs[j]:
        return match_score
    else:
        return mismatch_score


for i in range(0, len(sequence_1) + 1):
    for j in range(0, len(sequence_2rvs) + 1):
        if i == 0:
            array[0, j] = gap_penalty * j
        elif j == 0:
            array[i, 0] = gap_penalty * i
        else:
            array[i, j] = max(array[i - 1, j - 1] + p(i - 1, j - 1), array[i - 1, j] + gap_penalty,
                              array[i, j - 1] + gap_penalty)

print (array)

for i in range(0,len_1):
    elements.insert(i-1,array[i][i])




if array[1][1]==max(elements):
    print("H beltisth stoixish epikalupshs epitugxanetai me to prothema "+seq1_list[0] +
          " kai to epithema  : "+seq2_list[0]+"")

elif array[2][2]==max(elements):
    print("H beltisth stoixish epikalupshs epitugxanetai me to prothema  "+seq1_list[0]+seq1_list[1]
          + " kai to epithema : "+seq2_list[0]+seq2_list[1]+"")


elif array[3][3]==max(elements):
    print("H beltisth stoixish epikalupshs epitugxanetai me to prothema "+seq1_list[0]+seq1_list[1]+seq1_list[2]
          + " kai to epithema : "+seq2_list[0]+seq2_list[1]+seq2_list[2]+"")


elif array[4][4]==max(elements):
    print("H beltisth stoixish epikalupshs epitugxanetai me to prothema "+seq1_list[0]+seq1_list[1]+seq1_list[2]+seq1_list[3]
          +  " kai to epithema : "+seq2_list[0]+seq2_list[1]+seq2_list[2]+seq2_list[3]+"")


elif array[5][5]==max(elements):
    print("H beltisth stoixish epikalupshs epitugxanetai me to prothema "+seq1_list[0]+seq1_list[1]+seq1_list[2]+seq1_list[3]
          +seq1_list[4]
          + " kai to epithema : "+seq2_list[0]+seq2_list[1]+seq2_list[2]+seq2_list[3]+seq2_list[4]+"")


elif array[6][6]==max(elements):
    print("H beltisth stoixish epikalupshs epitugxanetai me to prothema "+seq1_list[0]+seq1_list[1]+seq1_list[2]+seq1_list[3]
          +seq1_list[4]+seq1_list[5]
          +" kai to epithema : "+seq2_list[0]+seq2_list[1]+seq2_list[2]+seq2_list[3]+seq2_list[4]+seq2_list[5]+"")




seq1 = "TATCCTGCAAGTTACATTCA"
seq2 = "TACGCA"

def fitting_alignment(v,w):

    # Arxikopoihsh pinakwn.
    array = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    backtrack = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]

    # Symplhrwsh pinakwn array kai backtrack.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [array[i-1][j] - 1, array[i][j-1] - 1, array[i-1][j-1] + [-1, 1][v[i-1] == w[j-1]]]
            array[i][j] = max(scores)
            backtrack[i][j] = scores.index(array[i][j])

    # Thesh me to megalytero keli poy antistoixei sto telos tis mikroterhs allhlouxias w
    j = len(w)
    i = max(enumerate([array[row][j] for row in xrange(len(w), len(v))]),key=lambda x: x[1])[0] + len(w)
    max_score = str(array[i][j])

    # Arxikopoihsh eythigrammismenwn allhlouxiwn sthn thesh me to megalitero score.
    v_aligned, w_aligned = v[:i], w[:j]

    # Lambda function gia eisxwrisi kenou '-'.
    insert_gap = lambda word, i: word[:i] + '-' + word[i:]

    # Anatrexoume ton pinaka gia na ksekinisei h stoixisi prosarmoghs.
    # opou 0 = - sthn w (gap)
    # opou 1 = - sthn v (gap)
    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_gap(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_gap(v_aligned, i)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1


    # Stamatame sto teleutaio shmeiou tou backtrack.
    v_aligned = v_aligned[i:]



    return max_score, v_aligned, w_aligned


print '\n'.join(fitting_alignment(seq1,seq2))

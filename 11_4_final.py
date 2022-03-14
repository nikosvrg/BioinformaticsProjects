import numpy as np
import math


class ex11_4:

    def __init__(self, state, init, reset, change, a, g, t, c):
        self.state = state
        self.init = np.exp(init)
        self.reset_state = np.exp(reset)
        self.change_state = np.exp(change)
        self.goA = np.exp(a)
        self.goG = np.exp(g)
        self.goT = np.exp(t)
        self.goC = np.exp(c)

    def  _(self):
        return 'HMM: ' % self.name



Sequence = list('TATGGC')
Seq_len = len(Sequence)

print('\n> Sequence: "%s"' % ''.join(Sequence))


HMM_A = ex11_4(state='A', init=0.5, reset=0.9, change=0.1, a=0.4, g=0.4, t=0.1, c=0.1)
HMM_B = ex11_4(state='B', init=0.5, reset=0.9, change=0.1, a=0.2, g=0.2, t=0.3, c=0.3)





# Arxikopoihsh ton score,me bash tis pithanothtes epiloghs kathe katastashs.

pathA = HMM_A.init
pathB = HMM_B.init
print('Path A: loge(%0.16f) = %0.8f' % (pathA, math.log(pathA)))
print('Path B: loge(%0.16f) = %0.8f' % (pathB, math.log(pathB)))

#krataei to path
path = ['Start']
#Arxikopoiei to kalutero score ws 0 gia thn periptwsh pou dwsoume adeia akolouthia
best_score = 0



#  Gia  na broume to megethos ths akolouthias.
for char in Sequence:

    print('\n> Looking for: %s.' % char)


    if char == 'G':
        pathA = np.exp((math.log(HMM_A.goG) * math.log(pathA)))
        pathB = np.exp((math.log(HMM_B.goG) * math.log(pathB)))

    elif char == 'C':
        pathA = np.exp((math.log(HMM_A.goC) * math.log(pathA)))
        pathB = np.exp((math.log(HMM_B.goC) * math.log(pathB)))

    elif char == 'T':
        pathA = np.exp((math.log(HMM_A.goT) * math.log(pathA)))
        pathB = np.exp((math.log(HMM_B.goT) * math.log(pathB)))

    else:
        pathA = np.exp((math.log(HMM_A.goA) * math.log(pathA)))
        pathB = np.exp((math.log(HMM_B.goA) * math.log(pathB)))

    print('Score A: loge(%0.16f) = (%0.8f).' % (pathA , math.log(pathA)))
    print('Score B: loge(%0.16f) = (%0.8f).' % (pathB , math.log(pathB)))

    best_score = max(pathA, pathB)

    if pathA >= pathB:
        pathB = pathA
        winner = 'A'
        path.append('A')
        #reset
        pathA = np.exp((math.log(HMM_A.reset_state) * math.log(pathA)))
        pathB = np.exp((math.log(HMM_B.change_state) * math.log(pathB)))

    else:
        pathA = pathB
        winner = 'B'
        path.append('B')
        #reset
        pathA = np.exp((math.log(HMM_A.change_state) * math.log(pathA)))
        pathB = np.exp((math.log(HMM_B.reset_state) * math.log(pathB)))

    print('Highest Score: Path %s.' % winner)
    print('Path:  %s.' % ' -> '.join(path))

print('\nBest Path: %s -> End.' % (' -> '.join(path)))
print('Scoring:   loge(%0.16f) = %0.16f.' % (best_score, math.log(best_score)))

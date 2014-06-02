import sys, getopt
import re
import pickle
from sets import Set
from os import listdir
from os.path import isfile, join


class Bayes(object):
    def __init__(self, th=.9):
        self.tokens = {}
        self.pos_count = 0
        self.neg_count = 0

    def _train_token(self, token, pos):
        if token in self.tokens:
            token = self.tokens[token]
        else:
            token = Token(token)
            self.tokens[token] = token
        if pos:
            token.pos_appear += 1
        else:
            token.neg_appear += 1

    def train_on_text(self, words, pos):
        for word in words:
            self._train_token(word, pos)
        if pos:
            self.pos_count += 1
        else:
            self.neg_count += 1

    def _get_p(self, var):
        total = self.pos_count + self.neg_count
        if var == 'pos':
            return self.pos_count / float(total)
        else:
            return self.neg_count / float(total)

    # returns p(s|w)
    # score p(s|w) based on
    # p(s|w) = p(w|s) / p(w|s) + p(w|h)
    # s - spam, w - word, h - ham (non-spam)
    def _score_token(self, tk, klass):
        if tk in self.tokens:
            return self._p_token_given(tk, klass)
        else: # word not seen before
            return 0.5

    # returns most likely klass label
    def classify_text(self, words):
        p_pos = 1
        p_neg = 1
        for word in words:
            p_pos *= self._score_token(word, 'pos')
            p_neg *= self._score_token(word, 'neg')

        # multiply by klass prior
        p_pos *= self._get_p('pos')
        p_neg *= self._get_p('neg')

        if p_pos > p_neg:
            return 'pos'
        else:
            return 'neg'

    def _p_token_given(self, token, klass):
        tk = self.tokens[token]

        # +1 for laplacian smoothing
        if klass == 'pos':
            appear = tk.pos_appear

        if klass == 'neg':
            appear = tk.neg_appear

        count = tk.pos_appear + tk.neg_appear
        return (appear + 1) / float(count)

    def train(self, pos_dir, neg_dir):
        pos_files = [f for f in listdir(pos_dir) if isfile(join(pos_dir, f))]
        for f in pos_files:
            pos_file = open(join(pos_dir, f))
            payload = pos_file.read()
            self.train_on_text(clean_text(payload), True)

        neg_files = [f for f in listdir(neg_dir) if isfile(join(neg_dir, f))]
        for f in neg_files:
            neg_file = open(join(neg_dir, f))
            payload = neg_file.read()
            self.train_on_text(clean_text(payload), False)
    


class Token(object):
    def __init__(self, tk):
        self.token = tk
        # Laplace estimation
        self.pos_appear = 1
        self.neg_appear = 1

    def __hash__(self):
        return hash(self.token)

    def __eq__(self, other):
        return self.token == other


def clean_text(text):
    regex = re.compile('<.*>|[^a-zA-Z0-9_\s]|http://.*')
    return Set(regex.sub('', text).lower().split())

if __name__ == '__main__':

    mode = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hm:p:n:", ["mode=", "posdir=", "negdir="])
    except getopt.GetoptError:
        print 'bayes.py -p <posdir> -n <negdir>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'bayes.py -m <mode> -p <posdir> -n <negdir>'
            sys.exit()
        elif opt in ("-m", "--mode"):
            mode = arg
        elif opt in ("-p", "--posdir"):
            pos_dir = arg
        elif opt in ("-n", "--negdir"):
            neg_dir = arg

    b = Bayes()

    if not mode:
        print 'bayes.py -m <mode> -p <posdir> -n <negdir>'
        sys.exit()

    if mode == "train":
        b.train(pos_dir, neg_dir)



        # print 'is pos w/ probability', b.classify_text(clean_text("I do not love this great movie"))
        # print 'is pos w/ probability', b.classify_text(clean_text("this is a really bad movie"))

import string

class Solution:
    def ladder_length(self, begin_word, end_word, words):
        words = set(words)
        if end_word not in words:
            return 0

        bs = {begin_word}
        es = {end_word}
        dis = 1

        while bs:
            # после первого прохода в bs будет список слов, который отличается от begin_word на одну букву
            # каждый раз мы вычитаем, потому что нам не нужны эти слова при повторной проверке (мы их уже нашли)
            words -= bs
            dis += 1
            ns = set()
            for w in bs:
                for i in range(len(w)):
                    pre = w[:i]
                    post = w[i+1:]
                    for c in string.ascii_lowercase:
                        nw = pre + c + post
                        if nw in words:
                            if nw in es:
                                return dis
                            ns.add(nw)
            bs = ns  # после первого прохода уходит begin_word, и сохраняем слова, которые нашли при первом проходе
            if len(bs) > len(es):  # меняем местами, чтобы сократить кол-во проходов в цикле. Мы как бы идем навстречу
                bs, es = es, bs
        return 0
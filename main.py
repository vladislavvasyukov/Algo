from graph import GraphForBFS


def build_graph(word_file):
    d = {}
    g = GraphForBFS()
    with open(word_file, 'r') as f:
        for line in f:
            word = line[:-1]

            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]

                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.add_edge(word1, word2)
        return g


if __name__ == '__main__':
    g = build_graph('words_file.txt')
    g.bfs(g.get_vertex('foul'))
    g.traverse(g.get_vertex('sale'))

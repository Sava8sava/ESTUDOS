import time
from wordt import _Filter
from TScomListTuple import ListTs
from collections import defaultdict, OrderedDict,Counter


class TSS:
    def __init__(self):
        self.words = _Filter()

        print("ADICIONAR PALAVRAS:\n")
        # dict
        self.test_dict, self.timrdict = self.with_dict()
        print(f"Dicionario:QUANTIDADE DE PALAVRAS:{len(self.test_dict)},TEMPO DE INSERÇÃO:{self.timrdict:.6f} segundos")

        # lista mais tupla
        self._list = ListTs()
        self.timlist = self.with_list()
        print(f"Listas+tuplas:QUANTIDADE DE PALAVRAS:{len(self._list)},TEMPO DE INSERÇÃO:{self.timlist:.6f} segundos")

        # OrderedDict
        self.orddict, self.timOdict = self.with_Ord_list()
        print(f"Dicionarios ordenados:QUANTIDADE DE PALAVRAS:{len(self.orddict)},TEMPO DE INSERÇÃO:{self.timOdict:.6f} segundos")

        # defaultdict
        self.dfdict, self.timDdict = self.with_dflt_list()
        print(f"Dicionarios Default:QUANTIDADE DE PALAVRAS:{len(self.dfdict)},TEMPO DE INSERÇÃO:{self.timDdict:.6f} segundos")

        #counter
        self.counter, self.timCounter = self.with_counter()
        print(f"Counter: QUANTIDADE DE PALAVRAS: {len(self.counter)}, TEMPO DE INSERÇÃO: {self.timCounter:.6f} segundos\n")

        print("CHECAR PALAVRAS NA ESTRUTURAS\n")
        # palavras para checar
        words_to_chk = ["Lisbon", "NASA", "Kyunghee", "Konkuk,", 'Sogang', 'momentarily', "rubella", 'vaccinations', 'government', 'Authorities']
        teste, time0 = self.check_words(self.test_dict, words_to_chk)
        teste2, time1 = self.check_words(self._list, words_to_chk)
        teste3, time2 = self.check_words(self.orddict, words_to_chk)
        teste4, time3 = self.check_words(self.dfdict, words_to_chk)
        teste5, time4 = self.check_words(self.counter, words_to_chk)

        print(f" dict:{teste}, tempo:{time0:.6f} segundos")
        print(f" list:{teste2}, tempo:{time1:.6f} segundos")
        print(f" ord dict:{teste3}, tempo:{time2:.6f} segundos")
        print(f" default dict:{teste4}, tempo:{time3:.6f} segundos")
        print(f" counter: {teste5}, tempo: {time4:.6f} segundos\n")


        #remover palavras 
        print("REMOVER PALAVRAS\n")
        rmv0,rmv_time0 = self.removes_words(self.test_dict,words_to_chk)
        rmv1,rmv_time1 = self.removes_words(self._list,words_to_chk)
        rmv2,rmv_time2 = self.removes_words(self.orddict,words_to_chk)
        rmv3,rmv_time3 = self.removes_words(self.dfdict,words_to_chk) 
        rmv4, rmv_time4 = self.removes_words(self.counter, words_to_chk)

        print(f'dict:{rmv0}, tempo:{rmv_time0:.6f} segundos')
        print(f'list:{rmv1}, tempo:{rmv_time1:.6f} segundos')
        print(f'ord dict:{rmv2}, tempo:{rmv_time2:.6f} segundos')
        print(f'default dict:{rmv3}, tempo:{rmv_time3:.6f} segundos')
        print(f'counter: {rmv4}, tempo: {rmv_time4:.6f} segundos\n')

    def with_dict(self):
        exdict = {}
        start = time.perf_counter()
        for word in self.words.words_list:
            exdict[word] = 1
        end = time.perf_counter()
        return exdict, (end - start)

    def with_list(self):
        start = time.perf_counter()
        for word in self.words.words_list:
            self._list.inserir(word, 1)
        end = time.perf_counter()
        return (end - start)

    def with_Ord_list(self):
        aux = OrderedDict()
        start = time.perf_counter()
        for word in self.words.words_list:
            aux[word] = 1
        end = time.perf_counter()
        return aux, (end - start)

    def with_dflt_list(self):
        aux = defaultdict(int)
        start = time.perf_counter()
        for word in self.words.words_list:
            aux[word] = 1
        end = time.perf_counter()
        return aux, (end - start)
    
    def with_counter(self):
        aux = Counter()
        start = time.perf_counter()
        for word in self.words.words_list:
            aux[word] += 1
        end = time.perf_counter()
        return aux, (end - start)

    def check_words(self, struct, words):
        if isinstance(struct, (dict, OrderedDict, defaultdict,Counter)):
            check_func = lambda word: word in struct
        elif isinstance(struct, ListTs):
            check_func = struct.existe
        else:
            raise TypeError("Erro")

        start = time.perf_counter()

        result = {word: check_func(word) for word in words}

        end = time.perf_counter()

        result_time = end - start
        
        return result, result_time

    def removes_words(self,struct,words):
        if isinstance(struct,(dict,OrderedDict,defaultdict,Counter)):
            remove_func = lambda word : struct.pop(word,None)
        elif isinstance(struct,ListTs):
            remove_func = struct.remover
        else:
            raise TypeError("erro")

        start = time.perf_counter()

        removed = {}
        for word in words:
            result = remove_func(word)
            removed[word] = result is not None #true para palavras removidas
        
        end = time.perf_counter()

        result_time = end-start

        return removed,result_time


TSS()

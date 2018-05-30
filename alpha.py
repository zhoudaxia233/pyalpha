import itertools
import copy

class Alpha():
    def __init__(self, log):
        self.log = set(log)
        self.tl = self.get_TL_set()
        self.ds = self.direct_succession()
        self.cs = self.causality(self.ds)
        self.pr = self.parallel(self.ds)
        self.ind = self.choice(self.tl, self.cs, self.pr)
        self.ti = self.get_TI_set()
        self.to = self.get_TO_set()
        self.xl = self.get_XL_set(self.tl, self.ind, self.cs)
        self.yl = self.get_YL_set(self.xl)
    
    def __str__(self):
        alpha_sets = []
        alpha_sets.append("TI set: {}".format(self.ti))
        alpha_sets.append("TO set: {}".format(self.to))
        alpha_sets.append("XL set: {}".format(self.xl))
        alpha_sets.append("YL set: {}".format(self.yl))
        return '\n'.join(alpha_sets)

    def get_TL_set(self):
        tl = set()
        for item in self.log:
            for i in item:
                tl.add(i)
        return tl
    
    def get_TI_set(self):
        ti = set()
        for item in self.log:
            ti.add(item[0])
        return ti

    def get_TO_set(self):
        to = set()
        for item in self.log:
            to.add(item[-1])
        return to
    
    def get_XL_set(self, tl, ind, cs):
        xl = set()
        subsets = itertools.chain.from_iterable(itertools.combinations(tl, r) for r in range(1, len(tl) + 1))
        independent_a_or_b = [a_or_b for a_or_b in subsets if self.__in_ind_set(a_or_b, ind)]
        for (a, b) in itertools.product(independent_a_or_b, independent_a_or_b):
            if (a, b) in cs:
                xl.add((a, b))
        return xl

    def __in_ind_set(self, s, ind):
        if len(s) == 1:
            return True
        else:
            s_all = itertools.combinations(s, 2)
            for pair in s_all:
                if pair not in ind:
                    return False
            return True
    
    def get_YL_set(self, xl):
        yl = copy.deepcopy(xl)
        s_all = itertools.combinations(yl, 2)
        for pair in s_all:
            if self.__issubset(pair[0], pair[1]):
                yl.discard(pair[0])
            elif self.__issubset(pair[1], pair[0]):
                yl.discard(pair[1])
        return yl
    
    def __issubset(self, a, b):
        if set(a[0]).issubset(b[0]) and set(a[1]).issubset(b[1]):
            return True
        return False
    
    def get_PL_set(self):
        pass
    
    def get_FL_set(self):
        pass
    
    def get_footprint(self):
        footprint = []
        footprint.append("All transitions: {}".format(self.tl))
        footprint.append("Direct succession: {}".format(self.ds))
        footprint.append("Causality: {}".format(self.cs))
        footprint.append("Parallel: {}".format(self.pr))
        footprint.append("Choice: {}".format(self.ind))
        return '\n'.join(footprint)
    
    def direct_succession(self):
        # x > y
        ds = set()
        for trace in self.log:
            for x, y in zip(trace, trace[1:]):
                ds.add((x, y))
        return ds
    
    def causality(self, ds):
        # x -> y
        cs = set()
        for pair in ds:
            if pair[::-1] not in ds:
                cs.add(pair)
        return cs

    
    def parallel(self, ds):
        # (x || y) & (y || x)
        pr = set()
        for pair in ds:
            if pair[::-1] in ds:
                pr.add(pair)
        return pr
    
    def choice(self, tl, cs, pr):
        # (x # y) & (y # x)
        ind = set()
        all_permutations = itertools.permutations(tl, 2)
        for pair in all_permutations:
            if pair not in cs and pair[::-1] not in cs and pair not in pr:
                ind.add(pair)
        return ind

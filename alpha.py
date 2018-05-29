import itertools
import copy

class Alpha():
    def __init__(self, log):
        self.log = set(log)
    
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
    
    def get_XL_set(self, tl, choice, cs):
        xl = set()
        subsets = itertools.chain.from_iterable(itertools.combinations(tl, r) for r in range(1, len(tl) + 1))
        independent_a_or_b = [a_or_b for a_or_b in subsets if self.in_choice_set(a_or_b, choice)]
        for (a, b) in itertools.product(independent_a_or_b, independent_a_or_b):
            if (a, b) in cs:
                xl.add((a, b))
        return xl

    def in_choice_set(self, s, choice):
        if len(s) == 1:
            return True
        else:
            # 现在要判断，s这个集合的元素是否两两互斥，也就是，s的大小为2的子集们是否都在choice里面，
            # 如果有一个不在，那就返回False
            s_all = itertools.combinations(s, 2)
            for pair in s_all:
                if pair not in choice:
                    return False
            return True
    
    def get_YL_set(self, xl):
        yl = copy.deepcopy(xl)
        s_all = itertools.combinations(yl, 2)
        for pair in s_all:
            if self.issubset(pair[0], pair[1]):
                yl.discard(pair[0])
            elif self.issubset(pair[1], pair[0]):
                yl.discard(pair[1])
        return yl
    
    def issubset(self, a, b):
        if set(a[0]).issubset(b[0]) and set(a[1]).issubset(b[1]):
            return True
        return False
    
    def get_PL_set(self):
        pass
    
    def get_FL_set(self):
        pass
    
    def get_footprint(self):
        pass
    
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
    
    def choice(self, tl, cs):
        # (x # y) & (y # x)
        choice = set()
        all_permutations = itertools.permutations(tl, 2)
        for pair in all_permutations:
            if pair not in cs and pair[::-1] not in cs:
                choice.add(pair)
        return choice

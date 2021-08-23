class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pars = []
        for c in s:
            npars = []
            collapse = False
            for par in pars:
                if collapse:
                    npars[-1][0] |= par[0]
                    npars[-1][1] += par[1]
                else:
                    npars.append(par)
                    if c in par[0]:
                        collapse = True
            if collapse:
                npars[-1][0].add(c)
                npars[-1][1] += 1
            else:
                npars.append([set(c), 1])
            pars = npars
        return [count for _, count in pars]
                    
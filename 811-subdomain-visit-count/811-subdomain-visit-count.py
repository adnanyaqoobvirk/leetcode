class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        for cpd in cpdomains:
            count, domain = cpd.split(' ')
            count = int(count)
            subd = ""
            for part in reversed(domain.split('.')):
                subd = f"{part}{'.' if subd else ''}{subd}"
                counts[subd] = counts.get(subd, 0) + count
        return [f"{v} {k}" for k, v in counts.items()]
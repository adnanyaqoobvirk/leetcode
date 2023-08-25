# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        res = []
        host = f"http://{startUrl.split('/')[2]}"
        q = [startUrl]
        visited = {startUrl}
        while q:
            nq = []
            for url in q:
                res.append(url)
                
                for childUrl in htmlParser.getUrls(url):
                    if childUrl.startswith(host) and childUrl not in visited:
                        nq.append(childUrl)
                        visited.add(childUrl)
            q = nq
        return res
import feedparser
import re

#returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
    d = feedparser.parse(url)
    wc = {}

    try:
        if d.feed.summary:
            words = getwords(d.feed.summary)
            for word in words:
                wc.setdefault(word, 0)
                wc[word] += 1
    except:
        print "no summary for url: %s" % url

    try:
        return d.href, wc
    except: 
        print "no href for url: %s" % url

def getwords(html):
    txt = re.compile(r'<[^>]+>').sub('',html)

    words = re.compile(r'[^A-Z^a-z]{2,}').split(txt)
    
    return [word.lower() for word in words if word != '']

def getsites():
    apcount = {}
    wordcounts = {}
    feedlist = [line for line in file('feedlistUnique.txt')]
    for x in feedlist:
        url, wc=getwordcounts(x)
        wordcounts[url] = wc
        for word,count in wc.items():
            apcount.setdefault(word,0)
            if count > 1:
                apcount[word] += 1

    wordlist=[]
    for w,bc in apcount.items():
        frac = float(bc)/len(feedlist)
        if frac>0.1 and frac < 0.6: wordlist.append(w)

    out = file('words.txt', 'w')
    out.write('Site')
    for word in wordlist: out.write('\t%s' % word)
    out.write('\n')
    for site,wc in wordcounts.items():
        out.write(site)
        for word in wordlist: 
            if word in wc: out.write('\t%d' % wc[word])
            else: out.write('\t0')
        out.write('\n')


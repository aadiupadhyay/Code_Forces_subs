'''
Aaditya Upadhyay 
                             ..........  .uoeeWWeeeu.
                      .:::::::::::::::::: "?$$$$$$$$$$c
                    ```....:::::::::::::::::`"$$$$$$$$$$e.
               ..:::::::::::```.::::::::::::::.`"??$$$$$$b
           ::::::::::::::` .:::::::` ::::::`` :::::::  `"?$
        .:::::::::::::``.::::::::` .:::`` ::::::::::::::::.
       :::::`.:::::::  ::::::::`  ::` . `:::::::::::::::::::.
     ::::` ::::::::`` :::::::`   .ue@$$ `:::::::::::::::::::::
     ::` .:::::::``z, :::::`.e$$$$$$$$$$.`::::::::::::::::::::
    :` :::::::``,e$$r`::: $$$$??'     `?b_ `::::::::::::::::::
   ' :::::::` ,?'   `?b,_` R$'     .,,.   `"iu ````:::::::::::::
    ::::::`   <  .,.   `?e. $eeee$$F???ee,3c   ..````::::::::.
   ::::::  ::  R$$$$$$$e4$ $$$$$$$"e     3$$$$$.:.  ``:::::::::``:.
  `:::::: :::::`F.   "?FJd$$$$$$'L~. . .$$$$L`!!~eec``::::::::.
  `::::::.```::.""$'     $$$$$$$$$.$bKUeiz$$$$$$'!~ $$  `::::::::
     ``````` ..: 3`beeed $$$$$$$$$e$Ned$$$$$$$$'u@z$ ::: `:::::::
             ::: ^NeeeP $$$$$$$$$$$$$$$$$$$$$$$$"NNeP ::::::`::::::
            .:::: $$$$F $$$$$$$?$$$$$$$$$$$$$$$$ $F .:::::::::::::
           : .::: ?$$$$$ $$$$$$$?c$$$$$$$$$$$$$F,e :::::::::::::``
             ::::,`$$$$$$,)?$X$$$$$$$$$$$?$$$$$ $$ :::::::::::``
             ::':: "$$$$$$$$$$$$$$$P?" .d$$$$F,$$ :::::::::`
             `  :::."$$EC""???"?Cz=d"ud$$$$$$".$$$ :::::`:`
                `:::.`?$$bu. 4$$$??Le$$$$$P".$$$$ ::```
                  `::: `?$$Pbeee$$$$$$$P".d$$$$$
                   `:`   `?$eJCCCNd$$$$F.z$$$$$$$ u.
                          u`?$$$$$$$$$F z$$$$$$$Pu`$$c.
                         c^bu?R$$$F"ue$$$$$$$$$$ $ $$$$$bc.
                       e$$ $$e,`"",e$$$$$$$$$$$$$$$ $$$$$$$$$"bc.
                    .e$$$$ '$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$'d$$$$be.
                ..e$$$$$EJ,?$$$$$$$$$$$$$$$$$$$$$$$'$$$$$$$"d$$$$$$$$$be

'''
from sys import stdin, stdout
from collections import *
from math import gcd, floor, ceil
def st(): return list(stdin.readline().strip())


def li(): return list(map(int, stdin.readline().split()))
def mp(): return map(int, stdin.readline().split())
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n)+"\n")


mod = 1000000007
INF = float('inf')


def solve():
    def F(l):
        x = []
        for i in range(0, len(l)-1, 2):
            if l[i] > l[i+1]:
                x.append(l[i])
            else:
                x.append(l[i+1])
        l = x
        return l
    n = inp()
    l = li()
    x = list(l)
    while len(x) > 2:
        x = F(x)
    pr(l.index(min(x))+1)


for _ in range(1):
    solve()
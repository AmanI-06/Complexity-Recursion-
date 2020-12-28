def drawline(l,lab=''):
    line='-'*l
    if lab:
        line+=' '+lab
    print(line)
def interval(dist):
    if dist>0:
        drawline(dist-1)
        drawline(dist)
        drawline(dist-1)
def ruler(inches,maxtickl):
    drawline(maxtickl,'0')
    for i in range(1,inches+1):
        interval(maxtickl-1)
        drawline(maxtickl,str(i))

a=ruler(5,5)

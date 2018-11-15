# -*- coding:utf-8 -*-

cty = []
medals = {'1': 'gold', '2': 'silver', '3': 'copper'}


class Country:
    def __init__(self, n, g, s, c):
        self.name = n
        self.gold = g
        self.silver = s
        self.copper = c

    def __str__(self):
        return 'gold %d,silver %d,copper %d,sum %d' % (self.gold, self.silver, self.copper, self.count())

    def count(self):
        return self.gold+self.silver+self.copper

    def get_place(self):
        n = input('gold?silver?copper?(1/2/3):')
        setattr(self, medals[n], (getattr(self, medals[n])+1))


def newc():
    n = input('country name:')
    g = int(input('gold medal:'))
    s = int(input('silver medal:'))
    c = int(input('copper medal:'))
    global cty
    cty.append(Country(n, g, s, c))


def gp():
    n = input('country name:')
    for i in cty:
        if i.name == n:
            i.get_place()


def toplist(n):
    l = sorted(cty, key=lambda x: getattr(x, medals[n]), reverse=True)
    print('%s list:\n' % medals[n])
    p = 0
    for i in l:
        p += 1
        print('%d:%s has %s:%d' % (p, i.name, medals[n], getattr(i, medals[n])))


while True:
    s = input('select？ 1:add country,2:enter country,3:toplist,4:exit')
    if s == '1':
        newc()
        continue
    if s == '2':
        c = input('country name:')
        while True:
            o = input('select operate 1:getplace,2:view info,3:back')
            if o == '1':
                for i in cty:
                    if i.name == c:
                        i.get_place()
                continue
            if o == '2':
                for i in cty:
                    if i.name == c:
                        print(i)
                continue
            else:
                break
        continue
    if s == '3':
        m = input('select medal type,gold?silver?copper?(1/2/3):')
        toplist(m)
        continue
    else:
        break




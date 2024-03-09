import sys

data = """1967 DavidBowie
1969 SpaceOddity
1970 TheManWhoSoldTheWorld
1971 HunkyDory
1972 TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars
1973 AladdinSane
1973 PinUps
1974 DiamondDogs
1975 YoungAmericans
1976 StationToStation
1977 Low
1977 Heroes
1979 Lodger
1980 ScaryMonstersAndSuperCreeps
1983 LetsDance
1984 Tonight
1987 NeverLetMeDown
1993 BlackTieWhiteNoise
1995 1.Outside
1997 Earthling
1999 Hours
2002 Heathen
2003 Reality
2013 TheNextDay
2016 BlackStar"""
data = [d.split() for d in data.split('\n')]

n = int(sys.stdin.readline())
for i in range(n):
    s, e = sys.stdin.readline().split()
    list_searched = [d for d in data if int(s) <= int(d[0]) <= int(e)]
    cnt = len(list_searched)
    print(cnt)
    if cnt > 0:
        print("\n".join(f"{d[0]} {d[1]}" for d in list_searched))
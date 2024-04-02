class Extractor: # iterator
    def __init__(self, parent):
        self._collection_owner = parent
        self._k = 0
    def __next__(self):
        j = self._k // 2
        if self._k % 2 == 0: # гравець A
            if j >= len(self._collection_owner._lstA):
                raise StopIteration
            res = self._collection_owner._lstA[j]
        else:  # self._k % 2 == 1 -- гравець B
            if j >= len(self._collection_owner._lstB):
                raise StopIteration
            res = self._collection_owner._lstB[j]
        #
        self._k += 1
        return res

class MyClass: # iteratable
    def __init__(self, lstA, lstB):
        self._lstA = lstA
        self._lstB = lstB
    def __iter__(self):
        itr = Extractor(self) # self - об'єкт класу MyClass, в якому обидва списки вже містяться
        return itr

if __name__ == "__main__":
    movesA = ['Nf3 Nf6', 'Nc3 Bg7', 'Bf4 d5']  # 7. Qxc4 c6 8. e4 Nbd7 9. Rd1 Nb6 10. Qc5 Bg4 11. Bg5 Na4 12. Qa3 Nxc3 13. bxc3 Nxe4 14. Bxe7 Qb6 15. Bc4 Nxc3 16. Bc5 Rfe8+ 17. Kf1 Be6 18. Bxb6 Bxc4+ 19. Kg1 Ne2+ 20. Kf1 Nxd4+ 21. Kg1 Ne2+ 22. Kf1 Nc3+ 23. Kg1 axb6 24. Qb4 Ra4 25. Qxb6 Nxd1 26. h3 Rxa2 27. Kh2 Nxf2 28. Re1 Rxe1 29. Qd8+ Bf8 30. Nxe1 Bd5 31. Nf3 Ne4 32. Qb8 b5 33. h4 h5 34. Ne5 Kg7 35. Kg1 Bc5+ 36. Kf1 Ng3+ 37. Ke1 Bb4+ 38. Kd1 Bb3+ 39. Kc1 Ne2+ 40. Kb1 Nc3+ 41. Kc1 Rc2# 0-1
    movesB = ['c4 g6', 'd4 O-O', 'Qb3 dxc4']
    obj = MyClass(movesA, movesB)

    for m in obj:
        print(m)
# очікуваний результат:
# Nf3 Nf6
# c4 g6
# Nc3 Bg7
# d4 O-O
# Bf4 d5
# Qb3 dxc4
# ...
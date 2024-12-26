class Postprocessing:
    def __init__(self):
        pass

    def inspect_solution(self):
        """wyświetla ostateczne wyniki"""
        print("\nprzemieszczenia")
        for num, disp in enumerate(self.node_disp.reshape(len(self.node_disp) // 3, 3)):
            print('węzeł numer ', num, ":", end="")
            print(['{0:<8}'.format(round(tmp, 8)) for tmp in disp])
        print('\nreakcje')
        for num, reac in enumerate(self.react.reshape(len(self.react) // 3, 3)):
            print('węzeł numer ', num, ":", end="")
            print(['{0:<8}'.format(round(tmp, 2)) for tmp in reac])

    def inspect_important(self):
        """Wyświetla kluczowe dane obliczeniowe

        wyświetla zawartość następujących zmiennych
            self.n_loc_element
            self.b
        """
        print('\nWspółczynniki wielomianów funkcji kształtu')
        for e in self.n_loc_element:
            print(e, '\n')
        print('\n\nWspółczynniki macierzy pochodnych')
        for e in self.b:
            print(e, '\n')
        print('\n\nmacierze sztywności elementów globalne')
        for e in self.k_e_glob:
            print('\n')
            for row in e:
                print(['{0:<8}'.format(round(tmp, 2)) for tmp in row])
        print('\n\n', 'Globalna macierz sztywności')
        for row in self.k:
            print(['{0:<8}'.format(round(tmp, 2)) for tmp in row])
            # print([round(mx,2) for mx in row])

    def inspect_element(self, num):
        """wyświetla dane dla zadanego elementu
        """
        print('Numer elementu', ' : ', num)
        print('\n\n', 'Właściwości zadane')
        print(self.elements[num], '\n')
        print('współrzędne końców w ukłądzie globalnym')
        print(self.node_glob[num], '\n')
        print('współrzędne końców w ukłądzie lokalnym')
        print(self.elem_loc[num], '\n')
        print('długość elementu')
        print(self.elem_length[num], '\n')
        print('współczynniki funkcji kształtu')
        print(self.n_loc_element[num], '\n')
        print('współczynniki pochodnej funkcji kształtu')
        print(self.b[num], '\n')
        print('macierz stywności w układzie lokalnym dla jednego stopnia swobody')
        print(self.k_e_loc[num], '\n')
        print('macierz stywności w układzie globalnym')
        print(self.k_e_glob[num], '\n')
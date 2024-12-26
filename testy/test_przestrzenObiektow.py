from Krzykacz import przestrzen_obiektow
import pytest
from Krzykacz import smutne_funkcje


def setup():
    global przestrzen
    przestrzen = przestrzen_obiektow.PrzestrzenObiektow()
    przestrzen.dodawanie_do_przestrzeni(None, 'a',
                                        magnet_points={'konce': [(10, 10), (300, 700)], 'srodki': [(110, 1000)]})
    przestrzen.dodawanie_do_przestrzeni(None, 'b', magnet_points={'konce': [(200, 10), (89, 90), (90, 89)],
                                                                  'srodki': [(110, 110)]})


#
#
# # obsługa przestrzeni
#
# def test_sort_priority_list():
#     good_li = [[0, 1], [4, 4], [5, 3]]
#     len_li = [[0, 1], [4, 4], [5, 3, 1]]
#     type_li = [[0, 1], [4, 4], [5, 'm']]
#     type_li1 = ['se', [0, 1], [4, 4], [5, 'm']]
#     val = sort_priority_list(good_li)
#     assert val == [[4, 4, 1], [5, 3, 2]]
#     with pytest.raises(przestrzen_obiektow.WrongLenghtException):
#         assert sort_priority_list(len_li)
#     with pytest.raises(TypeError):
#         assert sort_priority_list(type_li)
#     with pytest.raises(TypeError):
#         assert sort_priority_list(type_li1)


@pytest.mark.parametrize('non, tags', [['a', ('a', 'b')], ['b', 'loki'], ['b', ('a', 'b')]])
def test_add_tags(non, tags):
    przestrzen.add_tags(non, *tags)
    real = 1
    for tg in tags:
        if tg not in przestrzen.get_free_kwd(non, 'tagi'):
            real = 0
            break
    assert real == True


@pytest.mark.parametrize('non, tags', [[5, ('a', 'b')], [None, 'loki'], ['c', ('a', 'b')], ['b', (5, 'b')]])
def test_fail_add_tags(non, tags):
    with pytest.raises((TypeError, KeyError, IndexError)):
        przestrzen.add_tags(non, *tags)


def adding():
    params = [['a', ('a', 'b')], ['a', 'loki'], ['b', ('a', 'b')]]
    for elem in params:
        x, y = elem.pop(0), *elem
        przestrzen.add_tags(x, x+'d', 'type')
        przestrzen.add_tags(x, *y)


@pytest.mark.parametrize('non, tags', [['a', ('a', 'b')], ['a', 'loki'], ['b', ('a', 'b')]])
def test_del_tags(non, tags):
    adding()
    przestrzen.del_tags(non, *tags)
    real = 1
    for tg in tags:
        if tg in przestrzen.get_free_kwd(non, 'tagi'):
            real = 0
            break
    assert real == True


@pytest.mark.parametrize('non, tags', [[0, ('a')], [None, 'loki'], ['c', ('a', 'b')], ['b', (5, 'b')]])
def test_fail_del_tags(non, tags):
    with pytest.raises((TypeError, KeyError, IndexError)):
        przestrzen.del_tags(non, *tags)

def test_przyciaganie():
    przestrzen.zakres = 30
    assert smutne_funkcje.przyciaganie(20, 20, przestrzen) == (10, 10)
    assert smutne_funkcje.przyciaganie(100, 100, przestrzen) == (110, 110)
    with pytest.raises(TypeError):
        assert smutne_funkcje.przyciaganie(20, None, przestrzen)
    with pytest.raises(TypeError):
        assert smutne_funkcje.przyciaganie(20, 'coś', przestrzen)
    assert smutne_funkcje.przyciaganie(-10, 0, przestrzen) == (10, 10)


import pytest
from Krzykacz import generator_nazw

generator=None

def setup_module():
    global generator
    generator=generator_nazw.Generator()



@pytest.mark.parametrize('name, expected',[('linia','linia1'),('linia','linia2'),('kwadrat','kwadrat1'),
                        ('kwadrat','kwadrat2'),('linia','linia3'),('kwadrat','kwadrat3')])
def test_1(name, expected):
    global generator
    real=generator.nazwa(name)
    generator.inspect()
    assert real==expected


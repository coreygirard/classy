from src.main import *


def test_basic_classify():
    data = {
        "Class A": ["a b c", "a c e", "b a c", "e d f"],
        "Class B": ["e f g", "e y v", "f e w", "f e v", "v f d"],
    }

    c = Classifier(data)

    result = c.classify("a")
    assert result["Class A"] == max(result.values())


def test_custom_parse():
    data = {"1": ["a,b,c", "d,e f"], "2": ["i,j,k", "x y,z"]}

    c = Classifier(data)

    assert c.prior == {"1": 2, "2": 2}
    assert c.get_prior() == {"1": 0.5, "2": 0.5}
    assert c.word == {
        "1": {"abc": 1, "de": 1, "f": 1},
        "2": {"ijk": 1, "x": 1, "yz": 1},
    }
    assert c.corpus == {"abc": 1, "de": 1, "f": 1, "ijk": 1, "x": 1, "yz": 1}

    def new_parse(t):
        return [i for i in t.split(",") if i != ""]

    c2 = Classifier(data, f=new_parse)

    assert c2.prior == {"1": 2, "2": 2}
    assert c2.get_prior() == {"1": 0.5, "2": 0.5}
    assert c2.word == {
        "1": {"a": 1, "b": 1, "c": 1, "d": 1, "e f": 1},
        "2": {"i": 1, "j": 1, "k": 1, "x y": 1, "z": 1},
    }
    assert c2.corpus == {
        "a": 1,
        "b": 1,
        "c": 1,
        "d": 1,
        "e f": 1,
        "i": 1,
        "j": 1,
        "k": 1,
        "x y": 1,
        "z": 1,
    }

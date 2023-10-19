from analyzer import getClassNames, getMethodNames

test_input_path = "in.java"

def test_classnames():
    names = getClassNames(test_input_path)

    expected = ["Fun", "Fen", "Fin", "Fon", "Fan"]

    assert sorted(names) == sorted(expected)

def test_methodmap():
    methodmap = getMethodNames(test_input_path)

    expected = {'Fun': ['fun', 'main'], 'Fen': ['fen'], 'Fin': ['fin'], 'Fon': ['fon'], 'Fan': ['fan', 'run']}

    assert len(methodmap) == len(expected)

    for key in methodmap:
        assert sorted(methodmap[key]) == sorted(expected[key])

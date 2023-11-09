from analyzer import getClassNames, getMethodNames

test_input_path = "in.java"
test_input2_path = "Calculator.java"
test_input3_path = "Hotel.java"

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
def test_3_classnames():
    names = getClassNames(test_input2_path)
    print(names)
    assert len(names) == 1
    assert names[0] == 'CalculatorUI'

def test_4_methodnames():
    methodmap = getMethodNames(test_input2_path)
    assert len(methodmap['CalculatorUI']) == 8
    assert 'initButtons' in (methodmap['CalculatorUI'])

def test_5_method_and_classnames():
    classnames = getClassNames(test_input3_path)
    methodmap = getMethodNames(test_input3_path)

    assert len(classnames) == 8
    assert len(methodmap['write']) == 1
    assert methodmap['write'][0] == 'run'
    assert len(methodmap['Singleroom']) == 0

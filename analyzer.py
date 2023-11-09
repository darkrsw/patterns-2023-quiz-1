from javalang.parse import parse
import javalang
from typing import Any, Dict, List, Set, Optional, Union, Tuple, Type



def getClassNames(path: str) -> List[str]:
    with open(path) as f:
        code = f.read()

    my_ast = parse(code)

    clazznames = []

    for path, node in my_ast.filter(javalang.tree.ClassDeclaration):
        clazznames.append(node.name)

    return clazznames

def getMethodNames(path: str) -> Dict[str, List[str]]:
    with open(path) as f:
        code = f.read()

    my_ast = parse(code)

    methodmap = {}

    for path, node in my_ast.filter(javalang.tree.ClassDeclaration):
        methodlist = node.methods
        methodnames = []
        for amethod in methodlist:
            methodnames.append(amethod.name)

        methodmap[node.name] = methodnames

    return methodmap

if __name__ == '__main__':
    amap = getMethodNames("in.java")
    print(amap)
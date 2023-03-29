'''
20. Valid Parentheses
'''

def isValid( s: str) -> bool:

    o = ["(","[","{"]
    c = [")","]","}"]

    item = []
    for i in s:
        if i in o:
            item.append(i)
        elif i in c:
            if item == [] or c.index(i)!= o.index(item.pop()):
                return False

    return True if item ==[] else False


'''
71. Simplify Path
'''

def simplifyPath( path: str) -> str:
    size = 0
    stack = []
    path_dirs = path.split("/")
    for d in path_dirs:
        if len(d)==0 or d=="..":
            continue
        if d=="..":
            if size >0:
                del stack[size-1]
                size-=1
        else:
            stack.append(d)
            size+=1
            
    result = ""
    for r in stack:
        result = result + "/" +r
    
    if len(result)==0:
        return "/"
    return result
            
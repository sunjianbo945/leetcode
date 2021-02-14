
def main(str):
    state = 1
    for token in str:
        if token == 'a':
            pass
        elif token == 'b':
            state += 1
            if state > 3:
                state = 1
        else:
            return False
    
    return state == 3
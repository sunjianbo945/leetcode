# DFA, which stands for Deterministic finite automaton, is a state machine that either accepts or rejects a sequence of
# symbols by running through a state sequence uniquely determined by the string.
# The DFA I used to implement this answer is very simple:

# https://leetcode.com/problems/string-to-integer-atoi/
class Solution8:
    def myAtoi(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(str) == 0: return 0
        '''
        state = 0 means ' ', it can go to state 0, 1, and 2
        state = 1 means '+-', it only can go to state 2
        state = 2 means '0'-'9', it only can go to state 2
        '''
        while pos < len(str):
            current_char = str[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value


# https://leetcode.com/problems/valid-number/
class Solution65:
    def isNumber(self, s: str) -> bool:
        state = {
            'start': {'.': 'dot', '+': 'sign_before_exp', '-': 'sign_before_exp', 'd': 'digit_before_dot'},
            'sign_before_exp': {'.': 'dot', 'd': 'digit_before_dot'},
            'sign_after_exp': {'d': 'digit_after_exp'},
            'digit_before_dot': {'d': 'digit_before_dot', '.': 'digit_after_dot', 'e': 'exp', 'E': 'exp'},
            # digit before exp and dot, . transaction need to go to digit after dot
            'digit_after_dot': {'d': 'digit_after_dot', 'e': 'exp', 'E': 'exp'},  # cannot have .
            'digit_after_exp': {'d': 'digit_after_exp'},  # cannot have . or e or E
            'exp': {'d': 'digit_after_exp', '+': 'sign_after_exp', '-': 'sign_after_exp'},
            'dot': {'d': 'digit_after_dot'},
        }  # curr state -> transtion -> next state

        curr_state = 'start'
        trans_nextState = state[curr_state]

        for c in s:
            if c.isdigit():
                curr = 'd'
            else:
                curr = c

            if curr not in trans_nextState: return False
            curr_state = trans_nextState[curr]
            trans_nextState = state[curr_state]

        return curr_state in ('digit_after_exp', 'digit_after_dot', 'digit_before_dot')
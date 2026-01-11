class Solution(object):
    def evalRPN(self, tokens):
        values = []

        for token in tokens:
            if token == "+":
                b = values.pop()
                a = values.pop()
                values.append(a + b)

            elif token == "-":
                b = values.pop()
                a = values.pop()
                values.append(a - b)

            elif token == "*":
                b = values.pop()
                a = values.pop()
                values.append(a * b)

            elif token == "/":
                b = values.pop()
                a = values.pop()
                result = abs(a) // abs(b)
                if (a < 0) ^ (b < 0):
                    result = -result
                values.append(result)  # truncate toward zero

            else:
                values.append(int(token))

        return values[0]

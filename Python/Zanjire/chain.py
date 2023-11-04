class Chain:
    def __init__(self, value):
        if isinstance(value, (int, float)):
            self.result = value
            self.mode = 'number'
        elif isinstance(value, str):
            self.result = value + ' '
            self.mode = 'string'

    def __call__(self, value):
        if self.mode == 'number' and isinstance(value, (int, float)):
            self.result += value
        elif self.mode == 'string' and isinstance(value, str):
            self.result += value + ' '
        return self

    def __repr__(self):
        return str(self.result).rstrip()

    def __eq__(self, other):
        if isinstance(other, str) and self.mode == 'string':
            return self.result.rstrip() == other
        elif isinstance(other, (int, float)) and self.mode == 'number':
            return self.result == other
        else:
            return False

print(Chain('Ali')('Safinal')('is')('the')('best.'))
print(Chain('Ali')('Safinal')('is')('the')('best.') == 'Ali Safinal is the best.')

print(Chain(1)(2)(3)(4))
print(Chain(1)(2)(3)(4) == 10)

print(Chain('a')('b')('c')('d'))
print(Chain('a')('b')('c')('d') == 'abcd')


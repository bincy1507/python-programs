def test(a):
    '''
        info:This fn prints the value of a
    '''
    print(a)
print(test.__doc__)
help(test)
test(2)
test('bincy')
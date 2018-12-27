def nToFahrenheit(val):
    assert val>=0, "tmp is less than 0.. its very cold"
    return ((val-273)*1.8) + 32

print (nToFahrenheit(273))
print (int (nToFahrenheit(500.545454)))
print ( nToFahrenheit(-300))

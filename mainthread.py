from CalculateE_numba import findingValueOfE

if __name__ == "__main__":
    
    findE = findingValueOfE()
    findE.value_of_e(1000000)
    e = findE.get_e()

    print("E = %8.6f | N = %d"  % (e, findE.n))
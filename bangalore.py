numbers=(3,4,7,9,11,12)
print("original list: ",numbers)
result = map(lambda p:p+p+p,numbers)
print("\n tripple of said list numbers:")
print(list(result))
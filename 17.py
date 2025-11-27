my_dict={"apple":10,"banana":2,"cherry":15,"date":7}
ascending=dict(sorted(my_dict.items()))
descending=dict(sorted(my_dict.items(),reverse=True))
print("Original Dictionary:",my_dict)
print("Ascending Order:",ascending)
print("Descending Order:",descending)

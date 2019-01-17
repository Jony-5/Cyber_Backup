#list_example_2.py
files0 = ["IMG03.png", "IMG010.png", "IMG111.png", "IMG222.png"]
files1 = ["IMG-001.png", "IMG-002.png", "IMG-003.png", "IMG-004.png"]
print(files0)
print(files1)
for i in range(0,4):
	print ("mv "+files0[i]+" "+files1[i]+";")

"""
remark
"""

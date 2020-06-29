merge = ['ProductsData1.txt', 'ProductsData2.txt']
with open('Product_Data_Merge_1_2.py', 'w') as outfile:
    for fname in merge:
        with open(fname) as infile:
            outfile.write(infile.read())

from all_text_files import AllFiles
# from allfiles.all_text_files import AllCsvs

text_file = AllFiles('iris2.csv')
# print(text_file)
# print(next(text_file))
# print(iter(text_file))
print(next(text_file))
# print(text_file.read_all())
# print(text_file.read_last_two_lines())
# print(text_file.read_first_two_lines())


# with AllFiles('iris.csv') as textfile2:
#     print(textfile2.read_all())


# def RecieveBytesFromFile(myf):
#     pass

# RecieveBytesFromFile(text_file)
# abc = open('iris.csv','r')
# print(abc.read())
# print(abc.readline())
# print(abc.readlines())
# print(abc)
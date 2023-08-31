import os
import codecs


def convert_files(encode=1):
    if encode > 2:
        raise ValueError(f"Значение больше чем ожидалось")
    # Indicate the directory in which you need to convert files
    directory = './'
    base_encoding = "utf-8"
    to_encoding = "cp1251"

    if encode == 1:
        base_encoding = "cp1251"
        to_encoding = "utf-8"

    # We get a list of files in the directory
    files = os.listdir(directory)

    # We go through each file in the list
    for filename in files:
        print(filename)
        # Check that the file has an extension .rc
        if filename.endswith('.rc'):
            # Open the file in the current encoding and read its contents
            with codecs.open(os.path.join(directory, filename), 'r', base_encoding) as f:
                content = f.read()
            # Open the file in the UTF-8 encoding and write an attached content into it
            with codecs.open(os.path.join(directory, filename), 'w', to_encoding) as f:
                f.write(content)


if __name__ == "__main__":
    print(f"1 convert `Windows 1251->UTF-8` \n2 convert `UTF-8`->`Windows 1251`")
    answer = int(input())
    convert_files(answer)

import argparse

parser = argparse.ArgumentParser(description='command line interface')
parser.add_argument('-s', '--display_string', type=str, default='Hello Word', help='Enter a string')
args = parser.parse_args()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(args.display_string)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

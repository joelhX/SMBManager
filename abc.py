import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a',  action='store', help="add Project")
    parser.add_argument('-d',  action='store', help="delete Project")
    args = parser.parse_args()
    for k,v in vars(args).items():
        print( k,v)
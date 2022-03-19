import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--load_height', type=int, default=1024)
parser.add_argument('--load_width', type=int, default=768)
opt = parser.parse_args()
print(opt.load_height)
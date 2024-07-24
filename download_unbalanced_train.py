from audioset_download import Downloader
from argparse import ArgumentParser, Namespace

"""
A script made for my own convenience
"""

if __name__ == "__main__":

    argparser : ArgumentParser = ArgumentParser()
    argparser.add_argument("--n_splits", type=int)
    argparser.add_argument("--split_idx", type=int)
    args : Namespace = argparser.parse_args()

    n_splits : int = 1
    split_idx : int = 0

    if(args.n_splits):
        n_splits : int = args.n_splits

    if(args.split_idx):
        split_idx : int = args.split_idx

    print("Downloading the 'unbalanced_train' split in the wav file format...")
    print(f"{split_idx=}")
    print(f"{n_splits=}")

    d = Downloader(root_path='audioset', labels=None, n_jobs=12, download_type='unbalanced_train', copy_and_replicate=False, n_splits=n_splits, split_idx=split_idx)
    d.download(format = 'wav')

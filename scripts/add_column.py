import typer
import pandas as pd
import numpy as np


def main(input_file: str, output_file: str):
    input_frame = pd.read_csv(input_file)
    input_frame.loc[:, "extra_column"] = np.random.random(input_frame.shape[0])
    input_frame.to_csv(output_file, index=False)


if __name__ == "__main__":
    typer.run(main)

import typer
import pandas as pd
import numpy as np

from omegaconf import OmegaConf

conf = OmegaConf.load("params.yaml")


def main(
    input_file: str = conf.preprocess.input_file,
    output_file: str = conf.preprocess.output_file,
):
    input_frame = pd.read_csv(input_file)
    input_frame.loc[:, "extra_column"] = np.random.random(input_frame.shape[0])
    input_frame.to_csv(output_file, index=False)


if __name__ == "__main__":
    typer.run(main)

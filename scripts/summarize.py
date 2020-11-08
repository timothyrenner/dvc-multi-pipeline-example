import typer
import pandas as pd
import json


def main(bigfoot_file: str, haunted_places_file: str, output_file: str):
    bigfoot = pd.read_csv(bigfoot_file)
    haunted_places = pd.read_csv(haunted_places_file)

    bigfoot_avg = bigfoot.extra_column.mean()
    haunted_places_avg = haunted_places.extra_column.mean()

    with open(output_file, "w") as of:
        json.dump(
            {
                "bigfoot_avg": bigfoot_avg,
                "haunted_places_avg": haunted_places_avg,
            },
            of,
        )

    pass


if __name__ == "__main__":
    typer.run(main)

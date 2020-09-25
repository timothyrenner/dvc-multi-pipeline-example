# Run all sub-pipelines

```shell
dvc repro -P
```

Note in the above relative paths work.
DVC changes the working directory for each sub-pipeline before running it.
So all paths in `dvc.yaml` and `params.yaml` should be relative to the subdirectory, not the top.
Effectively each subdirectory is it's own project.

# Run one sub-pipeline.

```shell
dvc repro -c data/bigfoot_sightings
```

`-c` changes the working directory.
It can be used to just run one pipeline.
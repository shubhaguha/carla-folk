My Fair CARLA
===

Background
---

Folktables dataset: <https://github.com/zykls/folktables>

CARLA framework: <https://github.com/carla-recourse/CARLA>

[Planning](PLANNING.md)

Working Prototype
---

Requires exactly Python version 3.7.

```shell
python3 -m venv venv
source venv/bin/activate
pip install -U pip

pip install git+https://github.com/carla-recourse/carla.git

python3 run_carla.py
```

Presentation
---

[Google Slides](https://docs.google.com/presentation/d/10aP63UYQni7j4xdDA1-qGfvE4UWVl0gEYmIlbcmFMvI/edit?usp=sharing)

Reproducibility
---

We processed (binarized categorical features, dropped rows with missing values) and split the folktables dataset and add it to the [cf-data](https://github.com/shubhaguha/cf-data) repository. ([PR](https://github.com/carla-recourse/cf-data/pull/8))

We used this forked repository of datasets and updated the catalog of datasets and ML models in the [CARLA](https://github.com/shubhaguha/CARLA) repository. ([PR](https://github.com/carla-recourse/CARLA/pull/185))

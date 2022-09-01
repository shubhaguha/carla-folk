Planning
===

Setup & Exploration
---

- Install [CARLA](https://github.com/carla-recourse/CARLA)
- [Getting Started](https://carla-counterfactual-and-recourse-library.readthedocs.io/en/latest/notebooks/how_to_use_carla.html)
- [Causal Recourse](https://carla-counterfactual-and-recourse-library.readthedocs.io/en/latest/notebooks/how_to_use_carla_causal.html)

```shell
git clone https://github.com/shubhaguha/CARLA.git
cd CARLA

python3 -m venv venv
source venv/bin/activate
pip install -U pip  # update default pip versions so it stops giving warnings
pip install -e .    # install CARLA
pip install jupyter # helpful for exploration

venv/bin/jupyter notebook  # this is just to make sure you don't use some other jupyter installation that won't have access to the CARLA library you installed
```

- Get familiar with [Adult dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- Get familiar with [folktables dataset](https://github.com/zykls/folktables)
  - Especially why we should "retire" the Adult dataset and use this instead

Planning
===

Setup & Exploration
---

- Install [CARLA](https://github.com/carla-recourse/CARLA)
- [Getting Started](https://carla-counterfactual-and-recourse-library.readthedocs.io/en/latest/notebooks/how_to_use_carla.html)
- [Causal Recourse](https://carla-counterfactual-and-recourse-library.readthedocs.io/en/latest/notebooks/how_to_use_carla_causal.html)

I started making a [Getting Started](https://colab.research.google.com/drive/1b0wtcKRyYG90DugyoZMXPfHxIHFXFmC7?usp=sharing) notebook using Google Colab.

- Get familiar with [Adult dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- Get familiar with [folktables dataset](https://github.com/zykls/folktables)
  - Especially why we should "retire" the Adult dataset and use this instead

Objectives
---

For each dataset (Adult & Folktables):

1. Establish that there is bias in the dataset: Show histograms of group distributions. Demonstrate that groups are imbalanced.
1. Establish that there is bias in the trained model: Change values of protected features and see if prediction changes from low income to high income.
1. Establish that there is bias in the counterfactuals: Show that explanations are not as sparse or more often invalidated, etc., for "disadvantaged" groups (e.g. women or people of color) as for "privileged" groups (e.g. men or white people).

from carla.data.catalog import OnlineCatalog
from carla.models.catalog import MLModelCatalog
from carla.models.negative_instances import predict_negative_instances
import carla.recourse_methods.catalog as recourse_catalog


# Load catalog dataset
data_name = "ACSIncome"
dataset = OnlineCatalog(data_name)

# --- Train ML model
training_params = {"lr": 0.002, "epochs": 10, "batch_size": 1024, "hidden_size": [18, 9, 3]}

ml_model = MLModelCatalog(
    dataset,
    model_type="ann",
    load_online=False,
    backend="pytorch"
)

ml_model.train(
    learning_rate=training_params["lr"],
    epochs=training_params["epochs"],
    batch_size=training_params["batch_size"],
    hidden_size=training_params["hidden_size"]
)

# --- Negatively labeled samples

factuals = predict_negative_instances(ml_model, dataset.df)
test_factual = factuals.iloc[:5]

print(test_factual)

# --- Wachter et al (2018) (gradient method)

hyperparams = {"loss_type": "BCE", "binary_cat_features": True}
recourse_method = recourse_catalog.Wachter(ml_model, hyperparams)
df_cfs = recourse_method.get_counterfactuals(test_factual)

print(df_cfs)

# --- CCHVAE by Pawelczyk et al (2020) (manifold method)

# hyperparams = {
#     "data_name": dataset.name,
#     "n_search_samples": 100,
#     "p_norm": 1,
#     "step": 0.1,
#     "max_iter": 1000,
#     "clamp": True,
#     "binary_cat_features": True,
#     "vae_params": {
#         "layers": [len(ml_model.feature_input_order), 512, 256, 8],
#         "train": True,
#         "lambda_reg": 1e-6,
#         "epochs": 5,
#         "lr": 1e-3,
#         "batch_size": 32,
#     },
# }

# cchvae = recourse_catalog.CCHVAE(ml_model, hyperparams)
# df_cfs = cchvae.get_counterfactuals(test_factual)

# display(df_cfs)

# --- FOCUS by Lucic et al (2021) (tree method)

# ml_model = MLModelCatalog(dataset, "forest", backend="sklearn", load_online=False)
# ml_model.train(max_depth=2, n_estimators=5, force_train=True)

# factuals = predict_negative_instances(ml_model, dataset.df)
# test_factual = factuals.iloc[:5]

# print(test_factual)

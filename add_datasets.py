import kagglehub

path = kagglehub.dataset_download(
    "mssmartypants/paris-housing-price-prediction",
    output_dir="data/raw"
)

print("Dataset:", path)

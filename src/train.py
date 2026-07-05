"""CLI training script — train all models, evaluate, save best."""
import sys, json
from pathlib import Path
from ml_core import load_data, preprocess_data, train_models, evaluate_models, save_best_model

def main():
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "data"
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("models")
    out_dir.mkdir(exist_ok=True)

    from data_generator import load_and_prepare_dataset
    df = load_and_prepare_dataset(data_dir)
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)

    models = train_models(X_train, y_train)
    results = evaluate_models(models, X_test, y_test)

    save_best_model(models, scaler, out_dir)

    with open(out_dir / "training_report.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Training complete. Model saved.")

if __name__ == "__main__":
    main()

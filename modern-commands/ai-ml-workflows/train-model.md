# /train-model - ML Model Training Command

Train a machine learning model with experiment tracking and MLOps best practices.

---

## Usage

```
/train-model [model-type] [dataset]
```

Examples:
- `/train-model classifier user-data.csv`
- `/train-model recommender`
- `/train-model sentiment-analysis reviews-data`

---

## What This Command Does

1. **Setup Training Environment**
   - Initialize MLflow tracking
   - Configure experiment parameters
   - Set up model checkpointing

2. **Prepare Data**
   - Load and validate dataset
   - Split train/val/test sets
   - Create data loaders

3. **Train Model**
   - Initialize model architecture
   - Configure optimizer and loss
   - Run training loop with validation
   - Log metrics to MLflow

4. **Evaluate & Save**
   - Evaluate on test set
   - Log final metrics
   - Save model artifacts
   - Register model in MLflow

5. **Generate Report**
   - Training summary
   - Metrics visualization
   - Model card documentation

---

## Configuration

Create `.mlflow-config.json` in your project:

```json
{
  "tracking_uri": "http://localhost:5000",
  "experiment_name": "my-ml-project",
  "model_registry_uri": "sqlite:///mlflow.db"
}
```

---

**Related Commands:**
- `/deploy-model` - Deploy trained model
- `/evaluate-model` - Run model evaluation
- `/track-experiment` - View experiment results

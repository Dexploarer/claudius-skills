# AI/ML Operations Automator

**Category:** Machine Learning Operations
**Level:** Advanced
**Auto-trigger:** When user mentions ML model deployment, training pipelines, or MLOps workflows

---

## Description

Automates the setup and configuration of Machine Learning Operations (MLOps) infrastructure, including model training pipelines, experiment tracking, model versioning, deployment automation, and monitoring for ML models in production.

---

## Activation Phrases

This skill automatically activates when you say things like:

- "Set up MLOps pipeline"
- "Create ML model deployment workflow"
- "Configure experiment tracking"
- "Set up model versioning"
- "Create training pipeline"
- "Deploy ML model to production"
- "Monitor model performance"
- "Set up feature store"
- "Create ML data pipeline"
- "Configure model registry"

---

## What This Skill Does

When activated, I will:

1. **Assess ML Infrastructure Needs**
   - Identify model type (classification, regression, NLP, computer vision, etc.)
   - Determine deployment target (cloud, edge, hybrid)
   - Evaluate scale requirements (batch, real-time, streaming)
   - Check existing tools (frameworks, platforms, cloud services)

2. **Create Training Pipeline**
   - Set up data ingestion and preprocessing
   - Configure distributed training (if needed)
   - Implement experiment tracking (MLflow, Weights & Biases, Neptune)
   - Add hyperparameter tuning (Optuna, Ray Tune)
   - Create model checkpointing and versioning

3. **Configure Model Registry**
   - Set up model versioning system
   - Create model metadata tracking
   - Implement model lineage tracking
   - Add model approval workflow
   - Configure model promotion stages (dev, staging, prod)

4. **Build Deployment Pipeline**
   - Create model serving infrastructure (TensorFlow Serving, TorchServe, ONNX Runtime)
   - Set up containerization (Docker for models)
   - Configure orchestration (Kubernetes, KServe)
   - Implement A/B testing framework
   - Add canary deployment support
   - Create rollback mechanisms

5. **Implement Monitoring & Observability**
   - Set up model performance tracking
   - Configure data drift detection
   - Implement prediction logging
   - Create alerting for model degradation
   - Add business metrics tracking
   - Set up latency and throughput monitoring

6. **Configure Feature Store**
   - Set up feature repository (Feast, Tecton, AWS Feature Store)
   - Create feature pipelines
   - Implement feature versioning
   - Add feature monitoring
   - Configure online/offline feature serving

---

## Supported Frameworks & Tools

### ML Frameworks
- **TensorFlow/Keras** - Deep learning models
- **PyTorch** - Research and production models
- **Scikit-learn** - Classical ML models
- **XGBoost/LightGBM** - Gradient boosting
- **Hugging Face** - NLP models
- **ONNX** - Cross-framework model format

### MLOps Platforms
- **MLflow** - Experiment tracking, model registry
- **Kubeflow** - ML on Kubernetes
- **Seldon Core** - Model deployment
- **KServe** - Serverless ML inference
- **BentoML** - Model serving framework
- **Ray** - Distributed ML

### Experiment Tracking
- **Weights & Biases** - Comprehensive tracking
- **Neptune.ai** - Team collaboration
- **Comet.ml** - Experiment management
- **TensorBoard** - TensorFlow visualization

### Feature Stores
- **Feast** - Open-source feature store
- **Tecton** - Enterprise feature platform
- **AWS Feature Store** - SageMaker integration
- **Hopsworks** - Feature store + MLOps

### Cloud Platforms
- **AWS SageMaker** - End-to-end ML platform
- **Google Vertex AI** - Unified ML platform
- **Azure ML** - Microsoft ML platform
- **Databricks** - Unified analytics + ML

---

## Code Examples

### Example 1: MLflow Training Pipeline with PyTorch

```python
# training_pipeline.py
import mlflow
import mlflow.pytorch
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from typing import Dict, Any
import json
from pathlib import Path

class MLOpsTrainer:
    """
    MLOps-enabled training pipeline with experiment tracking,
    model versioning, and automatic logging.
    """

    def __init__(
        self,
        experiment_name: str,
        tracking_uri: str = "http://localhost:5000",
        model_registry_uri: str = None
    ):
        self.experiment_name = experiment_name

        # Configure MLflow
        mlflow.set_tracking_uri(tracking_uri)
        if model_registry_uri:
            mlflow.set_registry_uri(model_registry_uri)

        # Set or create experiment
        mlflow.set_experiment(experiment_name)

    def train(
        self,
        model: nn.Module,
        train_loader: DataLoader,
        val_loader: DataLoader,
        config: Dict[str, Any],
        epochs: int = 10
    ):
        """
        Train model with comprehensive MLOps tracking
        """

        # Start MLflow run
        with mlflow.start_run(run_name=config.get('run_name', 'training_run')):

            # Log parameters
            mlflow.log_params({
                'model_architecture': model.__class__.__name__,
                'epochs': epochs,
                'batch_size': train_loader.batch_size,
                'learning_rate': config['learning_rate'],
                'optimizer': config['optimizer'],
                **config.get('hyperparameters', {})
            })

            # Log model architecture
            mlflow.log_text(str(model), 'model_architecture.txt')

            # Setup optimizer and loss
            optimizer = self._create_optimizer(model, config)
            criterion = self._create_criterion(config)

            # Training loop
            best_val_loss = float('inf')
            for epoch in range(epochs):

                # Train
                train_metrics = self._train_epoch(
                    model, train_loader, optimizer, criterion, epoch
                )

                # Validate
                val_metrics = self._validate_epoch(
                    model, val_loader, criterion, epoch
                )

                # Log metrics
                mlflow.log_metrics({
                    f'train_{k}': v for k, v in train_metrics.items()
                }, step=epoch)
                mlflow.log_metrics({
                    f'val_{k}': v for k, v in val_metrics.items()
                }, step=epoch)

                # Save checkpoint if best model
                if val_metrics['loss'] < best_val_loss:
                    best_val_loss = val_metrics['loss']
                    self._save_checkpoint(
                        model, optimizer, epoch, val_metrics, 'best_model'
                    )

                    # Log model to MLflow
                    mlflow.pytorch.log_model(
                        model,
                        'model',
                        registered_model_name=f"{self.experiment_name}_model"
                    )

            # Log final artifacts
            self._log_training_artifacts(config)

            # Add model metadata tags
            mlflow.set_tags({
                'model_type': config.get('model_type', 'unknown'),
                'training_framework': 'pytorch',
                'production_ready': str(best_val_loss < config.get('quality_threshold', 0.1))
            })

            return best_val_loss

    def _train_epoch(self, model, loader, optimizer, criterion, epoch):
        """Single training epoch"""
        model.train()
        total_loss = 0
        correct = 0
        total = 0

        for batch_idx, (data, target) in enumerate(loader):
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
            total += target.size(0)

        return {
            'loss': total_loss / len(loader),
            'accuracy': correct / total
        }

    def _validate_epoch(self, model, loader, criterion, epoch):
        """Single validation epoch"""
        model.eval()
        total_loss = 0
        correct = 0
        total = 0

        with torch.no_grad():
            for data, target in loader:
                output = model(data)
                loss = criterion(output, target)

                total_loss += loss.item()
                pred = output.argmax(dim=1, keepdim=True)
                correct += pred.eq(target.view_as(pred)).sum().item()
                total += target.size(0)

        return {
            'loss': total_loss / len(loader),
            'accuracy': correct / total
        }

    def _save_checkpoint(self, model, optimizer, epoch, metrics, name):
        """Save model checkpoint"""
        checkpoint = {
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'metrics': metrics
        }
        path = Path(f'checkpoints/{name}.pth')
        path.parent.mkdir(parents=True, exist_ok=True)
        torch.save(checkpoint, path)
        mlflow.log_artifact(str(path))

    def _create_optimizer(self, model, config):
        """Create optimizer from config"""
        optimizer_name = config.get('optimizer', 'adam').lower()
        lr = config.get('learning_rate', 0.001)

        if optimizer_name == 'adam':
            return torch.optim.Adam(model.parameters(), lr=lr)
        elif optimizer_name == 'sgd':
            return torch.optim.SGD(
                model.parameters(),
                lr=lr,
                momentum=config.get('momentum', 0.9)
            )
        else:
            raise ValueError(f"Unknown optimizer: {optimizer_name}")

    def _create_criterion(self, config):
        """Create loss criterion from config"""
        criterion_name = config.get('loss', 'crossentropy').lower()

        if criterion_name == 'crossentropy':
            return nn.CrossEntropyLoss()
        elif criterion_name == 'mse':
            return nn.MSELoss()
        else:
            raise ValueError(f"Unknown criterion: {criterion_name}")

    def _log_training_artifacts(self, config):
        """Log training configuration and artifacts"""
        # Save config
        config_path = Path('config.json')
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        mlflow.log_artifact(str(config_path))


# Usage example
if __name__ == '__main__':
    from torchvision import datasets, transforms
    from models import MyModel  # Your model definition

    # Setup data
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    train_dataset = datasets.MNIST('data', train=True, download=True, transform=transform)
    val_dataset = datasets.MNIST('data', train=False, transform=transform)

    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=64)

    # Training configuration
    config = {
        'run_name': 'mnist_experiment_v1',
        'model_type': 'cnn_classifier',
        'learning_rate': 0.001,
        'optimizer': 'adam',
        'loss': 'crossentropy',
        'quality_threshold': 0.05,
        'hyperparameters': {
            'dropout': 0.5,
            'hidden_units': 128
        }
    }

    # Initialize trainer
    trainer = MLOpsTrainer(
        experiment_name='mnist_classification',
        tracking_uri='http://mlflow-server:5000'
    )

    # Train model
    model = MyModel()
    final_loss = trainer.train(model, train_loader, val_loader, config, epochs=10)

    print(f"Training complete! Final validation loss: {final_loss:.4f}")
```

### Example 2: Model Deployment with KServe

```yaml
# kserve_deployment.yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: ml-model-serving
  namespace: ml-production
  annotations:
    autoscaling.knative.dev/minScale: "2"
    autoscaling.knative.dev/maxScale: "10"
    autoscaling.knative.dev/target: "100"
spec:
  predictor:
    # Model server configuration
    pytorch:
      # Model URI from MLflow or S3
      storageUri: "s3://ml-models/my-model/v1"

      # Resource requirements
      resources:
        requests:
          cpu: "1"
          memory: "2Gi"
          nvidia.com/gpu: "1"
        limits:
          cpu: "2"
          memory: "4Gi"
          nvidia.com/gpu: "1"

      # Environment variables
      env:
        - name: MODEL_NAME
          value: "my-classifier"
        - name: ENABLE_METRICS
          value: "true"
        - name: LOG_LEVEL
          value: "INFO"

      # Readiness probe
      readinessProbe:
        httpGet:
          path: /v1/models/my-classifier
          port: 8080
        initialDelaySeconds: 30
        periodSeconds: 10

      # Liveness probe
      livenessProbe:
        httpGet:
          path: /v1/models/my-classifier
          port: 8080
        initialDelaySeconds: 60
        periodSeconds: 30

  # Canary deployment (optional)
  canaryTrafficPercent: 10
---
# Service Monitor for Prometheus
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: ml-model-metrics
  namespace: ml-production
spec:
  selector:
    matchLabels:
      serving.kserve.io/inferenceservice: ml-model-serving
  endpoints:
    - port: metrics
      interval: 30s
      path: /metrics
```

### Example 3: Feature Store with Feast

```python
# feature_store_setup.py
from feast import FeatureStore, Entity, Feature, FeatureView, FileSource, ValueType
from feast.types import Int64, Float32, String
from datetime import timedelta
import pandas as pd

# Define entities
user = Entity(
    name="user_id",
    value_type=ValueType.INT64,
    description="User identifier"
)

item = Entity(
    name="item_id",
    value_type=ValueType.INT64,
    description="Item identifier"
)

# Define feature sources
user_features_source = FileSource(
    path="data/user_features.parquet",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp"
)

item_features_source = FileSource(
    path="data/item_features.parquet",
    event_timestamp_column="event_timestamp",
    created_timestamp_column="created_timestamp"
)

# Define feature views
user_features_view = FeatureView(
    name="user_features",
    entities=["user_id"],
    ttl=timedelta(days=365),
    features=[
        Feature(name="age", dtype=Int64),
        Feature(name="country", dtype=String),
        Feature(name="signup_days", dtype=Int64),
        Feature(name="avg_session_duration", dtype=Float32),
        Feature(name="purchase_count_30d", dtype=Int64),
        Feature(name="total_spent_90d", dtype=Float32)
    ],
    source=user_features_source,
    tags={"team": "ml", "category": "user_profile"}
)

item_features_view = FeatureView(
    name="item_features",
    entities=["item_id"],
    ttl=timedelta(days=30),
    features=[
        Feature(name="category", dtype=String),
        Feature(name="price", dtype=Float32),
        Feature(name="views_7d", dtype=Int64),
        Feature(name="purchases_7d", dtype=Int64),
        Feature(name="rating_avg", dtype=Float32),
        Feature(name="stock_level", dtype=Int64)
    ],
    source=item_features_source,
    tags={"team": "ml", "category": "item_profile"}
)


class MLFeatureStore:
    """
    Wrapper for Feast feature store with ML-specific utilities
    """

    def __init__(self, repo_path: str = "."):
        self.store = FeatureStore(repo_path=repo_path)

    def get_training_data(
        self,
        entity_df: pd.DataFrame,
        features: list[str]
    ) -> pd.DataFrame:
        """
        Retrieve historical features for model training

        Args:
            entity_df: DataFrame with entity IDs and timestamps
            features: List of feature references (e.g., 'user_features:age')

        Returns:
            DataFrame with features joined to entities
        """
        training_df = self.store.get_historical_features(
            entity_df=entity_df,
            features=features
        ).to_df()

        return training_df

    def get_online_features(
        self,
        entity_rows: list[dict],
        features: list[str]
    ) -> dict:
        """
        Retrieve online features for real-time prediction

        Args:
            entity_rows: List of entity dictionaries
            features: List of feature references

        Returns:
            Dictionary of features
        """
        online_features = self.store.get_online_features(
            entity_rows=entity_rows,
            features=features
        ).to_dict()

        return online_features

    def materialize_features(
        self,
        start_date: str,
        end_date: str,
        feature_views: list[str] = None
    ):
        """
        Materialize features to online store

        Args:
            start_date: Start date (ISO format)
            end_date: End date (ISO format)
            feature_views: List of feature view names (None = all)
        """
        self.store.materialize(
            start_date=pd.to_datetime(start_date),
            end_date=pd.to_datetime(end_date),
            feature_views=feature_views
        )


# Usage example
if __name__ == '__main__':
    fs = MLFeatureStore(repo_path="feature_repo")

    # Get training data
    entity_df = pd.DataFrame({
        'user_id': [1001, 1002, 1003],
        'item_id': [5001, 5002, 5003],
        'event_timestamp': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03'])
    })

    training_data = fs.get_training_data(
        entity_df=entity_df,
        features=[
            'user_features:age',
            'user_features:country',
            'user_features:purchase_count_30d',
            'item_features:category',
            'item_features:price',
            'item_features:rating_avg'
        ]
    )

    print("Training data shape:", training_data.shape)
    print(training_data.head())

    # Get online features for prediction
    online_features = fs.get_online_features(
        entity_rows=[
            {'user_id': 1001, 'item_id': 5001}
        ],
        features=[
            'user_features:purchase_count_30d',
            'item_features:price'
        ]
    )

    print("\nOnline features:", online_features)
```

---

## Best Practices

### 1. **Experiment Tracking**
- Always log hyperparameters, metrics, and artifacts
- Use consistent naming conventions for experiments
- Track data versions alongside model versions
- Log model lineage and dependencies

### 2. **Model Versioning**
- Semantic versioning for models (major.minor.patch)
- Tag models with metadata (accuracy, f1-score, etc.)
- Maintain model registry with approval workflow
- Never deploy directly from training

### 3. **Data Management**
- Version training datasets
- Monitor data drift in production
- Implement feature store for consistency
- Validate data quality before training

### 4. **Deployment Strategy**
- Use canary deployments for new models
- Implement A/B testing framework
- Monitor latency and throughput
- Have rollback procedures ready

### 5. **Monitoring**
- Track model performance metrics
- Monitor prediction distributions
- Alert on degradation
- Log prediction examples for debugging

---

## Common Pitfalls

❌ **Training-Serving Skew**
```python
# Training: Using pandas
features = df[['age', 'income']].fillna(0)

# Serving: Different preprocessing
features = {'age': request.age or 0, 'income': request.income or 0}
# → Results will differ!
```

✅ **Solution: Use Feature Store**
```python
# Both training and serving use feature store
features = feature_store.get_features(entity_id, feature_list)
```

---

❌ **No Monitoring**
```python
# Just serve predictions
prediction = model.predict(features)
return prediction
```

✅ **Log Everything**
```python
# Log inputs, outputs, latency
start_time = time.time()
prediction = model.predict(features)
latency = time.time() - start_time

logger.log_prediction(
    features=features,
    prediction=prediction,
    latency=latency,
    model_version=model_version
)
```

---

## Testing Strategy

1. **Unit Tests**
   - Test data preprocessing
   - Test model loading
   - Test prediction logic

2. **Integration Tests**
   - Test full pipeline end-to-end
   - Test feature store integration
   - Test model serving API

3. **Performance Tests**
   - Measure inference latency
   - Test throughput under load
   - Validate resource usage

4. **Model Quality Tests**
   - Validate accuracy on test set
   - Check for bias
   - Test edge cases

---

## Production Checklist

- [ ] Model versioning configured
- [ ] Experiment tracking enabled
- [ ] Feature store implemented
- [ ] Monitoring dashboards created
- [ ] Alerting rules defined
- [ ] Canary deployment configured
- [ ] Rollback procedure documented
- [ ] Model approval workflow established
- [ ] Data drift detection enabled
- [ ] Prediction logging implemented
- [ ] Load testing completed
- [ ] Security review passed

---

## Related Skills

- **microservices-orchestrator** - For ML service orchestration
- **distributed-tracing-setup** - For request tracing
- **metrics-pipeline-builder** - For custom metrics
- **api-gateway-configurator** - For ML API gateway

---

**Last Updated:** 2025-11-02
**Version:** 1.0.0
**Maintainer:** Claudius Skills Project

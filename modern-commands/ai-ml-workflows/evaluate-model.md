# /evaluate-model - Model Evaluation Command

Comprehensive model evaluation with metrics, visualizations, and reports.

---

## Usage

```
/evaluate-model [model-name] [test-dataset]
/evaluate-model --compare [model1] [model2]
```

Examples:
- `/evaluate-model my-classifier test-data.csv`
- `/evaluate-model --compare model-v1 model-v2`

---

## What This Command Does

1. **Load Model & Data**
   - Load model from registry
   - Load test dataset
   - Validate compatibility

2. **Run Evaluation**
   - Generate predictions
   - Calculate metrics (accuracy, precision, recall, F1)
   - Confusion matrix
   - ROC curves

3. **Performance Analysis**
   - Latency measurements
   - Throughput testing
   - Memory usage
   - Batch vs single prediction

4. **Fairness & Bias**
   - Check for data drift
   - Analyze prediction distribution
   - Detect bias across groups
   - Generate fairness metrics

5. **Generate Report**
   - Model card
   - Metrics dashboard
   - Visualizations
   - Recommendations

---

## Output

```
📊 MODEL EVALUATION REPORT

Model: my-classifier-v1
Test Set: 10,000 samples

Performance Metrics:
✓ Accuracy: 94.5%
✓ Precision: 93.2%
✓ Recall: 95.1%
✓ F1-Score: 94.1%

Latency:
• p50: 12ms
• p95: 25ms
• p99: 45ms

Recommendations:
1. Model performs well
2. Consider optimization for p99 latency
3. No significant bias detected
```

---

**Related Commands:**
- `/train-model` - Train a new model
- `/deploy-model` - Deploy model to production

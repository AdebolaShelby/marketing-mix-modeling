from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
import numpy as np

def validate_model(model, X, y, cv=5):
    """
    Validate model performance using multiple metrics
    """
    # Cross-validation scores
    cv_scores = cross_val_score(model, X, y, cv=cv)
    
    # Train model on full dataset for additional metrics
    model.fit(X, y)
    y_pred = model.predict(X)
    
    # Calculate metrics
    metrics = {
        'cv_score_mean': cv_scores.mean(),
        'cv_score_std': cv_scores.std(),
        'mae': mean_absolute_error(y, y_pred),
        'rmse': np.sqrt(mean_squared_error(y, y_pred)),
        'r2': r2_score(y, y_pred)
    }
    
    return metrics

def print_validation_results(metrics):
    """
    Print validation results in a formatted way
    """
    print("\nModel Validation Results:")
    print(f"Cross-validation Score: {metrics['cv_score_mean']:.3f} (+/- {metrics['cv_score_std']*2:.3f})")
    print(f"Mean Absolute Error: {metrics['mae']:.3f}")
    print(f"Root Mean Squared Error: {metrics['rmse']:.3f}")
    print(f"R² Score: {metrics['r2']:.3f}")
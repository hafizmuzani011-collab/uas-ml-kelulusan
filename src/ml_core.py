"""Core ML functions: preprocessing, training, evaluation."""
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, balanced_accuracy_score, confusion_matrix,
                             classification_report)
from imblearn.over_sampling import SMOTE
import joblib
import json
from pathlib import Path

def preprocess_data(df, target_col="Target_binary", test_size=0.2, random_state=42):
    """Split and scale data."""
    # List of selected 10 features as specified in data_dictionary.md
    features = [
        "Previous qualification (grade)",
        "Admission grade",
        "Age at enrollment",
        "Curricular units 1st sem (approved)",
        "Curricular units 1st sem (grade)",
        "Curricular units 2nd sem (approved)",
        "Curricular units 2nd sem (grade)",
        "Tuition fees up to date",
        "Scholarship holder",
        "Debtor"
    ]
    
    # Map friendly names to actual UCI dataset columns if different
    # The actual columns in UCI dataset:
    # 'Previous qualification (grade)' -> 'Previous qualification (grade)' or similar
    # Let's print the actual columns first in the generator, or make sure we match them.
    # We will map standard UCI column names:
    col_mapping = {
        "Previous qualification (grade)": "Previous qualification (grade)",
        "Admission grade": "Admission grade",
        "Age at enrollment": "Age at enrollment",
        "Curricular units 1st sem (approved)": "Curricular units 1st sem (approved)",
        "Curricular units 1st sem (grade)": "Curricular units 1st sem (grade)",
        "Curricular units 2nd sem (approved)": "Curricular units 2nd sem (approved)",
        "Curricular units 2nd sem (grade)": "Curricular units 2nd sem (grade)",
        "Tuition fees up to date": "Tuition fees up to date",
        "Scholarship holder": "Scholarship holder",
        "Debtor": "Debtor"
    }
    
    # If the df columns have different casing or spacing (e.g. underscores), handle it:
    cleaned_cols = {}
    for col in df.columns:
        cleaned_cols[col.replace("_", " ").lower().strip()] = col
        
    selected_cols = []
    for f in features:
        key = f.lower().strip()
        if key in cleaned_cols:
            selected_cols.append(cleaned_cols[key])
        else:
            # Fallback to pattern matching
            matched = [col for col in df.columns if key[:10] in col.lower()]
            if matched:
                selected_cols.append(matched[0])
                
    if not selected_cols:
        # Fallback to top 10 features if nothing matched
        selected_cols = [c for c in df.columns if c != target_col][:10]
        
    X = df[selected_cols]
    y = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Save scaler
    joblib.dump(scaler, "D:/uas-ml-kelulusan-A11.2024.15549-A11.4401_A11.4410-Nailah_Azfa_Zarqarida/models/scaler.joblib")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, selected_cols

def get_mutual_info(X, y, feature_names):
    """Compute Mutual Information for feature selection."""
    mi = mutual_info_classif(X, y, random_state=42)
    mi_df = pd.DataFrame({"Feature": feature_names, "MI": mi})
    return mi_df.sort_values(by="MI", ascending=False)
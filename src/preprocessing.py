import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from imblearn.over_sampling import SMOTE
import yaml

def load_data(df_path):
    # Load data
    df = pd.read_csv(df_path)
    df.columns = ["age", "sex", "cp", "trestbps",
                  "chol", "fbs", "restecg", "thalach",
                  "exang", "oldpeak", "slope", "ca", "thal", "target"]
    return df

def prepare_data(df, impute_strategy='mean', selected_columns=None, random_seed=42):
    """
    Prepares train and test datasets for an ML model.
    
    Parameters:
    - df (pd.DataFrame): The input dataset.
    - impute_strategy (str): 'mean' or 'most_frequent' for missing value imputation.
    - selected_columns (list): Columns to use for training. If None, use all columns except target.
    - random_seed (int): Random seed for reproducibility.
    
    Returns:
    - X_train, X_test, y_train, y_test: Processed training and testing data.
    """
    
    # Define target variable
    target_col = 'target'
    
    # Select features
    if selected_columns:
        X = df[selected_columns]
    else:
        X = df.drop(columns=[target_col])

    y = df[target_col]
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_seed, stratify=y
    )

    # Handle missing values - Fit on X_train and transform both X_train & X_test
    imputer = SimpleImputer(strategy=impute_strategy)
    X_train_imputed = pd.DataFrame(imputer.fit_transform(X_train), columns=X_train.columns)
    X_test_imputed = pd.DataFrame(imputer.transform(X_test), columns=X_test.columns)

    # Handle class imbalance using SMOTE
    smote = SMOTE(random_state=random_seed)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train_imputed, y_train)

    # Join the train and test datasets
    X_train_resampled.reset_index(inplace=True, drop=True)
    y_train_resampled.reset_index(inplace=True, drop=True)
    X_test_imputed.reset_index(inplace=True, drop=True)
    y_test.reset_index(inplace=True, drop=True)

    df_train = pd.concat([X_train_resampled, y_train_resampled], axis=1)
    df_test = pd.concat([X_test_imputed, y_test], axis=1)
    
    return df_train, df_test

def save_data(df_train, df_test, train_name, test_name):
    df_train.to_csv(train_name)
    df_test.to_csv(test_name)

if __name__=="__main__":
    params = yaml.safe_load(open("params.yaml"))["new_data"]
    data_path = params['data_path']
    impute_strategy = params['impute_strategy']
    cols = params['columns']
    random_seed = params['random_seed']

    data = load_data(data_path)
    train_data, test_data = prepare_data(data,
                                         impute_strategy=impute_strategy,
                                         selected_columns=cols,
                                         random_seed=random_seed)
    save_data(train_data, test_data,
              'data/lab3_train_data.csv',
              'data/lab3_test_data.csv')
    
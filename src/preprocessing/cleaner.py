import pandas as pd 

class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()
    
    def drop_columns(self):
        # Drop unnecessary columns
        columns_to_drop = ['Unnamed: 0', 'Customer ID']
        self.df.drop(columns=[col for col in columns_to_drop if col in self.df.columns], inplace=True)
        return self 
    
    def standardize_booleans(self):
        # Convert yes/no columns to 1/0
        boolean_columns = ['Promo Code Used', 'Discount Applied', 'Subscription Status']
        for col in boolean_columns:
            self.df[col] = self.df[col].str.lower().map({'yes': 1, 'no': 0})
        return self
    
    def clean_column_names(self):
        # Standardize column names to lowercase
        self.df.columns = self.df.columns.str.strip().str.replace(' ', '_').str.lower()
        return self()
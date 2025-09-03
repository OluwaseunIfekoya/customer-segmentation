import pandas as pd

class FeatureEngineer:
    def __init__(self, df):
        self.df = df.copy()

    def add_age_group(self):
        bins = [17, 24, 34, 44, 54, 64, 74, 100]
        labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75+']
        self.df['age_group'] = pd.cut(self.df['age'], bins=bins, labels=labels)
        return self
    
    def add_spend_category(self):
        bins = [0, 40, 70, float('inf')]
        labels = ['Low Spender', 'Mid Spender', 'High Spender']
        self.df['spender_type'] = pd.cut(self.df['purchase_amount_(usd)'], bins=bins, labels=labels)
        return self
    
    def map_frequency_score(self):
        freq_map = {
            'Once': 0,
            'Annually': 1,
            'Quarterly': 2,
            'Every 3 months': 3,
            'Monthly': 4,
            'Fortnightly': 5,
            'Bi-Weekly': 6,
            'Weekly': 7,
            'Daily': 8 
        }
        self.df['purchase_frequency_score'] =self.df['frequency_of_purchases'].map(freq_map)
        return self
    
    def review_sentiment(self):
        #classify rating 1-2.9 = low, 3-3.9 = Medium, 4-5 = High
        self.df['review_sentiment'] = pd.cut(
            self.df['review_rating'],
            bins=[0, 2.9, 3.9, 5.0],
            labels=['Low', 'Medium', 'High']
        )
        return self
    
    def shipping_speed(self):
        express = ['Same Day', 'Next Day', 'Two-Day Shipping']
        standard = ['Standard Shipping', 'Free Shipping']
        self.df['shipping_speed'] = self.df['shipping_type'].apply(
            lambda x: 'Express' if x in express else 'Standard'
        )
        return self
    
    def promo_discount_combo(self):
        self.df['used_discount_or_promo'] = ((self.df['discount_applied'] == 1) | (self.df['promo_code_used'] == 1)).astype(int)
        return self
    
    def generate_features(self):
        return (self
                .add_age_group()
                .add_spend_category()
                .map_frequency_score()
                .review_sentiment()
                .shipping_speed()
                .promo_discount_combo()
                .df)
    
# generate_synthetic_data.py
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# --- customers.csv ---
n_customers = 1000
customers = pd.DataFrame({
    'customer_id': range(1, n_customers+1),
    'name': [f'Customer {i}' for i in range(1, n_customers+1)],
    'age': np.random.randint(18, 70, n_customers),
    'gender': np.random.choice(['M', 'F'], n_customers),
    'city': np.random.choice(['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba'], n_customers)
})
customers.to_csv('data/raw/customers.csv', index=False)

# --- transactions.csv ---
n_txn = 5000
txn_types = ['deposit', 'withdrawal', 'payment']
channels = ['app', 'branch', 'atm']

transactions = pd.DataFrame({
    'txn_id': range(1, n_txn+1),
    'customer_id': np.random.choice(customers['customer_id'], n_txn),
    'txn_date': [datetime.today() - timedelta(days=random.randint(0,365)) for _ in range(n_txn)],
    'txn_amount': np.round(np.random.uniform(10, 5000, n_txn),2),
    'txn_type': np.random.choice(txn_types, n_txn),
    'channel': np.random.choice(channels, n_txn)
})
transactions.to_csv('data/raw/transactions.csv', index=False)

print("✅ Dados sintéticos gerados em data/raw/")

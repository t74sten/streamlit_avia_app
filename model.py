import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix

import joblib

new_test = pd.read_csv('data/clients_fin.csv')
X = new_test.drop(columns=['satisfaction'])
y = new_test.satisfaction
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model_30 = GradientBoostingClassifier(learning_rate=0.1, n_estimators=1000, subsample=1.0,
                                     criterion='friedman_mse', min_samples_split=6, min_samples_leaf=1,
                                     min_weight_fraction_leaf=0.0, max_depth=6, min_impurity_decrease=0.0,
                                     init=None, random_state=42)
model_30.fit(X_train, y_train)
pred_30 = model_30.predict(X_test)

joblib.dump(model_30, 'data/model_fin.sav')
print(confusion_matrix(y_test, pred_30))

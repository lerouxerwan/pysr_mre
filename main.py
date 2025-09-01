from pysr import PySRRegressor

from utils_dataset import variable_names, X_units, y_units, X, y

model = PySRRegressor(parallelism='serial', random_state=42, deterministic=True)
model.fit(X, y, variable_names=variable_names, X_units=X_units, y_units=y_units)
print(f'{len(model.equations_)} equations with complexity: {model.equations_['complexity'].to_list()}')




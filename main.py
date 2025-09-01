from pysr import PySRRegressor

from utils_dataset import X, y

model = PySRRegressor(parallelism='serial', random_state=42, deterministic=True)
model.fit(X, y)
print(f'{len(model.equations_)} equations with complexity: {model.equations_['complexity'].to_list()}')
print(f'with loss list={model.equations_["loss"].values}')




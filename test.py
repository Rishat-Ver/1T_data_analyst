assert _test.node(
    ast.FunctionDef, name='make_features'
).exists, 'Не изменяйте прекод, нет функции make_features().'

_test.call(
    'make_features',
    m='Не изменяйте прекод, нет вызова функции make_features'
)

_test.call(
    'TimeSeriesSplit',
    m='Не изменяйте прекод, примените TimeSeriesSplit для разбиения данных'
)

_test.call(
    'LinearRegression',
    m='Не изменяйте прекод, нет создание LinearRegression'
)

_test.var_exists(
    'X_train',
    'X_test',
    'y_train',
    'y_test',
    'train_mae',
    'test_mae',
    'model',
    'y_pred_train',
    'y_pred_test',
    'mae_train',
    'mae_test',
    same_type=True,
    m='Не изменяйте прекод, не изменяйте название переменных'
)

_test.once('fit', m='Не изменяйте прекод, обучите модель')
_test.once('mean_absolute_error')
_test.once('predict')

avg_train_mae = sum(_u.train_mae) / len(_u.train_mae)
avg_test_mae = sum(_u.test_mae) / len(_u.test_mae)
output_strings =_u._output.split('\n')

msg = f'''
Проверьте, что значение MAE посчитано верно и на тестовой выборке не больше 37 000
Проверьте, что функция make_features имеет аргументы data, 10, 7 .
'''

assert avg_train_mae != avg_test_mae, 'Проверьте MAE обучающей выборки и тестовой выборки. Они не должны быть равны.'

assert avg_test_mae < 37000, msg

assert len(output_strings) == 2, 'Не меняйте формат вывода на экран (уже в прекоде).'
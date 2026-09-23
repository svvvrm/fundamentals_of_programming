## Задание 1

### Часть 1

В интерактивном режиме интерпретатора было выполнено выражение `2 + 3 * 4`, после чего интерпретатор вывел в терминал  `14`. После этого то же самое выражение было записано в файл `task_1.py`. Ожидалось, что после запуска `task_1.py`  в терминал будет выведено `14`, но в результате запуска файла ничего не было выведено в терминал.

Так произошло, потому что в интерактивном режиме после ввода выражения интерпретатор вычисляет его и автоматически выводит полученное значение. Поэтому результат `14` отображается без специальной команды вывода.

При запуске файла интерпретатор выполняет инструкции программы, но значения отдельных выражений автоматически не выводит. Выражение `2 + 3 * 4` вычисляется однако это значение нигде не используется и не выводится. Чтобы результат вывелся в терминал при запуске `task_1.py`, нужно явно использовать `print()`:

```python
print(2 + 3 * 4)
```


### Часть 2

В следующем коде:

```python
course = "Python"
hours = 4 * 2
print(f"{course}: {hours} часов")
```

-  Являются выражениями:
    -  `"Python"`
    - `4 * 2` 
    - `f"{course}: {hours} часов"`
- Являются инструкциями:
    -  `course = "Python"`
    -  `hours = 4 * 2`
    -  `print(f"{course}: {hours} часов")`
- Присутствуют литералы:
    -  `"Python"`
    -  `4`
    -  `2` 
    -  Пробелы
    -  Двоеточие
    - `часов`
- Создаются имена:
    -  course
    -  hours
    -  \_\_annotations\_\_
    -  \_\_annotations\_\_
    -  \_\_builtins\_\_
    -  \_\_cached\_\_
    -  \_\_doc\_\_
    -  \_\_file\_\_
    -  \_\_loader\_\_
    -  \_\_name\_\_
    -  \_\_package\_\_
    -  \_\_spec\_\_

### Часть 3

**Версия Python: 3.13.5**

В выводе команды `python -m ast task_1.py`:

```
Module(
   body=[
      Expr(
         value=Call(
            func=Name(id='print', ctx=Load()),
            args=[
               BinOp(
                  left=Constant(value=2),
                  op=Add(),
                  right=BinOp(
                     left=Constant(value=3),
                     op=Mult(),
                     right=Constant(value=4)))])),
      Assign(
         targets=[
            Name(id='course', ctx=Store())],
         value=Constant(value='Python')),
      Assign(
         targets=[
            Name(id='hours', ctx=Store())],
         value=BinOp(
            left=Constant(value=4),
            op=Mult(),
            right=Constant(value=2))),
      Expr(
         value=Call(
            func=Name(id='print', ctx=Load()),
            args=[
               JoinedStr(
                  values=[
                     FormattedValue(
                        value=Name(id='course', ctx=Load()),
                        conversion=-1),
                     Constant(value=': '),
                     FormattedValue(
                        value=Name(id='hours', ctx=Load()),
                        conversion=-1),
                     Constant(value=' часов')])]))])
```


-  Отвечают за присваивание:

```
Assign(
   targets=[
	  Name(id='course', ctx=Store())],
   value=Constant(value='Python'))
```

```
Assign(
   targets=[
	  Name(id='hours', ctx=Store())],
   value=BinOp(
	  left=Constant(value=4),
	  op=Mult(),
	  right=Constant(value=2)))
```

-  Отвечают за арифметические операции:

```
BinOp(
   left=Constant(value=2),
   op=Add(),
   right=BinOp(
	  left=Constant(value=3),
	  op=Mult(),
	  right=Constant(value=4)))]))
```

- Отвечает за вызов функции `print()`:

```
Expr(
   value=Call(
	  func=Name(id='print', ctx=Load()),
	  args=[
	     BinOp(
		    left=Constant(value=2),
		    op=Add(),
		    right=BinOp(
			   left=Constant(value=3),
			   op=Mult(),			                                        right=Constant(value=4)))]))
```


В выводе команды `python -m dis task_1.py`:


```
0           RESUME                   0

2           LOAD_NAME                0 (print)
			PUSH_NULL
			LOAD_CONST               0 (14)
			CALL                     1
			POP_TOP

5           LOAD_CONST               1 ('Python')
		    STORE_NAME               1 (course)

6           LOAD_CONST               2 (8)
		    STORE_NAME               2 (hours)

7           LOAD_NAME                0 (print)
		    PUSH_NULL
		    LOAD_NAME                1 (course)
		    FORMAT_SIMPLE
		    LOAD_CONST               3 (': ')
		    LOAD_NAME                2 (hours)
		    FORMAT_SIMPLE
		    LOAD_CONST               4 (' часов')
		    BUILD_STRING             4
		    CALL                     1
		    POP_TOP
		    RETURN_CONST             5 (None)
```

Инструкция `LOAD_CONST` отвечает  за загрузку констант, а интструкция `CALL` отвечает за вызов функций.

### Ответ на контрольный вопрос

Байткод CPython нельзя считать машинным кодом процессора, потому что данный байткод является командами для виртуальной машины Python (PVM) и не может быть выполнен процессором напрямую.

## Задание 2

О равенстве значений говорят, когда 2 пременные ссылаются на объекты с одинаковым содержимым. А об идентичности говорят когда 2 переменные ссылаются на один объект в памяти. 

```Python
a = 1000
b = a
c = int("1000")

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b)
print("a is b:", a is b)
print("a == c:", a == c)
print("a is c:", a is c)
```

### Ответы на контрольные вопросы:
1. Инструкция `b = a` не создает копию объекта. Такой вывод можно сделать потому, что `id(a)` и `id(b)` имеют одинаковое значение, т.е. обе переменных ссылаются на один объект в памяти.
2. `type()` возращает тип объекта, переданного ему в качестве аргумента, а `id()` возращает адрес в памяти объекта, переданного ему в качестве аргумента.
3. `None` принято сравнивать с помощью `is`, потому что в памяти хранится единственный объект с типом `None`. А числа и строки принято сравнивать с помощью `==`, потому что в памяти могут хранится сразу несколько объектов с одинаковым значением.
from pdl.pdl_ast import Program
from pdl.pdl_interpreter import (
    InterpreterState,
    contains_error,
    empty_scope,
    process_prog,
)

arith_data = {
    "description": "Test arith",
    "defs": {"X": "{{ 1 + 1 }}"},
    "document": "{{ X }}",
}


def test_arith():
    state = InterpreterState()
    data = Program.model_validate(arith_data)
    result, _, scope, _ = process_prog(state, empty_scope, data)
    assert result == "2"
    assert scope["X"] == 2


var_data = {
    "defs": {"X": {"data": 1}, "Y": {"data": 2}},
    "document": "{{ X + Y }}",
}


def test_var():
    state = InterpreterState()
    data = Program.model_validate(var_data)
    result, _, _, _ = process_prog(state, empty_scope, data)
    assert result == "3"


true_data = {
    "document": "{{ 1 < 2 }}",
}


def test_true():
    state = InterpreterState()
    data = Program.model_validate(true_data)
    result, _, _, _ = process_prog(state, empty_scope, data)
    assert result == "true"


false_data = {
    "document": "{{ 1 >= 2 }}",
}


def test_false():
    state = InterpreterState()
    data = Program.model_validate(false_data)
    result, _, _, _ = process_prog(state, empty_scope, data)
    assert result == "false"


undefined_var_data = {"document": "Hello {{ X }}"}


def test_undefined_var():
    state = InterpreterState()
    data = Program.model_validate(undefined_var_data)
    document, _, _, trace = process_prog(state, empty_scope, data)
    assert contains_error(trace)
    assert document == "Hello {{ X }}"


autoescape_data = {"document": "<|system|>"}


def test_autoescape():
    state = InterpreterState()
    data = Program.model_validate(autoescape_data)
    document, _, _, _ = process_prog(state, empty_scope, data)
    assert document == "<|system|>"


var_data1 = {"defs": {"X": "something"}, "document": "{{ X }}"}


def test_var1():
    state = InterpreterState()
    data = Program.model_validate(var_data1)
    result, _, _, _ = process_prog(state, empty_scope, data)
    assert result == "something"


var_data2 = {
    "defs": {"X": "something", "Y": "something else"},
    "document": "{{ [X, Y] }}",
}


def test_var2():
    state = InterpreterState()
    data = Program.model_validate(var_data2)
    result, _, scope, _ = process_prog(state, empty_scope, data)
    assert result == '["something", "something else"]'
    assert scope["X"] == "something"
    assert scope["Y"] == "something else"


list_data = {"defs": {"X": {"data": [1, 2, 3]}, "Y": "{{ X }}"}, "document": "{{ X }}"}


def test_list():
    state = InterpreterState()
    data = Program.model_validate(list_data)
    result, _, scope, _ = process_prog(state, empty_scope, data)
    assert result == "[1, 2, 3]"
    assert scope["X"] == [1, 2, 3]
    assert scope["Y"] == [1, 2, 3]


disable_jinja_block_data = {"document": '{% for x in ["hello", "bye"]%} X {% endfor %}'}


def test_disable_jinja_block():
    state = InterpreterState()
    data = Program.model_validate(disable_jinja_block_data)
    document, _, _, _ = process_prog(state, empty_scope, data)
    assert document == '{% for x in ["hello", "bye"]%} X {% endfor %}'


jinja_block_data = {
    "document": '{%%%%%PDL%%%%%%%%%% for x in ["hello", "bye"]%%%%%PDL%%%%%%%%%%}'
    + " X "
    + "{%%%%%PDL%%%%%%%%%% endfor %%%%%PDL%%%%%%%%%%}"
}


def test_jinja_block():
    state = InterpreterState()
    data = Program.model_validate(jinja_block_data)
    document, _, _, _ = process_prog(state, empty_scope, data)
    assert document == " X  X "

from pdl.pdl_ast import Program, RepeatBlock
from pdl.pdl_interpreter import (
    InterpreterState,
    contains_error,
    empty_scope,
    process_prog,
)

hello = {
    "description": "Hello world!",
    "document": ["Hello, world!\n", "This is your first prompt descriptor!\n"],
}


def repeat_data(n):
    return {
        "description": "Hello world with a nested block",
        "repeat": {
            "document": [
                "Hello, world!\n",
                "This is your first prompt descriptor!\n",
            ]
        },
        "num_iterations": n,
        "as": "document",
    }


def nested_repeat_data(n):
    return {
        "description": "Hello world with a nested block",
        "document": [
            "Hello, world!\n",
            "This is your first prompt descriptor!\n",
            {
                "repeat": ["This sentence repeats!\n"],
                "num_iterations": n,
                "as": "document",
            },
        ],
    }


def test_hello():
    state = InterpreterState()
    data = Program.model_validate(hello)
    document, _, _, _ = process_prog(state, empty_scope, data)
    assert document == "Hello, world!\nThis is your first prompt descriptor!\n"


def repeat(n):
    state = InterpreterState()
    data = Program.model_validate(repeat_data(n))
    document, _, _, _ = process_prog(state, empty_scope, data)
    assert_string = []
    for _ in range(0, n):
        assert_string.append("Hello, world!\n")
        assert_string.append("This is your first prompt descriptor!\n")
    assert document == "".join(assert_string)


def test_repeat_neg():
    repeat(-1)


def test_repeat0():
    repeat(0)


def test_repeat1():
    repeat(1)


def test_repeat2():
    repeat(2)


def test_repeat3():
    repeat(3)


def repeat_nested(n):
    state = InterpreterState()
    data = Program.model_validate(nested_repeat_data(n))
    document, _, _, _ = process_prog(state, empty_scope, data)
    assert_string = ["Hello, world!\n", "This is your first prompt descriptor!\n"]
    for _ in range(0, n):
        assert_string.append("This sentence repeats!\n")
    assert document == "".join(assert_string)


def test_repeat_nested0():
    repeat_nested(0)


def test_repeat_nested1():
    repeat_nested(1)


def test_repeat_nested2():
    repeat_nested(2)


def test_repeat_nested3():
    repeat_nested(3)


repeat_data_error = {
    "description": "Hello world with variable use",
    "repeat": [
        "Hello,",
        {"model": "watsonx/ibm/granite-20b-code-instruct-v", "def": "NAME"},
    ],
    "num_iterations": 3,
}


def test_repeat_error():
    state = InterpreterState()
    data = Program.model_validate(repeat_data_error)
    _, _, _, trace = process_prog(state, empty_scope, data)
    errors = 0
    print(trace)
    if isinstance(trace, RepeatBlock):
        traces = trace.trace or []
        for document in traces:
            if contains_error(document):
                errors += 1

    assert errors == 1

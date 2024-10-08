import yaml

from pdl.pdl_ast import Program
from pdl.pdl_interpreter import InterpreterState, empty_scope, process_prog


def parse_prog_str(prog_str):
    prog_yaml = yaml.safe_load(prog_str)
    prog = Program.model_validate(prog_yaml)
    return prog


def test_role1():
    prog_str = """
description: Test role
document:
- defs:
    ctx1: "{{context}}"
  document: A
  role: A
- Hi
- defs:
    ctx2: "{{context}}"
  document: B
  role: B
role: Top
"""
    prog = parse_prog_str(prog_str)
    state = InterpreterState()
    result, output, scope, _ = process_prog(state, empty_scope, prog)
    assert result == "AHiB"
    assert output == [
        {"role": "A", "content": "A"},
        {"role": "Top", "content": "Hi"},
        {"role": "B", "content": "B"},
    ]
    assert scope["ctx1"] == []
    assert scope["ctx2"] == [
        {"role": "A", "content": "A"},
        {"role": "Top", "content": "Hi"},
    ]

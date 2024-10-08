---
hide:
  - navigation
  - toc
---
# PDL Live Viewer

!!! note
    This is the PDL Live Document viewer. The left pane contains the final result of the program, and upon interaction, the right pane displays the code that created that part of the document, along with a breakdown of the PDL blocks on the left pane.
    To use the tool, upload a json using the following command:
    pdl --trace myresult.json myexample.pdl

<style>
  .pdl_block {
    border-radius: 3px;
    margin: 3px;
    padding: 5px;
    margin: 2px;
    vertical-align: middle;
    display: inline-block;
  }
  .pdl_show_result_false {
    color: rgba(0, 0, 0, 0.5);
  }
  .pdl_string {
    background-color: antiquewhite;
  }
  .pdl_empty {
    background-color: rgb(238, 184, 112);
  }
  .pdl_document {
    background-color: rgb(219, 215, 250);
  }
  .pdl_model {
    background-color: rgb(215, 250, 224);
  }
  .pdl_code {
    background-color: rgb(250, 215, 225);
  }
  .pdl_api {
    background-color: rgb(122, 246, 113);
  }
  .pdl_get {
    background-color: rgb(125, 229, 243);
  }
  .pdl_data {
    background-color: rgb(146, 181, 245);
  }
  .pdl_if {
    background-color: rgb(248, 99, 141);
  }
  .pdl_repeat {
    background-color: rgb(251, 201, 86);
  }
  .pdl_repeat_until {
    background-color: rgb(243, 209, 77);
  }
  .pdl_for {
    background-color: rgb(245, 241, 133);
  }
  .pdl_read {
    background-color: rgb(243, 77, 113);
  }
  .pdl_include {
    background-color: rgb(245, 18, 67);
  }
  .pdl_function {
    background-color: rgb(77, 243, 132);
  }
  .pdl_call {
    background-color: rgb(80, 243, 77);
  }
</style>
<!-- Main script -->
<script src="../dist/bundle.js"></script>
<!-- Multi column layout -->
<link rel="stylesheet" type="text/css" href="https://rawgit.com/vitmalina/w2ui/master/dist/w2ui.min.css">
<!-- Main window -->
<div id="mainview">
  <!-- Main window layout -->
  <input type="file" name="input_file" id="input_file">
  <script type="text/javascript">
      document.getElementById('input_file')
        .addEventListener('change', function () {
          let fr = new FileReader();
          fr.onload = function () {
            data = JSON.parse(fr.result)
            pdl_viewer.replace_div('doc', pdl_viewer.show_output(data))
          }
          fr.readAsText(this.files[0]);
        })
  </script>
  <div id="layout" style="height: 900px;"></div>
  <script type="module">
    import { w2layout } from 'https://rawgit.com/vitmalina/w2ui/master/dist/w2ui.es6.min.js'
    let pstyle = 'border: 1px solid #efefef; padding: 5px'
    new w2layout({
      box: '#layout',
      name: 'layout',
      panels: [
        { type: 'left', size: 600, resizable: true, style: pstyle, html: '<div id="doc"></div>' },
        { type: 'main', style: pstyle, html: '<div id="code">Please click on a word on the left to get started.</div>' }
      ]
    })
  </script>
  <script type="text/javascript">
    const example = {
      "kind": "document",
      "description": "Teaching PDL",
      "defs": {},
      "document": [{
        "kind": "read",
        "defs": {},
        "read": null,
        "message": null,
        "multiline": true,
        "def": "QUERY",
        "show_result": false,
        "result": "Bobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?\n",
        "location": {
          "path": ["document", "[0]"],
          "file": "examples/demo/4-arith-detector.pdl",
          "table": {
            "['description']": 1,
            "['document']": 2,
            "['document', '[0]']": 127,
            "['document', '[0]', 'read']": 3,
            "['document', '[0]', 'multiline']": 4,
            "['document', '[0]', 'def']": 146,
            "['document', '[0]', 'show_result']": 147,
            "['document', '[1]']": 148,
            "['document', '[1]', 'model']": 7,
            "['document', '[1]', 'parameters']": 8,
            "['document', '[1]', 'parameters', 'decoding_method']": 9,
            "['document', '[1]', 'input']": 10,
            "['document', '[1]', 'input', 'document']": 11,
            "['document', '[1]', 'input', 'document', '[0]']": 12,
            "['document', '[1]', 'input', 'document', 'Question']": 13,
            "['document', 'Answer']": 109,
            "['document', 'Question']": 121,
            "['document', '[0]', 'get']": 122,
            "['document', '[1]', 'def']": 124,
            "['document', '[1]', 'show_result']": 125,
            "['document', '[0]', 'model']": 45,
            "['document', '[0]', 'parameters']": 46,
            "['document', '[0]', 'parameters', 'decoding_method']": 47,
            "['document', '[0]', 'input']": 48,
            "['document', '[0]', 'input', 'document']": 49,
            "['document', '[0]', 'input', 'document', '[0]']": 50,
            "['document', '[0]', 'input', 'document', 'Question']": 51,
            "['document', 'description']": 111,
            "['document', 'document']": 112,
            "['document', 'document', '[0]']": 113,
            "['document', 'document', '[1]']": 114,
            "['document', 'while True']": 65,
            "['document', 'try']": 66,
            "['document', 'except EOFError']": 68,
            "['document', 'document', '[0]', 'lan']": 77,
            "['document', 'document', '[0]', 'code']": 78,
            "['document', 'document', '[0]', 'code', '[0]']": 79,
            "['document', 'document', '[0]', 'code', 'while True']": 81,
            "['document', 'document', '[0]', 'code', 'try']": 82,
            "['document', 'document', '[0]', 'code', 'except EOFError']": 84,
            "['document', 'document', '[2]']": 100,
            "['document', 'document', '[2]', 'lan']": 100,
            "['document', 'document', '[2]', 'code']": 101,
            "['document', 'document', '[2]', 'code', '[0]']": 102,
            "['document', 'document', '[3]']": 104,
            "['document', 'document', '[1]', 'lan']": 114,
            "['document', 'document', '[1]', 'code']": 115,
            "['document', 'document', '[1]', 'code', '[0]']": 116,
            "['document', '[0]', 'lan']": 127,
            "['document', '[0]', 'code']": 128,
            "['document', '[0]', 'code', '[0]']": 129,
            "['document', '[0]', 'code', '[1]']": 138,
            "['document', '[0]', 'code', '[1]', 'get']": 138,
            "['document', '[0]', 'code', '[2]']": 139,
            "['document', '[2]']": 149,
            "['document', '[2]', 'model']": 149
          }
        }
      }, {
        "kind": "model",
        "defs": {},
        "model": "ibm/granite-20b-code-instruct-v2",
        "input": {
          "kind": "document",
          "defs": {},
          "document": ["Question: Replace all arithmetic expressions by surrounding them with << >>\nBob had 5 + 2 apples. He ate all them and bought 8 * 67 skittles.\nHe wanted to distribute those among all of 10 children. So each kid\ngot a grand total of 8 * 67 / 10 skittle. Amazing!\n\nAnswer:\nBob had << 5 + 2 >> apples. He ate all them and bought << 8 * 67 >> skittles.\nHe wanted to distribute those among all of 10 children. So each kid\ngot a grand total of << 8 * 67 / 10 >>  skittle. Amazing!\n\nQuestion:\nThe world contains lots of soccer balls. Each team has 5 soccer balls per kid.\nThis team has 30 kids, so the team has 5 * 30 soccer balls.\n\nAnswer:\nThe world contains lots of soccer balls. Each team has 5 soccer balls per kid.\nThis team has 30 kids, so the team has << 5 * 30 >> soccer balls.\n\nQuestion:\nWhat is 5 + 2?\n\nAnswer:\nWhat is << 5 + 2 >>?\n\nQuestion:", {
            "kind": "get",
            "defs": {},
            "get": "QUERY",
            "result": "Bobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?\n",
            "location": {
              "path": ["document", "[1]", "input", "document", "[1]"],
              "file": "examples/demo/4-arith-detector.pdl",
              "table": {
                "['description']": 1,
                "['document']": 2,
                "['document', '[0]']": 127,
                "['document', '[0]', 'read']": 3,
                "['document', '[0]', 'multiline']": 4,
                "['document', '[0]', 'def']": 146,
                "['document', '[0]', 'show_result']": 147,
                "['document', '[1]']": 148,
                "['document', '[1]', 'model']": 7,
                "['document', '[1]', 'parameters']": 8,
                "['document', '[1]', 'parameters', 'decoding_method']": 9,
                "['document', '[1]', 'input']": 10,
                "['document', '[1]', 'input', 'document']": 11,
                "['document', '[1]', 'input', 'document', '[0]']": 12,
                "['document', '[1]', 'input', 'document', 'Question']": 13,
                "['document', 'Answer']": 109,
                "['document', 'Question']": 121,
                "['document', '[0]', 'get']": 122,
                "['document', '[1]', 'def']": 124,
                "['document', '[1]', 'show_result']": 125,
                "['document', '[0]', 'model']": 45,
                "['document', '[0]', 'parameters']": 46,
                "['document', '[0]', 'parameters', 'decoding_method']": 47,
                "['document', '[0]', 'input']": 48,
                "['document', '[0]', 'input', 'document']": 49,
                "['document', '[0]', 'input', 'document', '[0]']": 50,
                "['document', '[0]', 'input', 'document', 'Question']": 51,
                "['document', 'description']": 111,
                "['document', 'document']": 112,
                "['document', 'document', '[0]']": 113,
                "['document', 'document', '[1]']": 114,
                "['document', 'while True']": 65,
                "['document', 'try']": 66,
                "['document', 'except EOFError']": 68,
                "['document', 'document', '[0]', 'lan']": 77,
                "['document', 'document', '[0]', 'code']": 78,
                "['document', 'document', '[0]', 'code', '[0]']": 79,
                "['document', 'document', '[0]', 'code', 'while True']": 81,
                "['document', 'document', '[0]', 'code', 'try']": 82,
                "['document', 'document', '[0]', 'code', 'except EOFError']": 84,
                "['document', 'document', '[2]']": 100,
                "['document', 'document', '[2]', 'lan']": 100,
                "['document', 'document', '[2]', 'code']": 101,
                "['document', 'document', '[2]', 'code', '[0]']": 102,
                "['document', 'document', '[3]']": 104,
                "['document', 'document', '[1]', 'lan']": 114,
                "['document', 'document', '[1]', 'code']": 115,
                "['document', 'document', '[1]', 'code', '[0]']": 116,
                "['document', '[0]', 'lan']": 127,
                "['document', '[0]', 'code']": 128,
                "['document', '[0]', 'code', '[0]']": 129,
                "['document', '[0]', 'code', '[1]']": 138,
                "['document', '[0]', 'code', '[1]', 'get']": 138,
                "['document', '[0]', 'code', '[2]']": 139,
                "['document', '[2]']": 149,
                "['document', '[2]', 'model']": 149
              }
            }
          }, "\n\n"],
          "result": "Question: Replace all arithmetic expressions by surrounding them with << >>\nBob had 5 + 2 apples. He ate all them and bought 8 * 67 skittles.\nHe wanted to distribute those among all of 10 children. So each kid\ngot a grand total of 8 * 67 / 10 skittle. Amazing!\n\nAnswer:\nBob had << 5 + 2 >> apples. He ate all them and bought << 8 * 67 >> skittles.\nHe wanted to distribute those among all of 10 children. So each kid\ngot a grand total of << 8 * 67 / 10 >>  skittle. Amazing!\n\nQuestion:\nThe world contains lots of soccer balls. Each team has 5 soccer balls per kid.\nThis team has 30 kids, so the team has 5 * 30 soccer balls.\n\nAnswer:\nThe world contains lots of soccer balls. Each team has 5 soccer balls per kid.\nThis team has 30 kids, so the team has << 5 * 30 >> soccer balls.\n\nQuestion:\nWhat is 5 + 2?\n\nAnswer:\nWhat is << 5 + 2 >>?\n\nQuestion:Bobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?\n\n\n",
          "location": {
            "path": ["document", "[1]", "input"],
            "file": "examples/demo/4-arith-detector.pdl",
            "table": {
              "['description']": 1,
              "['document']": 2,
              "['document', '[0]']": 127,
              "['document', '[0]', 'read']": 3,
              "['document', '[0]', 'multiline']": 4,
              "['document', '[0]', 'def']": 146,
              "['document', '[0]', 'show_result']": 147,
              "['document', '[1]']": 148,
              "['document', '[1]', 'model']": 7,
              "['document', '[1]', 'parameters']": 8,
              "['document', '[1]', 'parameters', 'decoding_method']": 9,
              "['document', '[1]', 'input']": 10,
              "['document', '[1]', 'input', 'document']": 11,
              "['document', '[1]', 'input', 'document', '[0]']": 12,
              "['document', '[1]', 'input', 'document', 'Question']": 13,
              "['document', 'Answer']": 109,
              "['document', 'Question']": 121,
              "['document', '[0]', 'get']": 122,
              "['document', '[1]', 'def']": 124,
              "['document', '[1]', 'show_result']": 125,
              "['document', '[0]', 'model']": 45,
              "['document', '[0]', 'parameters']": 46,
              "['document', '[0]', 'parameters', 'decoding_method']": 47,
              "['document', '[0]', 'input']": 48,
              "['document', '[0]', 'input', 'document']": 49,
              "['document', '[0]', 'input', 'document', '[0]']": 50,
              "['document', '[0]', 'input', 'document', 'Question']": 51,
              "['document', 'description']": 111,
              "['document', 'document']": 112,
              "['document', 'document', '[0]']": 113,
              "['document', 'document', '[1]']": 114,
              "['document', 'while True']": 65,
              "['document', 'try']": 66,
              "['document', 'except EOFError']": 68,
              "['document', 'document', '[0]', 'lan']": 77,
              "['document', 'document', '[0]', 'code']": 78,
              "['document', 'document', '[0]', 'code', '[0]']": 79,
              "['document', 'document', '[0]', 'code', 'while True']": 81,
              "['document', 'document', '[0]', 'code', 'try']": 82,
              "['document', 'document', '[0]', 'code', 'except EOFError']": 84,
              "['document', 'document', '[2]']": 100,
              "['document', 'document', '[2]', 'lan']": 100,
              "['document', 'document', '[2]', 'code']": 101,
              "['document', 'document', '[2]', 'code', '[0]']": 102,
              "['document', 'document', '[3]']": 104,
              "['document', 'document', '[1]', 'lan']": 114,
              "['document', 'document', '[1]', 'code']": 115,
              "['document', 'document', '[1]', 'code', '[0]']": 116,
              "['document', '[0]', 'lan']": 127,
              "['document', '[0]', 'code']": 128,
              "['document', '[0]', 'code', '[0]']": 129,
              "['document', '[0]', 'code', '[1]']": 138,
              "['document', '[0]', 'code', '[1]', 'get']": 138,
              "['document', '[0]', 'code', '[2]']": 139,
              "['document', '[2]']": 149,
              "['document', '[2]', 'model']": 149
            }
          }
        },
        "parameters": {
          "decoding_method": "greedy",
          "max_new_tokens": 1024,
          "min_new_tokens": 1,
          "repetition_penalty": 1.05
        },
        "def": "QUERY1",
        "show_result": false,
        "result": "\nAnswer:\nBobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?",
        "location": {
          "path": ["document", "[1]"],
          "file": "examples/demo/4-arith-detector.pdl",
          "table": {
            "['description']": 1,
            "['document']": 2,
            "['document', '[0]']": 127,
            "['document', '[0]', 'read']": 3,
            "['document', '[0]', 'multiline']": 4,
            "['document', '[0]', 'def']": 146,
            "['document', '[0]', 'show_result']": 147,
            "['document', '[1]']": 148,
            "['document', '[1]', 'model']": 7,
            "['document', '[1]', 'parameters']": 8,
            "['document', '[1]', 'parameters', 'decoding_method']": 9,
            "['document', '[1]', 'input']": 10,
            "['document', '[1]', 'input', 'document']": 11,
            "['document', '[1]', 'input', 'document', '[0]']": 12,
            "['document', '[1]', 'input', 'document', 'Question']": 13,
            "['document', 'Answer']": 109,
            "['document', 'Question']": 121,
            "['document', '[0]', 'get']": 122,
            "['document', '[1]', 'def']": 124,
            "['document', '[1]', 'show_result']": 125,
            "['document', '[0]', 'model']": 45,
            "['document', '[0]', 'parameters']": 46,
            "['document', '[0]', 'parameters', 'decoding_method']": 47,
            "['document', '[0]', 'input']": 48,
            "['document', '[0]', 'input', 'document']": 49,
            "['document', '[0]', 'input', 'document', '[0]']": 50,
            "['document', '[0]', 'input', 'document', 'Question']": 51,
            "['document', 'description']": 111,
            "['document', 'document']": 112,
            "['document', 'document', '[0]']": 113,
            "['document', 'document', '[1]']": 114,
            "['document', 'while True']": 65,
            "['document', 'try']": 66,
            "['document', 'except EOFError']": 68,
            "['document', 'document', '[0]', 'lan']": 77,
            "['document', 'document', '[0]', 'code']": 78,
            "['document', 'document', '[0]', 'code', '[0]']": 79,
            "['document', 'document', '[0]', 'code', 'while True']": 81,
            "['document', 'document', '[0]', 'code', 'try']": 82,
            "['document', 'document', '[0]', 'code', 'except EOFError']": 84,
            "['document', 'document', '[2]']": 100,
            "['document', 'document', '[2]', 'lan']": 100,
            "['document', 'document', '[2]', 'code']": 101,
            "['document', 'document', '[2]', 'code', '[0]']": 102,
            "['document', 'document', '[3]']": 104,
            "['document', 'document', '[1]', 'lan']": 114,
            "['document', 'document', '[1]', 'code']": 115,
            "['document', 'document', '[1]', 'code', '[0]']": 116,
            "['document', '[0]', 'lan']": 127,
            "['document', '[0]', 'code']": 128,
            "['document', '[0]', 'code', '[0]']": 129,
            "['document', '[0]', 'code', '[1]']": 138,
            "['document', '[0]', 'code', '[1]', 'get']": 138,
            "['document', '[0]', 'code', '[2]']": 139,
            "['document', '[2]']": 149,
            "['document', '[2]', 'model']": 149
          }
        }
      }, {
        "kind": "model",
        "defs": {},
        "model": "ibm/granite-20b-code-instruct-v2",
        "input": {
          "kind": "document",
          "defs": {},
          "document": ["Question: Write the following prompts in PDL:\nHello world!\nThis is your first prompt descriptor!\n\nAnswer:\n```\ndescription: Hello world!\ndocument:\n- \"Hello, world!\\n\"\n- \"This is your first prompt descriptor!\\n\"      \n```\n\nQuestion: Turn the code into PDL:\ncontents = []\nwhile True:\ntry:\n  line = input()\nexcept EOFError:\n  break\ncontents.append(line + \"\\n\")\nresult = ''.join(contents)\n\nAnswer:\n```\ndescription: Example of PDL code block\ndocument:\n- lan: python\n  code:\n  - |\n    contents = []\n    while True:\n    try:\n      line = input()\n    except EOFError:\n      break\n    contents.append(line + \"\\n\")\n    result = ''.join(contents)\n```\n\nQuestion: Write the following in PDL where the parts in << >> are done in Python.\nHello world!\nThis is your << expr >> prompt descriptor!\n\nAnswer:\n```\ndescription: Hello world!\ndocument:\n- \"Hello, world!\\n\"\n- \"This is your \"\n- lan: python\n  code:\n  - |\n    result = expr\n- \" prompt descriptor!\"\n```\nQuestion: Write the following in PDL where the parts in << >> are done in Python.\nWhat is << 67+ 67 - 78 + 2 >>\n\nAnswer:\n```\ndescription: Hello world!\ndocument:\n- \"What is \"\n- lan: python\n  code:\n  - |\n    result = 67+ 67 - 78 + 2\n```\n\n\nQuestion: Write the following in PDL with parts << >> written in Python", {
            "kind": "get",
            "defs": {},
            "get": "QUERY1",
            "result": "\nAnswer:\nBobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?",
            "location": {
              "path": ["document", "[2]", "input", "document", "[1]"],
              "file": "examples/demo/4-arith-detector.pdl",
              "table": {
                "['description']": 1,
                "['document']": 2,
                "['document', '[0]']": 127,
                "['document', '[0]', 'read']": 3,
                "['document', '[0]', 'multiline']": 4,
                "['document', '[0]', 'def']": 146,
                "['document', '[0]', 'show_result']": 147,
                "['document', '[1]']": 148,
                "['document', '[1]', 'model']": 7,
                "['document', '[1]', 'parameters']": 8,
                "['document', '[1]', 'parameters', 'decoding_method']": 9,
                "['document', '[1]', 'input']": 10,
                "['document', '[1]', 'input', 'document']": 11,
                "['document', '[1]', 'input', 'document', '[0]']": 12,
                "['document', '[1]', 'input', 'document', 'Question']": 13,
                "['document', 'Answer']": 109,
                "['document', 'Question']": 121,
                "['document', '[0]', 'get']": 122,
                "['document', '[1]', 'def']": 124,
                "['document', '[1]', 'show_result']": 125,
                "['document', '[0]', 'model']": 45,
                "['document', '[0]', 'parameters']": 46,
                "['document', '[0]', 'parameters', 'decoding_method']": 47,
                "['document', '[0]', 'input']": 48,
                "['document', '[0]', 'input', 'document']": 49,
                "['document', '[0]', 'input', 'document', '[0]']": 50,
                "['document', '[0]', 'input', 'document', 'Question']": 51,
                "['document', 'description']": 111,
                "['document', 'document']": 112,
                "['document', 'document', '[0]']": 113,
                "['document', 'document', '[1]']": 114,
                "['document', 'while True']": 65,
                "['document', 'try']": 66,
                "['document', 'except EOFError']": 68,
                "['document', 'document', '[0]', 'lan']": 77,
                "['document', 'document', '[0]', 'code']": 78,
                "['document', 'document', '[0]', 'code', '[0]']": 79,
                "['document', 'document', '[0]', 'code', 'while True']": 81,
                "['document', 'document', '[0]', 'code', 'try']": 82,
                "['document', 'document', '[0]', 'code', 'except EOFError']": 84,
                "['document', 'document', '[2]']": 100,
                "['document', 'document', '[2]', 'lan']": 100,
                "['document', 'document', '[2]', 'code']": 101,
                "['document', 'document', '[2]', 'code', '[0]']": 102,
                "['document', 'document', '[3]']": 104,
                "['document', 'document', '[1]', 'lan']": 114,
                "['document', 'document', '[1]', 'code']": 115,
                "['document', 'document', '[1]', 'code', '[0]']": 116,
                "['document', '[0]', 'lan']": 127,
                "['document', '[0]', 'code']": 128,
                "['document', '[0]', 'code', '[0]']": 129,
                "['document', '[0]', 'code', '[1]']": 138,
                "['document', '[0]', 'code', '[1]', 'get']": 138,
                "['document', '[0]', 'code', '[2]']": 139,
                "['document', '[2]']": 149,
                "['document', '[2]', 'model']": 149
              }
            }
          }, "\n\n"],
          "result": "Question: Write the following prompts in PDL:\nHello world!\nThis is your first prompt descriptor!\n\nAnswer:\n```\ndescription: Hello world!\ndocument:\n- \"Hello, world!\\n\"\n- \"This is your first prompt descriptor!\\n\"      \n```\n\nQuestion: Turn the code into PDL:\ncontents = []\nwhile True:\ntry:\n  line = input()\nexcept EOFError:\n  break\ncontents.append(line + \"\\n\")\nresult = ''.join(contents)\n\nAnswer:\n```\ndescription: Example of PDL code block\ndocument:\n- lan: python\n  code:\n  - |\n    contents = []\n    while True:\n    try:\n      line = input()\n    except EOFError:\n      break\n    contents.append(line + \"\\n\")\n    result = ''.join(contents)\n```\n\nQuestion: Write the following in PDL where the parts in << >> are done in Python.\nHello world!\nThis is your << expr >> prompt descriptor!\n\nAnswer:\n```\ndescription: Hello world!\ndocument:\n- \"Hello, world!\\n\"\n- \"This is your \"\n- lan: python\n  code:\n  - |\n    result = expr\n- \" prompt descriptor!\"\n```\nQuestion: Write the following in PDL where the parts in << >> are done in Python.\nWhat is << 67+ 67 - 78 + 2 >>\n\nAnswer:\n```\ndescription: Hello world!\ndocument:\n- \"What is \"\n- lan: python\n  code:\n  - |\n    result = 67+ 67 - 78 + 2\n```\n\n\nQuestion: Write the following in PDL with parts << >> written in Python\nAnswer:\nBobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?\n\n",
          "location": {
            "path": ["document", "[2]", "input"],
            "file": "examples/demo/4-arith-detector.pdl",
            "table": {
              "['description']": 1,
              "['document']": 2,
              "['document', '[0]']": 127,
              "['document', '[0]', 'read']": 3,
              "['document', '[0]', 'multiline']": 4,
              "['document', '[0]', 'def']": 146,
              "['document', '[0]', 'show_result']": 147,
              "['document', '[1]']": 148,
              "['document', '[1]', 'model']": 7,
              "['document', '[1]', 'parameters']": 8,
              "['document', '[1]', 'parameters', 'decoding_method']": 9,
              "['document', '[1]', 'input']": 10,
              "['document', '[1]', 'input', 'document']": 11,
              "['document', '[1]', 'input', 'document', '[0]']": 12,
              "['document', '[1]', 'input', 'document', 'Question']": 13,
              "['document', 'Answer']": 109,
              "['document', 'Question']": 121,
              "['document', '[0]', 'get']": 122,
              "['document', '[1]', 'def']": 124,
              "['document', '[1]', 'show_result']": 125,
              "['document', '[0]', 'model']": 45,
              "['document', '[0]', 'parameters']": 46,
              "['document', '[0]', 'parameters', 'decoding_method']": 47,
              "['document', '[0]', 'input']": 48,
              "['document', '[0]', 'input', 'document']": 49,
              "['document', '[0]', 'input', 'document', '[0]']": 50,
              "['document', '[0]', 'input', 'document', 'Question']": 51,
              "['document', 'description']": 111,
              "['document', 'document']": 112,
              "['document', 'document', '[0]']": 113,
              "['document', 'document', '[1]']": 114,
              "['document', 'while True']": 65,
              "['document', 'try']": 66,
              "['document', 'except EOFError']": 68,
              "['document', 'document', '[0]', 'lan']": 77,
              "['document', 'document', '[0]', 'code']": 78,
              "['document', 'document', '[0]', 'code', '[0]']": 79,
              "['document', 'document', '[0]', 'code', 'while True']": 81,
              "['document', 'document', '[0]', 'code', 'try']": 82,
              "['document', 'document', '[0]', 'code', 'except EOFError']": 84,
              "['document', 'document', '[2]']": 100,
              "['document', 'document', '[2]', 'lan']": 100,
              "['document', 'document', '[2]', 'code']": 101,
              "['document', 'document', '[2]', 'code', '[0]']": 102,
              "['document', 'document', '[3]']": 104,
              "['document', 'document', '[1]', 'lan']": 114,
              "['document', 'document', '[1]', 'code']": 115,
              "['document', 'document', '[1]', 'code', '[0]']": 116,
              "['document', '[0]', 'lan']": 127,
              "['document', '[0]', 'code']": 128,
              "['document', '[0]', 'code', '[0]']": 129,
              "['document', '[0]', 'code', '[1]']": 138,
              "['document', '[0]', 'code', '[1]', 'get']": 138,
              "['document', '[0]', 'code', '[2]']": 139,
              "['document', '[2]']": 149,
              "['document', '[2]', 'model']": 149
            }
          }
        },
        "parameters": {
          "decoding_method": "greedy",
          "max_new_tokens": 1024,
          "min_new_tokens": 1,
          "repetition_penalty": 1.05
        },
        "def": "PDL",
        "show_result": false,
        "result": "\nAnswer:\n```\ndescription: Bobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?\ndocument:\n- \"Bobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?\"\n```",
        "location": {
          "path": ["document", "[2]"],
          "file": "examples/demo/4-arith-detector.pdl",
          "table": {
            "['description']": 1,
            "['document']": 2,
            "['document', '[0]']": 127,
            "['document', '[0]', 'read']": 3,
            "['document', '[0]', 'multiline']": 4,
            "['document', '[0]', 'def']": 146,
            "['document', '[0]', 'show_result']": 147,
            "['document', '[1]']": 148,
            "['document', '[1]', 'model']": 7,
            "['document', '[1]', 'parameters']": 8,
            "['document', '[1]', 'parameters', 'decoding_method']": 9,
            "['document', '[1]', 'input']": 10,
            "['document', '[1]', 'input', 'document']": 11,
            "['document', '[1]', 'input', 'document', '[0]']": 12,
            "['document', '[1]', 'input', 'document', 'Question']": 13,
            "['document', 'Answer']": 109,
            "['document', 'Question']": 121,
            "['document', '[0]', 'get']": 122,
            "['document', '[1]', 'def']": 124,
            "['document', '[1]', 'show_result']": 125,
            "['document', '[0]', 'model']": 45,
            "['document', '[0]', 'parameters']": 46,
            "['document', '[0]', 'parameters', 'decoding_method']": 47,
            "['document', '[0]', 'input']": 48,
            "['document', '[0]', 'input', 'document']": 49,
            "['document', '[0]', 'input', 'document', '[0]']": 50,
            "['document', '[0]', 'input', 'document', 'Question']": 51,
            "['document', 'description']": 111,
            "['document', 'document']": 112,
            "['document', 'document', '[0]']": 113,
            "['document', 'document', '[1]']": 114,
            "['document', 'while True']": 65,
            "['document', 'try']": 66,
            "['document', 'except EOFError']": 68,
            "['document', 'document', '[0]', 'lan']": 77,
            "['document', 'document', '[0]', 'code']": 78,
            "['document', 'document', '[0]', 'code', '[0]']": 79,
            "['document', 'document', '[0]', 'code', 'while True']": 81,
            "['document', 'document', '[0]', 'code', 'try']": 82,
            "['document', 'document', '[0]', 'code', 'except EOFError']": 84,
            "['document', 'document', '[2]']": 100,
            "['document', 'document', '[2]', 'lan']": 100,
            "['document', 'document', '[2]', 'code']": 101,
            "['document', 'document', '[2]', 'code', '[0]']": 102,
            "['document', 'document', '[3]']": 104,
            "['document', 'document', '[1]', 'lan']": 114,
            "['document', 'document', '[1]', 'code']": 115,
            "['document', 'document', '[1]', 'code', '[0]']": 116,
            "['document', '[0]', 'lan']": 127,
            "['document', '[0]', 'code']": 128,
            "['document', '[0]', 'code', '[0]']": 129,
            "['document', '[0]', 'code', '[1]']": 138,
            "['document', '[0]', 'code', '[1]', 'get']": 138,
            "['document', '[0]', 'code', '[2]']": 139,
            "['document', '[2]']": 149,
            "['document', '[2]', 'model']": 149
          }
        }
      }, {
        "kind": "code",
        "defs": {},
        "lan": "python",
        "code": ["from pdl import pdl_ast, pdl_interpreter\nfrom pdl.pdl_ast import Program\nfrom pdl.pdl_interpreter import process_prog\nfrom pdl.pdl_interpreter import InterpreterState\nfrom pdl.pdl_interpreter import empty_scope\nimport re\nimport yaml\ns = \"\"\"'\n", {
          "kind": "get",
          "defs": {},
          "get": "PDL",
          "result": "\nAnswer:\n```\ndescription: Bobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?\ndocument:\n- \"Bobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?\"\n```",
          "location": {
            "path": ["document", "[3]", "code", "[1]"],
            "file": "examples/demo/4-arith-detector.pdl",
            "table": {
              "['description']": 1,
              "['document']": 2,
              "['document', '[0]']": 127,
              "['document', '[0]', 'read']": 3,
              "['document', '[0]', 'multiline']": 4,
              "['document', '[0]', 'def']": 146,
              "['document', '[0]', 'show_result']": 147,
              "['document', '[1]']": 148,
              "['document', '[1]', 'model']": 7,
              "['document', '[1]', 'parameters']": 8,
              "['document', '[1]', 'parameters', 'decoding_method']": 9,
              "['document', '[1]', 'input']": 10,
              "['document', '[1]', 'input', 'document']": 11,
              "['document', '[1]', 'input', 'document', '[0]']": 12,
              "['document', '[1]', 'input', 'document', 'Question']": 13,
              "['document', 'Answer']": 109,
              "['document', 'Question']": 121,
              "['document', '[0]', 'get']": 122,
              "['document', '[1]', 'def']": 124,
              "['document', '[1]', 'show_result']": 125,
              "['document', '[0]', 'model']": 45,
              "['document', '[0]', 'parameters']": 46,
              "['document', '[0]', 'parameters', 'decoding_method']": 47,
              "['document', '[0]', 'input']": 48,
              "['document', '[0]', 'input', 'document']": 49,
              "['document', '[0]', 'input', 'document', '[0]']": 50,
              "['document', '[0]', 'input', 'document', 'Question']": 51,
              "['document', 'description']": 111,
              "['document', 'document']": 112,
              "['document', 'document', '[0]']": 113,
              "['document', 'document', '[1]']": 114,
              "['document', 'while True']": 65,
              "['document', 'try']": 66,
              "['document', 'except EOFError']": 68,
              "['document', 'document', '[0]', 'lan']": 77,
              "['document', 'document', '[0]', 'code']": 78,
              "['document', 'document', '[0]', 'code', '[0]']": 79,
              "['document', 'document', '[0]', 'code', 'while True']": 81,
              "['document', 'document', '[0]', 'code', 'try']": 82,
              "['document', 'document', '[0]', 'code', 'except EOFError']": 84,
              "['document', 'document', '[2]']": 100,
              "['document', 'document', '[2]', 'lan']": 100,
              "['document', 'document', '[2]', 'code']": 101,
              "['document', 'document', '[2]', 'code', '[0]']": 102,
              "['document', 'document', '[3]']": 104,
              "['document', 'document', '[1]', 'lan']": 114,
              "['document', 'document', '[1]', 'code']": 115,
              "['document', 'document', '[1]', 'code', '[0]']": 116,
              "['document', '[0]', 'lan']": 127,
              "['document', '[0]', 'code']": 128,
              "['document', '[0]', 'code', '[0]']": 129,
              "['document', '[0]', 'code', '[1]']": 138,
              "['document', '[0]', 'code', '[1]', 'get']": 138,
              "['document', '[0]', 'code', '[2]']": 139,
              "['document', '[2]']": 149,
              "['document', '[2]', 'model']": 149
            }
          }
        }, "'\"\"\"\npdl = s.split(\"```\")[1]\nobj = yaml.safe_load(pdl)\nstate = InterpreterState()\ndata = Program.model_validate(obj)\n_, result, _, _ = process_prog(state, empty_scope, data)\n"],
        "def": "RESULT",
        "result": "Bobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?",
        "location": {
          "path": ["document", "[3]"],
          "file": "examples/demo/4-arith-detector.pdl",
          "table": {
            "['description']": 1,
            "['document']": 2,
            "['document', '[0]']": 127,
            "['document', '[0]', 'read']": 3,
            "['document', '[0]', 'multiline']": 4,
            "['document', '[0]', 'def']": 146,
            "['document', '[0]', 'show_result']": 147,
            "['document', '[1]']": 148,
            "['document', '[1]', 'model']": 7,
            "['document', '[1]', 'parameters']": 8,
            "['document', '[1]', 'parameters', 'decoding_method']": 9,
            "['document', '[1]', 'input']": 10,
            "['document', '[1]', 'input', 'document']": 11,
            "['document', '[1]', 'input', 'document', '[0]']": 12,
            "['document', '[1]', 'input', 'document', 'Question']": 13,
            "['document', 'Answer']": 109,
            "['document', 'Question']": 121,
            "['document', '[0]', 'get']": 122,
            "['document', '[1]', 'def']": 124,
            "['document', '[1]', 'show_result']": 125,
            "['document', '[0]', 'model']": 45,
            "['document', '[0]', 'parameters']": 46,
            "['document', '[0]', 'parameters', 'decoding_method']": 47,
            "['document', '[0]', 'input']": 48,
            "['document', '[0]', 'input', 'document']": 49,
            "['document', '[0]', 'input', 'document', '[0]']": 50,
            "['document', '[0]', 'input', 'document', 'Question']": 51,
            "['document', 'description']": 111,
            "['document', 'document']": 112,
            "['document', 'document', '[0]']": 113,
            "['document', 'document', '[1]']": 114,
            "['document', 'while True']": 65,
            "['document', 'try']": 66,
            "['document', 'except EOFError']": 68,
            "['document', 'document', '[0]', 'lan']": 77,
            "['document', 'document', '[0]', 'code']": 78,
            "['document', 'document', '[0]', 'code', '[0]']": 79,
            "['document', 'document', '[0]', 'code', 'while True']": 81,
            "['document', 'document', '[0]', 'code', 'try']": 82,
            "['document', 'document', '[0]', 'code', 'except EOFError']": 84,
            "['document', 'document', '[2]']": 100,
            "['document', 'document', '[2]', 'lan']": 100,
            "['document', 'document', '[2]', 'code']": 101,
            "['document', 'document', '[2]', 'code', '[0]']": 102,
            "['document', 'document', '[3]']": 104,
            "['document', 'document', '[1]', 'lan']": 114,
            "['document', 'document', '[1]', 'code']": 115,
            "['document', 'document', '[1]', 'code', '[0]']": 116,
            "['document', '[0]', 'lan']": 127,
            "['document', '[0]', 'code']": 128,
            "['document', '[0]', 'code', '[0]']": 129,
            "['document', '[0]', 'code', '[1]']": 138,
            "['document', '[0]', 'code', '[1]', 'get']": 138,
            "['document', '[0]', 'code', '[2]']": 139,
            "['document', '[2]']": 149,
            "['document', '[2]', 'model']": 149
          }
        }
      }, "\n", {
        "kind": "model",
        "defs": {},
        "model": "ibm/granite-13b-instruct-v2",
        "result": "5",
        "location": {
          "path": ["document", "[5]"],
          "file": "examples/demo/4-arith-detector.pdl",
          "table": {
            "['description']": 1,
            "['document']": 2,
            "['document', '[0]']": 127,
            "['document', '[0]', 'read']": 3,
            "['document', '[0]', 'multiline']": 4,
            "['document', '[0]', 'def']": 146,
            "['document', '[0]', 'show_result']": 147,
            "['document', '[1]']": 148,
            "['document', '[1]', 'model']": 7,
            "['document', '[1]', 'parameters']": 8,
            "['document', '[1]', 'parameters', 'decoding_method']": 9,
            "['document', '[1]', 'input']": 10,
            "['document', '[1]', 'input', 'document']": 11,
            "['document', '[1]', 'input', 'document', '[0]']": 12,
            "['document', '[1]', 'input', 'document', 'Question']": 13,
            "['document', 'Answer']": 109,
            "['document', 'Question']": 121,
            "['document', '[0]', 'get']": 122,
            "['document', '[1]', 'def']": 124,
            "['document', '[1]', 'show_result']": 125,
            "['document', '[0]', 'model']": 45,
            "['document', '[0]', 'parameters']": 46,
            "['document', '[0]', 'parameters', 'decoding_method']": 47,
            "['document', '[0]', 'input']": 48,
            "['document', '[0]', 'input', 'document']": 49,
            "['document', '[0]', 'input', 'document', '[0]']": 50,
            "['document', '[0]', 'input', 'document', 'Question']": 51,
            "['document', 'description']": 111,
            "['document', 'document']": 112,
            "['document', 'document', '[0]']": 113,
            "['document', 'document', '[1]']": 114,
            "['document', 'while True']": 65,
            "['document', 'try']": 66,
            "['document', 'except EOFError']": 68,
            "['document', 'document', '[0]', 'lan']": 77,
            "['document', 'document', '[0]', 'code']": 78,
            "['document', 'document', '[0]', 'code', '[0]']": 79,
            "['document', 'document', '[0]', 'code', 'while True']": 81,
            "['document', 'document', '[0]', 'code', 'try']": 82,
            "['document', 'document', '[0]', 'code', 'except EOFError']": 84,
            "['document', 'document', '[2]']": 100,
            "['document', 'document', '[2]', 'lan']": 100,
            "['document', 'document', '[2]', 'code']": 101,
            "['document', 'document', '[2]', 'code', '[0]']": 102,
            "['document', 'document', '[3]']": 104,
            "['document', 'document', '[1]', 'lan']": 114,
            "['document', 'document', '[1]', 'code']": 115,
            "['document', 'document', '[1]', 'code', '[0]']": 116,
            "['document', '[0]', 'lan']": 127,
            "['document', '[0]', 'code']": 128,
            "['document', '[0]', 'code', '[0]']": 129,
            "['document', '[0]', 'code', '[1]']": 138,
            "['document', '[0]', 'code', '[1]', 'get']": 138,
            "['document', '[0]', 'code', '[2]']": 139,
            "['document', '[2]']": 149,
            "['document', '[2]', 'model']": 149
          }
        }
      }],
      "result": "Bobby had 3 apples. He then added 2. Hence 3 + 2 = 5 How many apple did Bobby have?\n5",
      "location": {
        "path": [],
        "file": "examples/demo/4-arith-detector.pdl",
        "table": {
          "['description']": 1,
          "['document']": 2,
          "['document', '[0]']": 127,
          "['document', '[0]', 'read']": 3,
          "['document', '[0]', 'multiline']": 4,
          "['document', '[0]', 'def']": 146,
          "['document', '[0]', 'show_result']": 147,
          "['document', '[1]']": 148,
          "['document', '[1]', 'model']": 7,
          "['document', '[1]', 'parameters']": 8,
          "['document', '[1]', 'parameters', 'decoding_method']": 9,
          "['document', '[1]', 'input']": 10,
          "['document', '[1]', 'input', 'document']": 11,
          "['document', '[1]', 'input', 'document', '[0]']": 12,
          "['document', '[1]', 'input', 'document', 'Question']": 13,
          "['document', 'Answer']": 109,
          "['document', 'Question']": 121,
          "['document', '[0]', 'get']": 122,
          "['document', '[1]', 'def']": 124,
          "['document', '[1]', 'show_result']": 125,
          "['document', '[0]', 'model']": 45,
          "['document', '[0]', 'parameters']": 46,
          "['document', '[0]', 'parameters', 'decoding_method']": 47,
          "['document', '[0]', 'input']": 48,
          "['document', '[0]', 'input', 'document']": 49,
          "['document', '[0]', 'input', 'document', '[0]']": 50,
          "['document', '[0]', 'input', 'document', 'Question']": 51,
          "['document', 'description']": 111,
          "['document', 'document']": 112,
          "['document', 'document', '[0]']": 113,
          "['document', 'document', '[1]']": 114,
          "['document', 'while True']": 65,
          "['document', 'try']": 66,
          "['document', 'except EOFError']": 68,
          "['document', 'document', '[0]', 'lan']": 77,
          "['document', 'document', '[0]', 'code']": 78,
          "['document', 'document', '[0]', 'code', '[0]']": 79,
          "['document', 'document', '[0]', 'code', 'while True']": 81,
          "['document', 'document', '[0]', 'code', 'try']": 82,
          "['document', 'document', '[0]', 'code', 'except EOFError']": 84,
          "['document', 'document', '[2]']": 100,
          "['document', 'document', '[2]', 'lan']": 100,
          "['document', 'document', '[2]', 'code']": 101,
          "['document', 'document', '[2]', 'code', '[0]']": 102,
          "['document', 'document', '[3]']": 104,
          "['document', 'document', '[1]', 'lan']": 114,
          "['document', 'document', '[1]', 'code']": 115,
          "['document', 'document', '[1]', 'code', '[0]']": 116,
          "['document', '[0]', 'lan']": 127,
          "['document', '[0]', 'code']": 128,
          "['document', '[0]', 'code', '[0]']": 129,
          "['document', '[0]', 'code', '[1]']": 138,
          "['document', '[0]', 'code', '[1]', 'get']": 138,
          "['document', '[0]', 'code', '[2]']": 139,
          "['document', '[2]']": 149,
          "['document', '[2]', 'model']": 149
        }
      }
    }
    window.addEventListener("load", function () {
      pdl_viewer.replace_div('doc', pdl_viewer.show_output(example))
    });
  </script>
</div>
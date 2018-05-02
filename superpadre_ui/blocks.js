
/********************************* 
Function calls
***********************************/
Blockly.Blocks['new_function'] = {
    init: function() {
      this.appendValueInput("params")
          .setCheck(null)
          .appendField(new Blockly.FieldDropdown([["void","void"], ["int","int"], ["float","float"], ["string","string"], ["boolean","boolean"]]), "func_type")
          .appendField(new Blockly.FieldTextInput("name of function"), "func_name")
          .appendField("(");
      this.appendDummyInput()
          .appendField(")");
      this.appendStatementInput("content")
          .setCheck(null);
      this.setPreviousStatement(true);
      this.setNextStatement(true);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['new_function'] = function(block) {
    var dropdown_func_type = block.getFieldValue('func_type');
    var text_func_name = block.getFieldValue('func_name');
    var value_params = Blockly.JavaScript.valueToCode(block, 'params', Blockly.JavaScript.ORDER_ATOMIC);
    var statements_content = Blockly.JavaScript.statementToCode(block, 'content');
    var value_params = value_params.replace(/int|string|float|boolean/g, function(word){
        return ', ' + word;
    }).replace(', ','');
    // TODO: Assemble JavaScript into code variable.
    var code = dropdown_func_type + ' ' + text_func_name + '(' + value_params + ') {\n' + statements_content + '}\n';
    return code;
  };


Blockly.Blocks['call_function'] = {
    init: function() {
      this.appendValueInput("func_call")
          .setCheck(null)
          .appendField(new Blockly.FieldTextInput("name of function"), "func_name")
          .appendField("(");
      this.appendDummyInput()
          .appendField(")");
      this.setPreviousStatement(true);
      this.setNextStatement(true);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
};

Blockly.JavaScript['call_function'] = function(block) {
    var text_func_name = block.getFieldValue('func_name');
    var value_func_call = Blockly.JavaScript.valueToCode(block, 'func_call', Blockly.JavaScript.ORDER_ATOMIC);
    value_func_call = value_func_call.substring(1);
    if (value_func_call.split(' ').length > 1){
        value_func_call = value_func_call.replace(/ /g, ', ');
    }
    var code = text_func_name + '(' + value_func_call +');';
    return code;
  };

Blockly.Blocks['assign_function'] = {
    init: function() {
      this.appendValueInput("func_call")
          .setCheck(null)
          .appendField(new Blockly.FieldTextInput("name of function"), "func_name")
          .appendField("(");
      this.appendDummyInput()
          .appendField(")");
      this.setOutput(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['assign_function'] = function(block) {
    var text_func_name = block.getFieldValue('func_name');
    var value_func_call = Blockly.JavaScript.valueToCode(block, 'func_call', Blockly.JavaScript.ORDER_ATOMIC);
    value_func_call = value_func_call.substring(1);
    if (value_func_call.split(' ').length > 1){
        value_func_call = value_func_call.replace(/ /g, ', ');
    }
    value_func_call = value_func_call.replace(/, +,|, -,|, \/,|, *,/, function(chars){
        return chars.substring(chars.length-2,chars.length-1);
    })
    var code = text_func_name + '(' + value_func_call +')';
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };


/********************************* 
Loops
***********************************/
  Blockly.Blocks['while'] = {
    init: function() {
      this.appendValueInput("WHILE")
          .setCheck(null)
          .appendField("while (");
      this.appendDummyInput()
          .appendField(")");
      this.appendStatementInput("DO")
          .setCheck(null)
          .appendField("do");
      this.setInputsInline(true);
      this.setPreviousStatement(true);
      this.setNextStatement(true);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['while'] = function(block) {
    var value_while = Blockly.JavaScript.valueToCode(block, 'WHILE', Blockly.JavaScript.ORDER_ATOMIC);
    var statements_do = Blockly.JavaScript.statementToCode(block, 'DO');
    // TODO: Assemble JavaScript into code variable.
    var code = 'while('+ value_while +') {\n'+ statements_do +'\n}';
    return code;
  };



/********************************* 
Conditions
***********************************/

Blockly.Blocks['if'] = {
    init: function() {
      this.appendValueInput("condition")
          .setCheck(null)
          .appendField("if  (");
      this.appendDummyInput()
          .appendField(")");
      this.appendStatementInput("NAME")
          .setCheck(null)
          .appendField("then");
      this.setInputsInline(true);
      this.setPreviousStatement(true);
      this.setNextStatement(true);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['if'] = function(block) {
    var value_condition = Blockly.JavaScript.valueToCode(block, 'condition', Blockly.JavaScript.ORDER_ATOMIC);
    var statements_name = Blockly.JavaScript.statementToCode(block, 'NAME');
    // TODO: Assemble JavaScript into code variable.
    var code = 'if ('+ value_condition+') {\n'+ statements_name + '}\n';
    return code;
  };

  Blockly.Blocks['else_if'] = {
    init: function() {
      this.appendValueInput("condition")
          .setCheck(null)
          .appendField("else if  (");
      this.appendDummyInput()
          .appendField(")");
      this.appendStatementInput("NAME")
          .setCheck(null)
          .appendField("then");
      this.setInputsInline(true);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['else_if'] = function(block) {
    var value_condition = Blockly.JavaScript.valueToCode(block, 'condition', Blockly.JavaScript.ORDER_ATOMIC);
    var statements_name = Blockly.JavaScript.statementToCode(block, 'NAME');
    // TODO: Assemble JavaScript into code variable.
    var code = 'else if ('+value_condition+') {\n' + statements_name + '\n}\n';
    return code;
  };

  Blockly.Blocks['else'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("else ");
      this.appendStatementInput("NAME")
          .setCheck(null)
          .appendField("then");
      this.setInputsInline(true);
      this.setPreviousStatement(true);
      this.setNextStatement(true);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['else'] = function(block) {
    var statements_name = Blockly.JavaScript.statementToCode(block, 'NAME');
    var code = 'else {\n' + statements_name + '}\n';
    return code;
  };

/********************************* 
Output, input, return, program
***********************************/
Blockly.Blocks['program'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("program")
          .appendField(new Blockly.FieldTextInput("id"), "prog_name")
          .appendField(";");
      this.setNextStatement(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['program'] = function(block) {
    var text_prog_name = block.getFieldValue('prog_name');
    // TODO: Assemble JavaScript into code variable.
    var code = 'program ' + text_prog_name +';\n';
    return code;
  };

  Blockly.Blocks['write'] = {
    init: function() {
      this.appendValueInput("NAME")
          .setCheck(null)
          .appendField("cwrite (");
      this.appendDummyInput()
          .appendField(")");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['write'] = function(block) {
    var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'cwrite('+ value_name+');\n';
    return code;
  };

  Blockly.Blocks['read'] = {
    init: function() {
      this.appendValueInput("NAME")
          .setCheck(null)
          .appendField("cread (");
      this.appendDummyInput()
          .appendField(")");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['read'] = function(block) {
    var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
    // TODO: Assemble JavaScript into code variable.
    var code = 'cread('+ value_name+')\n';
    return code;
  };

  Blockly.Blocks['return'] = {
    init: function() {
      this.appendValueInput("NAME")
          .setCheck(null)
          .appendField("return");
      this.appendDummyInput();
      this.setPreviousStatement(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['return'] = function(block) {
    var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
    var code = 'return '+ value_name+';\n';
    return code;
  };

  Blockly.Blocks['main'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("main( )");
      this.appendStatementInput("program")
          .setCheck(null);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(0);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['main'] = function(block) {
    var statements_program = Blockly.JavaScript.statementToCode(block, 'program');
    var code = 'main (){\n' + statements_program + '\n}';
    return code;
  };


/********************************* 
Variables
***********************************/
Blockly.Blocks['variable_types'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("vars")
          .appendField(new Blockly.FieldDropdown([["int","int"], ["float","float"], ["string","string"], ["boolean","boolean"]]), "vars_types");
      this.appendStatementInput("variables")
          .setCheck(null);
      this.setPreviousStatement(true);
      this.setNextStatement(true);
      this.setColour(120);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['variable_types'] = function(block) {
    var dropdown_vars_types = block.getFieldValue('vars_types');
    var statements_variables = Blockly.JavaScript.statementToCode(block, 'variables');
    statements_variables = statements_variables.substring(3);
    var count = statements_variables.split(' ');
    if (count.length > 1){
        statements_variables = statements_variables.replace(/ /g,', ');
    }
    var code = 'var '+ dropdown_vars_types + ' ' + statements_variables+';\n';
    return code;
  };


  Blockly.Blocks['var_new'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldTextInput("variable name"), "var_name");
      this.setInputsInline(true);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(120);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['var_new'] = function(block) {
    var text_var_name = block.getFieldValue('var_name');
    var code = ' ' + text_var_name;
    return code;
  };

  Blockly.Blocks['var_call'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldTextInput("variable name"), "var_name");
      this.setInputsInline(true);
      this.setOutput(true, null);
      this.setColour(120);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['var_call'] = function(block) {
    var text_var_name = block.getFieldValue('var_name');
    var code = ' ' + text_var_name;
    //return [code, Blockly.JavaScript.ORDER_NONE];
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
};

  Blockly.Blocks['var_assign'] = {
    init: function() {
      this.appendValueInput("NAME")
          .setCheck(null)
          .appendField(new Blockly.FieldTextInput("variable name"), "var_name")
          .appendField("=");
      this.appendDummyInput();
      this.setInputsInline(true);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(120);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['var_assign'] = function(block) {
    var text_var_name = block.getFieldValue('var_name');
    var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
    var code = text_var_name +' = '+ value_name+';\n';
    return code;
  };


  Blockly.Blocks['var_action'] = {
    init: function() {
      this.appendValueInput("NAME")
          .setCheck(null)
          .appendField(new Blockly.FieldTextInput("variable name"), "var_name");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(120);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['var_action'] = function(block) {
    var text_var_name = block.getFieldValue('var_name');
    var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' ' + text_var_name + value_name;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['parameter'] = {
    init: function() {
      this.appendValueInput("NAME")
          .setCheck(null)
          .appendField(new Blockly.FieldDropdown([["int","int"], ["string","string"], ["float","float"], ["boolean","boolean"]]), "type")
          .appendField(new Blockly.FieldTextInput("parameter name"), "par_name");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(120);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['parameter'] = function(block) {
    var dropdown_type = block.getFieldValue('type');
    var text_par_name = block.getFieldValue('par_name');
    var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
    var code = dropdown_type + ' ' + text_par_name + ' ' + value_name;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['lists'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("list")
          .appendField(new Blockly.FieldDropdown([["int","int"], ["string","string"], ["float","float"], ["boolean","boolean"]]), "type")
          .appendField(new Blockly.FieldTextInput("list name"), "name")
          .appendField(new Blockly.FieldNumber(0, 0), "fields");
      this.setInputsInline(true);
      this.setPreviousStatement(true);
      this.setNextStatement(true);
      this.setColour(230);
   this.setTooltip("data type - list name - number of elements");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['lists'] = function(block) {
    var dropdown_type = block.getFieldValue('type');
    var text_name = block.getFieldValue('name');
    var number_fields = block.getFieldValue('fields');
    // TODO: Assemble JavaScript into code variable.
    var code = 'list '+ dropdown_type + ' ' + text_name +'['+number_fields+'];\n';
    return code;
  };


/********************************* 
Math operators
***********************************/
Blockly.Blocks['relate_two'] = {
  init: function() {
    this.appendValueInput("first")
        .setCheck(null);
    this.appendValueInput("second")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["+","+"], ["-","-"], ["*","*"], ["/","/"]]), "NAME");
    this.setInputsInline(true);
    this.setOutput(true);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.JavaScript['relate_two'] = function(block) {
  var value_first = Blockly.JavaScript.valueToCode(block, 'first', Blockly.JavaScript.ORDER_ATOMIC);
  var dropdown_name = block.getFieldValue('NAME');
  var value_second = Blockly.JavaScript.valueToCode(block, 'second', Blockly.JavaScript.ORDER_ATOMIC);
  var code = value_first + ' ' + dropdown_name + ' ' + value_second;
  return [code, Blockly.JavaScript.ORDER_ATOMIC];
};


Blockly.Blocks['plus'] = {
    init: function() {
      this.appendValueInput("plus_text")
          .setCheck(null)
          .appendField("+");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

Blockly.JavaScript['plus'] = function(block) {
    var value_plus_text = Blockly.JavaScript.valueToCode(block, 'plus_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' +' + value_plus_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['minus'] = {
    init: function() {
      this.appendValueInput("minus_text")
          .setCheck(null)
          .appendField("-");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.JavaScript['minus'] = function(block) {
    var value_minus_text = Blockly.JavaScript.valueToCode(block, 'minus_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' -' + value_minus_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['multiply'] = {
    init: function() {
      this.appendValueInput("multiply_text")
          .setCheck(null)
          .appendField("*");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.JavaScript['multiply'] = function(block) {
    var value_multiply_text = Blockly.JavaScript.valueToCode(block, 'multiply_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' *' + value_multiply_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  
  Blockly.Blocks['division'] = {
    init: function() {
      this.appendValueInput("division_text")
          .setCheck(null)
          .appendField("/");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.JavaScript['division'] = function(block) {
    var value_division_text = Blockly.JavaScript.valueToCode(block, 'division_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' /' + value_division_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['value_input'] = {
    init: function() {
      this.appendValueInput("value_text")
          .setCheck(null)
          .appendField(new Blockly.FieldTextInput("value"), "value");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.JavaScript['value_input'] = function(block) {
    var text_value = block.getFieldValue('value');
    var value_value_text = Blockly.JavaScript.valueToCode(block, 'value_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' ' + text_value + value_value_text ;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['value_input_end'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldTextInput("value"), "value");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.JavaScript['value_input_end'] = function(block) {
    var text_value = block.getFieldValue('value');
    var code = ' ' + text_value;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['left_par'] = {
    init: function() {
      this.appendValueInput("left_par_text")
          .setCheck(null)
          .appendField("(");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['left_par'] = function(block) {
    var value_left_par_text = Blockly.JavaScript.valueToCode(block, 'left_par_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = '('+value_left_par_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['right_par'] = {
    init: function() {
      this.appendValueInput("right_par_text")
          .setCheck(null)
          .appendField(")");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['right_par'] = function(block) {
    var value_right_par_text = Blockly.JavaScript.valueToCode(block, 'right_par_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ')'+value_right_par_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };


/********************************* 
Logical operators
***********************************/

Blockly.Blocks['less_than'] = {
    init: function() {
      this.appendValueInput("less_than_text")
          .setCheck(null)
          .appendField("<");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['less_than'] = function(block) {
    var value_less_than_text = Blockly.JavaScript.valueToCode(block, 'less_than_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' <' + value_less_than_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };


  Blockly.Blocks['greater_than'] = {
    init: function() {
      this.appendValueInput("greater_than")
          .setCheck(null)
          .appendField(">");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['greater_than'] = function(block) {
    var value_greater_than = Blockly.JavaScript.valueToCode(block, 'greater_than', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' >' + value_greater_than;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['less_equal'] = {
    init: function() {
      this.appendValueInput("less_equal_text")
          .setCheck(null)
          .appendField("<=");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['less_equal'] = function(block) {
    var value_less_equal_text = Blockly.JavaScript.valueToCode(block, 'less_equal_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' <='+ value_less_equal_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['greater_equal'] = {
    init: function() {
      this.appendValueInput("greater_equal_text")
          .setCheck(null)
          .appendField(">=");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.JavaScript['greater_equal'] = function(block) {
    var value_greater_equal_text = Blockly.JavaScript.valueToCode(block, 'greater_equal_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' >=' + value_greater_equal_texts;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['not_equal'] = {
    init: function() {
      this.appendValueInput("not_equal_text")
          .setCheck(null)
          .appendField("!=");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['not_equal'] = function(block) {
    var value_not_equal_text = Blockly.JavaScript.valueToCode(block, 'not_equal_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' !=' + value_not_equal_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

Blockly.Blocks['equal'] = {
    init: function() {
      this.appendValueInput("equal_text")
          .setCheck(null)
          .appendField("==");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.JavaScript['equal'] = function(block) {
    var value_equal_text = Blockly.JavaScript.valueToCode(block, 'equal_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' =='+value_equal_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['and'] = {
    init: function() {
      this.appendValueInput("and_text")
          .setCheck(null)
          .appendField("&&");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.JavaScript['and'] = function(block) {
    var value_and_text = Blockly.JavaScript.valueToCode(block, 'and_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' &&'+ value_and_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['or'] = {
    init: function() {
      this.appendValueInput("or_text")
          .setCheck(null)
          .appendField("||");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.JavaScript['or'] = function(block) {
    var value_or_text = Blockly.JavaScript.valueToCode(block, 'or_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' ||' + value_or_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };

  Blockly.Blocks['not'] = {
    init: function() {
      this.appendValueInput("not_text")
          .setCheck(null)
          .appendField("!");
      this.setInputsInline(false);
      this.setOutput(true);
      this.setColour(315);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  Blockly.JavaScript['not'] = function(block) {
    var value_not_text = Blockly.JavaScript.valueToCode(block, 'not_text', Blockly.JavaScript.ORDER_ATOMIC);
    var code = ' !'+ value_not_text;
    return [code, Blockly.JavaScript.ORDER_ATOMIC];
  };
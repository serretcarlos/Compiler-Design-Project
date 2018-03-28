
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'and bool comma cread cteFloat cteInt cteString cwrite divide else elseif equals et false float ge gt id if int le left_cb left_dblquotes left_par left_sb list lt main minus multiply ne not or plus program return right_cb right_dblquotes right_par right_sb semicolon string true var void while\n    PROGRAMA : program id semicolon PROGRAMA_VARS PROGRAMA_FUNC main CUERPO\n    \n    PROGRAMA_VARS : VARS\n                  | empty\n    \n    PROGRAMA_FUNC : PROGRAMA_FUNC_AUX\n                  | PROGRAMA_FUNC PROGRAMA_FUNC_AUX\n    \n    PROGRAMA_FUNC_AUX : FUNC\n                      | empty\n    \n    VARS : VARS_AUX\n    \n    VARS_AUX : VARS_LIST_VAR\n             | VARS_AUX VARS_LIST_VAR\n    \n    VARS_LIST_VAR : VARS_LIST\n                  | VARS_VAR\n    \n    VARS_LIST : list TIPO VARS_LIST_AUX semicolon\n    \n    VARS_LIST_AUX : id left_sb cteInt right_sb\n                  | VARS_LIST_AUX comma id left_sb cteInt right_sb\n    \n    VARS_VAR : var TIPO VARS_VAR_AUX semicolon\n    \n    VARS_VAR_AUX : id\n                 | VARS_VAR_AUX comma id\n    \n    TIPO : int\n         | float\n         | bool\n         | string\n    \n    CUERPO : left_cb CUERPO_AUX right_cb\n    \n    CUERPO_AUX : CUERPO_VARS CUERPO_ESTATUTO\n               | CUERPO_AUX CUERPO_VARS CUERPO_ESTATUTO\n\n    \n    CUERPO_VARS : VARS\n                | empty\n    \n    CUERPO_ESTATUTO : ESTATUTO\n                    | empty\n    \n    CUERPOFUNC : CUERPOFUNC_AUX\n    \n    CUERPOFUNC_AUX : CUERPOFUNC_VARS CUERPOFUNC_ESTATUTO\n                   | CUERPOFUNC_AUX CUERPOFUNC_VARS CUERPOFUNC_ESTATUTO\n    \n    CUERPOFUNC_VARS : VARS\n                    | empty\n    \n    CUERPOFUNC_ESTATUTO : ESTATUTO\n                        | empty\n    \n    CUERPORETORNO : left_cb CUERPORETORNO_AUX right_cb\n    \n    CUERPORETORNO_AUX : CUERPORETORNO_CF_AUX RETORNO\n                      | CUERPORETORNO_AUX CUERPORETORNO_CF_AUX RETORNO\n    \n    CUERPORETORNO_CF_AUX : CUERPOFUNC\n                         | empty\n    \n    RETORNO : return EXP\n    \n    FUNC : TIPO id left_par FUNC_PARA right_par CUERPORETORNO\n         | VOIDFUNC\n    \n    FUNC_PARA : TIPO id\n              | FUNC_PARA comma TIPO id\n    \n    VOIDFUNC : void id left_par VOIDFUNC_PARA right_par left_cb CUERPOFUNC right_cb\n    \n    VOIDFUNC_PARA : TIPO id\n                  | VOIDFUNC_PARA comma TIPO id\n    \n    ESTATUTO : ASIGNACION\n             | CONDICION\n             | CICLO\n             | LECTURA\n             | ESCRITURA\n             | LLAMADA\n    \n    CONDICION : if CONDICION_ELSEIF CONDICION_ELSE \n    \n    CONDICION_ELSEIF : left_par EXPRESION right_par CUERPO\n                     | CONDICION_ELSEIF elseif left_par EXPRESION right_par CUERPO\n    \n    CONDICION_ELSE : else CUERPO\n                   | empty\n    \n    CICLO : while left_par EXPRESION right_par CUERPO\n    \n    LECTURA : cread left_par id right_par semicolon\n    \n    ESCRITURA : cwrite left_par EXPRESION right_par semicolon\n    \n    LLAMADA : left_par LLAMADA_EXPRESION right_par semicolon\n    \n    LLAMADA_EXPRESION : EXPRESION\n                      | LLAMADA_EXPRESION comma EXPRESION\n    \n    EXPRESION : EXPRESION_NOT EXPRESIONLOGICA EXPRESION_B\n    \n    EXPRESION_NOT : not\n                | empty\n    \n\tEXPRESION_B : and EXPRESION_NOT EXPRESIONLOGICA\n\t           | or EXPRESION_NOT EXPRESIONLOGICA\n\t\t\t   | empty\n\t\n    EXPRESIONLOGICA :  EXP EXPRESIONLOGICA_AUX\n    \n    EXPRESIONLOGICA_AUX : lt EXP\n                        | gt EXP\n                        | ne EXP\n                        | ge EXP\n                        | le EXP\n                        | et EXP\n                        | empty\n    \n    EXP : TERMINO EXP_AUX\n    \n    EXP_AUX : plus EXP\n            | minus EXP\n            | empty\n    \n    TERMINO : FACTOR TERMINO_AUX\n    \n    TERMINO_AUX : multiply TERMINO\n                | divide TERMINO\n                | empty\n    \n    FACTOR : left_par EXPRESION right_par\n            | CONSTANTE\n            | LISTA\n            | FACTOR_AUX\n    \n    FACTOR_AUX : id\n                | id LLAMADA_F\n    \n    LLAMADA_F : left_par EXPRESION LLAMADAF_AUX right_par\n    \n    LLAMADAF_AUX : comma EXPRESION LLAMADAF_AUX\n                    | empty\n    \n    LISTA : id left_sb EXP right_sb\n    \n    CONSTANTE : NUMERICA\n              | BOOLEANA\n              | STRINGS\n    \n    NUMERICA : NUMERICA_AUX\n             | plus NUMERICA_AUX\n             | minus NUMERICA_AUX\n    \n    NUMERICA_AUX : cteInt\n                 | cteFloat\n    \n    BOOLEANA : true\n             | false\n    \n    STRINGS : cteString\n    \n    ASIGNACION : ASIGNACION_AUX equals EXPRESION semicolon\n    \n    ASIGNACION_AUX : id\n                   | LISTA\n    \n    empty :\n    '
    
_lr_action_items = {'and':([108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,129,130,150,152,153,156,158,159,162,163,171,177,194,195,196,197,198,202,203,204,205,206,207,219,],[-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,166,-113,-98,-94,-81,-84,-103,-85,-88,-104,-73,-80,-82,-83,-89,-87,-86,-75,-74,-76,-77,-78,-79,-95,]),'gt':([108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,130,150,152,153,156,158,159,162,163,194,195,196,197,198,219,],[-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,170,-98,-94,-81,-84,-103,-85,-88,-104,-82,-83,-89,-87,-86,-95,]),'false':([69,84,86,87,88,90,92,93,94,117,131,149,151,154,155,160,161,166,168,170,172,173,174,175,176,182,200,201,214,],[-113,-113,108,-113,-113,108,-68,-69,-113,-113,-113,-113,-113,108,108,108,108,-113,-113,108,108,108,108,108,108,108,108,108,-113,]),'right_sb':([54,101,108,109,110,111,112,113,114,115,116,118,119,120,121,122,124,125,150,152,153,156,158,159,162,163,194,195,196,197,198,219,],[82,145,-108,150,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,-98,-94,-81,-84,-103,-85,-88,-104,-82,-83,-89,-87,-86,-95,]),'semicolon':([3,32,34,35,55,82,108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,128,129,130,132,145,146,150,152,153,156,158,159,162,163,164,167,169,171,177,194,195,196,197,198,202,203,204,205,206,207,216,217,219,],[4,40,43,-17,-18,-14,-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,165,-113,-113,179,-15,190,-98,-94,-81,-84,-103,-85,-88,-104,199,-67,-72,-73,-80,-82,-83,-89,-87,-86,-75,-74,-76,-77,-78,-79,-70,-71,-95,]),'int':([4,5,6,7,8,9,10,11,12,13,14,18,20,21,24,27,28,38,39,40,43,76,78,97,184,189,],[-113,-2,-11,-9,15,15,15,-8,-12,-3,15,-4,-44,-7,-6,-10,-5,15,15,-13,-16,15,15,-43,-37,-47,]),'float':([4,5,6,7,8,9,10,11,12,13,14,18,20,21,24,27,28,38,39,40,43,76,78,97,184,189,],[-113,-2,-11,-9,16,16,16,-8,-12,-3,16,-4,-44,-7,-6,-10,-5,16,16,-13,-16,16,16,-43,-37,-47,]),'cteFloat':([69,84,86,87,88,90,92,93,94,117,123,126,131,149,151,154,155,160,161,166,168,170,172,173,174,175,176,182,200,201,214,],[-113,-113,110,-113,-113,110,-68,-69,-113,-113,110,110,-113,-113,-113,110,110,110,110,-113,-113,110,110,110,110,110,110,110,110,110,-113,]),'left_sb':([33,53,62,112,],[42,81,86,86,]),'multiply':([108,110,111,112,114,115,116,118,119,120,121,122,124,125,150,152,158,163,196,219,],[-108,-106,-100,-93,-92,-102,-109,-107,-101,-90,-105,-99,161,-91,-98,-94,-103,-104,-89,-95,]),'ge':([108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,130,150,152,153,156,158,159,162,163,194,195,196,197,198,219,],[-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,174,-98,-94,-81,-84,-103,-85,-88,-104,-82,-83,-89,-87,-86,-95,]),'comma':([32,34,35,50,51,55,75,80,82,89,91,108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,129,130,134,142,145,150,152,153,156,158,159,162,163,167,169,171,177,178,193,194,195,196,197,198,202,203,204,205,206,207,216,217,219,220,],[41,44,-17,76,78,-18,-45,-48,-14,-65,131,-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,-113,-113,-46,-49,-15,-98,-94,-81,-84,-103,-85,-88,-104,-67,-72,-73,-80,-66,214,-82,-83,-89,-87,-86,-75,-74,-76,-77,-78,-79,-70,-71,-95,214,]),'cread':([6,7,11,12,27,37,40,43,45,46,47,48,56,58,60,61,65,66,67,68,70,73,74,85,95,98,100,104,107,108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,137,138,139,140,141,144,148,150,152,153,156,158,159,162,163,165,179,181,185,186,187,188,190,191,194,195,196,197,198,199,208,209,210,211,218,219,],[-11,-9,-8,-12,-10,-113,-13,-16,57,-26,-27,-113,-52,-53,-50,-28,-54,-29,-55,-51,-24,57,-23,-113,-25,-113,-113,-56,-60,-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,-33,-113,-34,57,-113,-34,-59,-98,-94,-81,-84,-103,-85,-88,-104,-110,-64,-38,-31,-35,-36,57,-62,-57,-82,-83,-89,-87,-86,-63,-61,-42,-39,-32,-58,-95,]),'right_par':([50,51,75,80,89,91,102,103,108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,127,129,130,133,134,142,150,152,153,156,157,158,159,162,163,167,169,171,177,178,192,193,194,195,196,197,198,202,203,204,205,206,207,213,215,216,217,219,220,221,],[77,79,-45,-48,-65,132,146,147,-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,164,-113,-113,180,-46,-49,-98,-94,-81,-84,196,-103,-85,-88,-104,-67,-72,-73,-80,-66,212,-113,-82,-83,-89,-87,-86,-75,-74,-76,-77,-78,-79,219,-97,-70,-71,-95,-113,-96,]),'cteString':([69,84,86,87,88,90,92,93,94,117,131,149,151,154,155,160,161,166,168,170,172,173,174,175,176,182,200,201,214,],[-113,-113,116,-113,-113,116,-68,-69,-113,-113,-113,-113,-113,116,116,116,116,-113,-113,116,116,116,116,116,116,116,116,116,-113,]),'id':([1,6,7,11,12,15,16,17,19,22,23,25,26,27,37,40,41,43,44,45,46,47,48,49,52,56,58,60,61,65,66,67,68,69,70,73,74,83,84,85,86,87,88,90,92,93,94,95,96,98,99,100,104,107,108,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,131,137,138,139,140,141,144,148,149,150,151,152,153,154,155,156,158,159,160,161,162,163,165,166,168,170,172,173,174,175,176,179,181,182,185,186,187,188,190,191,194,195,196,197,198,199,200,201,208,209,210,211,214,218,219,],[3,-11,-9,-8,-12,-19,-20,30,-21,-22,31,33,35,-10,-113,-13,53,-16,55,62,-26,-27,-113,75,80,-52,-53,-50,-28,-54,-29,-55,-51,-113,-24,62,-23,102,-113,-113,112,-113,-113,112,-68,-69,-113,-25,134,-113,142,-113,-56,-60,-108,-106,-100,-93,-113,-92,-102,-109,-113,-107,-101,-90,-105,-99,-113,-91,-113,-33,-113,-34,62,-113,-34,-59,-113,-98,-113,-94,-81,112,112,-84,-103,-85,112,112,-88,-104,-110,-113,-113,112,112,112,112,112,112,-64,-38,112,-31,-35,-36,62,-62,-57,-82,-83,-89,-87,-86,-63,112,112,-61,-42,-39,-32,-113,-58,-95,]),'if':([6,7,11,12,27,37,40,43,45,46,47,48,56,58,60,61,65,66,67,68,70,73,74,85,95,98,100,104,107,108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,137,138,139,140,141,144,148,150,152,153,156,158,159,162,163,165,179,181,185,186,187,188,190,191,194,195,196,197,198,199,208,209,210,211,218,219,],[-11,-9,-8,-12,-10,-113,-13,-16,59,-26,-27,-113,-52,-53,-50,-28,-54,-29,-55,-51,-24,59,-23,-113,-25,-113,-113,-56,-60,-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,-33,-113,-34,59,-113,-34,-59,-98,-94,-81,-84,-103,-85,-88,-104,-110,-64,-38,-31,-35,-36,59,-62,-57,-82,-83,-89,-87,-86,-63,-61,-42,-39,-32,-58,-95,]),'le':([108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,130,150,152,153,156,158,159,162,163,194,195,196,197,198,219,],[-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,175,-98,-94,-81,-84,-103,-85,-88,-104,-82,-83,-89,-87,-86,-95,]),'divide':([108,110,111,112,114,115,116,118,119,120,121,122,124,125,150,152,158,163,196,219,],[-108,-106,-100,-93,-92,-102,-109,-107,-101,-90,-105,-99,160,-91,-98,-94,-103,-104,-89,-95,]),'right_cb':([6,7,11,12,27,37,40,43,45,46,47,48,56,58,60,61,65,66,67,68,70,73,74,85,95,100,104,107,108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,137,138,140,141,143,144,148,150,152,153,156,158,159,162,163,165,179,181,185,186,187,188,190,191,194,195,196,197,198,199,208,209,210,211,218,219,],[-11,-9,-8,-12,-10,-113,-13,-16,-113,-26,-27,74,-52,-53,-50,-28,-54,-29,-55,-51,-24,-113,-23,-113,-25,-113,-56,-60,-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,-33,184,-113,-30,189,-34,-59,-98,-94,-81,-84,-103,-85,-88,-104,-110,-64,-38,-31,-35,-36,-113,-62,-57,-82,-83,-89,-87,-86,-63,-61,-42,-39,-32,-58,-95,]),'ne':([108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,130,150,152,153,156,158,159,162,163,194,195,196,197,198,219,],[-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,173,-98,-94,-81,-84,-103,-85,-88,-104,-82,-83,-89,-87,-86,-95,]),'lt':([108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,130,150,152,153,156,158,159,162,163,194,195,196,197,198,219,],[-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,172,-98,-94,-81,-84,-103,-85,-88,-104,-82,-83,-89,-87,-86,-95,]),'program':([0,],[1,]),'bool':([4,5,6,7,8,9,10,11,12,13,14,18,20,21,24,27,28,38,39,40,43,76,78,97,184,189,],[-113,-2,-11,-9,19,19,19,-8,-12,-3,19,-4,-44,-7,-6,-10,-5,19,19,-13,-16,19,19,-43,-37,-47,]),'cwrite':([6,7,11,12,27,37,40,43,45,46,47,48,56,58,60,61,65,66,67,68,70,73,74,85,95,98,100,104,107,108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,137,138,139,140,141,144,148,150,152,153,156,158,159,162,163,165,179,181,185,186,187,188,190,191,194,195,196,197,198,199,208,209,210,211,218,219,],[-11,-9,-8,-12,-10,-113,-13,-16,63,-26,-27,-113,-52,-53,-50,-28,-54,-29,-55,-51,-24,63,-23,-113,-25,-113,-113,-56,-60,-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,-33,-113,-34,63,-113,-34,-59,-98,-94,-81,-84,-103,-85,-88,-104,-110,-64,-38,-31,-35,-36,63,-62,-57,-82,-83,-89,-87,-86,-63,-61,-42,-39,-32,-58,-95,]),'var':([4,6,7,11,12,27,37,40,43,45,46,47,48,56,58,60,61,65,66,67,68,70,73,74,85,95,98,100,104,107,108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,137,138,139,140,141,144,148,150,152,153,156,158,159,162,163,165,179,181,185,186,187,188,190,191,194,195,196,197,198,199,208,209,210,211,218,219,],[10,-11,-9,10,-12,-10,10,-13,-16,-113,-26,-27,10,-52,-53,-50,-28,-54,-29,-55,-51,-24,-113,-23,-113,-25,10,10,-56,-60,-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,-33,10,-34,-113,10,-34,-59,-98,-94,-81,-84,-103,-85,-88,-104,-110,-64,-38,-31,-35,-36,-113,-62,-57,-82,-83,-89,-87,-86,-63,-61,-42,-39,-32,-58,-95,]),'main':([4,5,6,7,8,11,12,13,14,18,20,21,24,27,28,40,43,97,184,189,],[-113,-2,-11,-9,-113,-8,-12,-3,29,-4,-44,-7,-6,-10,-5,-13,-16,-43,-37,-47,]),'$end':([2,36,74,],[0,-1,-23,]),'return':([6,7,11,12,27,40,43,56,58,60,65,67,68,74,85,98,104,107,108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,135,136,137,138,139,140,141,144,148,150,152,153,156,158,159,162,163,165,179,181,183,185,186,187,188,190,191,194,195,196,197,198,199,208,209,210,211,218,219,],[-11,-9,-8,-12,-10,-13,-16,-52,-53,-50,-54,-55,-51,-23,-113,-113,-56,-60,-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,182,-40,-33,-113,-34,-113,-30,-34,-59,-98,-94,-81,-84,-103,-85,-88,-104,-110,-64,-38,182,-31,-35,-36,-113,-62,-57,-82,-83,-89,-87,-86,-63,-61,-42,-39,-32,-58,-95,]),'string':([4,5,6,7,8,9,10,11,12,13,14,18,20,21,24,27,28,38,39,40,43,76,78,97,184,189,],[-113,-2,-11,-9,22,22,22,-8,-12,-3,22,-4,-44,-7,-6,-10,-5,22,22,-13,-16,22,22,-43,-37,-47,]),'et':([108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,130,150,152,153,156,158,159,162,163,194,195,196,197,198,219,],[-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,176,-98,-94,-81,-84,-103,-85,-88,-104,-82,-83,-89,-87,-86,-95,]),'void':([4,5,6,7,8,11,12,13,14,18,20,21,24,27,28,40,43,97,184,189,],[-113,-2,-11,-9,23,-8,-12,-3,23,-4,-44,-7,-6,-10,-5,-13,-16,-43,-37,-47,]),'equals':([62,64,72,150,],[-111,88,-112,-98,]),'else':([74,85,191,218,],[-23,105,-57,-58,]),'elseif':([74,85,191,218,],[-23,106,-57,-58,]),'left_par':([6,7,11,12,27,30,31,37,40,43,45,46,47,48,56,57,58,59,60,61,63,65,66,67,68,69,70,71,73,74,84,85,86,87,88,90,92,93,94,95,98,100,104,106,107,108,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,131,137,138,139,140,141,144,148,149,150,151,152,153,154,155,156,158,159,160,161,162,163,165,166,168,170,172,173,174,175,176,179,181,182,185,186,187,188,190,191,194,195,196,197,198,199,200,201,208,209,210,211,214,218,219,],[-11,-9,-8,-12,-10,38,39,-113,-13,-16,69,-26,-27,-113,-52,83,-53,84,-50,-28,87,-54,-29,-55,-51,-113,-24,94,69,-23,-113,-113,117,-113,-113,117,-68,-69,-113,-25,-113,-113,-56,149,-60,-108,-106,-100,151,-113,-92,-102,-109,-113,-107,-101,-90,-105,-99,-113,-91,-113,-33,-113,-34,69,-113,-34,-59,-113,-98,-113,-94,-81,117,117,-84,-103,-85,117,117,-88,-104,-110,-113,-113,117,117,117,117,117,117,-64,-38,117,-31,-35,-36,69,-62,-57,-82,-83,-89,-87,-86,-63,117,117,-61,-42,-39,-32,-113,-58,-95,]),'not':([69,84,87,88,94,117,131,149,151,166,168,214,],[92,92,92,92,92,92,92,92,92,92,92,92,]),'true':([69,84,86,87,88,90,92,93,94,117,131,149,151,154,155,160,161,166,168,170,172,173,174,175,176,182,200,201,214,],[-113,-113,118,-113,-113,118,-68,-69,-113,-113,-113,-113,-113,118,118,118,118,-113,-113,118,118,118,118,118,118,118,118,118,-113,]),'left_cb':([29,77,79,105,147,180,212,],[37,98,100,37,37,37,37,]),'cteInt':([42,69,81,84,86,87,88,90,92,93,94,117,123,126,131,149,151,154,155,160,161,166,168,170,172,173,174,175,176,182,200,201,214,],[54,-113,101,-113,121,-113,-113,121,-68,-69,-113,-113,121,121,-113,-113,-113,121,121,121,121,-113,-113,121,121,121,121,121,121,121,121,121,-113,]),'list':([4,6,7,11,12,27,37,40,43,45,46,47,48,56,58,60,61,65,66,67,68,70,73,74,85,95,98,100,104,107,108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,137,138,139,140,141,144,148,150,152,153,156,158,159,162,163,165,179,181,185,186,187,188,190,191,194,195,196,197,198,199,208,209,210,211,218,219,],[9,-11,-9,9,-12,-10,9,-13,-16,-113,-26,-27,9,-52,-53,-50,-28,-54,-29,-55,-51,-24,-113,-23,-113,-25,9,9,-56,-60,-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,-33,9,-34,-113,9,-34,-59,-98,-94,-81,-84,-103,-85,-88,-104,-110,-64,-38,-31,-35,-36,-113,-62,-57,-82,-83,-89,-87,-86,-63,-61,-42,-39,-32,-58,-95,]),'or':([108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,129,130,150,152,153,156,158,159,162,163,171,177,194,195,196,197,198,202,203,204,205,206,207,219,],[-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,168,-113,-98,-94,-81,-84,-103,-85,-88,-104,-73,-80,-82,-83,-89,-87,-86,-75,-74,-76,-77,-78,-79,-95,]),'while':([6,7,11,12,27,37,40,43,45,46,47,48,56,58,60,61,65,66,67,68,70,73,74,85,95,98,100,104,107,108,110,111,112,113,114,115,116,118,119,120,121,122,124,125,137,138,139,140,141,144,148,150,152,153,156,158,159,162,163,165,179,181,185,186,187,188,190,191,194,195,196,197,198,199,208,209,210,211,218,219,],[-11,-9,-8,-12,-10,-113,-13,-16,71,-26,-27,-113,-52,-53,-50,-28,-54,-29,-55,-51,-24,71,-23,-113,-25,-113,-113,-56,-60,-108,-106,-100,-93,-113,-92,-102,-109,-107,-101,-90,-105,-99,-113,-91,-33,-113,-34,71,-113,-34,-59,-98,-94,-81,-84,-103,-85,-88,-104,-110,-64,-38,-31,-35,-36,71,-62,-57,-82,-83,-89,-87,-86,-63,-61,-42,-39,-32,-58,-95,]),'plus':([69,84,86,87,88,90,92,93,94,108,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,131,149,150,151,152,154,155,158,159,160,161,162,163,166,168,170,172,173,174,175,176,182,196,197,198,200,201,214,219,],[-113,-113,123,-113,-113,123,-68,-69,-113,-108,-106,-100,-93,154,-92,-102,-109,-113,-107,-101,-90,-105,-99,-113,-91,-113,-113,-98,-113,-94,123,123,-103,-85,123,123,-88,-104,-113,-113,123,123,123,123,123,123,123,-89,-87,-86,123,123,-113,-95,]),'minus':([69,84,86,87,88,90,92,93,94,108,110,111,112,113,114,115,116,117,118,119,120,121,122,124,125,131,149,150,151,152,154,155,158,159,160,161,162,163,166,168,170,172,173,174,175,176,182,196,197,198,200,201,214,219,],[-113,-113,126,-113,-113,126,-68,-69,-113,-108,-106,-100,-93,155,-92,-102,-109,-113,-107,-101,-90,-105,-99,-113,-91,-113,-113,-98,-113,-94,126,126,-103,-85,126,126,-88,-104,-113,-113,126,126,126,126,126,126,126,-89,-87,-86,126,126,-113,-95,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'EXPRESION':([69,84,87,88,94,117,131,149,151,214,],[89,103,127,128,133,157,178,192,193,220,]),'CONDICION_ELSE':([85,],[104,]),'EXPRESION_NOT':([69,84,87,88,94,117,131,149,151,166,168,214,],[90,90,90,90,90,90,90,90,90,200,201,90,]),'ESTATUTO':([45,73,140,188,],[61,61,186,186,]),'CICLO':([45,73,140,188,],[56,56,56,56,]),'VARS':([4,37,48,98,100,138,141,],[5,46,46,137,137,137,137,]),'PROGRAMA_VARS':([4,],[8,]),'VARS_LIST':([4,11,37,48,98,100,138,141,],[6,6,6,6,6,6,6,6,]),'TERMINO_AUX':([124,],[159,]),'CUERPO':([29,105,147,180,212,],[36,148,191,208,218,]),'RETORNO':([135,183,],[181,210,]),'LLAMADA_EXPRESION':([69,],[91,]),'BOOLEANA':([86,90,154,155,160,161,170,172,173,174,175,176,182,200,201,],[111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,]),'EXP':([86,90,154,155,170,172,173,174,175,176,182,200,201,],[109,130,194,195,202,203,204,205,206,207,209,130,130,]),'CUERPO_AUX':([37,],[48,]),'LLAMADA_F':([112,],[152,]),'CUERPOFUNC_AUX':([98,100,138,],[141,141,141,]),'LECTURA':([45,73,140,188,],[58,58,58,58,]),'ESCRITURA':([45,73,140,188,],[65,65,65,65,]),'CUERPOFUNC_ESTATUTO':([140,188,],[185,211,]),'CUERPORETORNO_CF_AUX':([98,138,],[135,183,]),'CUERPOFUNC':([98,100,138,],[136,143,136,]),'TIPO':([8,9,10,14,38,39,76,78,],[17,25,26,17,49,52,96,99,]),'VOIDFUNC_PARA':([39,],[51,]),'VARS_LIST_AUX':([25,],[32,]),'STRINGS':([86,90,154,155,160,161,170,172,173,174,175,176,182,200,201,],[119,119,119,119,119,119,119,119,119,119,119,119,119,119,119,]),'PROGRAMA_FUNC_AUX':([8,14,],[18,28,]),'TERMINO':([86,90,154,155,160,161,170,172,173,174,175,176,182,200,201,],[113,113,113,113,197,198,113,113,113,113,113,113,113,113,113,]),'CUERPOFUNC_VARS':([98,100,138,141,],[140,140,140,188,]),'ASIGNACION_AUX':([45,73,140,188,],[64,64,64,64,]),'VOIDFUNC':([8,14,],[20,20,]),'NUMERICA_AUX':([86,90,123,126,154,155,160,161,170,172,173,174,175,176,182,200,201,],[115,115,158,163,115,115,115,115,115,115,115,115,115,115,115,115,115,]),'empty':([4,8,14,37,45,48,69,73,84,85,87,88,94,98,100,113,117,124,129,130,131,138,140,141,149,151,166,168,188,193,214,220,],[13,21,21,47,66,47,93,66,93,107,93,93,93,139,144,156,93,162,169,177,93,139,187,144,93,93,93,93,187,215,93,215,]),'CONDICION_ELSEIF':([59,],[85,]),'EXPRESION_B':([129,],[167,]),'VARS_VAR_AUX':([26,],[34,]),'VARS_LIST_VAR':([4,11,37,48,98,100,138,141,],[7,27,7,7,7,7,7,7,]),'PROGRAMA_FUNC':([8,],[14,]),'CUERPORETORNO':([77,],[97,]),'LLAMADA':([45,73,140,188,],[67,67,67,67,]),'CONDICION':([45,73,140,188,],[68,68,68,68,]),'FUNC':([8,14,],[24,24,]),'VARS_VAR':([4,11,37,48,98,100,138,141,],[12,12,12,12,12,12,12,12,]),'CUERPO_ESTATUTO':([45,73,],[70,95,]),'LLAMADAF_AUX':([193,220,],[213,221,]),'CUERPO_VARS':([37,48,],[45,73,]),'ASIGNACION':([45,73,140,188,],[60,60,60,60,]),'EXPRESIONLOGICA_AUX':([130,],[171,]),'CONSTANTE':([86,90,154,155,160,161,170,172,173,174,175,176,182,200,201,],[120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,]),'FACTOR_AUX':([86,90,154,155,160,161,170,172,173,174,175,176,182,200,201,],[114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,]),'EXP_AUX':([113,],[153,]),'VARS_AUX':([4,37,48,98,100,138,141,],[11,11,11,11,11,11,11,]),'NUMERICA':([86,90,154,155,160,161,170,172,173,174,175,176,182,200,201,],[122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,]),'CUERPORETORNO_AUX':([98,],[138,]),'PROGRAMA':([0,],[2,]),'FACTOR':([86,90,154,155,160,161,170,172,173,174,175,176,182,200,201,],[124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,]),'EXPRESIONLOGICA':([90,200,201,],[129,216,217,]),'LISTA':([45,73,86,90,140,154,155,160,161,170,172,173,174,175,176,182,188,200,201,],[72,72,125,125,72,125,125,125,125,125,125,125,125,125,125,125,72,125,125,]),'FUNC_PARA':([38,],[50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> program id semicolon PROGRAMA_VARS PROGRAMA_FUNC main CUERPO','PROGRAMA',7,'p_PROGRAMA','CSP_yacc.py',7),
  ('PROGRAMA_VARS -> VARS','PROGRAMA_VARS',1,'p_PROGRAMA_VARS','CSP_yacc.py',12),
  ('PROGRAMA_VARS -> empty','PROGRAMA_VARS',1,'p_PROGRAMA_VARS','CSP_yacc.py',13),
  ('PROGRAMA_FUNC -> PROGRAMA_FUNC_AUX','PROGRAMA_FUNC',1,'p_PROGRAMA_FUNC','CSP_yacc.py',18),
  ('PROGRAMA_FUNC -> PROGRAMA_FUNC PROGRAMA_FUNC_AUX','PROGRAMA_FUNC',2,'p_PROGRAMA_FUNC','CSP_yacc.py',19),
  ('PROGRAMA_FUNC_AUX -> FUNC','PROGRAMA_FUNC_AUX',1,'p_PROGRAMA_FUNC_AUX','CSP_yacc.py',24),
  ('PROGRAMA_FUNC_AUX -> empty','PROGRAMA_FUNC_AUX',1,'p_PROGRAMA_FUNC_AUX','CSP_yacc.py',25),
  ('VARS -> VARS_AUX','VARS',1,'p_VARS','CSP_yacc.py',30),
  ('VARS_AUX -> VARS_LIST_VAR','VARS_AUX',1,'p_VARS_AUX','CSP_yacc.py',35),
  ('VARS_AUX -> VARS_AUX VARS_LIST_VAR','VARS_AUX',2,'p_VARS_AUX','CSP_yacc.py',36),
  ('VARS_LIST_VAR -> VARS_LIST','VARS_LIST_VAR',1,'p_VARS_LIST_VAR','CSP_yacc.py',41),
  ('VARS_LIST_VAR -> VARS_VAR','VARS_LIST_VAR',1,'p_VARS_LIST_VAR','CSP_yacc.py',42),
  ('VARS_LIST -> list TIPO VARS_LIST_AUX semicolon','VARS_LIST',4,'p_VARS_LIST','CSP_yacc.py',47),
  ('VARS_LIST_AUX -> id left_sb cteInt right_sb','VARS_LIST_AUX',4,'p_VARS_LIST_AUX','CSP_yacc.py',52),
  ('VARS_LIST_AUX -> VARS_LIST_AUX comma id left_sb cteInt right_sb','VARS_LIST_AUX',6,'p_VARS_LIST_AUX','CSP_yacc.py',53),
  ('VARS_VAR -> var TIPO VARS_VAR_AUX semicolon','VARS_VAR',4,'p_VARS_VAR','CSP_yacc.py',58),
  ('VARS_VAR_AUX -> id','VARS_VAR_AUX',1,'p_VARS_VAR_AUX','CSP_yacc.py',63),
  ('VARS_VAR_AUX -> VARS_VAR_AUX comma id','VARS_VAR_AUX',3,'p_VARS_VAR_AUX','CSP_yacc.py',64),
  ('TIPO -> int','TIPO',1,'p_TIPO','CSP_yacc.py',69),
  ('TIPO -> float','TIPO',1,'p_TIPO','CSP_yacc.py',70),
  ('TIPO -> bool','TIPO',1,'p_TIPO','CSP_yacc.py',71),
  ('TIPO -> string','TIPO',1,'p_TIPO','CSP_yacc.py',72),
  ('CUERPO -> left_cb CUERPO_AUX right_cb','CUERPO',3,'p_CUERPO','CSP_yacc.py',77),
  ('CUERPO_AUX -> CUERPO_VARS CUERPO_ESTATUTO','CUERPO_AUX',2,'p_CUERPO_AUX','CSP_yacc.py',82),
  ('CUERPO_AUX -> CUERPO_AUX CUERPO_VARS CUERPO_ESTATUTO','CUERPO_AUX',3,'p_CUERPO_AUX','CSP_yacc.py',83),
  ('CUERPO_VARS -> VARS','CUERPO_VARS',1,'p_CUERPO_VARS','CSP_yacc.py',89),
  ('CUERPO_VARS -> empty','CUERPO_VARS',1,'p_CUERPO_VARS','CSP_yacc.py',90),
  ('CUERPO_ESTATUTO -> ESTATUTO','CUERPO_ESTATUTO',1,'p_CUERPO_ESTATUTO','CSP_yacc.py',95),
  ('CUERPO_ESTATUTO -> empty','CUERPO_ESTATUTO',1,'p_CUERPO_ESTATUTO','CSP_yacc.py',96),
  ('CUERPOFUNC -> CUERPOFUNC_AUX','CUERPOFUNC',1,'p_CUERPOFUNC','CSP_yacc.py',101),
  ('CUERPOFUNC_AUX -> CUERPOFUNC_VARS CUERPOFUNC_ESTATUTO','CUERPOFUNC_AUX',2,'p_CUERPOFUNC_AUX','CSP_yacc.py',106),
  ('CUERPOFUNC_AUX -> CUERPOFUNC_AUX CUERPOFUNC_VARS CUERPOFUNC_ESTATUTO','CUERPOFUNC_AUX',3,'p_CUERPOFUNC_AUX','CSP_yacc.py',107),
  ('CUERPOFUNC_VARS -> VARS','CUERPOFUNC_VARS',1,'p_CUERPOFUNC_VARS','CSP_yacc.py',112),
  ('CUERPOFUNC_VARS -> empty','CUERPOFUNC_VARS',1,'p_CUERPOFUNC_VARS','CSP_yacc.py',113),
  ('CUERPOFUNC_ESTATUTO -> ESTATUTO','CUERPOFUNC_ESTATUTO',1,'p_CUERPOFUNC_ESTATUTO','CSP_yacc.py',118),
  ('CUERPOFUNC_ESTATUTO -> empty','CUERPOFUNC_ESTATUTO',1,'p_CUERPOFUNC_ESTATUTO','CSP_yacc.py',119),
  ('CUERPORETORNO -> left_cb CUERPORETORNO_AUX right_cb','CUERPORETORNO',3,'p_CUERPORETORNO','CSP_yacc.py',125),
  ('CUERPORETORNO_AUX -> CUERPORETORNO_CF_AUX RETORNO','CUERPORETORNO_AUX',2,'p_CUERPORETORNO_AUX','CSP_yacc.py',130),
  ('CUERPORETORNO_AUX -> CUERPORETORNO_AUX CUERPORETORNO_CF_AUX RETORNO','CUERPORETORNO_AUX',3,'p_CUERPORETORNO_AUX','CSP_yacc.py',131),
  ('CUERPORETORNO_CF_AUX -> CUERPOFUNC','CUERPORETORNO_CF_AUX',1,'p_CUERPORETORNO_CF_AUX','CSP_yacc.py',136),
  ('CUERPORETORNO_CF_AUX -> empty','CUERPORETORNO_CF_AUX',1,'p_CUERPORETORNO_CF_AUX','CSP_yacc.py',137),
  ('RETORNO -> return EXP','RETORNO',2,'p_RETORNO','CSP_yacc.py',144),
  ('FUNC -> TIPO id left_par FUNC_PARA right_par CUERPORETORNO','FUNC',6,'p_FUNC','CSP_yacc.py',149),
  ('FUNC -> VOIDFUNC','FUNC',1,'p_FUNC','CSP_yacc.py',150),
  ('FUNC_PARA -> TIPO id','FUNC_PARA',2,'p_FUNC_PARA','CSP_yacc.py',155),
  ('FUNC_PARA -> FUNC_PARA comma TIPO id','FUNC_PARA',4,'p_FUNC_PARA','CSP_yacc.py',156),
  ('VOIDFUNC -> void id left_par VOIDFUNC_PARA right_par left_cb CUERPOFUNC right_cb','VOIDFUNC',8,'p_VOIDFUNC','CSP_yacc.py',161),
  ('VOIDFUNC_PARA -> TIPO id','VOIDFUNC_PARA',2,'p_VOIDFUNC_PARA','CSP_yacc.py',166),
  ('VOIDFUNC_PARA -> VOIDFUNC_PARA comma TIPO id','VOIDFUNC_PARA',4,'p_VOIDFUNC_PARA','CSP_yacc.py',167),
  ('ESTATUTO -> ASIGNACION','ESTATUTO',1,'p_ESTATUTO','CSP_yacc.py',172),
  ('ESTATUTO -> CONDICION','ESTATUTO',1,'p_ESTATUTO','CSP_yacc.py',173),
  ('ESTATUTO -> CICLO','ESTATUTO',1,'p_ESTATUTO','CSP_yacc.py',174),
  ('ESTATUTO -> LECTURA','ESTATUTO',1,'p_ESTATUTO','CSP_yacc.py',175),
  ('ESTATUTO -> ESCRITURA','ESTATUTO',1,'p_ESTATUTO','CSP_yacc.py',176),
  ('ESTATUTO -> LLAMADA','ESTATUTO',1,'p_ESTATUTO','CSP_yacc.py',177),
  ('CONDICION -> if CONDICION_ELSEIF CONDICION_ELSE','CONDICION',3,'p_CONDICION','CSP_yacc.py',182),
  ('CONDICION_ELSEIF -> left_par EXPRESION right_par CUERPO','CONDICION_ELSEIF',4,'p_CONDICION_ELSEIF','CSP_yacc.py',187),
  ('CONDICION_ELSEIF -> CONDICION_ELSEIF elseif left_par EXPRESION right_par CUERPO','CONDICION_ELSEIF',6,'p_CONDICION_ELSEIF','CSP_yacc.py',188),
  ('CONDICION_ELSE -> else CUERPO','CONDICION_ELSE',2,'p_CONDICION_ELSE','CSP_yacc.py',193),
  ('CONDICION_ELSE -> empty','CONDICION_ELSE',1,'p_CONDICION_ELSE','CSP_yacc.py',194),
  ('CICLO -> while left_par EXPRESION right_par CUERPO','CICLO',5,'p_CICLO','CSP_yacc.py',199),
  ('LECTURA -> cread left_par id right_par semicolon','LECTURA',5,'p_LECTURA','CSP_yacc.py',204),
  ('ESCRITURA -> cwrite left_par EXPRESION right_par semicolon','ESCRITURA',5,'p_ESCRITURA','CSP_yacc.py',209),
  ('LLAMADA -> left_par LLAMADA_EXPRESION right_par semicolon','LLAMADA',4,'p_LLAMADA','CSP_yacc.py',214),
  ('LLAMADA_EXPRESION -> EXPRESION','LLAMADA_EXPRESION',1,'p_LLAMADA_EXPRESION','CSP_yacc.py',219),
  ('LLAMADA_EXPRESION -> LLAMADA_EXPRESION comma EXPRESION','LLAMADA_EXPRESION',3,'p_LLAMADA_EXPRESION','CSP_yacc.py',220),
  ('EXPRESION -> EXPRESION_NOT EXPRESIONLOGICA EXPRESION_B','EXPRESION',3,'p_EXPRESION','CSP_yacc.py',225),
  ('EXPRESION_NOT -> not','EXPRESION_NOT',1,'p_EXPRESION_NOT','CSP_yacc.py',230),
  ('EXPRESION_NOT -> empty','EXPRESION_NOT',1,'p_EXPRESION_NOT','CSP_yacc.py',231),
  ('EXPRESION_B -> and EXPRESION_NOT EXPRESIONLOGICA','EXPRESION_B',3,'p_EXPRESION_B','CSP_yacc.py',235),
  ('EXPRESION_B -> or EXPRESION_NOT EXPRESIONLOGICA','EXPRESION_B',3,'p_EXPRESION_B','CSP_yacc.py',236),
  ('EXPRESION_B -> empty','EXPRESION_B',1,'p_EXPRESION_B','CSP_yacc.py',237),
  ('EXPRESIONLOGICA -> EXP EXPRESIONLOGICA_AUX','EXPRESIONLOGICA',2,'p_EXPRESIONLOGICA','CSP_yacc.py',242),
  ('EXPRESIONLOGICA_AUX -> lt EXP','EXPRESIONLOGICA_AUX',2,'p_EXPRESIONLOGICA_AUX','CSP_yacc.py',247),
  ('EXPRESIONLOGICA_AUX -> gt EXP','EXPRESIONLOGICA_AUX',2,'p_EXPRESIONLOGICA_AUX','CSP_yacc.py',248),
  ('EXPRESIONLOGICA_AUX -> ne EXP','EXPRESIONLOGICA_AUX',2,'p_EXPRESIONLOGICA_AUX','CSP_yacc.py',249),
  ('EXPRESIONLOGICA_AUX -> ge EXP','EXPRESIONLOGICA_AUX',2,'p_EXPRESIONLOGICA_AUX','CSP_yacc.py',250),
  ('EXPRESIONLOGICA_AUX -> le EXP','EXPRESIONLOGICA_AUX',2,'p_EXPRESIONLOGICA_AUX','CSP_yacc.py',251),
  ('EXPRESIONLOGICA_AUX -> et EXP','EXPRESIONLOGICA_AUX',2,'p_EXPRESIONLOGICA_AUX','CSP_yacc.py',252),
  ('EXPRESIONLOGICA_AUX -> empty','EXPRESIONLOGICA_AUX',1,'p_EXPRESIONLOGICA_AUX','CSP_yacc.py',253),
  ('EXP -> TERMINO EXP_AUX','EXP',2,'p_EXP','CSP_yacc.py',258),
  ('EXP_AUX -> plus EXP','EXP_AUX',2,'p_EXP_AUX','CSP_yacc.py',263),
  ('EXP_AUX -> minus EXP','EXP_AUX',2,'p_EXP_AUX','CSP_yacc.py',264),
  ('EXP_AUX -> empty','EXP_AUX',1,'p_EXP_AUX','CSP_yacc.py',265),
  ('TERMINO -> FACTOR TERMINO_AUX','TERMINO',2,'p_TERMINO','CSP_yacc.py',271),
  ('TERMINO_AUX -> multiply TERMINO','TERMINO_AUX',2,'p_TERMINO_AUX','CSP_yacc.py',276),
  ('TERMINO_AUX -> divide TERMINO','TERMINO_AUX',2,'p_TERMINO_AUX','CSP_yacc.py',277),
  ('TERMINO_AUX -> empty','TERMINO_AUX',1,'p_TERMINO_AUX','CSP_yacc.py',278),
  ('FACTOR -> left_par EXPRESION right_par','FACTOR',3,'p_FACTOR','CSP_yacc.py',283),
  ('FACTOR -> CONSTANTE','FACTOR',1,'p_FACTOR','CSP_yacc.py',284),
  ('FACTOR -> LISTA','FACTOR',1,'p_FACTOR','CSP_yacc.py',285),
  ('FACTOR -> FACTOR_AUX','FACTOR',1,'p_FACTOR','CSP_yacc.py',286),
  ('FACTOR_AUX -> id','FACTOR_AUX',1,'p_FACTOR_AUX','CSP_yacc.py',291),
  ('FACTOR_AUX -> id LLAMADA_F','FACTOR_AUX',2,'p_FACTOR_AUX','CSP_yacc.py',292),
  ('LLAMADA_F -> left_par EXPRESION LLAMADAF_AUX right_par','LLAMADA_F',4,'p_LLAMADAF','CSP_yacc.py',297),
  ('LLAMADAF_AUX -> comma EXPRESION LLAMADAF_AUX','LLAMADAF_AUX',3,'p_LLAMADAF_AUX','CSP_yacc.py',302),
  ('LLAMADAF_AUX -> empty','LLAMADAF_AUX',1,'p_LLAMADAF_AUX','CSP_yacc.py',303),
  ('LISTA -> id left_sb EXP right_sb','LISTA',4,'p_LISTA','CSP_yacc.py',308),
  ('CONSTANTE -> NUMERICA','CONSTANTE',1,'p_CONSTANTE','CSP_yacc.py',313),
  ('CONSTANTE -> BOOLEANA','CONSTANTE',1,'p_CONSTANTE','CSP_yacc.py',314),
  ('CONSTANTE -> STRINGS','CONSTANTE',1,'p_CONSTANTE','CSP_yacc.py',315),
  ('NUMERICA -> NUMERICA_AUX','NUMERICA',1,'p_NUMERICA','CSP_yacc.py',320),
  ('NUMERICA -> plus NUMERICA_AUX','NUMERICA',2,'p_NUMERICA','CSP_yacc.py',321),
  ('NUMERICA -> minus NUMERICA_AUX','NUMERICA',2,'p_NUMERICA','CSP_yacc.py',322),
  ('NUMERICA_AUX -> cteInt','NUMERICA_AUX',1,'p_NUMERICA_AUX','CSP_yacc.py',327),
  ('NUMERICA_AUX -> cteFloat','NUMERICA_AUX',1,'p_NUMERICA_AUX','CSP_yacc.py',328),
  ('BOOLEANA -> true','BOOLEANA',1,'p_BOOLEANA','CSP_yacc.py',333),
  ('BOOLEANA -> false','BOOLEANA',1,'p_BOOLEANA','CSP_yacc.py',334),
  ('STRINGS -> cteString','STRINGS',1,'p_STRINGS','CSP_yacc.py',339),
  ('ASIGNACION -> ASIGNACION_AUX equals EXPRESION semicolon','ASIGNACION',4,'p_ASIGNACION','CSP_yacc.py',344),
  ('ASIGNACION_AUX -> id','ASIGNACION_AUX',1,'p_ASIGNACION_AUX','CSP_yacc.py',349),
  ('ASIGNACION_AUX -> LISTA','ASIGNACION_AUX',1,'p_ASIGNACION_AUX','CSP_yacc.py',350),
  ('empty -> <empty>','empty',0,'p_empty','CSP_yacc.py',355),
]

from pygments import lex
from condaLoader import condaLoader
import setting
from tkinter import font

############################################################################################################
class HighLighter:
    def __init__(self,parent,*args, **kwargs):

        self.parent = parent
        self.setting = condaLoader(self.parent.parent)
        
        self.definedColor = self.definingColor()
        
   
############################################################################################################
    def clear_existing_tags(self):
        ''' This function clear all creted tag of textArea'''
        for tag in self.parent.tag_names():
            self.parent.tag_delete(tag)

############################################################################################################    
    def definingColor(self,*args):
        themeApplier = setting.Appplier(parent = self.parent.parent)
        themeData = themeApplier.load_Theme()
        return themeData
      
############################################################################################################
    def getFontForTaggedText(self,*args, **kwargs):
        all_tags = self.parent.tag_names()
      
        new_property = dict()
        for tag_name in all_tags:
            if "Token.Comment.Single" == tag_name or "Token.Comment.Multiline" == tag_name:
                new_property["Tag.name"] = tag_name
                new_property["slant"] = "italic"
            elif "Token.Punctuation" == tag_name :
                print(tag_name)
                new_property["Tag.name"] = tag_name
                new_property["weight"] = "bold"
            elif "Token.Name.Function" == tag_name :
                print(tag_name)
                new_property["Tag.name"] = tag_name
                new_property["weight"] = "bold"
            else:
                pass
        
        return new_property
                
    def applygFont(self,*args, **kwargs):
        font_appling = self.getFontForTaggedText()
        font_loaded = self.setting.load_setting_data()["font"]
        # tag_nam = font_appling["Tag.name"]
        if len(font_appling) != 0:
            for prop in font_appling.keys():
                if prop in font_loaded.keys():
                    font_loaded[prop] = font_appling[prop]
                else:
                    pass
        else:
            pass
                 
        font1 = font.Font( family = font_loaded["family"],
                      size = font_loaded["size"],
                      slant = font_loaded["slant"],
                      weight = font_loaded["weight"],
                      underline = font_loaded["underline"])
        print(font_loaded)
        return font1
    
    def applyFont(self,*args, **kwargs):
        font_appling = kwargs
        font_loaded = self.setting.load_setting_data()["font"]
        # tag_nam = font_appling["Tag.name"]
        if len(font_appling) != 0:
            for prop in font_appling.keys():
                if prop in font_loaded.keys():
                    font_loaded[prop] = font_appling[prop]
                else:
                    pass
        else:
            pass
                 
        font1 = font.Font( family = font_loaded["family"],
                      size = font_loaded["size"],
                      slant = font_loaded["slant"],
                      weight = font_loaded["weight"],
                      underline = font_loaded["underline"])
        return font1


############################################################################################################
    def initial_highlight(self, lexer,*args):
        self.lexer = lexer
        self.clear_existing_tags()
    
        
        self.parent.mark_set("range_start", "1.0")
        data = self.parent.get("1.0", "end-1c")
        for token, content in lex(data, self.lexer):
           
            self.parent.mark_set("range_end", "range_start + %dc" % len(content))
            self.parent.tag_add(str(token), "range_start", "range_end")
            self.parent.mark_set("range_start", "range_end")
        
        self.parent.tag_configure('Token.Comment', foreground=self.definedColor["singleline_comment"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Comment.Single', foreground=self.definedColor["singleline_comment"],
                                  font=self.applyFont(slant="italic"))
        self.parent.tag_configure('Token.Comment.Multiline', foreground=self.definedColor["multiline_comment"],
                                  font=self.applyFont(slant="italic"))
        self.parent.tag_configure('Token.Comment.Special', foreground=self.definedColor["special_comment"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Comment.Special', foreground=self.definedColor["special_comment"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Comment.Preproc', foreground=self.definedColor["prepop_comment"],
                                  font=self.applyFont())

        self.parent.tag_configure('Token.Punctuation', foreground=self.definedColor["punctuation"],
                                  font=self.applyFont(weight="bold"))
        
        self.parent.tag_configure('Token.Operator', foreground=self.definedColor["operator"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Operator.Word', foreground=self.definedColor["word_operator"],
                                  font=self.applyFont())
        
        self.parent.tag_configure('Token.Literal.Number', foreground=self.definedColor["integer_number"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.Number.Bin', foreground=self.definedColor["binary_number"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.Number.Float', foreground=self.definedColor["float_number"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.Number.Hex', foreground=self.definedColor["hex_number"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.Number.Integer', foreground=self.definedColor["integer_number"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.Number.Oct', foreground=self.definedColor["oct_number"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.Number.Long', foreground=self.definedColor["long_number"],
                                  font=self.applyFont())
                
        self.parent.tag_configure('Token.String', foreground=self.definedColor["single_string"],font=self.applyFont())
        self.parent.tag_configure('Token.Literal.String.Char', foreground=self.definedColor["single_string"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.String.Double', foreground=self.definedColor["double_string"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.String.Single', foreground=self.definedColor["single_string"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.String.Doc', foreground=self.definedColor["doc_string"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.String.Escape', foreground=self.definedColor["escape_string"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.String.Interpol', foreground=self.definedColor["interpol_string"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Literal.String.Symbol', foreground=self.definedColor["symbol_string"],
                                  font=self.applyFont())

        self.parent.tag_configure('Token.Name', foreground=self.definedColor["name"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Text.Whitespace')
        self.parent.tag_configure('Token.Text',foreground=self.definedColor["entity_name"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Name.Attribute', foreground=self.definedColor["attribute_name"],
                                  font=self.applyFont(weight="bold"))
        self.parent.tag_configure('Token.Name.Builtin', foreground=self.definedColor["builtin_name"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Name.Builtin.Pseudo', foreground=self.definedColor["builtin_pseudo_name"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Name.Class', foreground=self.definedColor["class_name"],
                                  font=self.applyFont(weight="bold"))
        self.parent.tag_configure('Token.Name.Constant', foreground=self.definedColor["constant_name"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Name.Decorator', foreground=self.definedColor["decorator_name"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Name.Entity', foreground=self.definedColor["entity_name"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Name.Exception', foreground=self.definedColor["exception_name"],
                                  font=self.applyFont(weight="bold"))
        self.parent.tag_configure('Token.Name.Function', foreground=self.definedColor["function_name"],
                                  font=self.applyFont(weight="bold"))
        self.parent.tag_configure('Token.Name.Function.Magic', foreground=self.definedColor["function_magic_name"],
                                  font=self.applyFont(weight="bold"))
        self.parent.tag_configure('Token.Name.Namespace', foreground=self.definedColor["namesapce_name"],
                                  font=self.applyFont(weight="bold"))

        self.parent.tag_configure('Token.Name.Tag', foreground=self.definedColor["tag_name"],
                                  font=self.applyFont(weight="bold"))
        
        self.parent.tag_configure('Token.Name.Variable', foreground=self.definedColor["variable_name"],
                                  font=self.applyFont(slant="italic",wieght="bold"))
        self.parent.tag_configure('Token.Name.Variable.Class', foreground=self.definedColor["class_variable_name"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Name.Variable.Instance', foreground=self.definedColor["instance_variabke_name"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Name.Variable.Magic', foreground=self.definedColor["magic_variabl_name"],
                                  font=self.applyFont())
        
        self.parent.tag_configure('Token.Keyword', foreground=self.definedColor["keyword"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Keyword.Constant', foreground=self.definedColor["constant_keyword"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Keyword.Declaration', foreground=self.definedColor["declaration_keyword"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Keyword.Namespace', foreground=self.definedColor["namespace_keyword"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Keyword.Pseudo', foreground=self.definedColor["pseudo_keyword"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Keyword.Reserved', foreground=self.definedColor["reserved_keyword"],
                                  font=self.applyFont())
        self.parent.tag_configure('Token.Keyword.Type', foreground=self.definedColor["type_keyword"],
                                  font=self.applyFont())

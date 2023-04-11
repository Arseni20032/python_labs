# regular expression

K = 10
N = 4
mister_or_mrs_reg = r"([mM]r\.|[mM]rs\.)"
jr_reg = r"[Jj]r\."
etc_reg = r"(\setc\.\s[a-z])"
eg_reg = r"(e\.g\.\s[a-z])"
c_reg = r"(\sc\.\s[a-z])"
ie_reg = r"(i\.e\.\s[a-z])"
initials_reg = r"([\s.][A-Z]\.(\s[A-Z]\.|\s[A-Z]))"
not_punc_reg = r"([^\.\?\!])"
punc_reg = r"(((\.\.\.)|(\?\!)|\.|\?|\!))"
punc_reg_2 = r"((\.\.\.)|(\.))"
latin_symbol = r"[A-Za-z]"
reg_expr_to_word = r"\b[a-zA-z\d]+\b"
reg_expr_to_num = r'\b[\d+.]\b'
reg_expr_declarative = f"((({mister_or_mrs_reg}|{jr_reg}|{etc_reg}|{eg_reg}|{c_reg}|{ie_reg}|{initials_reg})|" \
                       f"{not_punc_reg})*{punc_reg})"
reg_expr_non_declarative = f"((({mister_or_mrs_reg}|{jr_reg}|{etc_reg}|{eg_reg}|{c_reg}|{ie_reg}|{initials_reg})|" \
                           f"{not_punc_reg})*{punc_reg_2})"

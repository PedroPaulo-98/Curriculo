import subprocess
import os

arquivo_tex = "curriculum.tex"
diretorio = os.path.dirname(os.path.abspath(arquivo_tex))
subprocess.run(["xelatex", arquivo_tex], cwd=diretorio)

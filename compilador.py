import subprocess
import os

arquivo_tex = "curriculo.tex"
diretorio = os.path.dirname(os.path.abspath(arquivo_tex))
subprocess.run(["xelatex", arquivo_tex], cwd=diretorio)

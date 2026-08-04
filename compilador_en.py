import shutil
import subprocess
import sys
from pathlib import Path

arquivo_tex = "curriculum.tex"
diretorio = Path(__file__).resolve().parent
pdf_final = "curriculum_Pedro_Paulo_Almeida.pdf"


def compilar_com_xelatex() -> None:
    subprocess.run(
        ["xelatex", "-interaction=nonstopmode", arquivo_tex],
        cwd=diretorio,
        check=True,
    )


def compilar_com_docker() -> None:
    if not shutil.which("docker"):
        raise FileNotFoundError(
            "Nem xelatex nem docker foram encontrados. "
            "Instale o MacTeX/BasicTeX ou o Docker."
        )

    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{diretorio}:/data",
            "-w",
            "/data",
            "texlive/texlive:latest",
            "xelatex",
            "-interaction=nonstopmode",
            arquivo_tex,
        ],
        check=True,
    )


def main() -> None:
    try:
        if shutil.which("xelatex"):
            print("Compilando com xelatex local...")
            compilar_com_xelatex()
        else:
            print("xelatex não encontrado. Compilando com Docker...")
            compilar_com_docker()

        origem = diretorio / arquivo_tex.replace(".tex", ".pdf")
        destino = diretorio / pdf_final
        if origem.exists():
            shutil.copy2(origem, destino)
            print(f"PDF gerado: {origem.name}")
            print(f"Cópia: {destino.name}")
        else:
            print("Compilação terminou, mas o PDF não foi encontrado.", file=sys.stderr)
            sys.exit(1)
    except subprocess.CalledProcessError as exc:
        print(f"Falha na compilação (código {exc.returncode}).", file=sys.stderr)
        sys.exit(exc.returncode)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

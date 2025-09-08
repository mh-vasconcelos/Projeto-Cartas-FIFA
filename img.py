# remove_bg.py
from rembg import remove as rembg_remove
from PIL import Image
from io import BytesIO
from pathlib import Path

def remove_fundo(input_path: str, output_path: str = "fundo-removido.png"):
    """
    Remove o fundo usando rembg:
    - lê binário da imagem de entrada
    - chama rembg (retorna bytes PNG com alfa)
    - escreve PNG RGBA no disco
    """
    input_path = Path(input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")

    # 1) Lê bytes do arquivo
    with open(input_path, "rb") as f:
        img_bytes = f.read()

    # 2) Executa rembg (retorna bytes PNG)
    try:
        result_bytes = rembg_remove(img_bytes)
    except Exception as e:
        raise RuntimeError(f"rembg falhou: {e}")

    # 3) Converte bytes em PIL e salva (garantindo RGBA)
    img = Image.open(BytesIO(result_bytes)).convert("RGBA")
    img.save(output_path)

    return output_path

# Exemplo de uso
if __name__ == "__main__":
    out = remove_fundo("ringo.jpg", "imagem_sem_fundo.png")
    print("Salvo em:", out)

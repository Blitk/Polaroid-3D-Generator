```python
import argparse
from pathlib import Path

from PIL import (
    Image,
    ImageOps,
    ImageDraw,
    ImageFont,
    ImageFilter
)


# ============================================================
# CONFIGURAÇÃO DA FONTE
# ============================================================

def carregar_fonte(tamanho):
    """
    Carrega a fonte usada na assinatura da Polaroid.

    A fonte deve estar dentro da pasta:

        fonts/Pacifico-Regular.ttf

    dentro do mesmo diretório deste script.

    Caso a fonte não seja encontrada, o programa utiliza
    a fonte padrão do Pillow.
    """

    caminho_fonte = (
        Path(__file__).parent
        / "fonts"
        / "Pacifico-Regular.ttf"
    )

    try:
        return ImageFont.truetype(
            caminho_fonte,
            tamanho
        )

    except OSError:
        print(
            "Aviso: fonte Pacifico-Regular.ttf "
            "não encontrada. Usando fonte padrão."
        )

        return ImageFont.load_default()


# ============================================================
# CRIAÇÃO DA POLAROID
# ============================================================

def criar_polaroid(
    caminho_imagem,
    instagram,
    caminho_saida=None
):
    """
    Cria uma imagem no estilo Polaroid 3D.

    Parâmetros:
        caminho_imagem:
            Caminho da foto original.

        instagram:
            Nome do Instagram que será exibido
            na parte inferior da Polaroid.

            Exemplo:
                @pessoa

        caminho_saida:
            Caminho opcional para salvar a imagem.

            Caso não seja informado, o programa cria
            automaticamente um arquivo com "_polaroid"
            no nome original.
    """

    # --------------------------------------------------------
    # ABRIR IMAGEM
    # --------------------------------------------------------

    imagem = Image.open(
        caminho_imagem
    ).convert("RGB")


    # ========================================================
    # CONFIGURAÇÕES DA POLAROID
    # ========================================================

    # Tamanho da fotografia dentro da Polaroid.
    foto_largura = 800
    foto_altura = 800

    # Espaçamento lateral da fotografia.
    margem_lateral = 70

    # Espaçamento superior da fotografia.
    margem_superior = 70

    # Espaço inferior maior para permitir
    # a assinatura do Instagram.
    margem_inferior = 220


    # Calcula o tamanho total da Polaroid.

    polaroid_largura = (
        foto_largura
        + margem_lateral * 2
    )

    polaroid_altura = (
        foto_altura
        + margem_superior
        + margem_inferior
    )


    # ========================================================
    # REDIMENSIONAR FOTO
    # ========================================================

    # ImageOps.fit redimensiona e corta a imagem
    # proporcionalmente para preencher exatamente
    # o tamanho desejado.

    foto = ImageOps.fit(
        imagem,
        (
            foto_largura,
            foto_altura
        ),
        method=Image.Resampling.LANCZOS
    )


    # ========================================================
    # CRIAR POLAROID
    # ========================================================

    # Cria uma folha branca onde a foto será posicionada.

    polaroid = Image.new(
        "RGBA",
        (
            polaroid_largura,
            polaroid_altura
        ),
        (255, 255, 255, 255)
    )


    # --------------------------------------------------------
    # POSICIONAR FOTO
    # --------------------------------------------------------

    polaroid.paste(
        foto,
        (
            margem_lateral,
            margem_superior
        )
    )


    # Cria o objeto responsável pelos desenhos
    # na imagem.

    draw = ImageDraw.Draw(
        polaroid
    )


    # ========================================================
    # PEQUENA SOMBRA ABAIXO DA FOTO
    # ========================================================

    # Cria uma pequena linha cinza abaixo da fotografia,
    # dando a impressão de profundidade.

    draw.rectangle(
        [
            margem_lateral,
            margem_superior + foto_altura,

            margem_lateral + foto_largura,
            margem_superior + foto_altura + 2
        ],
        fill=(220, 220, 220, 255)
    )


    # ========================================================
    # ASSINATURA DO INSTAGRAM
    # ========================================================

    # Carrega a fonte da assinatura.

    fonte = carregar_fonte(45)


    # O Instagram agora vem como argumento
    # do programa.

    texto = instagram


    # --------------------------------------------------------
    # CALCULAR TAMANHO DO TEXTO
    # --------------------------------------------------------

    bbox = draw.textbbox(
        (0, 0),
        texto,
        font=fonte
    )

    texto_largura = (
        bbox[2] - bbox[0]
    )

    texto_altura = (
        bbox[3] - bbox[1]
    )


    # Espaçamento entre a assinatura e a borda direita.

    margem_carimbo = 45


    # --------------------------------------------------------
    # CALCULAR POSIÇÃO
    # --------------------------------------------------------

    # Posiciona o Instagram no canto inferior direito.

    texto_x = (
        polaroid_largura
        - texto_largura
        - margem_carimbo
    )

    texto_y = (
        polaroid_altura
        - texto_altura
        - 35
    )


    # --------------------------------------------------------
    # DESENHAR ASSINATURA
    # --------------------------------------------------------

    draw.text(
        (
            texto_x,
            texto_y
        ),
        texto,
        font=fonte,
        fill=(138, 154, 91, 255)
    )


    # ========================================================
    # EFEITO 3D
    # ========================================================

    # Espaço adicional ao redor da Polaroid.
    # Esse espaço permite criar a sombra projetada.

    padding = 160


    # Tamanho final da imagem.

    canvas_largura = (
        polaroid_largura
        + padding * 2
    )

    canvas_altura = (
        polaroid_altura
        + padding * 2
    )


    # --------------------------------------------------------
    # FUNDO
    # --------------------------------------------------------

    canvas = Image.new(
        "RGBA",
        (
            canvas_largura,
            canvas_altura
        ),
        (245, 245, 245, 255)
    )


    # ========================================================
    # SOMBRA PROJETADA
    # ========================================================

    # Cria uma camada transparente para a sombra.

    sombra = Image.new(
        "RGBA",
        (
            canvas_largura,
            canvas_altura
        ),
        (0, 0, 0, 0)
    )


    sombra_draw = ImageDraw.Draw(
        sombra
    )


    # Desenha um retângulo preto levemente deslocado.

    sombra_draw.rectangle(
        [
            padding + 25,
            padding + 35,

            padding + polaroid_largura + 25,
            padding + polaroid_altura + 35
        ],
        fill=(0, 0, 0, 100)
    )


    # Desfoca a sombra para deixá-la mais natural.

    sombra = sombra.filter(
        ImageFilter.GaussianBlur(30)
    )


    # Coloca a sombra no canvas.

    canvas.alpha_composite(
        sombra
    )


    # ========================================================
    # EFEITO DE PROFUNDIDADE
    # ========================================================

    # Cria uma cópia da Polaroid.

    profundidade = polaroid.copy()


    # Cria uma camada preta parcialmente transparente.

    profundidade_overlay = Image.new(
        "RGBA",
        profundidade.size,
        (0, 0, 0, 35)
    )


    # Aplica a camada sobre a cópia.

    profundidade = Image.alpha_composite(
        profundidade,
        profundidade_overlay
    )


    # Coloca essa cópia ligeiramente deslocada.
    # Isso cria uma sensação de profundidade.

    canvas.alpha_composite(
        profundidade,
        (
            padding + 8,
            padding + 12
        )
    )


    # ========================================================
    # POLAROID PRINCIPAL
    # ========================================================

    # Coloca a Polaroid original por cima da camada
    # de profundidade.

    canvas.alpha_composite(
        polaroid,
        (
            padding,
            padding
        )
    )


    # ========================================================
    # BORDA DE LUZ
    # ========================================================

    # Cria uma camada transparente para o contorno.

    brilho = Image.new(
        "RGBA",
        polaroid.size,
        (0, 0, 0, 0)
    )


    brilho_draw = ImageDraw.Draw(
        brilho
    )


    # Desenha uma pequena borda branca.

    brilho_draw.rectangle(
        [
            2,
            2,

            polaroid_largura - 3,
            polaroid_altura - 3
        ],
        outline=(255, 255, 255, 180),
        width=3
    )


    # Aplica a borda sobre a Polaroid.

    canvas.alpha_composite(
        brilho,
        (
            padding,
            padding
        )
    )


    # ========================================================
    # DEFINIR ARQUIVO DE SAÍDA
    # ========================================================

    # Se o usuário não informou onde salvar,
    # cria automaticamente um nome.

    if caminho_saida is None:

        caminho = Path(
            caminho_imagem
        )

        caminho_saida = (
            caminho.parent
            / f"{caminho.stem}_polaroid.jpg"
        )


    # ========================================================
    # CONVERTER PARA RGB
    # ========================================================

    # JPEG não suporta transparência (RGBA).
    #
    # Por isso criamos uma imagem RGB branca e
    # utilizamos o canal Alpha como máscara.

    resultado = Image.new(
        "RGB",
        canvas.size,
        "white"
    )


    resultado.paste(
        canvas,
        mask=canvas.getchannel("A")
    )


    # ========================================================
    # SALVAR
    # ========================================================

    resultado.save(
        caminho_saida,
        "JPEG",
        quality=95
    )


    # Exibe informações no terminal.

    print(
        "\nPolaroid criada com sucesso!"
    )

    print(
        f"Instagram: {instagram}"
    )

    print(
        f"Arquivo: {caminho_saida}"
    )


# ============================================================
# INTERFACE DE LINHA DE COMANDO
# ============================================================

def main():

    # Cria o parser responsável por interpretar
    # os argumentos fornecidos pelo usuário.

    parser = argparse.ArgumentParser(
        description=(
            "Transforma uma foto em uma "
            "Polaroid com efeito 3D."
        )
    )


    # --------------------------------------------------------
    # FOTO DE ENTRADA
    # --------------------------------------------------------

    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Caminho da imagem de entrada."
    )


    # --------------------------------------------------------
    # INSTAGRAM
    # --------------------------------------------------------

    parser.add_argument(
        "-i",
        "--instagram",
        required=True,
        help=(
            "Instagram que será exibido "
            "na Polaroid. Exemplo: @pessoa"
        )
    )


    # --------------------------------------------------------
    # ARQUIVO DE SAÍDA
    # --------------------------------------------------------

    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help=(
            "Caminho do arquivo de saída. "
            "Se omitido, será criado automaticamente."
        )
    )


    # Processa os argumentos.

    args = parser.parse_args()


    # Cria a Polaroid.

    criar_polaroid(
        caminho_imagem=args.file,
        instagram=args.instagram,
        caminho_saida=args.output
    )


# ============================================================
# PONTO DE ENTRADA
# ============================================================

# Executa main() somente quando este arquivo
# for executado diretamente.

if __name__ == "__main__":
    main()
```

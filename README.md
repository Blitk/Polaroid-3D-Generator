# 📸 Polaroid 3D Generator

Um script em **Python** que transforma fotos comuns em imagens no estilo **Polaroid**, adicionando:

* 🖼️ Moldura estilo Polaroid
* ✨ Efeito de profundidade 3D
* 🌑 Sombra projetada
* 💡 Borda de luz
* 📱 Instagram personalizado
* 🔤 Fonte personalizada
* 🐍 Interface via linha de comando (CLI)

O projeto utiliza **Python + Pillow** e foi desenvolvido para ser simples de utilizar e modificar.

---

## 🖼️ Exemplo

O script recebe uma fotografia e gera automaticamente uma composição semelhante a uma fotografia Polaroid física.

Você pode informar qualquer Instagram na hora de executar o programa:

```bash
python polaroid.py -f foto.jpg -i @pessoa
```

O Instagram informado será exibido na parte inferior da Polaroid.

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

Entre na pasta:

```bash
cd SEU-REPOSITORIO
```

### 2. Instale o Pillow

O projeto utiliza a biblioteca **Pillow** para manipulação das imagens.

```bash
pip install Pillow
```

Ou:

```bash
python -m pip install Pillow
```

---

## 📁 Estrutura do projeto

```text
polaroid/
│
├── polaroid.py
│
├── fonts/
│   └── Pacifico-Regular.ttf
│
├── README.md
│
└── exemplo.jpg
```

### `polaroid.py`

Arquivo principal responsável pela geração da imagem.

### `fonts/`

Contém a fonte utilizada na assinatura da Polaroid.

### `README.md`

Documentação do projeto.

---

# 💻 Como usar

O programa possui três argumentos principais.

| Argumento            | Obrigatório | Descrição                           |
| -------------------- | ----------- | ----------------------------------- |
| `-f` / `--file`      | ✅ Sim       | Caminho da imagem de entrada        |
| `-i` / `--instagram` | ✅ Sim       | Instagram que aparecerá na Polaroid |
| `-o` / `--output`    | ❌ Não       | Nome/caminho do arquivo de saída    |

---

## 📷 Exemplo básico

```bash
python polaroid.py -f foto.jpg -i @pessoa
```

Nesse caso:

* `foto.jpg` é a imagem original;
* `@pessoa` será exibido na Polaroid;
* o programa criará automaticamente um arquivo chamado:

```text
foto_polaroid.jpg
```

---

## 📂 Escolhendo o arquivo de saída

Você também pode definir onde deseja salvar o resultado:

```bash
python polaroid.py -f foto.jpg -i @pessoa -o resultado.jpg
```

O arquivo será salvo como:

```text
resultado.jpg
```

Também é possível utilizar caminhos:

```bash
python polaroid.py -f fotos/foto.jpg -i @pessoa -o resultados/polaroid.jpg
```

---

# 🛠️ Argumentos disponíveis

Para visualizar todos os argumentos:

```bash
python polaroid.py --help
```

Exemplo de saída:

```text
usage: polaroid.py [-h] -f FILE -i INSTAGRAM [-o OUTPUT]

Transforma uma foto em uma Polaroid com efeito 3D.

options:
  -h, --help
      show this help message and exit

  -f FILE, --file FILE
      Caminho da imagem de entrada.

  -i INSTAGRAM, --instagram INSTAGRAM
      Instagram que será exibido na Polaroid.

  -o OUTPUT, --output OUTPUT
      Caminho do arquivo de saída.
```

---

# 🎨 Personalização

O projeto foi desenvolvido para que outras pessoas possam modificá-lo facilmente.

Dentro de `polaroid.py` existem algumas configurações que podem ser alteradas.

### Tamanho da fotografia

```python
foto_largura = 800
foto_altura = 800
```

Por exemplo:

```python
foto_largura = 1000
foto_altura = 1000
```

---

### Margens

```python
margem_lateral = 70
margem_superior = 70
margem_inferior = 220
```

Esses valores controlam o tamanho da moldura branca.

---

### Tamanho da assinatura

```python
fonte = carregar_fonte(45)
```

Você pode aumentar ou diminuir o tamanho:

```python
fonte = carregar_fonte(60)
```

---

### Cor da assinatura

Atualmente:

```python
fill=(138, 154, 91, 255)
```

O formato utilizado é:

```text
(R, G, B, Alpha)
```

Por exemplo, para utilizar preto:

```python
fill=(0, 0, 0, 255)
```

---

# 🔤 Fonte

A fonte utilizada neste projeto é a **Pacifico**.

O arquivo deve estar localizado em:

```text
fonts/Pacifico-Regular.ttf
```

O código procura automaticamente a fonte nessa pasta.

Caso ela não seja encontrada, o programa utiliza a fonte padrão do Pillow.

---

# 🧩 Tecnologias utilizadas

* 🐍 Python
* 🖼️ Pillow
* 📁 pathlib
* ⚙️ argparse

### Pillow

Responsável pelo processamento das imagens.

### pathlib

Utilizado para trabalhar com caminhos e arquivos de forma multiplataforma.

### argparse

Responsável pela interface de linha de comando.

---

# 📋 Requisitos

* Python **3.9 ou superior**
* Pillow

Verifique sua versão do Python:

```bash
python --version
```

---

# 🖥️ Sistemas operacionais

O script pode ser utilizado em diferentes sistemas operacionais, incluindo:

* Windows
* Linux
* macOS

Desde que o Python e o Pillow estejam instalados corretamente.

---

# 🔄 Fluxo do programa

De forma simplificada, o programa realiza:

```text
Imagem original
      │
      ▼
Redimensionamento
      │
      ▼
Criação da moldura
      │
      ▼
Inserção do Instagram
      │
      ▼
Criação da sombra
      │
      ▼
Efeito de profundidade
      │
      ▼
Borda de luz
      │
      ▼
Imagem Polaroid final
```

---

# 📌 Exemplos

### Instagram pessoal

```bash
python polaroid.py -f viagem.jpg -i @meuinstagram
```

### Instagram de uma loja

```bash
python polaroid.py -f produto.jpg -i @minhaloja
```

### Definindo o nome do resultado

```bash
python polaroid.py -f casamento.jpg -i @fotografo -o casamento_polaroid.jpg
```

---

# 🤝 Contribuindo

Contribuições são bem-vindas!

Você pode:

1. Fazer um **Fork** do projeto.
2. Criar uma branch:

```bash
git checkout -b minha-melhoria
```

3. Fazer suas alterações.
4. Commitar:

```bash
git commit -m "Adiciona nova melhoria"
```

5. Enviar para seu repositório:

```bash
git push origin minha-melhoria
```

6. Abrir um **Pull Request**.

---

# 💡 Ideias para futuras melhorias

Algumas funcionalidades que podem ser adicionadas:

* [ ] Escolha da cor da moldura
* [ ] Escolha da fonte via argumento
* [ ] Tamanho da Polaroid configurável
* [ ] Rotação da Polaroid
* [ ] Filtros fotográficos
* [ ] Diferentes estilos de sombra
* [ ] Exportação em PNG
* [ ] Processamento de várias imagens
* [ ] Interface gráfica
* [ ] Suporte a diferentes formatos de imagem

---

## 👨‍💻 Autor

Desenvolvido por **Raphael Rodrigues Oliveira**.

Projeto criado como uma ferramenta simples de processamento de imagens em Python e disponibilizado para que outras pessoas possam estudar, modificar e utilizar em seus próprios projetos.

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!

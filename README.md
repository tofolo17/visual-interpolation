# visual-interpolation

> 🇧🇷 [Português](#o-que-você-encontrará-neste-repositório) · 🇺🇸 [English](#what-will-you-find-in-this-repository)

## O que você encontrará neste repositório?

Visualização interativa de **interpolação**, feita em **julho de 2022** durante os estudos de métodos numéricos no
IME-USP (o repositório começou como `MAP2110-files`). Você clica na tela para criar pontos e vê, em tempo real, a
interpolação **linear** (segmentos brancos) e a **spline cúbica natural** (curva roxa) passando por eles.

A spline foi implementada a partir do zero, seguindo o Algoritmo 3.4 de *Numerical Analysis* (Burden & Faires, 9ª ed.),
sem usar SciPy. A mesma ideia de "clicar e ver a curva" reaparece, mais completa, na ferramenta da minha iniciação
científica, [SIICUSP-2025-5333](https://github.com/tofolo17/SIICUSP-2025-5333).

### Estrutura

- **`pyg/`** — a versão interativa em Pygame:
  - `run.py` — laço principal e eventos do mouse;
  - `Graphics/dots.py` — pontos editáveis, sempre mantidos em ordem de x;
  - `Graphics/interpolation.py` — classes `Linear` e `Spline` (a partir de uma base abstrata `Interpolation`);
  - `UI/` — esboço de caixas de seleção para ligar/desligar cada curva (não finalizado).
- **`matplotlib/`** — primeira versão: a mesma spline aplicada a um conjunto fixo de pontos e plotada com Matplotlib;
  `Modules/random.py` traz geradores pseudoaleatórios simples (congruencial linear e "meio do quadrado").

### Ferramentas

Python 3, Pygame, NumPy e Matplotlib.

### Como usar

```bash
git clone https://github.com/tofolo17/visual-interpolation.git
cd visual-interpolation
pip install -r requirements.txt
python -m pyg.run
```

| Ação                       | Controle                                  |
|----------------------------|-------------------------------------------|
| Adicionar / arrastar ponto | botão esquerdo do mouse                   |
| Remover ponto              | botão direito do mouse                    |

Para a versão em Matplotlib: `cd matplotlib && python main.py`.

### Licença

[MIT](LICENSE)

---

## What will you find in this repository?

An interactive **interpolation** visualizer, made in **July 2022** while studying numerical methods at IME-USP (the
repository started as `MAP2110-files`). You click on the screen to create points and watch, in real time, the
**linear** interpolation (white segments) and the **natural cubic spline** (purple curve) going through them.

The spline was implemented from scratch, following Algorithm 3.4 of *Numerical Analysis* (Burden & Faires, 9th ed.),
without SciPy. The same "click and see the curve" idea comes back, more complete, in my undergraduate research tool,
[SIICUSP-2025-5333](https://github.com/tofolo17/SIICUSP-2025-5333).

### Structure

- **`pyg/`** — the interactive Pygame version:
  - `run.py` — main loop and mouse events;
  - `Graphics/dots.py` — editable points, always kept sorted by x;
  - `Graphics/interpolation.py` — `Linear` and `Spline` classes (from an abstract `Interpolation` base);
  - `UI/` — a sketch of checkboxes to toggle each curve (unfinished).
- **`matplotlib/`** — the first version: the same spline applied to a fixed set of points and plotted with Matplotlib;
  `Modules/random.py` holds simple pseudo-random generators (linear congruential and "middle-square").

### Tools

Python 3, Pygame, NumPy and Matplotlib.

### How to use

```bash
git clone https://github.com/tofolo17/visual-interpolation.git
cd visual-interpolation
pip install -r requirements.txt
python -m pyg.run
```

| Action                  | Control                                   |
|-------------------------|-------------------------------------------|
| Add / drag a point      | left mouse button                         |
| Remove a point          | right mouse button                        |

For the Matplotlib version: `cd matplotlib && python main.py`.

### License

[MIT](LICENSE)

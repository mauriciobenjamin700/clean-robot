# Desafio

- Crie uma tabuleiro de Tamanho MxN, onde M e N são números inteiros positivos.
- O tabuleiro deve ser preenchido com 0 para local vazio, -1 para lixo e 1 para obstaculos.
- O robô deve começar na posição (X,Y) e deve se mover somente dentro do tabuleiro.
- O robô deve se mover apenas na horizontal e vertical.
- O robô não ficar em cima de obstaculos.
- O robô só pode dar "um passo" por vez.
- O robô deve andar sozinho e limpar todas as zonas possíveis

## Dependências para Linux Ubuntu

```bash
sudo apt update

sudo apt install libmpv-dev libmpv2

sudo ln -s /usr/lib/x86_64-linux-gnu/libmpv.so /usr/lib/libmpv.so.1

```

[Fonte](https://stackoverflow.com/questions/78007193/error-while-loading-shared-libraries-libmpv-so-1-cannot-open-shared-object-fil)

```bash
sudo apt-get update
sudo apt-get upgrade
sudo ubuntu-drivers autoinstall
```

## Criando um Projeto Flet

```bash
flet create .
```

```bash
flet run [app_directory]
```

## Ronando um Arquivo Flet na Web

```bash
flet run --web test.py
```

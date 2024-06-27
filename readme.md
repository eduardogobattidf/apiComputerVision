# DFvision - Visão Computacional

## Introdução
DFvision é uma API de reconhecimento de imagem que utiliza algoritmo de transforns para identificar produtos em imagens. Este projeto visa oferecer uma solução eficiente e fácil de usar para integrar reconhecimento de imagens em suas aplicações.

## Guia de Instalação

### Passo 1: Baixar e Instalar o Python
Para começar, você precisa ter o Python instalado em sua máquina. Você pode baixar a versão mais recente do Python no [site oficial](https://www.python.org/downloads/).

### Passo 2: Montar o Ambiente Virtual
É recomendado usar um ambiente virtual para gerenciar as dependências do projeto. Siga os passos abaixo para criar um ambiente virtual usando o `venv`:

1. Abra o terminal (ou prompt de comando).
2. Navegue até o diretório do seu projeto:

   ```bash
   cd caminho/do/seu/projeto


3. Crie um ambiente virtual:

```bash
   python -m venv .venv
```
4. Ative o ambiente virtual:

No Windows:
```bash
   .venv\Scripts\activate
```
No macOS/Linux:
```bash
  source .venv/bin/activate
```

### Passo 3: Instalar Dependências

Com o ambiente virtual ativado, instale as dependências necessárias usando o arquivo requirements.txt:
```bash
  pip install -r requirements.txt
```

## Uso da API
Após configurar o ambiente, você pode iniciar a API. O repositório contém duas rotas principais:

1. Verificar se a API está online
Rota: /
Método: GET
Descrição: Esta rota é usada para verificar se a API está online.
Resposta Esperada: "It's live"


2. Verificar Imagem
Rota: /verificaImage
Método: POST
Descrição: Esta rota é usada para enviar uma imagem para reconhecimento de produto.
Payload Esperado: JSON no formato {"image_url": "O link da imagem"}
Funcionamento: A API irá chamar o método de reconhecimento de produto e retornar o resultado.

## Exemplo de Requisição

### Verificar se a API está online
```bash
  curl -X GET http://localhost:5000/
```

### Verificar Imagem
```bash
curl -X POST http://localhost:5000/verificaImage -H "Content-Type: application/json" -d '{"image_url": "http://example.com/sua-imagem.jpg"}'
```

Este é um exemplo básico de como configurar e utilizar a API de reconhecimento de imagem DFvision. Certifique-se de ajustar os detalhes conforme necessário para o seu ambiente e requisitos específicos.
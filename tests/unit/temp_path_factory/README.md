# 🧪 Testes com criação de diretórios e arquivos temporários (`tmp_path` / `tmp_path_factory`)

Este pasta contém exemplos práticos demonstrando o uso de fixtures do **pytest**
para manipulação de arquivos e diretórios temporários durante os testes automatizados.

## 📘 Conceitos abordados

- Uso da fixture `tmp_path` para criar arquivos temporários em testes.
- Uso da fixture `tmp_path_factory` para gerar diretórios e arquivos compartilhados entre múltiplos testes.
- Diferença conceitual e prática entre `tmp_path` e `tmp_path_factory`.
- Manipulação de arquivos com `with open()` e boas práticas de fechamento automático.
- Compreensão da classe `_io.TextIOWrapper`, com métodos `.read()`, `.write()`, `.seek()` e `.close()` após abertura de arquivos.
- Compreensão do objeto `WindowsPath` da classe `pathlib.Path`, responsável por representar e manipular caminhos de arquivos.
- Entendimento de que as fixtures `tmp_path` e `tmp_path_factory` retornam objetos `WindowsPath` (ou `PosixPath` em sistemas Linux).
- Aplicação dos conceitos em **cenários reais**, como geração e validação de arquivos CSV temporários usados em testes de integração.

---

📂 Exemplos incluídos:
- Criação e remoção automática de arquivos temporários.
- Validação de conteúdo e estrutura de arquivos `.csv`.
- Testes com uso de setup, yield e teardown em fixtures para controlar o ciclo de vida dos arquivos temporários.
- Uso do arquivo `conftest.py` para agrupamento das fixtures em um único arquivo

# 🧪 Exemplos práticos de Testes com chamadas assíncronas

Exemplo real de testes de funções assíncronas incluindo  o uso de patch como decorator, mocker.path e mocker.patch.object para zombar(mockar) métodos e funções assíncronas.

## 📘 Conceitos abordados

-- Criação de classes/funções simples envolvendo chamadas assíncronas
-- Testes de funções assíncronass
-- Testes de funções assíncronas utilizando decorator patch, mocker.patch e mocker.patch.object para zombar(mockar).
-- Reforçou a compreensão da diferença entre utilizar patch decorator x mocker.patch x mocker.patch.object.
-- Compressão diferença entre as classes `Mock` x `AsyncMock`.

---

📂 **Estrutura de pastas de deste tópico:**

```sh

pytest/
└── tests/
    └── unit/
        └── async_functions/
            ├── src/
            │   ├── basic.py
            |   ├── cat_fact.py
            ├── README.md
            ├── test_async_cat_fact.py
            ├── test_basic.py
            ├── test_mock_version.py

```
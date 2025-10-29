# 🧪 Exemplos práticos de Testes com Mock/Patch

Exemplo real de mock/patch com exemplos simples para autorização de produto, calculo de peso de matéria prima e busca de rota para drone.

## 📘 Conceitos abordados

- Mock genericos criação de classes/funções
- Mocks com classes Reais
- Uso da fixture `mocker` do plugin `pytest-mock` ao invés de importar a classe `Mock`
- Patch
- Testes Unitários
- Isolamento com mock de algumas funções para atingir objetivo real do teste
- Fazerem com que testes obdeçam a assinatura da função/classe com `autospec`
- Compreensão entre return_value x side_effect no uso do patch
---

📂 **Estrutura de pastas de deste tópico:**

```sh

pytest/
└── tests/
    └── integration/
        └── mock_patch/
            ├── src/
            │   ├── produto.py
            |   ├── rota_drone.py
            ├── README.md
            ├── test_mock_generic.py
            ├── test_mock_real_class_produto_autospec.py
            ├── test_mock_real_class_produto.py
            ├── test_patch_requests.py
            ├── test_patch_return_value_side_effect.py

```
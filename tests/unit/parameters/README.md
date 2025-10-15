# 🧪 Testes com Parametrizações

As parametrizações foram aplicadas em testes com funções, classes e fixtures.  
Foram desenvolvidos cenários que exploram diferentes estratégias de parametrização e geração dinâmica de dados de teste.

## 📘 Conceitos abordados

- Compreensão de testes com parametrização em **funções, classes e fixtures**.
- Compreensão de testes de função com **parametrização combinada** (múltiplos `@parametrize` empilhados).
- Compreensão de testes utilizando o recurso **`pytest_generate_tests`**, que permite **parametrizações dinâmicas** geradas em tempo de coleta.
- Exemplos de **regras de negócio reais** aplicadas aos testes (como cálculos de peso de máteria prima em Aluminio ou Ferro e descontos de produtos por categoria_id).
- Criação da pasta `/src`, que contém **funções de exemplo** representando o contexto de negócio, separando a lógica de domínio do código de teste.

---

📂 **Estrutura de pastas de deste tópico:**

```sh

pytest/
└── tests/
    └── unit/
        └── parameters/
            │
            tests/
                ├── src/
                │   ├── calcular_valor_total_produto.py
                │   ├── class_parameterization.py
                |   |__ function_parameterization.py
                ├── conftest.py
                ├── test_function_parametrization.py
                ├── test_class_parametrization.py
                ├── test_function_parameterization_combined.py
                ├── test_fixture_parametrization.py
                ├── test_generate_tests.py
                ├── README.md 

```

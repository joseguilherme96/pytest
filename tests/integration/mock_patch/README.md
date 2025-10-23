# 🧪 Exemplos Práticos de Testes com Mock

Exemplo real de mock em uma implementação conceitual simples real baseado no voo de um drone.

## 📘 Conceitos abordados

- Implementação conceitual
- Falsificação de classes
- Mock
- Testes de integração Hibrida(com Mock + Falsificação + Classe Real)
- Isolamento com mock de algumas funções para atingir objetivo real do teste
- Fazerem com que testes obdeçam a assinatura da função/classe com `autospec`
- Registros de logs com a classe `logging`
- Uso da fixture `caplog` do pytest para exibir os logs caso houver erro.
- Injeção de Depêndencia
- Classe Base Abstratata(ABC) que define contratos entre a classe fornecedora e a classe consumidora.
- Realizado um exemplo prático de teste de zombaria(Mock) de uma classe conceitual que coloca processa imagens, alterando suas dimensões automaticamente de acordo com a quantidade de imagens por folha, após alteração, o processamento é finalizado com a inserção automática destas imagens dentro de uma folha padronizada no modelo A4, após a inserção o pdf com as imagens é gerado automaticamente.
---

📂 **Estrutura de pastas de deste tópico:**

```sh

pytest/
└── tests/
    └── integration/
        └── mock_patch/
            ├── src/
            │   ├── implementacao_conceitual_drone_para_teste_mock.py
            ├── README.md
            ├── test_mock_bateria_baixa_drone.py
            ├── test_mock_sensor_drone.py
            ├── test_dependency_injection.py
```
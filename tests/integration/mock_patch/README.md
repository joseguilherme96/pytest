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
```
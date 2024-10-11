# Sistema Bancário em Python

## Descrição

Este é um sistema bancário simples, desenvolvido em Python, que implementa as operações básicas de um banco: Depósito, Saque e Extrato. O sistema foi projetado para permitir a interação do usuário por meio de um menu intuitivo, permitindo realizar transações com limite diário de saques.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

1. **Depósito**: Permite ao usuário adicionar um valor positivo ao saldo da conta.
2. **Saque**: O usuário pode sacar um valor, respeitando o limite diário e o limite por transação.
3. **Extrato**: Mostra todas as movimentações (depósitos e saques) realizadas no período.
4. **Limite de Saque por Transação**: Exibe o valor máximo que pode ser sacado em uma única transação.
5. **Limite de Saques Diários Restantes**: Informa quantos saques ainda podem ser feitos no dia.
6. **Sair**: Encerra a aplicação.

## Regras de Negócio

- O sistema permite um limite de **3 saques diários**.
- O **limite máximo por saque** é de **R$500,00**.
- Não é possível realizar depósitos ou saques com valores negativos ou inválidos.
- O extrato apresenta todas as movimentações e o saldo atualizado do usuário.

## Menu de Operações

O menu oferece as seguintes opções:

```bash
[1] Depositar
[2] Sacar
[3] Extrato
[4] Limite de Saque por Transação
[5] Limite de Saques Diários Restantes
[0] Sair

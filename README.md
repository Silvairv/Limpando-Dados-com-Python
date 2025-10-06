# 🐼 Exemplos de Tratamento de Dados Faltantes com Pandas

Este repositório contém um script Python que demonstra várias técnicas comuns para tratar valores ausentes (`NaN` - Not a Number) em DataFrames do Pandas. O tratamento de dados faltantes é uma etapa crucial no processo de limpeza e preparação de dados para análise.

## 📜 Sobre o Código

O script cria três DataFrames distintos para ilustrar diferentes cenários e as estratégias de preenchimento mais adequadas para cada um:

1.  **Dados Numéricos Contínuos (Salários):** Preenchimento com medidas de tendência central.
2.  **Dados Sequenciais (Temperaturas):** Preenchimento por propagação.
3.  **Dados Categóricos (Cidades):** Preenchimento com um valor constante.

-----

## 🛠️ Técnicas Demonstradas

Abaixo estão detalhadas as técnicas utilizadas no script.

### 1\. Preenchimento com Medidas Estatísticas (Média e Mediana)

Ideal para colunas numéricas onde os dados faltantes podem ser razoavelmente representados por uma medida de tendência central do conjunto de dados existente.

  * **Média (`.mean()`):** Substitui os valores nulos pela média de todos os outros valores na coluna. É sensível a outliers (valores extremos).
  * **Mediana (`.median()`):** Substitui os valores nulos pela mediana (o valor central). É mais robusta a outliers, sendo geralmente uma escolha mais segura.

## ⚙️ Como Executar o Código

Para rodar este script, você precisa ter o Python e as bibliotecas Pandas e NumPy instaladas.

1.  **Instale as dependências:**

    ```bash
    pip install pandas numpy
    ```

2.  **Execute o script:**
    Salve o código em um arquivo (ex: `tratar_nulos.py`) e execute-o pelo terminal:

    ```bash
    python tratar_nulos.py
    ```

    Alternativamente, você pode executar cada célula de código em um ambiente interativo como [Jupyter Notebook](https://jupyter.org/) para analisar a saída de cada etapa individualmente.

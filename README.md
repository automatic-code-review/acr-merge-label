# acr-merge-label

Arquivo config.json

- configs
    - description: Descrição do comentario que deve ser adicionado
    - labels: Labels que precisam estar presente
    - authors: Autores que ira verificar se tem a label
    - branches: Branches que ira verificar se tem a label, sendo uma lista de regex

```json
{
  "stage": "static",
  "language": "PYTHON",
  "configs": [
    {
      "description": "${LABEL}",
      "labels": [
        ""
      ],
      "authors": [
        ""
      ]
    },
    {
      "description": "${LABEL}",
      "labels": [
        ""
      ],
      "branches": [
        ""
      ]
    }
  ]
}

```

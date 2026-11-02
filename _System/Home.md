---
type: system
---
# Home

## Inbox
```dataview
LIST FROM "Inbox" SORT file.ctime DESC
```

## Bancos de dados
```dataview
TABLE WITHOUT ID file.link AS "Nota", status AS "Status"
FROM "Concepts"
WHERE contains(area, "databases")
SORT file.name
```

## Sistemas distribuídos
```dataview
TABLE WITHOUT ID file.link AS "Nota", status AS "Status"
FROM "Concepts"
WHERE contains(area, "distributed-systems")
SORT file.name
```

## System design
```dataview
TABLE WITHOUT ID file.link AS "Nota", status AS "Status"
FROM "Concepts"
WHERE contains(area, "system-design")
SORT file.name
```

## Compiladores
```dataview
TABLE WITHOUT ID file.link AS "Nota", status AS "Status"
FROM "Concepts"
WHERE contains(area, "compilers")
SORT file.name
```

## Algoritmos
```dataview
TABLE WITHOUT ID file.link AS "Nota", status AS "Status"
FROM "Concepts"
WHERE contains(area, "algorithms")
SORT file.name
```

## Redes
```dataview
TABLE WITHOUT ID file.link AS "Nota", status AS "Status"
FROM "Concepts"
WHERE contains(area, "networking")
SORT file.name
```

# Manutenção

## Notas por preencher
```dataview
LIST FROM "Concepts" WHERE status = "stub" SORT file.name
```

## Em andamento
```dataview
LIST FROM "Concepts" WHERE status = "wip" SORT file.name
```

## Precisa de frase de abertura
```dataview
LIST FROM #needs-intro AND "Concepts" SORT file.name
```

## Notas inacabadas
```dataview
LIST FROM #todo AND "Concepts" SORT file.name
```

## Links para notas que não existem
```dataview
TABLE WITHOUT ID out AS "Destino", rows.file.link AS "Citado em"
FROM "Concepts"
FLATTEN file.outlinks AS out
WHERE !out.file AND !contains(string(out), ".png")
GROUP BY out
```

## Notas sem nenhuma conexão
```dataview
LIST FROM "Concepts"
WHERE area AND length(file.inlinks) = 0 AND length(file.outlinks) = 0
SORT file.name
```

# Como usar

1. Escreva livremente: notas novas vão para `Inbox/`, sem template, metadados ou links. Para organizar, peça ao Claude Code: "organize my inbox". Revise o resultado no diff do Git.
2. Comece a nota com uma frase própria dizendo o que é o conceito. Nas notas com a tag `needs-intro`, escreva a frase e remova a tag.
3. Coloque links apenas em `## Related`, nunca no meio do texto. Imagens e notas `moc` são exceção.
4. Em notas inacabadas, adicione `todo` ao campo `tags`, nunca no meio do texto.
5. Preencha `area` com: `databases`, `distributed-systems`, `system-design`, `compilers`, `algorithms` ou `networking`. Uma nota pode ter mais de uma.
6. Preencha `source` com o livro, artigo ou curso de origem.
7. Atualize `status`: `stub` (só o título), `wip` (em andamento) ou `active` (em uso).
8. Use `type` para o tipo da nota: `concept`, `moc` ou `project`.
9. Para aplicar as regras e atualizar o índice sem organizar o inbox, rode `python _System/organize.py`.

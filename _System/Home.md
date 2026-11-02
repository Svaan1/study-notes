---
type: system
---
# Home

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

1. Crie notas em `Concepts/` a partir de um template.
2. Preencha `area` com: `databases`, `distributed-systems`, `system-design`, `compilers`, `algorithms` ou `networking`. Uma nota pode ter mais de uma.
3. Atualize `status`: `stub` (só o título), `wip` (em andamento) ou `active` (em uso).
4. Use `type` para o tipo da nota: `concept`, `moc`, `list`, `note` ou `project`.

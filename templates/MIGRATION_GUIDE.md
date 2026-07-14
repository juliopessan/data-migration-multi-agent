# Dashboard Template — Guia de Migração

Converta um dashboard HTML existente para usar o sistema de template reutilizável.

## 📋 Pré-Requisitos

- Dashboard HTML existente
- Python 3.11+
- 10 minutos do seu tempo

## 🔄 Processo de Migração

### Passo 1: Analisar Estrutura Atual

Abra seu `dashboard.html` existente e identifique:

1. **Variáveis Dinâmicas**
   - Título da página
   - Seções principais
   - Métricas/KPIs
   - Links de navegação
   - Tabelas de dados
   - Botões de ação

2. **Estrutura de Seções**
```html
<!-- Seu dashboard -->
<div class="hero">
  <h1>Título</h1>
  <p>Descrição</p>
</div>

<div class="metrics">
  <div class="metric">...</div>
</div>

<div class="benefits">
  <div class="item">...</div>
</div>
```

### Passo 2: Criar Arquivo de Configuração

Crie `templates/seu-dashboard.json`:

```json
{
  "page_title": "Seu Dashboard | Executivo",
  "page_description": "Descrição",
  "eyebrow": "TIPO",
  "hero_title": "Título com <span class=\"word\">destaque</span>",
  "hero_subtitle": "Subtítulo",
  
  "hero_buttons": [
    {
      "label": "Botão 1 →",
      "href": "link1",
      "style": "primary"
    },
    {
      "label": "Botão 2 →",
      "href": "link2",
      "style": "ghost"
    }
  ],
  
  "metrics": [
    {
      "value": "100",
      "label": "Label 1",
      "emphasize": true
    },
    {
      "value": "200",
      "label": "Label 2",
      "emphasize": false
    },
    {
      "value": "300",
      "label": "Label 3",
      "emphasize": false
    },
    {
      "value": "400",
      "label": "Label 4",
      "emphasize": false
    }
  ],
  
  "sections": [
    {
      "type": "benefits",
      "label": "BENEFÍCIOS",
      "title": "Benefícios Principais",
      "intro": "Intro text",
      "items": [
        {
          "emoji": "⚡",
          "title": "Item 1",
          "description": "Descrição"
        },
        {
          "emoji": "📈",
          "title": "Item 2",
          "description": "Descrição"
        },
        {
          "emoji": "🔒",
          "title": "Item 3",
          "description": "Descrição"
        },
        {
          "emoji": "🚀",
          "title": "Item 4",
          "description": "Descrição"
        }
      ]
    },
    {
      "type": "impact",
      "label": "IMPACTO",
      "title": "Métricas de Impacto",
      "items": [
        {
          "value": "1.2M",
          "description": "Métrica 1"
        },
        {
          "value": "45%",
          "description": "Métrica 2"
        },
        {
          "value": "3.6TB",
          "description": "Métrica 3"
        },
        {
          "value": "5min",
          "description": "Métrica 4"
        }
      ]
    },
    {
      "type": "table",
      "label": "DADOS",
      "title": "Tabela de Dados",
      "columns": ["Coluna 1", "Coluna 2", "Coluna 3", "Status"],
      "rows": [
        ["Linha 1", "Valor A", "Valor B", {"value": "✓", "class": "badge"}],
        ["Linha 2", "Valor C", "Valor D", {"value": "✓", "class": "badge"}],
        ["Linha 3", "Valor E", "Valor F", {"value": "✓", "class": "badge"}]
      ]
    }
  ],
  
  "cta_title": "Próximos Passos",
  "cta_subtitle": "Descrição da CTA",
  "cta_link": "seu-link.html",
  "cta_button_text": "Botão →",
  
  "footer_left": "© 2026 - Avanade",
  "footer_right": "Atualizado em 2026-07-13"
}
```

### Passo 3: Gerar Novo Dashboard

```bash
# Ative ambiente Python
.venv\Scripts\Activate.ps1

# Gere o novo dashboard
python scripts/generate_dashboard.py \
  --name "Seu Dashboard" \
  --output outputs/<projeto>/novo_dashboard.html \
  --config templates/seu-dashboard.json
```

### Passo 4: Validar

1. Abra `outputs/<projeto>/novo_dashboard.html` no browser
2. Verifique:
   - ✅ Todos os textos aparecem
   - ✅ Métricas estão corretas
   - ✅ Animações funcionam
   - ✅ Links navegam corretamente
   - ✅ Responsivo em mobile

### Passo 5: Compartilhar

```bash
# Copiar para compartilhar
cp outputs/<projeto>/novo_dashboard.html shared/
```

## 📊 Mapeamento de Componentes

| Seu Dashboard | Template JSON |
|---|---|
| `<h1>Título</h1>` | `hero_title` |
| `<p>Subtítulo</p>` | `hero_subtitle` |
| `<button>` | `hero_buttons` |
| `<div class="metric">` | `metrics` (array) |
| `<div class="benefits">` | `sections[0]` type: "benefits" |
| `<table>` | `sections[2]` type: "table" |

## 🎨 Personalizações Avançadas

### Customizar Cores

Abra `templates/dashboard.template.html` e altere:

```css
:root {
  --paper: #FAF8F4;
  --ink: #121610;
  --ember: #FF5800;        /* ← Mude aqui */
  --graphite: #3D3C39;
  --smoke: #8B8A86;
}
```

### Adicionar Seção Personalizada

1. Crie tipo novo em JSON:
```json
{
  "type": "custom",
  "label": "MINHA SEÇÃO",
  "title": "Título",
  "content": "<div>HTML customizado</div>"
}
```

2. Edite `scripts/generate_dashboard.py`:
```python
elif sec_type == "custom":
    html.append(f'<section id="custom">')
    html.append(config["content"])
    html.append('</section>')
```

### Remover Seção

Simplesmente remova do array `sections` no JSON.

## ✅ Checklist de Migração

- [ ] Arquivo JSON criado
- [ ] Todos os textos preenchidos
- [ ] Métricas/KPIs mapeadas
- [ ] Links verificados
- [ ] Tabelas mapeadas
- [ ] Dashboard gerado
- [ ] Validado no browser
- [ ] Responsivo testado
- [ ] Links funcionam
- [ ] Animações funcionam

## 🐛 Troubleshooting

### Dashboard não gera
```bash
# Verifique syntax do JSON
python -m json.tool templates/seu-dashboard.json

# Se houver erro, corrija e tente novamente
```

### Caracteres especiais aparecem estranhos
Certifique-se que o arquivo JSON está em UTF-8:
```bash
# Windows PowerShell
[System.IO.File]::WriteAllText(
  'templates/seu-dashboard.json',
  $(Get-Content 'templates/seu-dashboard.json'),
  [System.Text.Encoding]::UTF8
)
```

### Animações não funcionam
- Verifique conexão com CDN GSAP
- Ou baixe GSAP localmente

### Layout quebrado em mobile
Verifique que todas as strings no JSON não têm quebras de linha:
```json
// ✅ Correto
"intro": "Texto em uma linha"

// ❌ Errado
"intro": "Texto em
múltiplas linhas"
```

## 🚀 Próximos Passos

1. **Versionamento**
   ```bash
   git add templates/seu-dashboard.json
   git commit -m "Add: dashboard configuration for Seu Dashboard"
   ```

2. **Automatizar geração**
   ```bash
   # Criar script batch que gera múltiplos dashboards
   ```

3. **Integrar com pipeline**
   ```bash
   # GitHub Actions, Azure Pipelines, etc.
   ```

## 📞 Exemplos Completos

- [migration_dashboard.html](../outputs/cloudera-fabric/docs/migration_dashboard.html) — Cloudera→Fabric
- [example-config.json](./example-config.json) — Template de config

---

**Tempo estimado:** 10-15 minutos  
**Dificuldade:** ⭐⭐ (Fácil)  
**Resultado:** Dashboard profissional reutilizável

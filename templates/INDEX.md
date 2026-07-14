# Templates — Sistema de Dashboards Reutilizáveis

## 📁 Estrutura

```
templates/
├── README.md                    # 📚 Guia completo de uso
├── dashboard.template.html      # 🎨 Template HTML base
├── example-config.json          # 📋 Exemplo de configuração
└── dashboard-template-system.md # 🔧 Documentação técnica (em memoria/)
```

## 🎯 Propósito

Sistema profissional e reutilizável para criar dashboards executivos com:
- Design premium (inspirado em Julio Pessan Portfolio)
- Animações GSAP + ScrollTrigger
- Totalmente responsivo
- Zero dependências de frameworks
- Customizável via JSON

## ⚡ Quick Start

### 1. Criar nova configuração
```bash
cp templates/example-config.json templates/seu-projeto.json
```

### 2. Editar arquivo JSON
```json
{
  "page_title": "Seu Projeto | Dashboard",
  "hero_title": "Seu <span class=\"word\">Projeto</span>",
  "metrics": [
    { "value": "100", "label": "Métrica 1", "emphasize": true }
  ]
}
```

### 3. Gerar dashboard
```bash
python scripts/generate_dashboard.py \
  --name "Seu Projeto" \
  --output outputs/<projeto>/novo_dashboard.html \
  --config templates/seu-projeto.json
```

## 📚 Documentação Completa

👉 [Leia o README.md](./README.md)

## 🎨 Design System

| Aspecto | Valor |
|---------|-------|
| Fundo | #FAF8F4 (Paper) |
| Texto | #121610 (Ink) |
| Destaque | #FF5800 (Ember Orange) |
| Tipografia Display | Space Grotesk |
| Tipografia Body | Inter |
| Tipografia Code | JetBrains Mono |

## 📦 Últimas Criações

### ✅ migration_dashboard.html
**Criado em:** 2026-07-13  
**Tipo:** Migração Cloudera → Microsoft Fabric  
**Seções:** Hero, Meter KPIs, Plano (6 fases), Benefícios, Impacto, Tabelas (9 itens), Próximos Passos, CTA  
**Status:** 🟢 Pronto para stakeholders

## 🚀 Como Adicionar Novo Tipo de Seção

1. **Defina a estrutura JSON** em seu `config.json`:
```json
{
  "type": "seu_tipo",
  "label": "LABEL",
  "title": "Título",
  "dados": [ ... ]
}
```

2. **Implemente em `generate_dashboard.py`**:
```python
elif sec_type == "seu_tipo":
    # gerar HTML...
    html.append(...)
```

3. **Teste com um arquivo config e valide**

## 📊 Tipos de Seção Suportados

| Tipo | Descrição |
|------|-----------|
| `benefits` | Grid 2x2 com ícones e descrições |
| `impact` | Métricas de grande impacto |
| `table` | Tabelas de dados com formatação |

## ✨ Features do Template

- ✅ Preloader com contador (0-100%)
- ✅ Progress bar na scroll
- ✅ Nav fixa com hide ao scroll
- ✅ Parallax background com orbs
- ✅ Reveal animations ao scroll
- ✅ Cursor glow effect
- ✅ Stagger animations em grids
- ✅ Hover effects em cards/tables
- ✅ Responsivo (4 breakpoints)
- ✅ Acessível (WCAG)
- ✅ Badges e indicators
- ✅ CTA animada
- ✅ Footer customizável

## 🔗 Integrações

| Sistema | Status |
|---------|--------|
| Azure Data Factory | Pronto (links na CTA) |
| Microsoft Fabric | Pronto (links na CTA) |
| SharePoint | Pronto (hospedagem) |
| Teams | Pronto (embed) |

## 📞 Suporte & Extensões

Para perguntas ou adicionar features:
1. Consulte [README.md](./README.md)
2. Verifique `example-config.json`
3. Modifique `dashboard.template.html` ou `generate_dashboard.py`
4. Teste com: `python scripts/generate_dashboard.py --name "Test" --output test.html --config templates/example-config.json`

---

**Versão:** 1.0  
**Criação:** 2026-07-13  
**Compatibilidade:** Chrome/Firefox/Safari/Edge (últimas 2 versões)  
**Licença:** Avanade Global AI Hub

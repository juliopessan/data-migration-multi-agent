#!/usr/bin/env python
"""
Dashboard Template Generator
Gera novos dashboards a partir do template reutilizável.

Uso:
  python scripts/generate_dashboard.py --name "Migração Projeto X" --output outputs/<projeto>/novo_dashboard.html
"""

import argparse
import json
from pathlib import Path
from datetime import datetime


def load_template():
    """Carrega o template HTML base."""
    template_path = Path(__file__).parent.parent / "templates" / "dashboard.template.html"
    return template_path.read_text(encoding="utf-8")


def generate_meter_cells(metrics: dict) -> str:
    """Gera as células do medidor KPI."""
    cells = []
    for metric in metrics:
        ember_class = " ember" if metric.get("emphasize") else ""
        cell = f'''
    <div class="meter-cell">
      <div class="val{ember_class}">{metric["value"]}</div>
      <div class="lbl">{metric["label"]}</div>
    </div>
'''
        cells.append(cell)
    return "".join(cells)


def generate_nav_links(nav_items: list) -> str:
    """Gera os links de navegação."""
    links = []
    for item in nav_items:
        link = f'<a href="{item["href"]}">{item["label"]}</a>'
        links.append(link)
    # Adiciona CTA no final
    links.append('<a href="#cta" class="nav-cta">Começar →</a>')
    return "\n      ".join(links)


def generate_hero_buttons(buttons: list) -> str:
    """Gera os botões do hero."""
    btns = []
    for btn in buttons:
        btn_class = f"btn-{btn.get('style', 'primary')}"
        button = f'<a href="{btn["href"]}" class="btn {btn_class}">{btn["label"]}</a>'
        btns.append(button)
    return "\n      ".join(btns)


def generate_main_sections(sections: list) -> str:
    """Gera as seções principais."""
    html = []

    for section in sections:
        sec_type = section.get("type", "generic")

        if sec_type == "benefits":
            html.append(f'''
<section id="beneficios" class="reveal">
  <div class="sec-label">🎯 {section.get("label", "BENEFÍCIOS")}</div>
  <h2>{section["title"]}</h2>
  <p class="sec-intro">{section.get("intro", "")}</p>
  <div class="grid-2 stagger">
''')
            for item in section["items"]:
                html.append(f'''
    <div class="grid-item">
      <div class="emoji">{item.get("emoji", "✓")}</div>
      <h3>{item["title"]}</h3>
      <p>{item["description"]}</p>
    </div>
''')
            html.append("  </div>\n</section>")

        elif sec_type == "impact":
            html.append(f'''
<section id="impacto">
  <div class="sec-label">📊 {section.get("label", "IMPACTO")}</div>
  <h2>{section["title"]}</h2>
  <div class="impact reveal">
    <div class="impact-grid stagger">
''')
            for item in section["items"]:
                html.append(f'''
      <div class="impact-item">
        <div class="big">{item["value"]}</div>
        <p>{item["description"]}</p>
      </div>
''')
            html.append('''    </div>
  </div>
</section>''')

        elif sec_type == "table":
            html.append(f'''
<section id="dados" class="reveal">
  <div class="sec-label">📋 {section.get("label", "DADOS")}</div>
  <h2>{section["title"]}</h2>
  <table class="data-table">
    <thead>
      <tr>
''')
            for col in section["columns"]:
                html.append(f"        <th>{col}</th>\n")
            html.append("      </tr>\n    </thead>\n    <tbody>\n")

            for row in section["rows"]:
                html.append("      <tr>\n")
                for i, cell in enumerate(row):
                    if isinstance(cell, dict):
                        content = cell.get("value", "")
                        cell_class = f' class="{cell.get("class", "")}"' if cell.get("class") else ""
                        html.append(f"        <td{cell_class}>{content}</td>\n")
                    else:
                        html.append(f"        <td>{cell}</td>\n")
                html.append("      </tr>\n")

            html.append("    </tbody>\n  </table>\n</section>")

    return "\n".join(html)


def generate_dashboard(
    name: str,
    output_path: str,
    config: dict = None,
    config_file: str = None,
) -> None:
    """
    Gera um novo dashboard a partir do template.

    Args:
        name: Nome do projeto/dashboard
        output_path: Caminho de saída do HTML
        config: Dicionário de configuração (alternativa a config_file)
        config_file: Caminho para arquivo JSON de configuração
    """

    # Carrega configuração
    if config_file:
        with open(config_file, encoding="utf-8") as f:
            config = json.load(f)
    elif not config:
        config = {}

    # Carrega template
    template = load_template()

    # Prepara valores padrão
    now = datetime.now().strftime("%Y-%m-%d")

    # Substitui variáveis no template
    replacements = {
        "{{PAGE_TITLE}}": config.get("page_title", f"{name} | Dashboard Executivo"),
        "{{PAGE_DESCRIPTION}}": config.get("page_description", f"Plano executivo: {name}"),
        "{{LOADING_TEXT}}": config.get("loading_text", "Carregando dados..."),
        "{{LOGO_TEXT}}": config.get("logo_text", "Dashboard"),
        "{{LOGO_SUFFIX}}": config.get("logo_suffix", ""),
        "{{NAV_LINKS}}": generate_nav_links(
            config.get("nav_links", [{"label": "Visão Geral", "href": "#top"}])
        ),
        "{{EYEBROW}}": config.get("eyebrow", "Plano Estratégico"),
        "{{HERO_TITLE}}": config.get("hero_title", name),
        "{{HERO_SUBTITLE}}": config.get("hero_subtitle", ""),
        "{{HERO_BUTTONS}}": generate_hero_buttons(config.get("hero_buttons", [])),
        "{{METER_TITLE}}": config.get("meter_title", "Status do Projeto"),
        "{{METER_SUBTITLE}}": config.get("meter_subtitle", "Métricas em tempo real"),
        "{{METER_CELLS}}": generate_meter_cells(config.get("metrics", [])),
        "{{MAIN_SECTIONS}}": generate_main_sections(config.get("sections", [])),
        "{{CTA_TITLE}}": config.get("cta_title", "Próximos Passos"),
        "{{CTA_SUBTITLE}}": config.get("cta_subtitle", ""),
        "{{CTA_LINK}}": config.get("cta_link", "#"),
        "{{CTA_BUTTON_TEXT}}": config.get("cta_button_text", "Continuar →"),
        "{{FOOTER_LEFT}}": config.get("footer_left", f"© {datetime.now().year} - Avanade"),
        "{{FOOTER_RIGHT}}": config.get("footer_right", f"Atualizado em {now}"),
    }

    # Aplica substituições
    html = template
    for key, value in replacements.items():
        html = html.replace(key, str(value))

    # Escreve arquivo
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(html, encoding="utf-8")

    print(f"✅ Dashboard gerado: {output_file}")
    print(f"   Nome: {name}")
    print(f"   Tamanho: {len(html) / 1024:.1f} KB")


def main():
    parser = argparse.ArgumentParser(description="Gera novos dashboards do template")
    parser.add_argument("--name", required=True, help="Nome do projeto/dashboard")
    parser.add_argument("--output", required=True, help="Caminho de saída do HTML")
    parser.add_argument("--config", help="Arquivo JSON de configuração")

    args = parser.parse_args()

    generate_dashboard(
        name=args.name,
        output_path=args.output,
        config_file=args.config,
    )


if __name__ == "__main__":
    main()

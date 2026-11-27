"""Genera i loghi del sito (stile "Blocchi").

    python3 tools/make_logos.py

Scrive:
  - assets/logo.svg            logo generale: piccola griglia di blocchi colorati su quadrato scuro arrotondato
  - assets/icon.svg            lo stesso a tutto quadrato, per le icone (iPhone, Android)
  - assets/sections/<nome>.svg icona di ogni sezione (games, manga, books, movies, series)
Le icone PNG (favicon, apple-touch-icon, icon-192/512) si ricavano da assets/icon.svg.
"""
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

BLOCKS = ('<rect x="22" y="22" width="34" height="76" rx="11" fill="#5b6ee8"/>'
          '<rect x="62" y="22" width="36" height="34" rx="11" fill="#ffd166"/>'
          '<rect x="62" y="62" width="15" height="36" rx="7" fill="#ff8fab"/>'
          '<rect x="82" y="62" width="16" height="36" rx="7" fill="#4fd18b"/>')


def logo(rounded=True):
    bg = '<rect width="120" height="120" rx="32" fill="#16161a"/>' if rounded else '<rect width="120" height="120" fill="#16161a"/>'
    if not rounded:  # sull'icona del telefono i blocchi stanno un po' più al centro
        return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120">' + bg
                + '<g transform="translate(9 9) scale(.85)">' + BLOCKS + '</g></svg>\n')
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120">' + bg + BLOCKS + '</svg>\n'


# icone delle sezioni: quadrato arrotondato colorato con disegno a linee (viewBox 64)
GLYPH = {
    'games': ('#5b6ee8', '#ffffff', '<path d="M6 8h12a4 4 0 0 1 3.9 4.8l-.7 3.4a2.5 2.5 0 0 1-4.3 1.1L15 15H9l-1.9 2.3a2.5 2.5 0 0 1-4.3-1.1l-.7-3.4A4 4 0 0 1 6 8z"/><path d="M8 10.5v3M6.5 12h3"/><path d="M15.5 11.2h.01M17 13h.01"/>'),
    'manga': ('#ff5fa2', '#ffffff', '<path d="M5 3h11a2 2 0 0 1 2 2v15H7a2 2 0 0 1-2-2z"/><path d="M5 18a2 2 0 0 1 2-2h11"/><path d="M9 6.5h6v4h-3.5L10 12v-1.5H9z"/>'),
    'books': ('#e0a21a', '#ffffff', '<path d="M3 5.5c3-1 6-1 9 1 3-2 6-2 9-1V19c-3-1-6-1-9 1-3-2-6-2-9-1z"/><path d="M12 6.5V20"/>'),
    'movies': ('#ff6b6b', '#ffffff', '<rect x="3" y="9" width="18" height="11" rx="2"/><path d="M3.3 9 2.8 5.6 19.6 3l.6 3.4z"/><path d="M8.2 4.8l1.6 3M13.4 4l1.6 3"/>'),
    'series': ('#4fd1c5', '#0b3d38', '<rect x="3" y="6" width="18" height="13" rx="2.5"/><path d="M8 2.5l4 3.5 4-3.5"/><path d="M10.5 10v5l4-2.5z"/>'),
}


def section(name):
    bg, ink, paths = GLYPH[name]
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
            f'<rect width="64" height="64" rx="18" fill="{bg}"/>'
            f'<g transform="translate(14 14) scale(1.5)" fill="none" stroke="{ink}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{paths}</g>'
            '</svg>\n')


def main():
    os.makedirs(os.path.join(ROOT, 'assets', 'sections'), exist_ok=True)
    open(os.path.join(ROOT, 'assets', 'logo.svg'), 'w').write(logo())
    open(os.path.join(ROOT, 'assets', 'icon.svg'), 'w').write(logo(rounded=False))
    for name in GLYPH:
        open(os.path.join(ROOT, 'assets', 'sections', f'{name}.svg'), 'w').write(section(name))
    print('Loghi scritti in assets/ e assets/sections/')


if __name__ == '__main__':
    main()

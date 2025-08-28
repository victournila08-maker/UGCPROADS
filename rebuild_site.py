#!/usr/bin/env python3
"""Utility script to regenerate the static site files.

If the site files are lost, run::

    python rebuild_site.py

By default files are written to the repository root. Use --dest to specify
another directory.
"""

from pathlib import Path
import argparse

INDEX_HTML = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>UGC Pro Ads</title>
  <link rel=\"stylesheet\" href=\"css/style.css\" />
</head>
<body>
  <header>
    <h1>UGC Pro Ads</h1>
    <nav>
      <a href=\"index.html\">Home</a>
      <a href=\"services.html\">Services</a>
      <a href=\"portfolio.html\">Portfolio</a>
      <a href=\"testimonials.html\">Testimonials</a>
      <a href=\"quote.html\">Get a Quote</a>
    </nav>
  </header>
  <main>
    <section class=\"hero\">
      <h2>UGC That Converts</h2>
      <p>Your site has been rebuilt from the ground up.</p>
    </section>
  </main>
  <footer>&copy; <span id=\"year\"></span> UGC Pro Ads</footer>
  <script src=\"js/main.js\"></script>
</body>
</html>
"""

STYLE_CSS = """body{font-family:sans-serif;margin:0;padding:0;line-height:1.6;}
header{background:#f1f1f1;padding:1rem;}
nav a{margin-right:1rem;text-decoration:none;color:#333;}
.hero{padding:2rem;}
footer{background:#f1f1f1;padding:1rem;text-align:center;margin-top:2rem;}
"""

MAIN_JS = """document.addEventListener('DOMContentLoaded',()=>{const y=document.getElementById('year');if(y){y.textContent=new Date().getFullYear();}});
"""

def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Wrote {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild static site files.")
    parser.add_argument("--dest", type=Path, default=Path.cwd(), help="Destination directory for site files.")
    args = parser.parse_args()

    dest = args.dest
    write_file(dest / "index.html", INDEX_HTML)
    write_file(dest / "css/style.css", STYLE_CSS)
    write_file(dest / "js/main.js", MAIN_JS)


if __name__ == "__main__":
    main()

# Static Site Generator

A modern static site generator that converts Markdown content into complete HTML websites. Built as a practice project for the ["Build a Static Site Generator"](https://www.boot.dev/courses/build-static-site-generator-python) course from [Boot.dev](https://www.boot.dev).

## Features

- **Markdown → HTML conversion**: Transforms `.md` files into complete web pages
- **HTML templates**: Template system with dynamic variables
- **Supported elements**:
  - Headers (`#`, `##`, `###`, etc.)
  - Formatted text (bold, italic, inline code)
  - Ordered and unordered lists
  - Block quotes
  - Code blocks with formatting
  - Links and images
- **Static file copying**: CSS, images, and other resources
- **Recursive generation**: Processes complete content directories

## Project structure

```
├── src/                    # Source code
│   ├── main.py            # Main entry point
│   ├── htmlnode.py        # Base class for HTML nodes
│   ├── leafnode.py        # HTML nodes without children
│   ├── parentnode.py      # HTML nodes with children
│   ├── textnode.py        # Text representation with types
│   ├── markdown_to_blocks.py  # Markdown parser
│   └── ...                # Other modules
├── content/               # Markdown content
├── static/               # Static files (CSS, images)
├── template.html         # Base HTML template
└── public/              # Generated site (output)
```

## Usage

### Basic execution
```bash
# Generate the site
./main.sh

# Or directly with Python
python3 src/main.py
```

### Running tests
```bash
./test.sh
# Or with unittest directly
python3 -m unittest discover -s src
```

### Local server
The `main.sh` script includes a local HTTP server:
```bash
./main.sh  # Generates the site and serves at http://localhost:8888
```

## How it works

1. **Cleanup**: Removes the previous `public/` directory
2. **Static copy**: Transfers files from `static/` to `public/`
3. **Conversion**: Processes each `.md` in `content/`:
   - Extracts the title (first `# Header`)
   - Converts Markdown to HTML node tree
   - Applies the HTML template
   - Saves the result in `public/`

## Technologies

- **Python 3.11+** with type hints
- **HTML5** and **CSS3**
- **Markdown** as content format
- **Unittest** for testing

## Technical features

- Object-oriented architecture with HTML node hierarchy
- Robust Markdown parser with support for nested elements
- Python type system for better safety
- Complete unit test coverage

---

*This project was developed following Python best practices and as a hands-on exercise from the Boot.dev educational program.*
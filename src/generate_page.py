from extract_title import extract_title
from markdown_to_blocks import markdown_to_html_node


def generate_page(from_path: str, template_path: str, dest_path: str, base_path: str = "/") -> None:
    print("Generating page from ", from_path, " to ", dest_path, " using template ", template_path)
    try: 
        markdown_content = ""
        with open(from_path, "r") as f:
            markdown_content = f.read()
        template_content = ""
        with open(template_path, "r") as f:
            template_content = f.read()
        html_content = markdown_to_html_node(markdown_content).to_html()
        title = extract_title(markdown_content)
        final_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
        if base_path != "/":
            final_content = final_content.replace('href="/', f'href="{base_path}/').replace('src="/', f'src="{base_path}/')
        with open(dest_path, "w") as f:
            f.write(final_content)
        print("Page generated at ", dest_path)

    except Exception as e:
        print("Error reading markdown file:", e)
        return

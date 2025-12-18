import os
import shutil
import sys
from converter import markdown_to_html_node

def main():

    site_base_path = "./"

    for arg in sys.argv[1:]:
        site_base_path = arg

    static_file_path = "static"
    public_file_path = "docs"
    content_file_path = "content"
    template_file_path = "template.html"

    print(f"Base site path: {site_base_path}")

    clear_public(public_file_path)
    copy_static_to_public(static_file_path, public_file_path)
    generate_pages_recursive(content_file_path, template_file_path, public_file_path, site_base_path)



def clear_public(base_path):
    if os.path.exists(base_path):
        shutil.rmtree(base_path)
    os.makedirs(base_path)

def copy_static_to_public(base_path, destination_path):
    file_list = os.listdir(base_path)
    for item in file_list:
        item_path = os.path.join(base_path, item)
        if not os.path.isfile(item_path):
            dir_path = os.path.join(destination_path, item)
            print(f"Creating directory: {dir_path}")
            os.mkdir(dir_path)
            copy_static_to_public(item_path, dir_path)
        else:
            dest_path = os.path.join(destination_path, item)
            print(f"Copying: {item_path} to {dest_path}")
            shutil.copy(item_path, dest_path)

def extract_title(markdown):
    md_lines = markdown.split("\n")
    for line in md_lines:
        if line.startswith("#"):
            return line.split("#")[1].strip()
    return "Title Not Found"



def generate_page(from_path, template_path, dest_path, site_base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md:
        markdown = md.read()
    template = open(template_path).read()
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace(r"{{ Title }}", title)
    template = template.replace(r"{{ Content }}", html_string)
    template = template.replace("href=\"/", f"href=\"{site_base_path}")
    template = template.replace("src=\"/", f"src=\"{site_base_path}")

    if not os.path.exists(dest_path):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path,"w") as f:
            f.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, site_base_path):
    files_found = os.listdir(dir_path_content)
    for file in files_found:
        file_path = os.path.join(dir_path_content, file)
        if not os.path.isfile(file_path):
            os.mkdir(os.path.join(dest_dir_path, file))
            src_path = os.path.join(dir_path_content, file)
            dest_path = os.path.join(dest_dir_path, file)
            generate_pages_recursive(src_path, template_path, dest_path, site_base_path)
        else:
            if ".md" in file:
                file = file.replace(".md", ".html")
                generate_page(file_path, template_path, os.path.join(dest_dir_path, file), site_base_path)
    


main()
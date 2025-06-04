import sys
import os
import re
import shutil

import subprocess



def main():
    if len(sys.argv) < 2:
        print("No Variable provided.")
        return


    # Print results
    # print("\nVar 1: ", sys.argv[1])
    # print("\nVar 2: ", sys.argv[2])
    #print("Image folder path:", os.path.abspath(image_folder))

    # ──────── ✏️ PARSE VARIABLES ─────────────
    obsidian_post_dir = sys.argv[1]
    if not os.path.exists(obsidian_post_dir):
        print(f"Error: The directory '{obsidian_post_dir}' does not exist.")
        return
    else:
        print(f"Obsidian post directory: {obsidian_post_dir}")
    

    blog_name  = sys.argv[2]
    if not blog_name:
        print("Error: Blog name is empty.")
        return
    # else:
    #     print(f"Blog name: {blog_name}")
    

    obsidian_img_dir = os.path.join(obsidian_post_dir, "attachments")
    if not os.path.exists(obsidian_img_dir):
        print(f"Error: The directory '{obsidian_img_dir}' does not exist.")
        return
    # else:
    #     print(f"Image folder path: {obsidian_img_dir}")

    # jekyll_img_dir    = "assets/images"
    # jekyll_post_dir   = "_posts"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    jekyll_img_dir  = os.path.join(script_dir, "assets", "images")
    jekyll_post_dir = os.path.join(script_dir, "_posts")
    # ───────────────────────────────────────────────

    
    def sanitize_filename(name):
        return name.replace(" ", "-")

    # Step 1: Construct paths
    obsidian_md_path = os.path.join(obsidian_post_dir, blog_name)
    jekyll_post_name = sanitize_filename(blog_name)
    jekyll_md_path = os.path.join(jekyll_post_dir, jekyll_post_name)
    # print(f"Jekyll post path: {jekyll_md_path}")

    # Ensure folders exist
    os.makedirs(jekyll_img_dir, exist_ok=True)
    os.makedirs(jekyll_post_dir, exist_ok=True)


    try:
        with open(obsidian_md_path, 'r') as f:
            print("File is readable")
            # print(f"Obsidian post path: {obsidian_md_path}")
    except PermissionError:
        print(f"Cannot read file due to permission issue: {obsidian_md_path}")


    shutil.copy2(obsidian_md_path, jekyll_md_path)
    print(f"[Copied] Blog post copied to: {jekyll_md_path}")

    # Step 3: Read copied post
    with open(jekyll_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 4: Replace image links
    obsidian_img_pattern = r'!\[\[(.*?)\]\]'
    replaced_imgs = {}

    def replace_img(match):
        img_filename = match.group(1)

        # If no extension, try common ones
        if not os.path.splitext(img_filename)[1]:
            found = False
            for ext in ['.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg']:
                test_file = img_filename + ext
                test_path = os.path.join(obsidian_img_dir, test_file)
                if os.path.exists(test_path):
                    img_filename = test_file
                    found = True
                    break
            if not found:
                print(f"[Warning] Image not found with any known extension: {img_filename}")
                return match.group(0)

        original_img_path = os.path.join(obsidian_img_dir, img_filename)
        if not os.path.exists(original_img_path):
            print(f"[Warning] Image not found: {original_img_path}")
            return match.group(0)

        sanitized_img_name = sanitize_filename(img_filename)
        jekyll_img_path = os.path.join(jekyll_img_dir, sanitized_img_name)

        shutil.copy2(original_img_path, jekyll_img_path)
        print(f"[Copied] {original_img_path} --> {jekyll_img_path}")


        # rel_img_path = os.path.join("/", jekyll_img_dir, sanitized_img_name).replace("\\", "/")
        rel_img_path = f"/assets/images/{sanitized_img_name}"

        return f"![Image]({rel_img_path})"



    # Step 5: Apply image replacements
    updated_content = re.sub(obsidian_img_pattern, replace_img, content)

    # Step 6: Save updated post
    with open(jekyll_md_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"[Success] Final blog post saved at: {jekyll_md_path}")

    # Run Jekyll build command

def run_jekyll_server():
    try:
        # Change directory to your Jekyll site root
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # subprocess.run(["bundle", "exec", "jekyll", "serve"], cwd=script_dir, check=True)
        subprocess.run("bundle exec jekyll serve", cwd=script_dir, shell=True)

        print("Jekyll server started successfully.")
    except subprocess.CalledProcessError as e:
        print("Failed to start Jekyll server.")
        print("Error:", e)

if __name__ == "__main__":
    main()
    run_jekyll_server()
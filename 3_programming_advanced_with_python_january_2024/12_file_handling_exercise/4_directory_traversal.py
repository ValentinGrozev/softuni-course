import os


def save_extensions(dir_name):
    extensions = {}
    for filename in os.listdir(dir_name):
        extension = filename.split(".")[-1]
        extensions[extension] = extensions.get(extension, []) + [filename]
    return extensions


def main():
    directory = input("Choose your directory: ")
    extensions = save_extensions(directory)
    sorted_extensions = sorted(extensions.items(), key=lambda x: x[0])

    output_file = open("../12_1_files/first_level/report.txt", "w")

    for extension, filenames in sorted_extensions:
        output_file.write(f".{extension}\n")
        for filename in sorted(filenames):
            output_file.write(f"- - - {filename}\n")

    output_file.close()


main()

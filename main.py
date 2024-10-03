import os
from PyPDF2 import PdfReader, PdfWriter
from tqdm import tqdm


def split_pdf(input_pdf, output_dir):
    """
    Splits the input PDF into individual pages, naming each file as "Page {page_number}.pdf".

    Parameters:
        input_pdf (str): Path to the source PDF file.
        output_dir (str): Directory where the split pages will be saved.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory at '{output_dir}'.")

    try:
        # Initialize PyPDF2 PdfReader
        pdf_reader = PdfReader(input_pdf)
        total_pages = len(pdf_reader.pages)
        print(f"Total pages to split: {total_pages}")

        # Iterate over pages with tqdm progress bar
        for i, page in enumerate(
            tqdm(pdf_reader.pages, desc="Splitting Pages"), start=1
        ):
            output_filename = f"Page {i}.pdf"
            output_path = os.path.join(output_dir, output_filename)

            # Use PdfWriter to write the single page
            writer = PdfWriter()
            writer.add_page(page)

            # Save the single-page PDF
            with open(output_path, "wb") as f:
                writer.write(f)

            print(f"Saved: {output_filename}")

        print("PDF splitting completed successfully.")

    except Exception as e:
        print(f"An error occurred while splitting the PDF: {e}")


def get_pdf_filename():
    """
    Prompts the user to enter the name of the PDF file located in the 'source' folder.

    Returns:
        str: The full path to the selected PDF file.
    """
    source_dir = "source"
    if not os.path.exists(source_dir):
        print(f"The source directory '{source_dir}' does not exist.")
        exit(1)

    # List available PDF files in the source directory
    available_pdfs = [f for f in os.listdir(source_dir) if f.lower().endswith(".pdf")]
    if not available_pdfs:
        print(f"No PDF files found in the '{source_dir}' directory.")
        exit(1)

    print("Available PDF files:")
    for idx, pdf in enumerate(available_pdfs, start=1):
        print(f"{idx}. {pdf}")

    while True:
        try:
            choice = int(
                input(
                    f"Enter the number of the PDF file you want to split (1-{len(available_pdfs)}): "
                )
            )
            if 1 <= choice <= len(available_pdfs):
                selected_pdf = available_pdfs[choice - 1]
                input_pdf_path = os.path.join(source_dir, selected_pdf)
                print(f"Selected file: '{selected_pdf}'")
                return input_pdf_path
            else:
                print(f"Please enter a number between 1 and {len(available_pdfs)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_output_directory():
    """
    Prompts the user to enter the name of the output directory or use the default 'output'.

    Returns:
        str: The path to the output directory.
    """
    default_output = "output"
    choice = input(
        f"Enter the name of the output directory (default: '{default_output}'): "
    ).strip()
    return choice if choice else default_output


if __name__ == "__main__":
    print("=== PDF Splitter ===\n")

    # Prompt the user to select a PDF file from the 'source' directory
    input_pdf_path = get_pdf_filename()

    # Prompt the user to specify the output directory
    output_directory = get_output_directory()

    # Call the split_pdf function
    split_pdf(input_pdf_path, output_directory)

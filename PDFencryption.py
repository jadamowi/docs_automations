import PyPDF2
from pathlib import Path


def pdfencryption(inpath, outpath, pdfpass):
    """
    Function loops through the given path looking for PDF files, encrypts them
    and save in a given folder.
    :param inpath: Path to the folder with PDF files to be encrypted
    :param outpath: Path where the PDFs have to be saved
    :param pdfpass: Password the files are encrypted with
    :return: Function does not return any object
    """

    pathlist = Path(inpath).rglob('*.pdf')

    for path in pathlist:
        path_in_str = str(path)
        pdf_file = open(path_in_str, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()

        for page_num in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

        pdf_writer.encrypt(pdfpass)
        result_pdf = open(outpath + path_in_str[(len(inpath)):], 'wb')
        pdf_writer.write(result_pdf)
        result_pdf.close()


# Values that the user enters
in_path = input("Please enter a path where the PDFs are stored:\n")
out_path = input("Please enter a new path where the encrypted PDFs have to be stored:\n")
password = input("Please enter a password:\n")

if __name__ == '__main__':
    pdfencryption(in_path, out_path, password)

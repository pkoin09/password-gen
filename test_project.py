from project import generate_password
from project import generate_qr
from project import save_as_pdf
from pathlib import Path


def test_generate_password():
    assert len(generate_password(2)) == 2
    assert len(generate_password(10)) == 10


def test_generate_qr():
    p = 123
    name = "png_file_name"
    png_path = Path("png_file_name.png")
    qr_file = generate_qr(p, name)

    assert qr_file == "png_file_name.png"
    assert png_path.exists() == True
    assert png_path.is_file() == True


def test_save_pdf():
    qr_file = "png_file_name.png"
    name = "pdf_file_name"
    pdf_filename = save_as_pdf(qr_file, name)
    pdf_path = Path("pdf_file_name.pdf")

    assert pdf_filename == "pdf_file_name.pdf"
    assert pdf_path.exists() == True
    assert pdf_path.is_file() == True


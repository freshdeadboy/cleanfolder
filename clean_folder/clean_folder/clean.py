from pathlib import Path
import shutil
import sys
from .file_parser import scan, JPEG_IMAGES, JPG_IMAGES, PNG_IMAGES, SVG_IMAGES, AVI_VIDEO, MP4_VIDEO, MOV_VIDEO, MKV_VIDEO, \
    DOC_DOCUMENTS, DOCX_DOCUMENTS, TXT_DOCUMENTS, PDF_DOCUMENTS, XLSX_DOCUMENTS, PPTX_DOCUMENTS, MP3_MUSIC, OGG_MUSIC, \
    WAV_MUSIC, AMR_MUSIC, ZIP_ARCHIVES, GZ_ARCHIVES, TAR_ARCHIVES, MY_OTHER, FOLDERS
from .normalize import normalize


def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))


def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.name.replace(file_name.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute()), str(folder_for_file.absolute()))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()


def main(folder: Path):
    scan(folder)
    for file in JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in AVI_VIDEO:
        handle_media(file, folder / 'videos' / 'AVI')
    for file in MP4_VIDEO:
        handle_media(file, folder / 'videos' / 'MP4')
    for file in MOV_VIDEO:
        handle_media(file, folder / 'videos' / 'MOV')
    for file in MKV_VIDEO:
        handle_media(file, folder / 'videos' / 'MKV')
    for file in DOC_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in DOCX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in TXT_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in PDF_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in XLSX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'XLSX')
    for file in PPTX_DOCUMENTS:
        handle_media(file, folder / 'documents' / 'PPTX')
    for file in MP3_MUSIC:
        handle_media(file, folder / 'music' / 'MP3')
    for file in OGG_MUSIC:
        handle_media(file, folder / 'music' / 'OGG')
    for file in WAV_MUSIC:
        handle_media(file, folder / 'music' / 'WAV')
    for file in AMR_MUSIC:
        handle_media(file, folder / 'music' / 'AMR')
    for file in ZIP_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'ZIP')
    for file in GZ_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'GZ')
    for file in TAR_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'TAR')
    for file in MY_OTHER:
        handle_media(file, folder / 'MY_OTHER')

    for sub_folder in FOLDERS[::-1]:
        try:
            sub_folder.rmdir()
        except OSError:
            print(f'Error during remove folder {sub_folder}')


if __name__ == "__main__":
    folder_process = Path(sys.argv[1])
    main(folder_process.resolve())
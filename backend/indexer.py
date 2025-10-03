from pypdf import PdfReader
from models import db, Source, Chunk
import os

CHUNK_SIZE = 800

def pdf_to_text(path):
    reader = PdfReader(path)
    return "\n".join([p.extract_text() or '' for p in reader.pages])

def chunk_text(text):
    text = text.replace('\n', ' ')
    return [text[i:i+CHUNK_SIZE].strip() for i in range(0, len(text), CHUNK_SIZE)]

def ingest_file(filepath, name=None, url=None, source_type='upload'):
    text = pdf_to_text(filepath) if filepath.endswith('.pdf') else open(filepath, 'r', encoding='utf-8').read()
    src = Source(source_type=source_type, name=name or os.path.basename(filepath), url=url)
    db.session.add(src)
    db.session.commit()
    for idx, c in enumerate(chunk_text(text)):
        db.session.add(Chunk(source_id=src.id, chunk_text=c, position=idx))
    db.session.commit()
    return src.id
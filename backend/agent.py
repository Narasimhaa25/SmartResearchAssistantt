from models import db
from config import OPENAI_API_KEY
from sqlalchemy import text


def fts_search(query, limit=8):
    sql = text("""
        SELECT c.id as chunk_id, c.chunk_text, c.position, s.id as source_id, s.name as source_name, s.source_type, s.url
        FROM chunk_fts f JOIN chunk c ON f.rowid = c.id
        JOIN source s ON c.source_id = s.id
        WHERE chunk_fts MATCH :q
        ORDER BY rank
        LIMIT :limit
    """)
    return [dict(r) for r in db.session.execute(sql, {'q': query, 'limit': limit}).mappings().all()]

def gather_evidence(question):
    return fts_search(question, limit=12)


def summarize_with_llm(evidence, question):
    if OPENAI_API_KEY:
        import openai
        openai.api_key = OPENAI_API_KEY
        prompt = build_prompt(evidence, question)
        resp = openai.ChatCompletion.create(
            model='gpt-4o-mini',
            messages=[{'role':'user','content':prompt}],
            max_tokens=800
        )
        return resp['choices'][0]['message']['content']
    else:
        return mock_summarize(evidence, question)

def build_prompt(evidence, question):
    parts = [f"[{i+1}] {e['source_name']} ({e.get('url')}): {e['chunk_text'][:400]}" for i,e in enumerate(evidence)]
    return f"Question: {question}\n\nEvidence:\n" + "\n".join(parts)

def mock_summarize(evidence, question):
    return f"TL;DR: {question}. Sources used: {len(evidence)}"
from flask import Flask, request, jsonify
from models import db, User, Source, Chunk, AskLog
from config import DATABASE_URL, COST_PER_QUESTION, COST_PER_REPORT
from indexer import ingest_file
from agent import gather_evidence, summarize_with_llm
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def init_db():
    db.create_all()
    with db.engine.connect() as conn:
        conn.execute("CREATE VIRTUAL TABLE IF NOT EXISTS chunk_fts USING fts5(chunk_text, content='chunk', content_rowid='id')")

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    if User.query.filter_by(username=username).first():
        return jsonify({'error':'exists'}), 400
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return jsonify({'id':user.id, 'credits_questions':user.credits_questions, 'credits_reports':user.credits_reports})

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('file')
    if not f: return jsonify({'error':'no file'}), 400
    path = os.path.join('uploads', f.filename)
    os.makedirs('uploads', exist_ok=True)
    f.save(path)
    src_id = ingest_file(path, name=f.filename)
    return jsonify({'source_id':src_id})

@app.route('/ask', methods=['POST'])
def ask():
    user_id = request.json.get('user_id')
    question = request.json.get('question')
    make_report = request.json.get('report', True)
    user = User.query.get(user_id)
    if not user: return jsonify({'error':'no user'}), 404
    if user.credits_questions < COST_PER_QUESTION:
        return jsonify({'error':'no credits'}), 402
    user.credits_questions -= COST_PER_QUESTION
    evidence = gather_evidence(question)
    summary = ''
    if make_report:
        if user.credits_reports < COST_PER_REPORT:
            return jsonify({'error':'no report credits'}), 402
        user.credits_reports -= COST_PER_REPORT
        summary = summarize_with_llm(evidence, question)
    db.session.add(AskLog(user_id=user.id, question=question, used_credits_question=COST_PER_QUESTION, used_credits_report=COST_PER_REPORT if make_report else 0))
    db.session.commit()
    return jsonify({'summary':summary, 'credits':{'questions':user.credits_questions,'reports':user.credits_reports}})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
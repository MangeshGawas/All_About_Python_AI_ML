from flask import Flask, request, render_template
import pickle

# Load model
df = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommendation(song):
    idx = df[df['song']==song].index[0]
    distances = sorted(list(enumerate(similarity[idx])),reverse=False,key=lambda x:x[1])
    songs = []
    for i in distances[1:21]:
        songs.append(df.iloc[i[0]].song)
    return songs

# App
app = Flask(__name__)

# Path
@app.route('/')
def index():
    names = list(df['song'].values)
    return render_template('index.html',name=names)

@app.route('/recommend', methods=['POST'])
def recom_song():
    user_song = request.form['song']  # Changed key to 'song'
    songs = recommendation(user_song)
    return render_template('index.html', songs=songs)


if __name__ == "__main__":
    app.run(debug=True)

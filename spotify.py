import spotipy

# - q - the search query
#                 - limit  - the number of items to return
#                 - offset - the index of the first item to return
#                 - type - the type of item to return. One of 'artist', 'album',
#                          'track' or 'playlist'
def buscar_musica(criterio, limite = 10):
    if limite > 50:
        raise Exception("Cantidad no permitida", "No puede exceder el limite de 50 resultados")
    resultados = []
    sp = spotipy.Spotify()
    results = sp.search(q=criterio, limit=limite)
    for track in results['tracks']['items']:
        artistas = ""
        for artist in track['artists']:
            artistas += "%s, " % artist['name']
        resultados.append([track['name'], track['popularity'], track['preview_url'], track['duration_ms'], artistas, track['id']])
    return resultados


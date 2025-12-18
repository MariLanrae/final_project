from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

space_objects = [
    {
        "id": 1,
        "name": "Туманность Ориона",
        "type": "Туманность",
        "constellation": "Орион",
        "distance_ly": 1344,
        "description": "Одна из самых известных туманностей, видимая в созвездии Ориона."
    },
    {
        "id": 2,
        "name": "Галактика Андромеды",
        "type": "Галактика",
        "constellation": "Андромеда",
        "distance_ly": 2500000,
        "description": "Соседняя спиральная галактика, ближайшая к Млечному Пути."
    }
]

# --- Маршруты для веб-интерфейса ---

@app.route('/')
def home():
    return render_template('index.html', objects=space_objects)

# --- API маршруты ---

@app.route('/api/objects', methods=['GET'])
def get_objects():
    """Получить список всех космических объектов."""
    return jsonify(space_objects)

@app.route('/api/objects', methods=['POST'])
def add_object():
    """Добавить новый космический объект."""
    data = request.get_json()
    if not data or 'name' not in data or 'type' not in data:
        return jsonify({"error": "Неверные данные. Требуются 'name' и 'type'."}), 400

    new_obj = {
        "id": len(space_objects) + 1,
        "name": data['name'],
        "type": data['type'],
        "constellation": data.get("constellation", "Неизвестно"),
        "distance_ly": data.get("distance_ly", 0),
        "description": data.get("description", "")
    }
    space_objects.append(new_obj)
    return jsonify(new_obj), 201

@app.route('/api/objects/<int:obj_id>', methods=['GET'])
def get_object(obj_id):
    """Получить космический объект по ID."""
    obj = next((o for o in space_objects if o['id'] == obj_id), None)
    if not obj:
        return jsonify({"error": "Объект не найден"}), 404
    return jsonify(obj)

@app.route('/api/objects/<int:obj_id>', methods=['DELETE'])
def delete_object(obj_id):
    """Удалить космический объект по ID."""
    global space_objects
    initial_length = len(space_objects)
    space_objects = [o for o in space_objects if o['id'] != obj_id]
    if len(space_objects) == initial_length:
        return jsonify({"error": "Объект не найден"}), 404
    return jsonify({"message": "Объект успешно удалён"}), 200

if __name__ == '__main__':
    app.run(debug=True)
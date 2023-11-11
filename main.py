from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a single item
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    items.append(new_item)
    return jsonify(new_item), 201

# Update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_item = request.json
    index = next((i for i, item in enumerate(items) if item['id'] == item_id), None)
    if index is None:
        return jsonify({"error": "Item not found"}), 404
    items[index] = updated_item
    return jsonify(updated_item)

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

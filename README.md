@app.route('/delete_connection/<connection_name>', methods=['DELETE'])
def delete_connection(connection_name):
    connections = load_connections()
    
    if connection_name in connections:
        del connections[connection_name]
        save_connections(connections)
        return jsonify({"message": "Connection deleted successfully"}), 200
    
    return jsonify({"error": "Connection not found"}), 404


    @app.route('/test_connection/<connection_name>', methods=['POST'])
def test_connection(connection_name):
    connections = load_connections()
    
    if connection_name not in connections:
        return jsonify({"error": "Connection not found"}), 404
    
    # Implement the test connection logic here
    return jsonify({"message": "Connection test successful"}), 200




     <div class="container mx-auto p-6">
        <h1 class="text-3xl font-bold mb-6">Connections</h1>
        <table class="min-w-full bg-white border border-gray-300 rounded-lg shadow-md">
            <thead class="bg-gray-200">
                <tr>
                    <th class="py-3 px-6 text-left text-gray-700">Connection Name</th>
                    <th class="py-3 px-6 text-left text-gray-700">Type</th>
                    <th class="py-3 px-6 text-left text-gray-700">Actions</th>
                </tr>
            </thead>
            <tbody id="connections-table">
                <!-- Rows will be inserted here by JavaScript -->
            </tbody>
        </table>
    </div>







  <!-- Edit Connection Modal -->
    <div id="edit-modal" class="fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center hidden">
        <div class="bg-white p-6 rounded-lg shadow-lg max-w-lg w-full">
            <h2 class="text-2xl font-bold mb-4">Edit Connection</h2>
            <form id="edit-form">
                <input type="hidden" id="edit-connection-name">
                <div class="mb-4">
                    <label for="edit-connection-type" class="block text-gray-700">Connection Type</label>
                    <select id="edit-connection-type" class="block w-full mt-1 border border-gray-300 rounded-lg p-2">
                        <!-- Options will be inserted here -->
                    </select>
                </div>
                <!-- Other fields will be dynamically added based on the selected connection type -->
                <button type="submit" class="bg-blue-500 text-white py-2 px-4 rounded-lg">Save</button>
                <button type="button" id="close-edit-modal" class="ml-4 bg-gray-500 text-white py-2 px-4 rounded-lg">Cancel</button>
            </form>
        </div>
    </div>





     <div id="test-modal" class="fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center hidden">
        <div class="bg-white p-6 rounded-lg shadow-lg max-w-lg w-full">
            <h2 class="text-2xl font-bold mb-4">Test Connection</h2>
            <p id="test-result" class="mb-4">Testing...</p>
            <button type="button" id="close-test-modal" class="bg-gray-500 text-white py-2 px-4 rounded-lg">Close</button>
        </div>
    </div>








    document.addEventListener('DOMContentLoaded', () => {
    const connectionsTable = document.getElementById('connections-table');
    const editModal = document.getElementById('edit-modal');
    const testModal = document.getElementById('test-modal');
    const editForm = document.getElementById('edit-form');
    const editConnectionNameInput = document.getElementById('edit-connection-name');
    const editConnectionTypeSelect = document.getElementById('edit-connection-type');
    const testResult = document.getElementById('test-result');

    const fetchConnections = async () => {
        try {
            const response = await axios.get('/connections');
            const connections = response.data;
            connectionsTable.innerHTML = '';
            Object.keys(connections).forEach((connName) => {
                const connection = connections[connName];
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td class="py-3 px-6 border-b border-gray-300">${connection.name_of_connection}</td>
                    <td class="py-3 px-6 border-b border-gray-300">${connName}</td>
                    <td class="py-3 px-6 border-b border-gray-300">
                        <button class="bg-yellow-500 text-white py-1 px-2 rounded-lg mr-2" onclick="editConnection('${connName}')">Edit</button>
                        <button class="bg-red-500 text-white py-1 px-2 rounded-lg mr-2" onclick="deleteConnection('${connName}')">Delete</button>
                        <button class="bg-green-500 text-white py-1 px-2 rounded-lg" onclick="testConnection('${connName}')">Test</button>
                    </td>
                `;
                connectionsTable.appendChild(row);
            });
        } catch (error) {
            console.error('Error fetching connections:', error);
        }
    };









     document.addEventListener('DOMContentLoaded', () => {
            fetchConnections();
        });

        function fetchConnections() {
            axios.get('/connections')
                .then(response => {
                    const connections = response.data;
                    const connectionsTable = document.getElementById('connections-table');
                    connectionsTable.innerHTML = '';

                    Object.keys(connections).forEach(connName => {
                        const connection = connections[connName];
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td class="py-3 px-6 border-b border-gray-300">${connection.name_of_connection}</td>
                            <td class="py-3 px-6 border-b border-gray-300">${connName}</td>
                            <td class="py-3 px-6 border-b border-gray-300">
                                <button class="bg-yellow-500 text-white py-1 px-2 rounded-lg mr-2" onclick="openEditModal('${connName}')">Edit</button>
                                <button class="bg-red-500 text-white py-1 px-2 rounded-lg mr-2" onclick="deleteConnection('${connName}')">Delete</button>
                                <button class="bg-green-500 text-white py-1 px-2 rounded-lg" onclick="testConnection('${connName}')">Test</button>
                            </td>
                        `;
                        connectionsTable.appendChild(row);
                    });
                })
                .catch(error => {
                    console.error('Error fetching connections:', error);
                });
        }

        function openEditModal(connectionName) {
            axios.get(`/connection/${connectionName}`)
                .then(response => {
                    const connection = response.data;
                    if (!connection) return;

                    const editModal = document.getElementById('edit-modal');
                    const editConnectionTypeSelect = document.getElementById('edit-connection-type');
                    const editFieldsContainer = document.getElementById('edit-fields-container');
                    const editConnectionNameInput = document.getElementById('edit-connection-name');

                    editConnectionNameInput.value = connectionName;
                    editConnectionTypeSelect.innerHTML = connectionTypes.map(type => `<option value="${type}" ${type === connection.connection_type ? 'selected' : ''}>${type}</option>`).join('');
                    showEditFields(); // Show fields based on type

                    editModal.classList.remove('hidden');
                })
                .catch(error => {
                    console.error('Error loading connection details:', error);
                });
        }





function updateConnection(event) {
            event.preventDefault();
            const connectionName = document.getElementById('edit-connection-name').value;
            const connectionType = document.getElementById('edit-connection-type').value;
            const formData = new FormData(document.getElementById('edit-form'));
            const data = Object.fromEntries(formData.entries());

            axios.put(`/update_connection/${connectionName}`, {
                connection_type: connectionType,
                ...data
            })
                .then(() => {
                    fetchConnections();
                    document.getElementById('edit-modal').classList.add('hidden');
                })
                .catch(error => {
                    console.error('Error updating connection:', error);
                });
        }

        function deleteConnection(connectionName) {
            if (confirm('Are you sure you want to delete this connection?')) {
                axios.delete(`/delete_connection/${connectionName}`)
                    .then(() => {
                        fetchConnections();
                    })
                    .catch(error => {
                        console.error('Error deleting connection:', error);
                    });
            }
        }

        function testConnection(connectionName) {
            axios.post(`/test_connection/${connectionName}`)
                .then(response => {
                    document.getElementById('test-result').textContent = 'Connection test successful';
                })
                .catch(error => {
                    document.getElementById('test-result').textContent = 'Connection test failed';
                    console.error('Error testing connection:', error);
                });
            document.getElementById('test-modal').classList.remove('hidden');
        }

        document.getElementById('close-edit-modal').addEventListener('click', () => {
            document.getElementById('edit-modal').classList.add('hidden');
        });

        document.getElementById('close-test-modal').addEventListener('click', () => {
            document.getElementById('test-modal').classList.add('hidden');
        });

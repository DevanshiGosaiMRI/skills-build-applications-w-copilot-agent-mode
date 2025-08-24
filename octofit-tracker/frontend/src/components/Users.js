import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';

function Users() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`);
      const data = await response.json();
      console.log('Users data:', data);
      setUsers(data.results || data);
    };
    fetchData();
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Users</h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.username}</td>
              <td>{user.email}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default Users;

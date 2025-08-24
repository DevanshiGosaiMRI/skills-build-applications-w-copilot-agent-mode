import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`);
      const data = await response.json();
      console.log('Workouts data:', data);
      setWorkouts(data.results || data);
    };
    fetchData();
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Workouts</h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((workout) => (
            <tr key={workout.id}>
              <td>{workout.id}</td>
              <td>{workout.name}</td>
              <td>{workout.description}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default Workouts;

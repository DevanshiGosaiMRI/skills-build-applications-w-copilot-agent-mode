import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`);
      const data = await response.json();
      console.log('Activities data:', data);
      setActivities(data.results || data);
    };
    fetchData();
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4">Activities</h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Type</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
          {activities.map((activity) => (
            <tr key={activity.id}>
              <td>{activity.id}</td>
              <td>{activity.type}</td>
              <td>{activity.duration}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
}

export default Activities;

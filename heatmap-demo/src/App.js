import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [clicks, setClicks] = useState([]);

  const handleClick = (e) => {
    const x = e.clientX;
    const y = e.clientY;
    setClicks([...clicks, { x, y }]);
    axios.post('/heatmap', { x, y });
  };

  return (
    <div onClick={handleClick}>
      <h1>Click anywhere to add data to heatmap</h1>
      <ul>
        {clicks.map((click, i) => (
          <li key={i}>x: {click.x}, y: {click.y}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
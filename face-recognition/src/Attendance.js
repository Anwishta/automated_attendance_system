import React, { useState } from 'react';
import axios from 'axios';

function Attendance() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [attendance, setAttendance] = useState([]);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        const formData = new FormData();
        formData.append('image', selectedFile);

        try {
            const response = await axios.post('http://127.0.0.1:5000/recognize', formData);
            setAttendance(response.data);
        } catch (error) {
            console.error('Error recognizing face:', error);
        }
    };

    return (
        <div>
            <h1>Automated Attendance System</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} accept="image/*" />
                <button type="submit">Upload and Recognize</button>
            </form>
            <h2>Recognized Faces:</h2>
            <ul>
                {attendance.map((name, index) => (
                    <li key={index}>{name}</li>
                ))}
            </ul>
        </div>
    );
}

export default Attendance;
import React from 'react';
import { Box, Typography, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const Dashboard: React.FC = () => {
  const navigate = useNavigate();
  const handleLogout = () => {
    localStorage.removeItem('access_token');
    navigate('/login');
  };
  return (
    <Box sx={{ mt: 4, textAlign: 'center' }}>
      <Typography variant="h4" mb={2}>Welcome to the IAM Dashboard</Typography>
      <Button variant="outlined" color="secondary" onClick={handleLogout}>Logout</Button>
    </Box>
  );
};

export default Dashboard; 
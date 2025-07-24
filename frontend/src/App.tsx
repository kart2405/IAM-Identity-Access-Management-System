import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { Container, Box, CssBaseline } from '@mui/material';
import Login from './components/Login';
import Register from './components/Register';
import Dashboard from './components/Dashboard';
import Navigation from './components/Navigation';
import Users from './components/Users';
import Roles from './components/Roles';
import Tenants from './components/Tenants';
import AuditLog from './components/AuditLog';

function App() {
  return (
    <Router>
      <CssBaseline />
      <Navigation />
      <Container maxWidth="sm" sx={{ mt: 8 }}>
        <Box>
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/users" element={<Users />} />
            <Route path="/roles" element={<Roles />} />
            <Route path="/tenants" element={<Tenants />} />
            <Route path="/audit-log" element={<AuditLog />} />
            <Route path="/" element={<Navigate to="/login" />} />
          </Routes>
        </Box>
      </Container>
    </Router>
  );
}

export default App;

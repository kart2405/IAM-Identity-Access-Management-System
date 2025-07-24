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
import { AuthProvider } from './AuthContext';
import ProtectedRoute from './ProtectedRoute';

function App() {
  return (
    <AuthProvider>
      <Router>
        <CssBaseline />
        <Navigation />
        <Container maxWidth="sm" sx={{ mt: 8 }}>
          <Box>
            <Routes>
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/dashboard" element={
                <ProtectedRoute>
                  <Dashboard />
                </ProtectedRoute>
              } />
              <Route path="/users" element={
                <ProtectedRoute requiredRole="admin">
                  <Users />
                </ProtectedRoute>
              } />
              <Route path="/roles" element={
                <ProtectedRoute requiredRole="admin">
                  <Roles />
                </ProtectedRoute>
              } />
              <Route path="/tenants" element={
                <ProtectedRoute requiredRole="superuser">
                  <Tenants />
                </ProtectedRoute>
              } />
              <Route path="/audit-log" element={
                <ProtectedRoute requiredRole="superuser">
                  <AuditLog />
                </ProtectedRoute>
              } />
              <Route path="/" element={<Navigate to="/login" />} />
            </Routes>
          </Box>
        </Container>
      </Router>
    </AuthProvider>
  );
}

export default App;

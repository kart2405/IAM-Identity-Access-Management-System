import React, { useEffect, useState } from 'react';
import { Box, Typography, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, CircularProgress, Alert } from '@mui/material';
import api from '../api';

interface Tenant {
  id: number;
  name: string;
  created_at?: string;
}

const Tenants: React.FC = () => {
  const [tenants, setTenants] = useState<Tenant[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchTenants = async () => {
      setLoading(true);
      setError('');
      try {
        const res = await api.get('/tenants');
        setTenants(res.data);
      } catch (err: any) {
        setError(err.response?.data?.detail || 'Failed to load tenants');
      } finally {
        setLoading(false);
      }
    };
    fetchTenants();
  }, []);

  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h5" mb={2}>Tenants</Typography>
      <Button variant="contained" color="primary" sx={{ mb: 2 }}>Add Tenant</Button>
      {loading ? <CircularProgress /> : error ? <Alert severity="error">{error}</Alert> : (
        <TableContainer component={Paper}>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>Name</TableCell>
                <TableCell>Created At</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {tenants.map(tenant => (
                <TableRow key={tenant.id}>
                  <TableCell>{tenant.name}</TableCell>
                  <TableCell>{tenant.created_at ? new Date(tenant.created_at).toLocaleDateString() : ''}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Box>
  );
};

export default Tenants; 
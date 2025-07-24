import React from 'react';
import { Box, Typography, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

const Tenants: React.FC = () => {
  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h5" mb={2}>Tenants</Typography>
      <Button variant="contained" color="primary" sx={{ mb: 2 }}>Add Tenant</Button>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Created At</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            <TableRow>
              <TableCell>Acme Corp</TableCell>
              <TableCell>2024-07-24</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default Tenants; 
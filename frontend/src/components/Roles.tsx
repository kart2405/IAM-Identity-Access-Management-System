import React from 'react';
import { Box, Typography, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

const Roles: React.FC = () => {
  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h5" mb={2}>Roles</Typography>
      <Button variant="contained" color="primary" sx={{ mb: 2 }}>Add Role</Button>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Description</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            <TableRow>
              <TableCell>Admin</TableCell>
              <TableCell>Full access</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default Roles; 
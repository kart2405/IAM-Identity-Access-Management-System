import React from 'react';
import { Box, Typography, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';

const AuditLog: React.FC = () => {
  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h5" mb={2}>Audit Log</Typography>
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>User</TableCell>
              <TableCell>Action</TableCell>
              <TableCell>Details</TableCell>
              <TableCell>Timestamp</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            <TableRow>
              <TableCell>user@example.com</TableCell>
              <TableCell>Login</TableCell>
              <TableCell>Success</TableCell>
              <TableCell>2024-07-24 10:00</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
};

export default AuditLog; 
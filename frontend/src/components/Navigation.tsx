import React from 'react';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { Link, useLocation } from 'react-router-dom';

const navItems = [
  { label: 'Dashboard', path: '/dashboard' },
  { label: 'Users', path: '/users' },
  { label: 'Roles', path: '/roles' },
  { label: 'Tenants', path: '/tenants' },
  { label: 'Audit Log', path: '/audit-log' },
];

const Navigation: React.FC = () => {
  const location = useLocation();
  return (
    <AppBar position="static" color="default" elevation={0}>
      <Toolbar>
        <Typography variant="h6" color="inherit" sx={{ flexGrow: 1, fontWeight: 700, letterSpacing: 1 }}>
          IAM System
        </Typography>
        <Box>
          {navItems.map(item => (
            <Button
              key={item.path}
              color={location.pathname === item.path ? 'primary' : 'inherit'}
              component={Link}
              to={item.path}
              sx={{ fontWeight: location.pathname === item.path ? 700 : 400 }}
            >
              {item.label}
            </Button>
          ))}
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navigation; 
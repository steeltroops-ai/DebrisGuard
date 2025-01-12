// frontend/src/components/Dashboard/Dashboard.jsx
import React from 'react';
import { useSelector } from 'react-redux';
import { DebrisMap } from '../Maps';
import { AlertPanel } from '../Alerts';

export const Dashboard = () => {
  const debris = useSelector(state => state.debris.items);
  
  return (
    <div className="dashboard">
      <DebrisMap debris={debris} />
      <AlertPanel />
    </div>
  );
};
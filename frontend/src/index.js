// frontend/src/store/index.js
import { configureStore } from '@reduxjs/toolkit';
import debrisReducer from './slices/debrisSlice';
import alertsReducer from './slices/alertsSlice';

export const store = configureStore({
  reducer: {
    debris: debrisReducer,
    alerts: alertsReducer,
  },
});
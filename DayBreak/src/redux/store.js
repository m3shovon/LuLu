// src/redux/store.js
import { configureStore } from '@reduxjs/toolkit';
import incomeReducer from './incomeSlice';
import expenseReducer from './expenseSlice';

export const store = configureStore({
  reducer: {
    income: incomeReducer,
    expenses: expenseReducer,
  },
});

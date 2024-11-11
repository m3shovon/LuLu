// app/expenses.js
import React from 'react';
import { View, Text, Button } from 'react-native';
import { useSelector, useDispatch } from 'react-redux';
import { addExpense } from '../src/redux/expenseSlice';
import { useRouter } from 'expo-router';

export default function ExpenseScreen() {
  const router = useRouter();
  const expenses = useSelector((state) => state.expenses);
  const dispatch = useDispatch();

  const handleAddExpense = () => {
    dispatch(addExpense({ amount: 50, description: 'Groceries' }));
  };

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Expenses Screen</Text>
      <Button title="Add Expense" onPress={handleAddExpense} />
      <Button title="Go Back Home" onPress={() => router.push('/')} />
    </View>
  );
}

import React from 'react';
import { View, Text } from 'react-native';
import { useSelector } from 'react-redux';

export default function ExpenseScreen() {
  const expenseList = useSelector((state) => state.expenses);

  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text>Expense Entries</Text>
      {expenseList.map((expense) => (
        <View key={expense.id}>
          <Text>{expense.description}: ${expense.amount}</Text>
        </View>
      ))}
    </View>
  );
}

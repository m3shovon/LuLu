import React from 'react';
import { View, Text, Button } from 'react-native';
import { useSelector } from 'react-redux';

export default function IncomeScreen() {
  const incomeList = useSelector((state) => state.income);

  return (
    <View style={{ flex: 1, padding: 16 }}>
      <Text>Income Entries</Text>
      {incomeList.map((income) => (
        <View key={income.id}>
          <Text>{income.description}: ${income.amount}</Text>
        </View>
      ))}
    </View>
  );
}

// app/income.js
import React from 'react';
import { View, Text, Button } from 'react-native';
import { useSelector, useDispatch } from 'react-redux';
import { addIncome } from '../src/redux/incomeSlice';
import { useRouter } from 'expo-router';

export default function IncomeScreen() {
  const router = useRouter();
  const income = useSelector((state) => state.income);
  const dispatch = useDispatch();

  const handleAddIncome = () => {
    dispatch(addIncome({ amount: 100, description: 'Freelance work' }));
  };

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Income Screen</Text>
      <Button title="Add Income" onPress={handleAddIncome} />
      <Button title="Go Back Home" onPress={() => router.push('/')} />
    </View>
  );
}

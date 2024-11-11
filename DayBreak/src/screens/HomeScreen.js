import React from 'react';
import { View, Text, Button } from 'react-native';

export default function HomeScreen({ navigation }) {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text>Welcome to Income Expense Tracker</Text>
      <Button title="Go to Income" onPress={() => navigation.navigate('Income')} />
      <Button title="Go to Expenses" onPress={() => navigation.navigate('Expenses')} />
    </View>
  );
}

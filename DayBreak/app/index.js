// app/index.js
import React from 'react';
import { View, Text, Button, StatusBar } from 'react-native';
import { Provider } from 'react-redux';
import { store } from '../src/redux/store';
import { useRouter } from 'expo-router';

export default function App() {
  const router = useRouter();

  return (
    <Provider store={store}>
      <StatusBar barStyle="dark-content" />
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <Text>Welcome to Income Expense Tracker</Text>
        <Button title="Go to Income" onPress={() => router.push('/income')} />
        <Button title="Go to Expenses" onPress={() => router.push('/expenses')} />
      </View>
    </Provider>
  );
}

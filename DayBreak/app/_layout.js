// app/_layout.js
import { Tabs } from 'expo-router';  // Expo router's tab navigation

export default function Layout() {
  return (
    <Tabs>
      <Tabs.Screen name="index" />
      <Tabs.Screen name="income" />
      <Tabs.Screen name="expense" />
    </Tabs>
  );
}
